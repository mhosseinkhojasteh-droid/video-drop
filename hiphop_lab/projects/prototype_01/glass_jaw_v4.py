"""GLASS JAW v4 — rebuilt from the story outward (the King's verdict on v3: soul 10/20, low end "muffled alien").

THE STORY (one city night, 2 AM, G-Unit-era menace)
  Scene 0  bars  1–4   COLD OPEN   rain-grey street, the piano heard through a car window (low-pass opening), vinyl hiss,
                                   one 808 note on the last beat = the car door shuts.
  Scene 1  bars  5–12  THE BLOCK   impact + full drums: the crew steps out. Horns answer the piano in bars 4 and 8 of the hook.
  Scene 2  bars 13–28  THE WALK    verse: thinner piano, the MC talks. 25–28 = something is pulling up: strings climb a semitone
                                   ladder (Gb→G→Ab→A), piano repeats its stab on every beat, hats double, snare roll, one beat of
                                   silence, a reverse swell — then
  Scene 3  bars 29–36  THE HIT     the drop: 808 glides C1→F1 under an impact, choir pad, horn stabs every 2 bars, open hats.
  Scene 4  bars 37–52  AFTERMATH   verse 2; bars 45–52 = the switch: half-time (snare on 3 only), piano down an octave at half speed,
                                   a bell answers, 808 slides, no hats; 51–52 rebuild (hats 16ths, snare roll, riser).
  Scene 5  bars 53–60  STANDING    hook 3 at full size: shaker 16ths, strings an octave up, horns every bar.
  Scene 6  bars 61–64  DAWN        drums leave, piano closes through the filter, one last 808 boom + the final chord, the vinyl stops.

LOW END LAW (v3 failure: kick had 78 % of its energy in 40–60 Hz and 0 % above 250 Hz, peak 6 dB under the snare; bass peak −15 dBFS):
  kick = sampled transient + knock (60–200 Hz) + click (3 kHz), peak ≥ snare peak; 808 = tuned sine with drive (2nd harmonic at ~87 Hz
  for car systems) + 90 Hz presence, long decay, glides; 808 ducked 6 dB by the kick; mix band shares checked against Candy Shop /
  In Da Club (40–60 ≈ 25–40 %, 60–150 ≈ 30–40 %, 20–40 ≤ 10 %).
"""
import sys, os, json
sys.path.insert(0, 'scripts/engine'); sys.path.insert(0, 'projects/prototype_01')
import numpy as np, pedalboard as pb, scipy.signal as ss
from paths import VST3_DIR, SURGE_DIR
import dsp
from dsp import SR
from render import Song, Track, Note, render_track, export
from theory import n
from folder_sampler import FolderSampler
from sfz import SFZ
import concepts as C

BPM = 90.0
OUT = 'projects/prototype_01/renders/glass_jaw_v4'
SURGE = SURGE_DIR
LIB = 'sound_library/incoming/'

M1 = [(0, .22, 'F3', 112), (0.75, .22, 'F3', 96), (1.5, .3, 'Ab3', 108), (2.0, .45, 'Gb3', 116), (2.75, .22, 'F3', 100)]
M2 = [(0, .22, 'C3', 112), (0.75, .22, 'Db3', 104), (1.5, .3, 'C3', 100), (2.5, .22, 'Eb3', 108), (3.0, .5, 'Db3', 112)]
B1 = [(0, .9, 'F1', 118), (.75, .5, 'F1', 104), (2.5, 1.2, 'F1', 112)]
B2 = [(0, .9, 'C2', 116), (.75, .5, 'Db2', 106), (2.5, .5, 'Eb2', 108), (3.0, .95, 'Db2', 112)]
HORN = [(3.0, .3, 'F3', 110), (3.5, .3, 'Gb3', 104), (3.75, .25, 'F3', 96)]       # answer in the last beat of the bar
BELL = [[(1.5, .5, 'Ab5', 90), (2.0, .5, 'Gb5', 84), (2.5, 1.0, 'F5', 96)], [(1.5, .5, 'Db5', 88), (2.5, 1.5, 'C5', 92)]]
FORM = [('intro', 4), ('hook', 8), ('verse', 16), ('drop', 8), ('verse2', 16), ('hook3', 8), ('outro', 4)]


def plan_bars():
    P = []; bar = 0
    for sec, L in FORM:
        for i in range(L):
            p = dict(bar=bar, sec=sec, i=i, odd=bar % 2 == 1, kick=True, snare=True, hats='8', open_hat=False, shaker=False, roll=False,
                     piano='thin', piano_lp=None, cello=False, strings=None, choir=False, horn=False, bell=False, bass=True,
                     half=False, build=False, vinyl=False)
            if sec == 'intro':
                p.update(kick=False, snare=False, hats=None, bass=False, piano='full', piano_lp=[500, 900, 1800, 5000][i], vinyl=True)
            elif sec == 'hook':
                p.update(piano='full', cello=True, strings='low', horn=(i % 4 == 3), open_hat=p['odd'], roll=(i == 7))
            elif sec == 'verse':
                drop = i in (0, 8)
                p.update(kick=not drop, bass=not drop, piano_lp=4500, cello=(8 <= i < 12 and i % 2 == 0))
                if i >= 12:  # the build, bars 25-28
                    p.update(build=True, strings='ladder', piano='stab' if i >= 14 else 'thin', hats='16' if i >= 14 else '8',
                             roll=(i == 15), kick=(i != 15), bass=(i < 14), open_hat=(i == 13))
            elif sec == 'drop':
                p.update(piano='full', cello=True, strings='low', choir=True, horn=(i % 2 == 1), open_hat=True, hats='16' if i >= 4 else '8', roll=(i == 7))
            elif sec == 'verse2':
                if i < 8:
                    p.update(kick=(i != 0), bass=(i != 0), piano_lp=4500, cello=(i >= 4 and i % 2 == 0))
                elif i < 14:
                    p.update(half=True, hats=None, shaker=True, piano='half', bell=(i % 2 == 1), strings='lowlow', cello=False)
                else:
                    p.update(build=True, hats='16', roll=(i == 15), strings='ladder', piano='stab', bass=(i == 14))
            elif sec == 'hook3':
                p.update(piano='full', cello=True, strings='high', choir=True, horn=True, shaker=True, open_hat=p['odd'], hats='16', roll=(i == 7))
            else:  # outro
                p.update(kick=False, snare=False, hats='8' if i == 0 else None, bass=(i == 3), piano=['full', 'thin', 'chord', 'chord'][i],
                         piano_lp=[None, 6000, 2500, 1200][i], strings='low' if i < 2 else None, cello=(i == 0), vinyl=(i >= 2))
            P.append(p); bar += 1
    return P


# ------------------------------------------------------------------------------------------------ sound design
def layered_kick():
    """Sampled transient + knock + click, saturated. Peak-normalised."""
    rusty = SFZ(LIB + 'karoryfer.big-rusty-drums/Programs/02-basic.sfz')
    a = rusty.render_note(36, 127, 0.5)
    if a is None: a = C.kit('virt').render_note(36, 127, 0.5)
    b = C.kit('virt').render_note(36, 127, 0.5)
    L = max(len(a), len(b)); k = np.zeros((L, 2), np.float32)
    k[:len(a)] += dsp.bpf(a, 55, 220, order=2) * 1.2            # knock
    k[:len(b)] += dsp.hp(b, 1500, order=2) * 0.9                  # click/beater
    # synthetic thump glues the two (60 Hz, 120 ms)
    t = np.arange(int(0.25 * SR)) / SR; th = np.sin(2 * np.pi * (54 * (1 + 1.5 * np.exp(-t / 0.012))).cumsum() / SR) * np.exp(-t / 0.07)
    k[:len(t)] += np.stack([th, th], 1) * 0.55
    k = dsp.peq(k, 75, 3, 1.0); k = dsp.peq(k, 3200, 4, 1.2); k = dsp.sat(k, 7)
    k = k[:int(0.45 * SR)] * np.minimum(1, (len(k[:int(0.45 * SR)]) - np.arange(len(k[:int(0.45 * SR)]))) / (0.03 * SR))[:, None]
    return (k / np.abs(k).max()).astype(np.float32)


def layered_snare():
    vk = C.kit('virt')
    rim = vk.render_note(40, 127, 0.3); cen = vk.render_note(38, 120, 0.3); cl = dsp.clap_synth(seed=9)
    t = np.arange(int(0.12 * SR)) / SR; body = np.sin(2 * np.pi * 190 * t) * np.exp(-t / 0.045)
    L = max(len(rim), len(cen), len(cl)); s = np.zeros((L, 2), np.float32)
    s[:len(rim)] += rim * 0.9; s[:len(cen)] += cen * 0.5; s[:len(cl)] += np.stack([cl, cl], 1) * 0.7; s[:len(t)] += np.stack([body, body], 1) * 0.5
    s = dsp.peq(s, 200, 2, 1.2); s = dsp.peq(s, 5000, 3, 0.9); s = dsp.sat(s, 4)
    return (s / np.abs(s).max()).astype(np.float32)


def bass_808_v4(notes, spb, total_s, decay=0.75, drive_db=7, sr=SR):
    """notes = (beat, dur, midi, vel[, glide_from_midi]). Sine + pitch kick + glide + drive; 2nd-harmonic presence for small speakers."""
    N = int(total_s * sr); y = np.zeros(N)
    for nt in sorted(notes):
        beat, dur, m, vel = nt[:4]; gfrom = nt[4] if len(nt) > 4 else None
        s = int(beat * spb * sr); L = min(int((dur * spb + 0.15) * sr), N - s)
        if L <= 0: continue
        t = np.arange(L) / sr; f0 = 440 * 2 ** ((m - 69) / 12)
        f = f0 * (1 + 1.4 * np.exp(-t / 0.014))
        if gfrom is not None:
            fg = 440 * 2 ** ((gfrom - 69) / 12); g = int(min(L, 0.35 * sr))
            f[:g] = np.geomspace(fg, f0, g) * (1 + 1.4 * np.exp(-t[:g] / 0.014))
        x = np.sin(2 * np.pi * np.cumsum(f) / sr) * np.exp(-t / decay) * (vel / 127)
        x *= np.minimum(1, t / 0.002) * np.minimum(1, (L - np.arange(L)) / (0.03 * sr))
        y[s:s + L] = x + y[s:s + L] * np.exp(-np.arange(L) / (0.003 * sr))
    y = dsp.sat(y, drive_db)
    y2 = np.stack([y, y], 1)
    y2 = dsp.peq(y2, 88, 1.0, 1.0); y2 = dsp.lp(y2, 2500, order=2)
    return (y2 / (np.abs(y2).max() + 1e-9)).astype(np.float32)


def duck(x, trigger_times, depth_db=-6, att_ms=4, rel_ms=90, sr=SR):
    env = np.ones(len(x))
    a = int(att_ms * 1e-3 * sr); r = int(rel_ms * 1e-3 * sr); d = 10 ** (depth_db / 20)
    for t in trigger_times:
        i = int(t * sr)
        if i >= len(x): continue
        env[i:i + a] = np.minimum(env[i:i + a], np.linspace(1, d, min(a, len(x) - i)))
        j = i + a; seg = np.linspace(d, 1, min(r, max(0, len(x) - j)))
        env[j:j + len(seg)] = np.minimum(env[j:j + len(seg)], seg)
    return x * env[:, None]


def riser(dur_s, sr=SR, seed=5):
    """Band-limited noise sweep 300 → 6000 Hz + rising sine; short, belongs to the drum world."""
    N = int(dur_s * sr); t = np.arange(N) / sr; rng = np.random.default_rng(seed)
    nz = rng.standard_normal(N); out = np.zeros(N); hop = 1024
    for i in range(0, N, hop):
        fc = 300 * (6000 / 300) ** (i / N); seg = nz[i:i + hop]
        sos = ss.butter(2, [fc / 1.6, min(fc * 1.6, sr / 2 - 1)], 'bandpass', fs=sr, output='sos')
        out[i:i + hop] = ss.sosfilt(sos, seg)
    env = (t / dur_s) ** 2.2
    y = out / (np.abs(out).max() + 1e-9) * env
    return np.stack([y, y * 0.9], 1).astype(np.float32)


def impact(sr=SR, seed=6):
    """Sub drop 70 → 32 Hz + saturated noise burst; the 'hit' at a drop."""
    N = int(1.6 * sr); t = np.arange(N) / sr
    f = 70 * (32 / 70) ** np.minimum(1, t / 0.5); sub = np.sin(2 * np.pi * np.cumsum(f) / sr) * np.exp(-t / 0.55)
    nz = dsp.bpf(np.random.default_rng(seed).standard_normal(N), 150, 4000) * np.exp(-t / 0.12)
    y = dsp.sat(sub * 1.0 + nz * 0.35, 6)
    return (np.stack([y, y], 1) / np.abs(y).max()).astype(np.float32)


def reverse_cymbal(oh, sr=SR):
    x = oh[::-1].copy(); x = x * np.linspace(0, 1, len(x))[:, None] ** 1.5
    return dsp.hp(x, 2500)


def place(buf, x, t_s):
    s = int(t_s * SR)
    if s < 0: x = x[-s:]; s = 0
    L = min(len(x), len(buf) - s)
    if L > 0: buf[s:s + L] += x[:L]


def mix_bands(x):
    m = x.mean(1); S = np.abs(np.fft.rfft(m)) ** 2; f = np.fft.rfftfreq(len(m), 1 / SR); tot = S.sum()
    return {b: round(100 * S[(f >= a) & (f < b)].sum() / tot, 1) for a, b in [(20, 40), (40, 60), (60, 100), (100, 150), (150, 250), (250, 500), (500, 2000), (2000, 8000)]}


# ------------------------------------------------------------------------------------------------ build
def build():
    P = plan_bars(); bars = len(P)
    s = Song(BPM, bars, swing=63); spb = s.spb; T = s.length_s() + 7; N = int(T * SR)
    t_of = lambda beat, sw=63: s.beat_to_s(beat, sw)
    vk = C.kit('virt')
    KICK, SNARE = layered_kick(), layered_snare()
    HAT_C = [vk.render_note(42, v, 0.1) for v in (70, 90, 110)]
    HAT_O = vk.render_note(46, 100, 0.4)
    shk = vk.render_note(82, 100, 0.2)
    if shk is None:
        shk = np.stack([dsp.hp(dsp.hat_synth(), 6000)] * 2, 1) * 0.6
    stems = {k: np.zeros((N, 2), np.float32) for k in ('kick', 'snare', 'hats', 'shaker', 'piano', 'cello', 'strings', 'bass', 'fx', 'vinyl')}
    kick_times = []
    P_notes, CE, BL, HORN_N, BELL_N, CHOIR_N = [], [], [], [], [], []
    for p in P:
        o = p['bar'] * 4; odd = p['odd']; mot = M2 if odd else M1
        # ---- drums
        if p['kick']:
            if p['half']:
                kt = (0, 2.5) if not odd else (0, 1.75, 2.5)
            elif p['build'] and p['i'] in (14,) and p['sec'] == 'verse':
                kt = (0, 1, 2, 3)
            else:
                kt = (0, 0.75, 2.5) + ((3.75,) if odd else ())
            for x in kt:
                tt = t_of(o + x); kick_times.append(tt); place(stems['kick'], KICK * (1.0 if x == 0 else 0.92), tt)
        if p['snare']:
            st = (2,) if p['half'] else (1, 3)
            for x in st: place(stems['snare'], SNARE, t_of(o + x) + 0.006)
        if p['roll']:
            for j in range(8):
                v = 0.25 + 0.75 * j / 7
                place(stems['snare'], SNARE * v * 0.8, t_of(o + 3 + j * 0.125))
        if p['hats'] == '8':
            for i in range(8):
                v = 2 if i % 2 == 0 else 0; place(stems['hats'], HAT_C[v] * (0.8 if i % 2 else 1), t_of(o + i * .5))
        elif p['hats'] == '16':
            for i in range(16):
                v = 2 if i % 4 == 0 else (1 if i % 2 == 0 else 0); place(stems['hats'], HAT_C[v] * (0.7 + 0.3 * (i % 4 == 0)), t_of(o + i * .25))
        if p['open_hat']: place(stems['hats'], HAT_O * 0.8, t_of(o + 3.5))
        if p['shaker']:
            for i in range(16): place(stems['shaker'], shk * (0.9 if i % 2 == 0 else 0.55), t_of(o + i * .25))
        # ---- piano
        if p['piano'] == 'full':
            for st_, du, nm, ve in mot: P_notes += [Note(o + st_, du, n(nm), ve), Note(o + st_, du, n(nm) + 12, ve - 14)]
        elif p['piano'] == 'thin':
            for st_, du, nm, ve in mot: P_notes.append(Note(o + st_, du, n(nm), ve - 12))
        elif p['piano'] == 'stab':
            for b_ in range(4): P_notes += [Note(o + b_, .2, n('F3'), 112), Note(o + b_ + .5, .18, n('Gb3'), 100)]
        elif p['piano'] == 'half':
            half = M1 if (p['i'] // 2) % 2 == 0 else M2
            k2 = (p['i'] % 2) * 2  # which half of the doubled motif this bar carries
            for st_, du, nm, ve in half:
                st2 = st_ * 2
                if k2 <= st2 < k2 + 4: P_notes += [Note(o + st2 - k2, du * 2, n(nm) - 12, ve - 6), Note(o + st2 - k2, du * 2, n(nm), ve - 20)]
        elif p['piano'] == 'chord':
            if p['i'] == 2: P_notes += [Note(o, 3.8, n('F2'), 92), Note(o, 3.8, n('C3'), 84), Note(o, 3.8, n('Gb3'), 88), Note(o, 3.8, n('F4'), 78)]
            else: P_notes += [Note(o, 6, n('F2'), 96), Note(o, 6, n('C3'), 86), Note(o, 6, n('F3'), 90), Note(o, 6, n('Ab4'), 76)]
        if p['cello']: CE += [Note(o + st_, du + .1, n(nm) - 12, ve - 8) for st_, du, nm, ve in mot]
        if p['horn']: HORN_N += [Note(o + st_, du, n(nm), ve) for st_, du, nm, ve in HORN]
        if p['bell']: BELL_N += [Note(o + st_, du, n(nm), ve) for st_, du, nm, ve in BELL[(p['i'] // 2) % 2]]
        if p['choir']: CHOIR_N += [Note(o, 4.1, n(x), 70) for x in (('F3', 'C4', 'Gb4') if not odd else ('C3', 'Ab3', 'Db4'))]
        # ---- bass
        if p['bass']:
            if p['sec'] == 'outro': BL.append((o, 5.0, n('F1'), 124))
            elif p['half']:
                BL += [(o, 2.2, n('F1'), 118, n('Db1') if odd else None), (o + 2.5, 1.3, n('Db1') if odd else n('F1'), 108)] if not odd else [(o, 2.2, n('C2'), 116, n('F1')), (o + 2.5, 1.3, n('Db2'), 108)]
            elif p['sec'] in ('drop',) and p['i'] == 0:
                BL += [(o, 1.4, n('F1'), 124, n('C1')), (o + 2.5, 1.2, n('F1'), 112)]
            else:
                BL += [(o + st_, du, n(nm), ve) for st_, du, nm, ve in (B2 if odd else B1)]
        if p['sec'] == 'intro' and p['i'] == 3: BL.append((o + 3, 1.0, n('F1'), 110))
        # ---- vinyl & fx events
        if p['vinyl']: place(stems['vinyl'], dsp.vinyl(int(4 * spb * SR), level_db=-30, seed=p['bar']), t_of(o, 50))
    # strings
    vs = C.kit('vln_sus')
    def vln(nm, bar, bars_, vel=66, oct_=0):
        x = vs.render_note(n(nm) + oct_, vel, bars_ * 4 * spb); place(stems['strings'], x, bar * 4 * spb)
    for p in P:
        st = p['strings']
        if st == 'low' and p['i'] % 2 == 0: vln('Gb5' if (p['i'] // 2) % 2 == 0 else 'F5', p['bar'], 2)
        elif st == 'high' and p['i'] % 2 == 0: vln('Gb5' if (p['i'] // 2) % 2 == 0 else 'F5', p['bar'], 2, 74, 12)
        elif st == 'lowlow' and p['i'] % 2 == 0: vln('Gb4', p['bar'], 2, 60)
        elif st == 'ladder':
            j = p['i'] - 12 if p['sec'] == 'verse' else 2 + (p['i'] - 14)
            vln(['Gb5', 'G5', 'Ab5', 'A5'][j], p['bar'], 1, 70 + 4 * j)
    # clean stems of the two 'build' bars 14 & 15 of verse2 that mis-index ladder (safe: ladder j in 0..3 handled)
    # cello
    cs = C.kit('cello_spic')
    for nt in CE: place(stems['cello'], cs.render_note(nt.pitch, nt.vel, nt.dur * spb), t_of(nt.beat, 50))
    stems['cello'] = dsp.width(dsp.hp(stems['cello'], 70), 0.3)
    # piano (sampled, per-bar filter automation)
    pz = render_track(s, Track('piano', ('sfz', C.kit('piano')), P_notes, swing=50, fx=C.board(pb.HighpassFilter(140), pb.Compressor(threshold_db=-18, ratio=3, attack_ms=2, release_ms=60))), tail_s=7)[:N]
    pz = np.pad(pz, ((0, N - len(pz)), (0, 0))); out = np.zeros_like(pz)
    for p in P:
        a = int(t_of(p['bar'] * 4, 50) * SR); b = int(t_of(p['bar'] * 4 + 4, 50) * SR) if p['bar'] < bars - 1 else N
        seg = pz[a:b]
        if p['piano_lp']: seg = dsp.lp(seg, p['piano_lp'], order=2)
        out[a:b] += seg
    stems['piano'] = dsp.width(out, 0.4)
    # horns (VSCO F horn staccato), bell + choir (Surge)
    hs = FolderSampler(LIB + 'VSCO-2-CE/Brass/F Horn/stac', release=0.2)
    hb = np.zeros((N, 2), np.float32)
    for nt in HORN_N:
        for oc in (0, 12): place(hb, hs.render_note(nt.pitch + oc, nt.vel, nt.dur * spb) * (1 if oc == 0 else 0.6), t_of(nt.beat, 50))
    stems['horns'] = dsp.width(dsp.hp(hb, 180), 0.5)
    bell = render_track(s, Track('bell', ('vst', 'Surge XT.vst3', SURGE + 'Plucks/Bell 1.fxp', None), BELL_N, swing=50, pan=0.25), tail_s=7)[:N]
    stems['bell'] = np.pad(dsp.hp(bell, 400), ((0, N - len(bell)), (0, 0)))
    choir = render_track(s, Track('choir', ('vst', 'Surge XT.vst3', SURGE + 'Pads/Retro Choir.fxp', None), CHOIR_N, swing=50), tail_s=7)[:N]
    stems['choir'] = dsp.width(dsp.lp(dsp.hp(np.pad(choir, ((0, N - len(choir)), (0, 0))), 250), 3500), 0.7)
    # bass 808 + duck by kick
    stems['bass'] = duck(bass_808_v4(BL, spb, T)[:N], kick_times)
    # FX: impacts at bar 5, 29, 53; reverse cymbal into 5/29/53; risers into 29 and 53; one beat of silence before 29 & 53 (applied below)
    IMP = impact(); RC = reverse_cymbal(HAT_O); RS = riser(4 * spb)
    for hb_ in (4, 28, 52):
        d = t_of(hb_ * 4, 50); place(stems['fx'], IMP * 0.9, d); place(stems['fx'], RC * 0.7, d - len(RC) / SR)
        if hb_ > 4:
            place(stems['fx'], RS * 0.5, d - 4 * spb)
            src = stems['piano'][int((d - 2 * spb) * SR):int(d * SR)]; rev = src[::-1] * np.linspace(0, 1, len(src))[:, None] ** 2
            place(stems['fx'], dsp.hp(rev, 300) * 0.8, d - 2 * spb)
    # the silence beat: everything but fx muted for the last beat before bars 29 and 53
    for hb_ in (28, 52):
        a = int(t_of(hb_ * 4 - 1, 50) * SR); b = int(t_of(hb_ * 4, 50) * SR); fade = int(0.008 * SR)
        for k in stems:
            if k in ('fx',): continue
            stems[k][a + fade:b] = 0; stems[k][a:a + fade] *= np.linspace(1, 0, fade)[:, None]
    # ---- gains (dB) — set by design, then the low end is verified against the reference band shares on the drop
    G = dict(kick=0.0, snare=-1.0, hats=-5, shaker=-10, piano=-3, cello=-10, strings=-11, bass=-2.0, fx=-6, vinyl=-14, horns=-6, bell=-9, choir=-12)
    sends = dict(snare=0.07, piano=0.14, cello=0.12, strings=0.35, horns=0.25, bell=0.3, choir=0.25, fx=0.2)
    def mixed(G):
        mix = np.zeros((N, 2), np.float32); send = np.zeros((N, 2), np.float32)
        for k, v in stems.items():
            g = 10 ** (G[k] / 20); mix += v * g
            if k in sends: send += v * g * sends[k]
        rv = C.board(pb.Reverb(room_size=0.42, damping=0.55, wet_level=1.0, dry_level=0.0, width=0.8))(send)
        mix += dsp.width(dsp.hp(rv, 300), 0.6)
        return mix
    a, b = int(t_of(28 * 4, 50) * SR), int(t_of(36 * 4, 50) * SR)
    # LOW-END LAW, measured on the drop: the 808 is the bass line, so its 35-120 Hz RMS sits +1 dB over the kick's; kick peak = snare peak +1.5 dB.
    def lowrms(x): return 20 * np.log10(np.sqrt(np.mean(dsp.bpf(x[a:b], 35, 120) ** 2)) + 1e-9)
    kp = 20 * np.log10(np.abs(stems['kick'][a:b]).max()); sp = 20 * np.log10(np.abs(stems['snare'][a:b]).max())
    G['kick'] = G['snare'] + 1.5 - (kp - sp)
    G['bass'] = G['kick'] + lowrms(stems['kick']) + 1.0 - lowrms(stems['bass'])
    bd = mix_bands(mixed(G)[a:b])
    print('gains', {k: round(v, 1) for k, v in G.items()}); print('drop bands pre-master', bd)
    mix = mixed(G)
    end = int(s.length_s() * SR); tail = np.abs(mix[end:]).max(1); q = np.where(tail > 10 ** (-60 / 20))[0]
    mix = mix[:end + (q[-1] if len(q) else 0) + int(0.4 * SR)]; fd = int(0.4 * SR); mix[-fd:] *= np.linspace(1, 0, fd)[:, None]
    # master: gentle glue, soft clip high threshold (keep the 808 shape), true-peak limiter, loudness to -9.6 LUFS
    y = dsp.compress(mix, thr_db=-16, ratio=1.8, att_ms=40, rel_ms=200, knee_db=8)
    g = 0.0
    for _ in range(7):
        z = dsp.true_peak_limit(dsp.soft_clip(y * 10 ** (g / 20), thr=0.94), -1.0)
        l = dsp.lufs(z)
        if abs(l + 10.2) < 0.15: break
        g += (-10.2 - l)
    export(OUT, z)
    for k, v in stems.items(): export(OUT + '_stems/' + k, (v * 10 ** (G[k] / 20))[:len(z)], mp3=False)
    info = dict(bars=bars, bpm=BPM, form=FORM, duration_s=round(len(z) / SR, 2), gains=G, metrics=C.metrics(z), drop_bands=mix_bands(z[a:b]))
    json.dump(info, open(OUT + '.json', 'w'), indent=1, default=float); print(json.dumps(info, default=float))


if __name__ == '__main__':
    build()
