"""GLASS JAW v8 — v7 = 15.5/20. Fixes: 0:11-0:19 transition (prelude lands softly on Fm where the riff begins; riff enters right-hand only, under one continuous filter sweep and a volume fade, heartbeat from bar 6 and softer); tag style=soft (warm whisper) to match the soft, artistic beat.
GLASS JAW v7 — v6 notes: tag robotic/beepy -> dark Kanye-style tag; intro piano sounded like random keys -> composed PRELUDE (prelude.py), filter opening on a smooth curve, same prelude closes the song.
GLASS JAW v6 — v5 scored 13/20. Fixes: (1) ONE swing grid for every instrument (v5 had the kick swung on the 1a/4a but the 808 straight = ~40 ms flam, "two machines against each other"); piano lay-back cut to 3 ms; (2) the intro IS the King's favourite moment — the pianist cadence — then the crime ladder teaser, then the GOLDEN V signature, a 1/16 breath and the BOOM; (3) the outro no longer brakes: a one-beat stop, an impact, and the intro theme returns (full circle).

Previous notes (v5): the King's notes on v4 (12/20):
  KEEP: the booms (kick/808), the 'crime' string ladder at ~1:09, the boom-bap pocket, the piano's fast-stab excitement.
  FIX : intro too ordinary · main piano riff basic/mechanical · drums not natural · the fast snare roll sounds like a child ·
        piano gets boring · outro chords unmusical.

What changed (all in this file; sound design helpers reused from v4):
  PIANO  — a real two-hand part. Harmony i (Fm) -> bII (Gb, Neapolitan) -> V7b9 (C7b9): harmonic-minor/Phrygian noir.
           RH voiced dyads/triads with grace-note appoggiaturas (Gb->F), LH octave roots; 4 riff variants (A, B, A', B'),
           chords rolled 8-22 ms low->high, velocity shaped by beat strength + random +-7, RH lays back +6..+14 ms, +-5 ms jitter,
           tape-warm tone. Verse = RH only (808 carries the root); stab bursts kept for builds and the end of every hook.
  DRUMS  — every hit humanised: velocity-layered round-robin snare variants, ghost notes (vel 28-45) at 1.75/3.75 in verses,
           hats with accent pattern + random drop/double, kick +-3 ms, snare lays back 8+-4 ms, crash after fills,
           small Dragonfly room on the drum bus + parallel compression. The 32nd roll is gone: fills are tom/snare phrases.
  INTRO  — rain/vinyl, low cello drone, a rubato high piano line, a heartbeat kick (low-passed), the riff fading in under the filter.
  OUTRO  — drums out, riff thins, a tape-stop on the beat, then a rubato pianist cadence Dbmaj7 -> C7b9 -> Fm(add9) with the last boom.
"""
import sys, os, json, random
sys.path.insert(0, 'scripts/engine'); sys.path.insert(0, 'projects/prototype_01')
import numpy as np, pedalboard as pb
from paths import VST3_DIR, SURGE_DIR
import dsp
from dsp import SR
from render import Song, Track, Note, render_track, export
from theory import n
from folder_sampler import FolderSampler
import concepts as C
import glass_jaw_v4 as V4
from prelude import prelude_events

BPM = 90.0
OUT = 'projects/prototype_01/renders/glass_jaw_v8'
SW = 57.0   # the single swing value every part is placed on
SURGE = SURGE_DIR
LIB = 'sound_library/incoming/'
RNG = random.Random(51)
FORM = [('intro', 8), ('hook', 8), ('verse', 16), ('drop', 8), ('verse2', 16), ('hook3', 8), ('outro', 4)]

# ------------------------------------------------------------------ the new piano part (beats inside one bar)
# each event: (beat, dur, [notes], role)  role: 'R' right hand, 'L' left hand, 'G' grace note (played 0.07 beat early)
RIFF_A = [(0.0, 1.3, ['F2', 'F3'], 'L'), (0.0, .45, ['Ab3', 'C4', 'F4'], 'R'),
          (0.7, .06, ['Gb4'], 'G'), (0.75, .25, ['F4'], 'R'),
          (1.5, .4, ['Ab3', 'Db4'], 'R'), (1.5, .9, ['C3'], 'L'),
          (2.5, .9, ['F2'], 'L'), (2.75, .3, ['Gb3', 'C4'], 'R'),
          (3.25, .2, ['F4'], 'R'), (3.5, .45, ['Ab4'], 'R')]
RIFF_B = [(0.0, 1.3, ['Gb2', 'Gb3'], 'L'), (0.0, .5, ['Bb3', 'Db4', 'Gb4'], 'R'), (0.75, .22, ['Bb3', 'Db4', 'F4'], 'R'),
          (1.5, .45, ['Ab3', 'C4', 'F4'], 'R'), (1.5, .9, ['Db3'], 'L'),
          (2.5, 1.4, ['C2', 'C3'], 'L'), (2.5, .3, ['E3', 'Bb3', 'Db4'], 'R'), (3.0, .25, ['E3', 'Bb3', 'Db4'], 'R'),
          (3.5, .2, ['C4'], 'R'), (3.75, .2, ['Db4'], 'R')]
# variants: A' answers in the upper octave on beat 4, B' ends with a falling run into the next bar
RIFF_A2 = RIFF_A[:-2] + [(3.25, .18, ['C5'], 'R'), (3.5, .18, ['Db5'], 'R'), (3.75, .25, ['C5'], 'R')]
RIFF_B2 = RIFF_B[:-2] + [(3.25, .15, ['Db4'], 'R'), (3.5, .15, ['C4'], 'R'), (3.75, .2, ['Bb3'], 'R')]
RIFFS = [RIFF_A, RIFF_B, RIFF_A2, RIFF_B2]
B1 = [(0, .9, 'F1', 118), (.75, .5, 'F1', 104), (2.5, 1.2, 'F1', 112)]
B2 = [(0, .9, 'Db2', 116), (.75, .5, 'Db2', 104), (2.5, .5, 'Eb2', 108), (3.0, .95, 'C2', 112)]   # follows the new i - bII - V harmony


def plan_bars():
    P = []; bar = 0
    for sec, L in FORM:
        for i in range(L):
            p = dict(bar=bar, sec=sec, i=i, odd=bar % 2 == 1, var=(bar // 2) % 2, kick=True, snare=True, hats='8', open_hat=False,
                     shaker=False, fill=None, crash=False, ghosts=False, piano='full', piano_lp=None, cello=False, strings=None,
                     choir=False, horn=False, bell=False, bass=True, half=False, vinyl=False, heartbeat=False)
            if sec == 'intro':   # 0-3 the pianist alone in the rain · 4-5 riff behind the glass + heartbeat · 6-7 crime teaser, tag, boom
                p.update(kick=False, snare=False, hats=('8' if i >= 6 else None), bass=False,
                         piano=['theme', 'none', 'none', 'none', 'rh', 'rh', 'full', 'full'][i],
                         piano_lp=None, vinyl=(i < 6), heartbeat=(5 <= i < 8), cello=False,
                         strings=('ladder' if i >= 6 else None))
            elif sec == 'hook':
                p.update(cello=True, strings='low', horn=(i % 4 == 3), open_hat=p['odd'], crash=(i == 0),
                         fill='toms' if i == 7 else None, piano='stab_end' if i == 7 else 'full')
            elif sec == 'verse':
                drop = i in (0, 8)
                p.update(kick=not drop, bass=not drop, piano='rh', piano_lp=5000, ghosts=True, crash=(i == 0),
                         cello=(8 <= i < 12 and i % 2 == 0), fill='flam' if i in (3, 11) else None)
                if i >= 12:  # the crime build — the King's favourite moment, kept and sharpened
                    p.update(strings='ladder', piano='stab' if i >= 14 else 'rh', hats='16' if i >= 14 else '8', ghosts=False,
                             fill='build' if i == 15 else None, kick=(i != 15), bass=(i < 14), open_hat=(i == 13))
            elif sec == 'drop':
                p.update(cello=True, strings='low', choir=True, horn=(i % 2 == 1), open_hat=True, crash=(i in (0, 4)),
                         hats='16' if i >= 4 else '8', fill='toms' if i == 7 else None, piano='stab_end' if i in (3, 7) else 'full')
            elif sec == 'verse2':
                if i < 8:
                    p.update(kick=(i != 0), bass=(i != 0), piano='rh', piano_lp=5000, ghosts=True, crash=(i == 0),
                             cello=(i >= 4 and i % 2 == 0), fill='flam' if i == 3 else None)
                elif i < 14:
                    p.update(half=True, hats=None, shaker=True, piano='half', bell=(i % 2 == 1), strings='lowlow', cello=False)
                else:
                    p.update(hats='16', fill='build' if i == 15 else None, strings='ladder', piano='stab', bass=(i == 14), kick=(i != 15))
            elif sec == 'hook3':
                p.update(cello=True, strings='high', choir=True, horn=True, shaker=True, open_hat=p['odd'], hats='16', crash=(i in (0, 4)),
                         fill='toms' if i == 7 else None, piano='stab_end' if i in (3, 7) else 'full')
            else:  # outro: beat, beat with a one-beat stop, then BOOM + the intro theme returns (full circle)
                p.update(kick=(i < 2), snare=(i < 2), hats='8' if i < 2 else None, bass=(i < 2 or i == 2), piano=['full', 'rh', 'coda', 'coda'][i],
                         piano_lp=[None, 5000, None, None][i], strings='low' if i < 2 else None, cello=(i == 0), vinyl=(i >= 2), crash=(i == 0))
            P.append(p); bar += 1
    return P


# ------------------------------------------------------------------ humanised piano
SWB = lambda b: b  # replaced in build() by the song's swing-grid mapper (beats -> swung beats)


def piano_events(o, riff, spb, vel_scale=1.0, oct_shift=0, roles=('R', 'L', 'G'), lay_ms=3):
    out = []
    for beat, dur, notes, role in riff:
        if role not in roles: continue
        strength = 1.0 if beat in (0.0, 2.0) else 0.92 if beat in (1.0, 3.0) else 0.85
        base = (100 if role == 'L' else 96 if role == 'R' else 70) * strength * vel_scale
        jitter = RNG.gauss(0, 2) / 1000 / spb
        lay = (lay_ms + RNG.uniform(-2, 2)) / 1000 / spb if role != 'L' else 0.0
        roll = RNG.uniform(6, 14) / 1000 / spb if len(notes) > 1 else 0
        b0 = SWB(o + beat) + jitter + lay
        if role == 'G': b0 -= 0.0
        for k, nm in enumerate(notes):
            v = int(np.clip(base - 6 * (len(notes) - 1 - k) * (role == 'R') + RNG.gauss(0, 7), 25, 127))
            if role == 'R' and k == len(notes) - 1: v = min(127, v + 8)  # melody note on top sings
            out.append(Note(b0 + k * roll, dur * RNG.uniform(0.9, 1.15), n(nm) + oct_shift, v))
    return out


def coda_events(o, spb):
    """Rubato cadence over 2 bars: Dbmaj7 (rolled up) -> C7b9 (rolled, broken) -> Fm(add9) final chord, slower roll, held."""
    ev = []
    def roll(beat, notes, vel, dur, spread_ms):
        for k, nm in enumerate(notes):
            ev.append(Note(o + beat + k * spread_ms / 1000 / spb, dur, n(nm), int(np.clip(vel + RNG.gauss(0, 5) - 3 * k, 30, 120))))
    roll(0.0, ['Db2', 'Ab2', 'C4', 'F4', 'Ab4'], 82, 1.9, 38)            # bVI maj7: the sigh
    ev += [Note(o + 1.55, .4, n('C5'), 70), Note(o + 1.8, .5, n('Bb4'), 64)]   # a small falling answer
    roll(2.3, ['C2', 'G2', 'E3', 'Bb3', 'Db4'], 86, 1.6, 30)             # V7b9: the question
    ev += [Note(o + 3.2, .25, n('Db5'), 72), Note(o + 3.45, .25, n('C5'), 66), Note(o + 3.7, .35, n('Bb4'), 60), Note(o + 3.95, .6, n('E4'), 58)]
    roll(4.35, ['F1', 'F2', 'C3', 'Ab3', 'G4', 'C5'], 90, 4.5, 55)       # i(add9): the end, slow roll like a hand opening
    ev.append(Note(o + 5.9, 2.5, n('F5'), 52))                            # one last high note, very soft
    return ev


# ------------------------------------------------------------------ humanised drums
def drum_kit():
    vk = C.kit('virt')
    KICK = V4.layered_kick()
    base_sn = V4.layered_snare()
    snares = []
    for v in (112, 120, 127):
        cen = vk.render_note(38, v, 0.3); rim = vk.render_note(40, v, 0.3)
        L = max(len(cen), len(rim), len(base_sn)); s = np.zeros((L, 2), np.float32)
        s[:len(base_sn)] += base_sn * 0.75; s[:len(cen)] += cen * 0.35; s[:len(rim)] += rim * 0.25
        snares.append(s / np.abs(s).max())
    ghosts = [vk.render_note(38, v, 0.2) for v in (30, 38, 46)]
    hats = [vk.render_note(42, v, 0.1) for v in (55, 72, 90, 110)]
    toms = {k: vk.render_note(k, 112, 0.5) for k in (48, 45, 41)}
    toms = {k: (v if v is not None else vk.render_note(43, 112, 0.5)) for k, v in toms.items()}
    crash = vk.render_note(49, 105, 1.5)
    return dict(KICK=KICK, SN=snares, GH=ghosts, HAT=hats, HAT_O=vk.render_note(46, 100, 0.4), TOM=toms, CRASH=crash,
                SHK=vk.render_note(82, 100, 0.2))


def build():
    P = plan_bars(); bars = len(P)
    global SWB
    s = Song(BPM, bars, swing=SW); spb = s.spb; T = s.length_s() + 9; N = int(T * SR)
    t_of = lambda beat, sw=SW: s.beat_to_s(beat, SW)
    SWB = lambda b: s.beat_to_s(b, SW) / spb if abs(b * 4 - round(b * 4)) < 1e-6 else b
    K = drum_kit()
    if K['SHK'] is None: K['SHK'] = np.stack([dsp.hp(dsp.hat_synth(), 6000)] * 2, 1) * 0.6
    stems = {k: np.zeros((N, 2), np.float32) for k in ('kick', 'snare', 'hats', 'shaker', 'toms', 'cymbals', 'piano', 'cello', 'strings', 'bass', 'fx', 'vinyl', 'drone', 'theme')}
    place = V4.place
    kick_times = []
    PN, CE, BL, HORN_N, BELL_N, CHOIR_N, TH = [], [], [], [], [], [], []
    hum = lambda ms: RNG.gauss(0, ms) / 1000
    for p in P:
        o = p['bar'] * 4; odd = p['odd']; riff = RIFFS[(p['bar'] % 4)]
        # -------- drums
        if p['kick']:
            kt = ((0, 2.5) if not odd else (0, 1.75, 2.5)) if p['half'] else (0, 0.75, 2.5) + ((3.75,) if odd else ())
            for x in kt:
                tt = t_of(o + x) + hum(3); kick_times.append(tt)
                place(stems['kick'], K['KICK'] * (1.0 if x == 0 else RNG.uniform(0.85, 0.95)), tt)
        if p['snare']:
            for x in ((2,) if p['half'] else (1, 3)):
                sn = RNG.choice(K['SN'][1:]); place(stems['snare'], sn * RNG.uniform(0.9, 1.0), t_of(o + x) + 0.008 + hum(4))
        if p['ghosts']:
            for x in (1.75, 3.25) if odd else (1.75, 3.75):
                if RNG.random() < 0.8: place(stems['snare'], RNG.choice(K['GH']) * 0.9, t_of(o + x) + 0.006 + hum(5))
        if p['hats'] in ('8', '16'):
            step = 0.5 if p['hats'] == '8' else 0.25
            for i in range(int(4 / step)):
                pos = i * step
                if p['fill'] and pos >= 3: break
                acc = 3 if pos % 1 == 0 else (2 if pos % 0.5 == 0 else 1)
                if RNG.random() < 0.04: continue
                h = K['HAT'][min(3, max(0, acc + RNG.choice((-1, 0, 0, 0))))]
                place(stems['hats'], h * RNG.uniform(0.8, 1.0), t_of(o + pos) + hum(5))
                if step == 0.5 and RNG.random() < 0.06: place(stems['hats'], K['HAT'][0] * 0.7, t_of(o + pos + 0.25) + hum(4))
        if p['open_hat']: place(stems['hats'], K['HAT_O'] * 0.75, t_of(o + 3.5) + hum(4))
        if p['shaker']:
            for i in range(16): place(stems['shaker'], K['SHK'] * (0.9 if i % 2 == 0 else 0.55) * RNG.uniform(0.85, 1), t_of(o + i * .25) + hum(4))
        if p['crash']: place(stems['cymbals'], K['CRASH'] * 0.8, t_of(o) + hum(3))
        # fills: musical phrases instead of a machine roll
        if p['fill'] == 'toms':
            seq = [(3.0, 'SN', 0.9), (3.25, 48, 0.85), (3.5, 45, 0.9), (3.75, 41, 1.0)]
        elif p['fill'] == 'flam':
            seq = [(3.5, 'GH', 0.8), (3.52, 'SN', 0.7)]
        elif p['fill'] == 'build':
            seq = [(2.0, 'SN', .55), (2.5, 'SN', .65), (2.75, 48, .7), (3.0, 'SN', .8), (3.25, 45, .85), (3.5, 'SN', .9), (3.625, 41, .9), (3.75, 'SN', 1.0)]
        else:
            seq = []
        for x, what, g in seq:
            src = RNG.choice(K['SN']) if what == 'SN' else RNG.choice(K['GH']) if what == 'GH' else K['TOM'][what]
            place(stems['toms' if isinstance(what, int) else 'snare'], src * g * RNG.uniform(0.92, 1.0), t_of(o + x) + hum(6))
        # -------- piano
        pk = p['piano']
        if pk in ('full', 'stab_end'):
            PN += piano_events(o, riff[:-3] if pk == 'stab_end' else riff, spb)
            if pk == 'stab_end':
                for b_ in (2.5, 2.75, 3.0, 3.25, 3.5, 3.75): PN += piano_events(o, [(b_, .16, ['C3', 'C4'] if b_ < 3.5 else ['Db3', 'Db4'], 'R')], spb, 1.05, lay_ms=4)
        elif pk == 'rh':
            PN += piano_events(o, riff, spb, 0.82, roles=('R', 'G'))
        elif pk == 'stab':
            for b_ in range(4):
                PN += piano_events(o, [(b_, .2, ['F2', 'F3'], 'L'), (b_ + .5, .16, ['Gb3', 'C4'], 'R'), (b_ + .75, .14, ['F3', 'Ab3'], 'R')], spb, 1.0 + 0.04 * b_, lay_ms=4)
        elif pk == 'half':
            src = RIFFS[(p['i'] // 2) % 2]; k2 = (p['i'] % 2) * 2
            half = [(b_ * 2 - k2, d * 2, [x for x in nts], r) for b_, d, nts, r in src if k2 <= b_ * 2 < k2 + 4]
            PN += piano_events(o, half, spb, 0.85, oct_shift=-12, lay_ms=14)
        elif pk == 'coda' and p['i'] == 2:
            TH += prelude_events(o, spb, halves=4, final=True)
        elif pk == 'theme':
            TH += prelude_events(o, spb, halves=8)
            TH += [Note(o + 16 + k * 0.02 / spb, 7.0, n(x), 62 - 3 * k) for k, x in enumerate(['F2', 'C3', 'Ab3', 'C4', 'F4'])]   # the prelude lands on Fm exactly where the riff begins
        elif False:
            # the answer: rising F-Ab-C, then the b2 (Db) hanging, then the V7b9 rolled -> the riff enters on bar 5
            PN += [Note(o + 10.0, .6, n('F4'), 60), Note(o + 10.6, .6, n('Ab4'), 64), Note(o + 11.2, .7, n('C5'), 68), Note(o + 12.0, 1.6, n('Db5'), 72)]
            for k, nm in enumerate(['C2', 'G2', 'E3', 'Bb3', 'Db4']):
                PN.append(Note(o + 13.0 + k * 0.035 / spb, 2.8, n(nm), 80 - 3 * k))
        if False:   # (v5 rubato line replaced by the theme)
            line = [(0.5, 1.2, 'F5', 58), (1.9, .5, 'Gb5', 52), (2.5, 1.4, 'F5', 55)] if p['i'] == 0 else [(0.3, .8, 'Ab5', 54), (1.4, .7, 'Gb5', 50), (2.2, 1.8, 'C5', 56)]
            PN += [Note(o + b_ + hum(25) / spb, d, n(nm), v) for b_, d, nm, v in line]
        if p['cello']: CE += [Note(o + b_, d + .1, n(nts[0]) - (12 if r == 'R' else 0), 92) for b_, d, nts, r in riff if r in ('L',)]
        if p['horn']: HORN_N += [Note(o + b_, d, n(nm), v) for b_, d, nm, v in V4.HORN]
        if p['bell']: BELL_N += [Note(o + b_, d, n(nm), v) for b_, d, nm, v in V4.BELL[(p['i'] // 2) % 2]]
        if p['choir']: CHOIR_N += [Note(o, 4.1, n(x), 70) for x in (('F3', 'C4', 'Ab4') if not odd else ('Gb3', 'Db4', 'Bb4'))]
        # -------- 808
        if p['bass']:
            if p['sec'] == 'outro': BL.append((o, 3.5, n('F1'), 120))
            elif p['half']:
                BL += [(o, 2.2, n('F1'), 118), (o + 2.5, 1.3, n('C1') + 12, 108, n('F1'))] if not odd else [(o, 2.2, n('Gb1'), 116, n('F1')), (o + 2.5, 1.3, n('C1') + 12, 108)]
            elif p['sec'] == 'drop' and p['i'] == 0:
                BL += [(o, 1.4, n('F1'), 124, n('C1')), (o + 2.5, 1.2, n('F1'), 112)]
            else:
                for e in (B2 if odd else B1):
                    BL.append((o + e[0], e[1], n(e[2]) + (12 if e[2].startswith('C1') else 0), e[3]) + ((n(e[4]),) if len(e) > 4 else ()))
        if p['sec'] == 'outro' and p['i'] == 2: BL[-1] = (o, 7.5, n('F1'), 124, n('C1'))
        if p['heartbeat']:   # low-passed kick 'heartbeat' under the rain
            for x in (0, 0.5) if p['i'] < 3 else (0, 0.5, 2, 2.5):
                place(stems['fx'], dsp.lp(K['KICK'], 160) * (0.55 if x % 1 == 0 else 0.4) * (0.25 + 0.1 * (p['i'] - 5)), t_of(o + x))
        if p['vinyl']: place(stems['vinyl'], dsp.vinyl(int(4 * spb * SR), level_db=-30, seed=p['bar']), t_of(o))
    # -------- intro drone (cello sustain-ish low F, bars 1-4)
    cs_sus = FolderSampler(LIB + 'VSCO-2-CE/Strings/Cello Section/susvib', release=1.2)
    place(stems['drone'], cs_sus.render_note(n('F2'), 64, 6 * 4 * spb) * np.linspace(0, 1, int(len(cs_sus.render_note(n('F2'), 64, 6 * 4 * spb))))[:, None] ** 0.5, 0)
    # -------- strings (same voicing as v4: the King liked the crime ladder)
    vs = C.kit('vln_sus')
    def vln(nm, bar, bars_, vel=66, oct_=0):
        place(stems['strings'], vs.render_note(n(nm) + oct_, vel, bars_ * 4 * spb), bar * 4 * spb)
    for p in P:
        st = p['strings']
        if st == 'low' and p['i'] % 2 == 0: vln('Gb5' if (p['i'] // 2) % 2 == 0 else 'F5', p['bar'], 2)
        elif st == 'high' and p['i'] % 2 == 0: vln('Gb5' if (p['i'] // 2) % 2 == 0 else 'F5', p['bar'], 2, 74, 12)
        elif st == 'lowlow' and p['i'] % 2 == 0: vln('Gb4', p['bar'], 2, 60)
        elif st == 'ladder':
            j = p['i'] - 12 if p['sec'] == 'verse' else (p['i'] - 6) * 2 if p['sec'] == 'intro' else 2 + (p['i'] - 14)
            vln(['Gb5', 'G5', 'Ab5', 'A5'][j], p['bar'], 1, 70 + 4 * j)
    cs = C.kit('cello_spic')
    for nt in CE: place(stems['cello'], cs.render_note(nt.pitch, nt.vel, nt.dur * spb), t_of(nt.beat))
    stems['cello'] = dsp.width(dsp.hp(stems['cello'], 60), 0.3)
    # -------- piano render: warm tone (gentle comp, tape, top roll-off) + per-bar filter automation
    tape = pb.load_plugin(VST3_DIR + 'CHOWTapeModel.vst3')
    pz = render_track(s, Track('piano', ('sfz', C.kit('piano')), PN, swing=50,
                               fx=C.board(pb.HighpassFilter(70), pb.Compressor(threshold_db=-20, ratio=2.5, attack_ms=8, release_ms=120))), tail_s=9)[:N]
    pz = np.pad(pz, ((0, N - len(pz)), (0, 0)))
    pz = tape(pz.T.astype(np.float32), SR).T; pz = dsp.lp(pz, 9000, order=2); pz = dsp.peq(pz, 300, -2, 0.8)
    out = np.zeros_like(pz)
    for p in P:
        a = int(t_of(p['bar'] * 4, 50) * SR); b = int(t_of(p['bar'] * 4 + 4, 50) * SR) if p['bar'] < bars - 1 else N
        seg = pz[a:b]
        if p['piano_lp']: seg = dsp.lp(seg, p['piano_lp'], order=2)
        out[a:b] += seg
    # intro riff (bars 5-8): one continuous filter sweep 450 Hz -> open + a volume fade-in, so the listener never hears a 'phase change'
    i0, i1 = int(t_of(16) * SR), int(t_of(32) * SR)
    seg = out[i0:i1]; dk = dsp.lp(seg, 1100, order=2); L = len(seg)
    w = (np.arange(L) / L) ** 1.5; vol = np.minimum(1, 0.8 + 0.2 * np.arange(L) / (0.4 * L))
    out[i0:i1] = (dk * (1 - w[:, None]) + seg * w[:, None]) * vol[:, None]
    stems['piano'] = dsp.width(out, 0.45)
    th = render_track(s, Track('theme', ('sfz', C.kit('piano')), TH, swing=50,
                               fx=C.board(pb.HighpassFilter(45), pb.Compressor(threshold_db=-24, ratio=2, attack_ms=15, release_ms=150))), tail_s=9)[:N]
    th = np.pad(th, ((0, N - len(th)), (0, 0)))
    th = tape(th.T.astype(np.float32), SR).T; th = dsp.lp(th, 10000, order=2)
    dark = dsp.lp(th, 650, order=2)
    e0 = int(t_of(6) * SR)   # filter fully open after 1.5 bars
    w = np.ones(N); w[:e0] = (np.arange(e0) / e0) ** 1.6
    stems['theme'] = dsp.width(dark * (1 - w[:, None]) + th * w[:, None], 0.6)
    hs = FolderSampler(LIB + 'VSCO-2-CE/Brass/F Horn/stac', release=0.2); hb = np.zeros((N, 2), np.float32)
    for nt in HORN_N:
        for oc in (0, 12): place(hb, hs.render_note(nt.pitch + oc, nt.vel, nt.dur * spb) * (1 if oc == 0 else 0.6), t_of(nt.beat) + hum(6))
    stems['horns'] = dsp.width(dsp.hp(hb, 180), 0.5)
    bell = render_track(s, Track('bell', ('vst', 'Surge XT.vst3', SURGE + 'Plucks/Bell 1.fxp', None), BELL_N, swing=SW, pan=0.25), tail_s=9)[:N]
    stems['bell'] = np.pad(dsp.hp(bell, 400), ((0, N - len(bell)), (0, 0)))
    choir = render_track(s, Track('choir', ('vst', 'Surge XT.vst3', SURGE + 'Pads/Retro Choir.fxp', None), CHOIR_N, swing=SW), tail_s=9)[:N]
    stems['choir'] = dsp.width(dsp.lp(dsp.hp(np.pad(choir, ((0, N - len(choir)), (0, 0))), 250), 3500), 0.7)
    BL = [(SWB(e[0]),) + tuple(e[1:]) for e in BL]
    stems['bass'] = V4.duck(V4.bass_808_v4(BL, spb, T)[:N], kick_times)
    # -------- FX: impacts, reverse cymbal, riser, reversed piano swell, the silence beat (as v4)
    IMP = V4.impact(); RC = V4.reverse_cymbal(K['HAT_O']); RS = V4.riser(4 * spb)
    for hb_ in (8, 32, 56):
        d = t_of(hb_ * 4); place(stems['fx'], IMP * 0.9, d); place(stems['fx'], RC * 0.7, d - len(RC) / SR)
        if hb_ > 8:
            place(stems['fx'], RS * 0.45, d - 4 * spb)
            src = stems['piano'][int((d - 2 * spb) * SR):int(d * SR)]; rev = src[::-1] * np.linspace(0, 1, len(src))[:, None] ** 2
            place(stems['fx'], dsp.hp(rev, 300) * 0.8, d - 2 * spb)
    for hb_ in (32, 56):
        a = int(t_of(hb_ * 4 - 1) * SR); b = int(t_of(hb_ * 4) * SR); fade = int(0.008 * SR)
        for k in stems:
            if k == 'fx': continue
            stems[k][a + fade:b] = 0; stems[k][a:a + fade] *= np.linspace(1, 0, fade)[:, None]
    # -------- drum bus: small room + parallel compression (natural, glued)
    room = pb.load_plugin(VST3_DIR + 'DragonflyRoomReverb.vst3')
    drum_keys = ('kick', 'snare', 'hats', 'toms', 'cymbals', 'shaker')
    G = dict(kick=0.0, snare=-1.0, hats=-6, shaker=-11, toms=-4, cymbals=-12, piano=-2.5, theme=-1.0, cello=-11, strings=-11, bass=-2.0, fx=-6,
             vinyl=-15, horns=-7, bell=-9, choir=-12, drone=-14)
    sends = dict(snare=0.07, piano=0.12, theme=0.22, cello=0.12, strings=0.35, horns=0.25, bell=0.3, choir=0.25, fx=0.2, drone=0.3)
    a, b = int(t_of(32 * 4) * SR), int(t_of(40 * 4) * SR)
    def lowrms(x): return 20 * np.log10(np.sqrt(np.mean(dsp.bpf(x[a:b], 35, 120) ** 2)) + 1e-9)
    kp = 20 * np.log10(np.abs(stems['kick'][a:b]).max()); sp = 20 * np.log10(np.abs(stems['snare'][a:b]).max())
    G['kick'] = G['snare'] + 1.5 - (kp - sp)
    G['bass'] = G['kick'] + lowrms(stems['kick']) + 1.0 - lowrms(stems['bass'])
    mix = np.zeros((N, 2), np.float32); send = np.zeros((N, 2), np.float32); dbus = np.zeros((N, 2), np.float32)
    for k, v in stems.items():
        g = 10 ** (G[k] / 20)
        if k in drum_keys: dbus += v * g
        else: mix += v * g
        if k in sends: send += v * g * sends[k]
    dr_room = room(dsp.hp(dbus, 200).T.astype(np.float32), SR).T * 0.12
    crushed = dsp.compress(dbus, thr_db=-24, ratio=6, att_ms=3, rel_ms=60, makeup_db=6)
    dbus = dbus + dsp.hp(dr_room, 300) + 0.22 * dsp.hp(crushed, 120)
    mix += dbus
    rv = C.board(pb.Reverb(room_size=0.42, damping=0.55, wet_level=1.0, dry_level=0.0, width=0.8))(send)
    mix += dsp.width(dsp.hp(rv, 300), 0.6)
    # -------- GOLDEN V signature: last 2 beats of the intro are cleared, the tag speaks, 1/16 breath, BOOM on bar 9
    import signature
    tag, lead = signature.golden_v_tag(BPM, [29, 41, 48, 56, 67, 72], C.kit('piano'), style='soft')
    d9 = int(t_of(8 * 4) * SR); c0 = d9 - int(lead * SR); fade = int(0.01 * SR)
    mix[c0 + fade:d9] = 0; mix[c0:c0 + fade] *= np.linspace(1, 0, fade)[:, None]
    mix[c0:c0 + len(tag)] += tag[:len(mix) - c0] * 0.5
    # -------- outro: one-beat stop at the end of outro bar 2, impact on bar 3 under the returning theme
    ob = [p['bar'] for p in P if p['sec'] == 'outro'][0]
    t0 = int(t_of((ob + 1) * 4 + 3) * SR); t1 = int(t_of((ob + 2) * 4) * SR)
    keep = mix[t1:].copy()
    mix[t0 + fade:t1] = 0; mix[t0:t0 + fade] *= np.linspace(1, 0, fade)[:, None]
    rc = V4.reverse_cymbal(K['HAT_O']) * 10 ** (-8 / 20); mix[t1 - len(rc):t1] += rc
    imp = V4.impact() * 10 ** (-7 / 20); mix[t1:t1 + len(imp)] += imp[:len(mix) - t1]
    end = int(s.length_s() * SR); tail = np.abs(mix[end:]).max(1); q = np.where(tail > 10 ** (-62 / 20))[0]
    mix = mix[:end + (q[-1] if len(q) else 0) + int(0.5 * SR)]; fd = int(0.6 * SR); mix[-fd:] *= np.linspace(1, 0, fd)[:, None]
    y = dsp.compress(mix, thr_db=-16, ratio=1.8, att_ms=40, rel_ms=200, knee_db=8)
    g = 0.0
    for _ in range(7):
        z = dsp.true_peak_limit(dsp.soft_clip(y * 10 ** (g / 20), thr=0.94), -1.0)
        l = dsp.lufs(z)
        if abs(l + 10.2) < 0.15: break
        g += (-10.2 - l)
    export(OUT, z)
    for k, v in stems.items(): export(OUT + '_stems/' + k, (v * 10 ** (G[k] / 20))[:len(z)], mp3=False)
    info = dict(bars=bars, bpm=BPM, form=FORM, duration_s=round(len(z) / SR, 2), gains={k: round(float(v), 1) for k, v in G.items()},
                metrics=C.metrics(z), drop_bands=V4.mix_bands(z[a:b]), piano_notes=len(PN))
    json.dump(info, open(OUT + '.json', 'w'), indent=1, default=float); print(json.dumps(info, default=float))


if __name__ == '__main__':
    build()
