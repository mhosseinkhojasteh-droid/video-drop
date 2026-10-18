"""GLASS JAW — full arrangement of concept B (G-Unit street, F phrygian, 90 BPM).

Form (Template A, producer_bible/arrangement_principles.md):
  intro 4 | hook 8 | verse 16 | hook 8 | verse 16 | hook 8 | outro 4   = 64 bars ~ 2:51
Rules applied: arrange by subtraction; single-bar kick/808 drop on bar 1 (and bar 9) of every verse; ear candy every 4th bar;
hook = full motif (octaves) + cello + violin pedal; verse = motif in one octave, thinner, no strings; a reversed-piano swell
(built from the record's own piano) into every hook; outro ends on a punctuation hit + tail.
"""
import sys, os, json
sys.path.insert(0, 'scripts/engine'); sys.path.insert(0, 'projects/prototype_01')
import numpy as np, pedalboard as pb
import dsp
from dsp import SR
from render import Song, Track, Note, render_track, mixdown, master_chain, export, auto_balance
from theory import n
import concepts as C

BPM = 90.0
FORM = [('intro', 4), ('hook', 8), ('verse', 16), ('hook', 8), ('verse', 16), ('hook', 8), ('outro', 4)]
OUT = 'projects/prototype_01/renders/glass_jaw_v3'

M1 = [(0, .22, 'F3', 112), (0.75, .22, 'F3', 96), (1.5, .3, 'Ab3', 108), (2.0, .45, 'Gb3', 116), (2.75, .22, 'F3', 100)]
M2 = [(0, .22, 'C3', 112), (0.75, .22, 'Db3', 104), (1.5, .3, 'C3', 100), (2.5, .22, 'Eb3', 108), (3.0, .5, 'Db3', 112)]
B1 = [(0, .7, 'F2', 118), (.75, .6, 'F2', 100), (2.5, 1.0, 'F2', 110)]
B2 = [(0, .7, 'C2', 116), (.75, .6, 'Db2', 104), (2.5, .5, 'Eb2', 106), (3.0, .9, 'Db2', 110)]


def bar_plan():
    plan = []; bar = 0
    for sec, L in FORM:
        for i in range(L):
            p = dict(bar=bar, sec=sec, i=i, phrase_odd=(bar % 2 == 1))
            if sec == 'intro':
                p.update(piano='full' if i >= 2 else 'thin', piano_lp=[700, 1400, 3000, 9000][i], cello=False, strings=False,
                         kick=False, snare=(i == 3), hats=(i >= 2), roll=(i == 3), bass=False)
            elif sec == 'hook':
                p.update(piano='full', piano_lp=None, cello=True, strings=True, kick=True, snare=True, hats=True,
                         roll=(i % 4 == 3), bass=True, open_hat=(i % 2 == 1))
            elif sec == 'verse':
                drop = i in (0, 8)
                p.update(piano='thin', piano_lp=4500, cello=(i >= 8 and i % 2 == 0), strings=False, kick=not drop, snare=True, hats=True,
                         roll=(i % 4 == 3), bass=not drop, open_hat=False)
            else:  # outro
                p.update(piano='full' if i < 3 else 'last', piano_lp=[9000, 5000, 2500, 1200][i], cello=i < 2, strings=i < 3, kick=i < 2,
                         snare=i < 2, hats=i < 3, roll=False, bass=i < 2 or i == 3)
            plan.append(p); bar += 1
    return plan


def build():
    plan = bar_plan(); bars = len(plan)
    s = Song(BPM, bars, swing=63); spb = s.spb; T = s.length_s() + 6
    vk = C.kit('virt')
    k808 = dsp.kick_808(f0=46, decay=0.3, pitch_drop=3.0, click=0.35, drive_db=8)
    sn = vk.render_note(40, 125, 0.3); cl = dsp.clap_synth(seed=9)
    sc = np.zeros((max(len(sn), len(cl)), 2), np.float32); sc[:len(sn)] += sn; sc[:len(cl)] += np.stack([cl, cl], 1) * 0.8
    hat = dsp.hat_synth(); ohat = dsp.hat_synth(open_=True)
    shots = {36: np.stack([k808, k808], 1), 38: sc, 42: np.stack([hat, hat], 1), 46: np.stack([ohat, ohat], 1)}
    K, S, H, P, CE, BL = [], [], [], [], [], []
    for p in plan:
        o = p['bar'] * 4; odd = p['phrase_odd']
        if p['kick']:
            K += [Note(o + x, .25, 36, 120) for x in (0, 0.75, 2.5)] + ([Note(o + 3.75, .25, 36, 100)] if odd else [])
        if p['snare']:
            S += [Note(o + 1, .25, 38, 124), Note(o + 3, .25, 38, 124)]
        if p['hats']:
            if p['roll']:
                H += [Note(o + i * .5, .25, 42, 92) for i in range(6)] + [Note(o + 3 + i * .125, .125, 42, 70 + 6 * i) for i in range(8)]
            else:
                H += [Note(o + i * .5, .25, 42, 100 if i % 2 == 0 else 78) for i in range(8)]
            if p.get('open_hat'): H.append(Note(o + 3.5, .5, 46, 84))
        mot = M2 if odd else M1
        if p['piano'] == 'last':
            P += [Note(o, 3.5, n('F3'), 100), Note(o, 3.5, n('F2'), 96), Note(o, 3.5, n('C4'), 80)]
        elif p['piano']:
            for st, du, nm, ve in mot:
                if p['piano'] == 'full':
                    P += [Note(o + st, du, n(nm), ve), Note(o + st, du, n(nm) + 12, ve - 14)]
                else:
                    P.append(Note(o + st, du, n(nm), ve - 12))
        if p['cello']:
            CE += [Note(o + st, du + .1, n(nm) - 12, ve - 8) for st, du, nm, ve in mot]
        if p['bass']:
            if p['sec'] == 'outro' and p['i'] == 3:
                BL.append((o, 3.5, n('F1'), 118))
            else:
                BL += [(o + st, du, n(nm) - 12, ve) for st, du, nm, ve in (B2 if odd else B1)]
    s.tracks = [Track('kick', ('oneshot', shots), K, mono=True),
                Track('snare', ('oneshot', shots), S, timing_ms=6, send_reverb=0.06,
                      fx=C.board(pb.HighpassFilter(120), pb.Compressor(threshold_db=-12, ratio=4, attack_ms=3, release_ms=70))),
                Track('hats', ('oneshot', shots), H, humanize_ms=2, vel_jitter=6, pan=-0.12),
                Track('piano', ('sfz', C.kit('piano')), P, swing=50, send_reverb=0.12,
                      fx=C.board(pb.HighpassFilter(150), pb.Compressor(threshold_db=-18, ratio=3, attack_ms=2, release_ms=60)))]
    stems = {t.name: render_track(s, t, tail_s=6) for t in s.tracks}
    N = int(T * SR)
    for k in stems: stems[k] = np.pad(stems[k][:N], ((0, max(0, N - len(stems[k]))), (0, 0)))
    # piano automation: per-bar low-pass (intro opening / outro closing / verse darker)
    pz = stems['piano']; out = np.zeros_like(pz); fade = int(0.01 * SR)
    for p in plan:
        a = int(s.beat_to_s(p['bar'] * 4, 50) * SR); b = int(s.beat_to_s(p['bar'] * 4 + 4, 50) * SR) if p['bar'] < bars - 1 else N
        seg = pz[a:b]
        if p['piano_lp']: seg = dsp.lp(seg, p['piano_lp'], order=2)
        out[a:b] += seg
    stems['piano'] = dsp.width(out, 0.4)
    # cello (VSCO spiccato) and violin pedal
    cs = C.kit('cello_spic'); cb = np.zeros((N, 2), np.float32)
    for nt in CE:
        x = cs.render_note(nt.pitch, nt.vel, nt.dur * spb); st = int(s.beat_to_s(nt.beat, 50) * SR); cb[st:st + len(x)] += x[:N - st]
    cm = cb.mean(1, keepdims=True); stems['cello'] = dsp.hp(np.concatenate([cm + 0.3 * (cb[:, :1] - cm), cm + 0.3 * (cb[:, 1:] - cm)], 1), 70)
    vs = C.kit('vln_sus'); vb = np.zeros((N, 2), np.float32)
    for p in plan:
        if p['strings'] and p['i'] % 2 == 0:
            nm = 'Gb5' if (p['i'] // 2) % 2 == 0 else 'F5'
            x = vs.render_note(n(nm), 66, 2 * 4 * spb); st = int(p['bar'] * 4 * spb * SR); vb[st:st + len(x)] += x[:N - st]
    stems['strings'] = dsp.width(vb, 0.5)
    stems['bass'] = dsp.bass_808(BL, spb, T, decay=0.45)[:N]
    # reversed-piano swell into every hook (the record's own material), last 1 beat before the hook downbeat
    sw = np.zeros((N, 2), np.float32)
    hook_starts = [p['bar'] for p in plan if p['sec'] == 'hook' and p['i'] == 0]
    for hb in hook_starts:
        d = int(s.beat_to_s(hb * 4, 50) * SR); L = int(1.5 * spb * SR)
        src = stems['piano'][d:d + L] if hb > 0 else stems['piano'][:L]
        rev = src[::-1] * np.linspace(0, 1, len(src))[:, None] ** 2
        st = max(0, d - len(rev)); sw[st:st + len(rev)] += rev[:d - st] if d - st < len(rev) else rev
    stems['swell'] = dsp.hp(sw, 300)
    # balance by loudness (same targets as concept B + swell)
    stems, gains = auto_balance(stems, {'kick': 0.0, 'snare': 0, 'hats': -9, 'piano': -1.5, 'cello': -9, 'strings': -10, 'bass': -4.5, 'swell': -8})
    s.tracks += [Track('cello', ('func', None), [], send_reverb=0.1), Track('strings', ('func', None), [], send_reverb=0.3),
                 Track('bass', ('func', None), []), Track('swell', ('func', None), [], send_reverb=0.4)]
    mix = mixdown(s, stems)
    # trim to the end of the outro tail (find where the mix decays below -60 dBFS after the last bar)
    end = int(s.length_s() * SR); tail = np.abs(mix[end:]).max(1); q = np.where(tail > 10 ** (-60 / 20))[0]
    mix = mix[:end + (q[-1] if len(q) else 0) + int(0.3 * SR)]
    fade = int(0.3 * SR); mix[-fade:] *= np.linspace(1, 0, fade)[:, None]
    m = master_chain(mix, target_lufs=-11.0)
    export(OUT, m)
    for k, v in stems.items(): export(OUT + '_stems/' + k, v[:len(m)], mp3=False)
    info = dict(bars=bars, bpm=BPM, form=FORM, duration_s=round(len(m) / SR, 2), gains=gains, metrics=C.metrics(m))
    json.dump(info, open(OUT + '.json', 'w'), indent=1, default=float)
    print(json.dumps(info, default=float))


if __name__ == '__main__':
    build()
