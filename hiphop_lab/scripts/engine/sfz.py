"""Minimal, dependency-light SFZ sampler (enough of SFZ v1/v2 for the sfzinstruments/Karoryfer libraries).

Supports: #define, #include, <control> default_path / set_cc, header inheritance (global > master > group > region),
key/lokey/hikey/pitch_keycenter, lovel/hivel, tune/transpose/pitch_keytrack, volume/amplitude/pan, offset,
seq_length/seq_position (round robin), lorand/hirand, trigger (attack only), sw_last/sw_default keyswitches,
locc/hicc conditions evaluated against set_cc defaults (+ overrides), loop_mode one_shot, ampeg_attack/release.
Not supported (ignored): CC modulation curves, filters, LFOs, crossfades, release triggers.
"""
import os, re, random
import numpy as np, soundfile as sf
from scipy.signal import resample_poly

NOTE_NAMES = {'c': 0, 'd': 2, 'e': 4, 'f': 5, 'g': 7, 'a': 9, 'b': 11}


def note_num(v):
    v = str(v).strip()
    try:
        return int(v)
    except ValueError:
        m = re.match(r'([a-gA-G])([#b]?)(-?\d+)', v)
        if not m: return None
        n = NOTE_NAMES[m.group(1).lower()] + (1 if m.group(2) == '#' else -1 if m.group(2) == 'b' else 0)
        return n + (int(m.group(3)) + 1) * 12


class SFZ:
    def __init__(self, path, cc=None, sr=48000, key_offset=0):
        """key_offset: measured correction so that render_note(k) SOUNDS at MIDI k (Growlybass: +12, measured with pYIN)."""
        self.key_offset = key_offset
        self.path = path; self.root = os.path.dirname(path); self.sr = sr
        self.defines = {}; self.cc = {}; self.default_path = ''
        self.regions = []; self.cache = {}; self.rr = {}
        text = self._load(path)
        self._parse(text)
        if cc: self.cc.update(cc)
        self.sw_default = None
        for r in self.regions:
            if 'sw_default' in r: self.sw_default = note_num(r['sw_default'])

    def _load(self, path, depth=0):
        txt = open(path, encoding='utf-8', errors='ignore').read()
        txt = re.sub(r'/\*.*?\*/', '', txt, flags=re.S)
        txt = re.sub(r'//[^\n]*', '', txt)
        def inc(m):
            p2 = os.path.join(self.root, m.group(1))
            return '\n' + self._load(p2, depth + 1) + '\n' if depth < 12 and os.path.exists(p2) else ''
        txt = re.sub(r'#include\s+"([^"]+)"', inc, txt)
        def dfn(m):
            self.defines[m.group(1)] = m.group(2); return ''
        txt = re.sub(r'#define\s+(\$\w+)\s+(\S+)', dfn, txt)
        return txt

    def _sub(self, s):
        for k in sorted(self.defines, key=len, reverse=True): s = s.replace(k, self.defines[k])
        return s

    def _parse(self, text):
        text = self._sub(text)
        tokens = re.split(r'(<\w+>)', text)
        level = {'global': {}, 'master': {}, 'group': {}}
        cur = None; cur_hdr = None
        def opcodes(s):
            # values may contain spaces (sample paths): split at ' key=' boundaries
            res = {}
            for m in re.finditer(r'(\w+)=(.*?)(?=\s+\w+=|$)', s.strip().replace('\n', ' ')):
                res[m.group(1)] = m.group(2).strip()
            return res
        for tok in tokens:
            if not tok.strip(): continue
            if re.match(r'<\w+>', tok):
                cur_hdr = tok[1:-1]
                if cur_hdr == 'global': level = {'global': {}, 'master': {}, 'group': {}}
                elif cur_hdr == 'master': level['master'] = {}; level['group'] = {}
                elif cur_hdr == 'group': level['group'] = {}
                continue
            ops = opcodes(tok)
            if cur_hdr == 'control':
                if 'default_path' in ops: self.default_path = ops['default_path'].replace('\\', '/')
                for k, v in ops.items():
                    m = re.match(r'set_(?:hd)?cc(\d+)', k)
                    if m:
                        val = float(v); self.cc[int(m.group(1))] = val * 127 if 'hdcc' in k else val
            elif cur_hdr in ('global', 'master', 'group'):
                level[cur_hdr].update(ops)
            elif cur_hdr == 'region':
                r = {}; r.update(level['global']); r.update(level['master']); r.update(level['group']); r.update(ops)
                if 'sample' in r and not r['sample'].startswith('*'):
                    r['_sample'] = os.path.normpath(os.path.join(self.root, self.default_path, r['sample'].replace('\\', '/')))
                    self.regions.append(r)

    # ------------------------------------------------------------------
    def _ok(self, r, key, vel):
        lk = note_num(r.get('lokey', r.get('key', 0))); hk = note_num(r.get('hikey', r.get('key', 127)))
        if lk is None or hk is None or not (lk <= key <= hk): return False
        if not (int(r.get('lovel', 1)) <= vel <= int(r.get('hivel', 127))): return False
        if r.get('trigger', 'attack') not in ('attack', 'first'): return False
        if 'sw_last' in r and self.sw_default is not None and note_num(r['sw_last']) != self.sw_default: return False
        for k, v in r.items():
            m = re.match(r'locc(\d+)$', k)
            if m and self.cc.get(int(m.group(1)), 0) < float(v): return False
            m = re.match(r'hicc(\d+)$', k)
            if m and self.cc.get(int(m.group(1)), 0) > float(v): return False
        return True

    def _sample(self, p):
        if p not in self.cache:
            if not os.path.exists(p):
                alt = [os.path.splitext(p)[0] + e for e in ('.flac', '.wav', '.ogg')]
                p2 = next((a for a in alt if os.path.exists(a)), None)
                if p2 is None: raise FileNotFoundError(p)
            else:
                p2 = p
            x, sr = sf.read(p2, always_2d=True, dtype='float32')
            if x.shape[1] == 1: x = np.repeat(x, 2, 1)
            if sr != self.sr: x = resample_poly(x, self.sr, sr, axis=0).astype(np.float32)
            self.cache[p] = x
        return self.cache[p]

    def render_note(self, key, vel, dur, rng=None):
        """Return stereo float32 array for one note (dur in seconds of note-on; release appended)."""
        rng = rng or random
        key = key + self.key_offset
        cands = [r for r in self.regions if self._ok(r, key, vel)]
        if not cands: return None
        # round robin groups
        if any('seq_length' in r for r in cands):
            slen = int(cands[0].get('seq_length', 1)); pos = self.rr.get((key, vel // 16), 0) % slen + 1
            self.rr[(key, vel // 16)] = pos
            c2 = [r for r in cands if int(r.get('seq_position', 1)) == pos]; cands = c2 or cands
        rv = rng.random()
        c2 = [r for r in cands if float(r.get('lorand', 0)) <= rv < float(r.get('hirand', 1.0001))]
        cands = c2 or cands
        out = None
        for r in cands:
            x = self._sample(r['_sample'])
            off = int(float(r.get('offset', 0)) * self.sr / 44100)
            x = x[off:]
            kc = note_num(r.get('pitch_keycenter', r.get('key', key))) or key
            kt = float(r.get('pitch_keytrack', 100)) / 100
            semis = (key - kc) * kt + float(r.get('transpose', 0)) + float(r.get('tune', 0)) / 100
            if abs(semis) > 1e-3:
                ratio = 2 ** (semis / 12)
                n = int(len(x) / ratio)
                idx = np.arange(n) * ratio
                x = np.stack([np.interp(idx, np.arange(len(x)), x[:, c]) for c in range(2)], 1).astype(np.float32)
            g = 10 ** (float(r.get('volume', 0)) / 20) * float(r.get('amplitude', 100)) / 100
            vt = float(r.get('amp_veltrack', 100)) / 100
            g *= (1 - vt) + vt * (vel / 127) ** 2
            pan = float(r.get('pan', 0)) / 100
            x = x * g * np.array([min(1, 1 - pan), min(1, 1 + pan)], dtype=np.float32)
            one_shot = r.get('loop_mode', '') == 'one_shot'
            if not one_shot:
                rel = float(r.get('ampeg_release', 0.25))
                n_on = int(dur * self.sr); n_rel = int(rel * self.sr)
                x = x[:n_on + n_rel].copy()
                if len(x) > n_on:
                    env = np.ones(len(x), dtype=np.float32)
                    tail = len(x) - n_on
                    env[n_on:] = np.exp(-5 * np.arange(tail) / max(1, n_rel))
                    x *= env[:, None]
            att = float(r.get('ampeg_attack', 0))
            if att > 0.0005:
                na = min(len(x), int(att * self.sr)); x[:na] *= np.linspace(0, 1, na)[:, None]
            out = x if out is None else _mix(out, x)
        return out


def _mix(a, b):
    n = max(len(a), len(b)); o = np.zeros((n, 2), np.float32); o[:len(a)] += a; o[:len(b)] += b; return o
