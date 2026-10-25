"""Song model + renderer: tracks of note events -> stems -> mix bus -> master.

A Song is defined in beats. Swing and per-track micro-timing are applied at render time, so the same
pattern can be rendered straight, MPC-swung, or laid-back without touching the notes.
"""
import os, json, random
import numpy as np, soundfile as sf
from paths import VST3_DIR, SURGE_DIR
import pedalboard
from mido import Message
import dsp
from dsp import SR

VST = VST3_DIR


class Note:
    __slots__ = ('beat', 'dur', 'pitch', 'vel')

    def __init__(self, beat, dur, pitch, vel=100):
        self.beat, self.dur, self.pitch, self.vel = beat, dur, pitch, vel


class Track:
    """instrument: ('sfz', SFZ) | ('vst', path, fxp_or_None, params) | ('oneshot', {pitch: array}) | ('func', f(pitch, vel, dur_s)->array)"""

    def __init__(self, name, instrument, notes=None, gain_db=0.0, pan=0.0, timing_ms=0.0, humanize_ms=0.0,
                 vel_jitter=0, swing=None, fx=None, send_reverb=0.0, mono=False):
        self.name, self.instrument = name, instrument
        self.notes = notes or []
        self.gain_db, self.pan, self.timing_ms, self.humanize_ms = gain_db, pan, timing_ms, humanize_ms
        self.vel_jitter, self.swing, self.fx, self.send_reverb, self.mono = vel_jitter, swing, fx, send_reverb, mono


class Song:
    def __init__(self, bpm, bars, swing=50.0, seed=7):
        self.bpm, self.bars, self.swing, self.seed = bpm, bars, swing, seed
        self.tracks = []

    @property
    def spb(self):  # seconds per beat
        return 60.0 / self.bpm

    def beat_to_s(self, beat, swing):
        """Swing delays every odd 16th; swing in % (50 = straight, 66.7 = triplet)."""
        six = beat * 4.0
        i = int(np.floor(six + 1e-6)); frac = six - i
        delay = 0.0
        if i % 2 == 1 and frac < 1e-3:
            delay = (swing - 50.0) / 50.0 * (self.spb / 4)
        return beat * self.spb + delay

    def length_s(self):
        return self.bars * 4 * self.spb


def _place(buf, x, start):
    if x is None or start >= len(buf): return
    if start < 0: x = x[-start:]; start = 0
    n = min(len(x), len(buf) - start)
    buf[start:start + n] += x[:n]


def render_track(song, tr, tail_s=4.0):
    rng = random.Random(song.seed + hash(tr.name) % 1000)
    n = int((song.length_s() + tail_s) * SR)
    buf = np.zeros((n, 2), np.float32)
    sw = tr.swing if tr.swing is not None else song.swing
    kind = tr.instrument[0]
    if kind in ('sfz', 'oneshot', 'func'):
        for nt in tr.notes:
            t = song.beat_to_s(nt.beat, sw) + tr.timing_ms / 1000 + rng.gauss(0, tr.humanize_ms / 1000 if tr.humanize_ms else 0)
            vel = int(np.clip(nt.vel + (rng.randint(-tr.vel_jitter, tr.vel_jitter) if tr.vel_jitter else 0), 1, 127))
            dur_s = nt.dur * song.spb
            if kind == 'sfz':
                x = tr.instrument[1].render_note(nt.pitch, vel, dur_s, rng)
            elif kind == 'oneshot':
                src = tr.instrument[1][nt.pitch]
                x = src * (vel / 127) ** 1.5
                if x.ndim == 1: x = np.stack([x, x], 1)
            else:
                x = tr.instrument[1](nt.pitch, vel, dur_s)
                if x.ndim == 1: x = np.stack([x, x], 1)
            if x is None:
                tr.missing = getattr(tr, 'missing', 0) + 1; continue
            _place(buf, x.astype(np.float32), int(t * SR))
    elif kind == 'vst':
        _, path, fxp, params = tr.instrument
        plug = pedalboard.load_plugin(VST + path)
        if fxp:
            import jucestate
            jucestate.load_fxp_into(plug, fxp)
            plug([], duration=0.5, sample_rate=SR, reset=False)
        for k, v in (params or {}).items():
            setattr(plug, k, v)
        msgs = []
        for nt in tr.notes:
            t = song.beat_to_s(nt.beat, sw) + tr.timing_ms / 1000 + rng.gauss(0, tr.humanize_ms / 1000 if tr.humanize_ms else 0)
            t = max(0.0, t)
            vel = int(np.clip(nt.vel + (rng.randint(-tr.vel_jitter, tr.vel_jitter) if tr.vel_jitter else 0), 1, 127))
            msgs.append((t, Message('note_on', note=int(nt.pitch), velocity=vel)))
            msgs.append((t + nt.dur * song.spb, Message('note_off', note=int(nt.pitch), velocity=0)))
        msgs.sort(key=lambda m: (m[0], m[1].type == 'note_on'))
        out = plug([m.copy(time=t) for t, m in msgs], duration=n / SR, sample_rate=SR, reset=False)
        buf = out.T.astype(np.float32)
        if buf.shape[1] == 1: buf = np.repeat(buf, 2, 1)
        buf = buf[:n]
    if tr.mono:
        m = buf.mean(1, keepdims=True); buf = np.repeat(m, 2, 1)
    if tr.fx is not None:
        buf = tr.fx(buf)
    # pan (constant power) + gain
    p = (tr.pan + 1) * np.pi / 4
    buf = buf * np.array([np.cos(p), np.sin(p)], np.float32) * np.sqrt(2) * 10 ** (tr.gain_db / 20)
    return buf


def plate_reverb(x, room=0.35, damp=0.6, wet=1.0):
    board = pedalboard.Pedalboard([pedalboard.Reverb(room_size=room, damping=damp, wet_level=wet, dry_level=0.0, width=0.9)])
    return board(x.T, SR).T


def mixdown(song, stems, reverb=None, bus=None, master=None, reverb_width=0.6):
    n = max(len(s) for s in stems.values())
    mix = np.zeros((n, 2), np.float32); send = np.zeros((n, 2), np.float32)
    for tr in song.tracks:
        s = stems[tr.name]
        mix[:len(s)] += s
        if tr.send_reverb > 0: send[:len(s)] += s * tr.send_reverb
    if send.any():
        rv = (reverb or plate_reverb)(send)
        rv = dsp.hp(rv, 250)  # keep the low end dry and mono-safe
        m_, s_ = rv.mean(1, keepdims=True), (rv[:, :1] - rv[:, 1:]) / 2
        rv = np.concatenate([m_ + reverb_width * s_, m_ - reverb_width * s_], 1)  # refs are narrow (median side-mid -19 dB)
        mix[:len(rv)] += rv
    if bus: mix = bus(mix)
    if master: mix = master(mix)
    return mix


def master_chain(x, target_lufs=-9.5, ceiling_db=-1.0, glue=True):
    y = x.copy()
    if glue:
        y = dsp.compress(y, thr_db=-14, ratio=2, att_ms=30, rel_ms=150, knee_db=6)
    # loudness: gain into soft clip + true-peak limiter, iterate to target
    g = 0.0
    for _ in range(6):
        z = dsp.true_peak_limit(dsp.soft_clip(y * 10 ** (g / 20)), ceiling_db)
        l = dsp.lufs(z)
        if abs(l - target_lufs) < 0.15: break
        g += (target_lufs - l)
    return z


def export(path_noext, x, mp3=True):
    os.makedirs(os.path.dirname(path_noext), exist_ok=True)
    sf.write(path_noext + '.wav', x, SR, subtype='PCM_24')
    if mp3:
        os.system(f'ffmpeg -v error -y -i "{path_noext}.wav" -b:a 320k "{path_noext}.mp3"')


def auto_balance(stems, targets_lu, ref='snare'):
    """Gain-stage stems by measured loudness: targets_lu = {stem: LU relative to the reference stem}.
    Loudness = BS.1770 integrated (gated, so silence/rests don't count). Returns new dict + applied gains."""
    import pyloudnorm as pyln
    meter = pyln.Meter(SR)
    L = {k: meter.integrated_loudness(v) for k, v in stems.items() if np.abs(v).max() > 1e-5}
    base = L[ref]
    out, gains = {}, {}
    for k, v in stems.items():
        if k in targets_lu and k in L and np.isfinite(L[k]):
            g = base + targets_lu[k] - L[k]; out[k] = v * 10 ** (g / 20); gains[k] = round(g, 1)
        else:
            out[k] = v
    return out, gains
