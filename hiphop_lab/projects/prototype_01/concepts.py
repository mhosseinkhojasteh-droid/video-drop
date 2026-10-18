"""Prototype 01 — three original 8-bar concepts (Phase 9 step 1).

A  "SUNSET GHOST"   West Coast / G-funk   93 BPM, A dorian (Am9 <-> D9), light swing, whistle lead answers in bars 4 & 8
B  "GLASS JAW"      G-Unit street-club     90 BPM, F phrygian (b2 menace), staccato octave piano + cello, 808 bass, bounce swing
C  "CONCRETE PSALM" dark NY boom-bap       87 BPM, C minor jazz dissonance rendered as a fake 'record', SP-1200 drums, heavy late hats

All motifs are written here from scratch (no reference melody, riff or sample). Run: python3 -I projects/prototype_01/concepts.py [A B C]
"""
import sys, os, json
sys.path.insert(0, 'scripts/engine')
import numpy as np, pedalboard as pb
import dsp
from dsp import SR
from render import Song, Track, Note, render_track, mixdown, master_chain, export, auto_balance
from sfz import SFZ
from folder_sampler import FolderSampler
from theory import n, chord

LIB = 'sound_library/incoming/'
OUT = 'projects/prototype_01/renders/'
SURGE = '/usr/share/surge-xt/patches_factory/'

_cache = {}


def kit(name):
    if name not in _cache:
        _cache[name] = {'virt': lambda: SFZ(LIB + 'virtuosity_drums/Programs/01-basic-kit.sfz'),
                        'virt_vint': lambda: SFZ(LIB + 'virtuosity_drums/Programs/08-vintage-mic.sfz'),
                        'rusty': lambda: SFZ(LIB + 'karoryfer.big-rusty-drums/Programs/02-basic.sfz'),
                        'piano': lambda: SFZ(LIB + 'SalamanderGrandPiano/Salamander Grand Piano V3.sfz'),
                        'upright': lambda: SFZ(LIB + 'karoryfer.meatbass/Programs/pizz_three.sfz'),
                        'cello_spic': lambda: FolderSampler(LIB + 'VSCO-2-CE/Strings/Cello Section/spic', release=0.15),
                        'vln_sus': lambda: FolderSampler(LIB + 'VSCO-2-CE/Strings/Violin Section/susVib', release=0.6),
                        'growly': lambda: SFZ(LIB + 'karoryfer.growlybass/growlybass_clean.sfz', key_offset=12),
                        }[name]()
    return _cache[name]


def board(*plugins):
    b = pb.Pedalboard(list(plugins))
    return lambda x: b(x.T.astype(np.float32), SR).T


def oneshots_from_sfz(sfz, keys_vel):
    return {k: sfz.render_note(k, v, 0.5) for k, v in keys_vel.items()}


# ---------------------------------------------------------------------------------------------- A
def concept_A(bars=8):
    bpm = 93.0; s = Song(bpm, bars, swing=58)
    spb = s.spb
    # drums: tight sampled kick layered with short 808 body, snare + clap, swung hats
    vk = kit('virt')
    kick = vk.render_note(36, 120, 0.3)
    k808 = dsp.kick_808(f0=52, decay=0.22, pitch_drop=2.5, click=0.15, drive_db=6)
    n_ = max(len(kick), len(k808)); kk = np.zeros((n_, 2), np.float32); kk[:len(kick)] += kick * 0.8; kk[:len(k808)] += np.stack([k808, k808], 1) * 0.7
    sn = vk.render_note(38, 118, 0.3); cl = dsp.clap_synth(); sc = np.zeros((max(len(sn), len(cl)), 2), np.float32)
    sc[:len(sn)] += sn; sc[:len(cl)] += np.stack([cl, cl], 1) * 0.55
    shots = {36: kk, 38: sc, 42: vk.render_note(42, 90, 0.1), 46: vk.render_note(46, 85, 0.3)}
    K, S, H, O = [], [], [], []
    for b in range(bars):
        o = b * 4
        K += [Note(o + x, .25, 36, 118) for x in ((0, 1.75, 2.5) if b % 2 == 0 else (0, 0.5, 2.5, 3.25))]
        S += [Note(o + 1, .25, 38, 120), Note(o + 3, .25, 38, 122)]
        H += [Note(o + i * .5, .25, 42, 96 if i % 2 == 0 else 74) for i in range(8) if not (b % 4 == 3 and i == 7)]
        if b % 4 == 3: O.append(Note(o + 3.5, .5, 46, 92))
    drum_fx = board(pb.HighpassFilter(35), pb.Compressor(threshold_db=-14, ratio=3, attack_ms=8, release_ms=90))
    s.tracks += [Track('kick', ('oneshot', shots), K, gain_db=-3, mono=True),
                 Track('snare', ('oneshot', shots), S, gain_db=-5, timing_ms=10, fx=drum_fx, send_reverb=0.08),
                 Track('hats', ('oneshot', shots), H + O, gain_db=-14, humanize_ms=3, vel_jitter=8, pan=0.15)]
    # Rhodes-style comping (Surge 'EP 1'): Am9 bar 1, D9 bar 2  (dorian i - IV)
    am9 = [n('G3'), n('C4'), n('E4'), n('B4')]; d9 = [n('F#3'), n('C4'), n('E4'), n('A4')]
    comp = []
    for b in range(bars):
        o = b * 4; v = am9 if b % 2 == 0 else d9
        for st, du, ve in ((0, 1.4, 78), (1.75, .5, 70), (2.5, 1.3, 74)):
            comp += [Note(o + st, du, p, ve) for p in v]
    s.tracks.append(Track('keys', ('vst', 'Surge XT.vst3', SURGE + 'Keys/EP 1.fxp', None), comp, gain_db=-9, swing=54,
                          fx=board(pb.HighpassFilter(180), pb.Chorus(rate_hz=0.6, depth=0.15, mix=0.3)), send_reverb=0.18))
    # funk bass (Growlybass clean), roots + chromatic approach
    bl = []
    for b in range(bars):
        o = b * 4
        if b % 2 == 0:
            bl += [Note(o, .7, n('A1'), 112), Note(o + 1.75, .25, n('A1'), 96), Note(o + 2.5, .4, n('C2'), 104), Note(o + 3, .45, n('E2'), 100), Note(o + 3.5, .4, n('C#2'), 96)]
        else:
            bl += [Note(o, .7, n('D2'), 112), Note(o + 1.5, .25, n('D2'), 92), Note(o + 2, .5, n('F#2'), 102), Note(o + 2.75, .5, n('A2'), 98), Note(o + 3.5, .4, n('G#1'), 96)]
    s.tracks.append(Track('bass', ('sfz', kit('growly')), bl, gain_db=-4, swing=56, mono=True,
                          fx=board(pb.LowpassFilter(1800), pb.Compressor(threshold_db=-16, ratio=4, attack_ms=5, release_ms=80))))
    # whistle lead answers in bars 4 and 8 only (the vocal keeps bars 1-3)
    lead = []
    for b in (3, 7):
        o = b * 4
        lead += [(o + 0.5, .5, n('E5'), 90), (o + 1, .75, n('G5'), 100), (o + 1.75, 1.25, n('A5'), 104), (o + 3, .5, n('G5'), 92), (o + 3.5, .5, n('E5'), 84)]
    s.tracks.append(Track('lead', ('func', None), [], gain_db=-17, pan=-0.1, send_reverb=0.25))
    s.extra = {'lead': dsp.glide_lead(lead, spb, s.length_s() + 4)}
    s.balance = {'kick': 0.5, 'snare': 0, 'hats': -9, 'keys': -4, 'bass': -3, 'lead': -6}
    return s


# ---------------------------------------------------------------------------------------------- B
def concept_B(bars=8):
    bpm = 90.0; s = Song(bpm, bars, swing=63)
    spb = s.spb
    vk = kit('virt')
    k808 = dsp.kick_808(f0=46, decay=0.3, pitch_drop=3.0, click=0.35, drive_db=8)
    sn = vk.render_note(40, 125, 0.3)  # rimshot snare: harder crack
    cl = dsp.clap_synth(seed=9); sc = np.zeros((max(len(sn), len(cl)), 2), np.float32); sc[:len(sn)] += sn; sc[:len(cl)] += np.stack([cl, cl], 1) * 0.8
    hat = dsp.hat_synth(); ohat = dsp.hat_synth(open_=True)
    shots = {36: np.stack([k808, k808], 1), 38: sc, 42: np.stack([hat, hat], 1), 46: np.stack([ohat, ohat], 1)}
    K, S, H = [], [], []
    for b in range(bars):
        o = b * 4
        K += [Note(o + x, .25, 36, 120) for x in (0, 0.75, 2.5)] + ([Note(o + 3.75, .25, 36, 100)] if b % 2 else [])
        S += [Note(o + 1, .25, 38, 124), Note(o + 3, .25, 38, 124)]
        if b % 4 == 3:  # hat roll into the next phrase
            H += [Note(o + i * .5, .25, 42, 92) for i in range(6)] + [Note(o + 3 + i * .125, .125, 42, 70 + 6 * i) for i in range(8)]
        else:
            H += [Note(o + i * .5, .25, 42, 100 if i % 2 == 0 else 78) for i in range(8)]
    s.tracks += [Track('kick', ('oneshot', shots), K, gain_db=-2, mono=True),
                 Track('snare', ('oneshot', shots), S, gain_db=-6, timing_ms=6,
                       fx=board(pb.HighpassFilter(120), pb.Compressor(threshold_db=-12, ratio=4, attack_ms=3, release_ms=70)), send_reverb=0.06),
                 Track('hats', ('oneshot', shots), H, gain_db=-17, humanize_ms=2, vel_jitter=6, pan=-0.12)]
    # staccato octave piano motif, F phrygian, 2-bar sentence with a rest on beat 4 of bar 1 and a 'question' at the end of bar 2
    m1 = [(0, .22, 'F3', 112), (0.75, .22, 'F3', 96), (1.5, .3, 'Ab3', 108), (2.0, .45, 'Gb3', 116), (2.75, .22, 'F3', 100)]
    m2 = [(0, .22, 'C3', 112), (0.75, .22, 'Db3', 104), (1.5, .3, 'C3', 100), (2.5, .22, 'Eb3', 108), (3.0, .5, 'Db3', 112)]
    pn, ce = [], []
    for b in range(bars):
        o = b * 4
        for st, du, nm, ve in (m1 if b % 2 == 0 else m2):
            pn += [Note(o + st, du, n(nm), ve), Note(o + st, du, n(nm) + 12, ve - 14)]
            ce.append(Note(o + st, du + .1, n(nm) - 12, ve - 8))
    s.tracks.append(Track('piano', ('sfz', kit('piano')), pn, gain_db=-7, swing=50,
                          fx=board(pb.HighpassFilter(150), pb.Compressor(threshold_db=-18, ratio=3, attack_ms=2, release_ms=60)), send_reverb=0.12))
    s.tracks.append(Track('cello', ('sfz' if False else 'func', None), [], gain_db=-10))
    s.extra = {}
    cs = kit('cello_spic'); buf = np.zeros((int((s.length_s() + 4) * SR), 2), np.float32)
    for nt in ce:
        x = cs.render_note(nt.pitch, nt.vel, nt.dur * spb); st = int(s.beat_to_s(nt.beat, 50) * SR); buf[st:st + len(x)] += x[:len(buf) - st]
    s.extra['cello'] = dsp.hp(buf, 70)
    # violin pedal (tension) bars 5-8: Gb5 -> F5
    vs = kit('vln_sus'); vb = np.zeros_like(buf)
    for b, nm in ((4, 'Gb5'), (6, 'F5')):
        x = vs.render_note(n(nm), 70, 2 * 4 * spb); st = int(b * 4 * spb * SR); vb[st:st + len(x)] += x[:len(vb) - st]
    s.extra['strings'] = vb * 0.6
    s.tracks.append(Track('strings', ('func', None), [], gain_db=-14, send_reverb=0.3))
    # 808 bass follows the motif roots, leaves beat 4 of bar 1 empty
    bl = []
    for b in range(bars):
        o = b * 4
        if b % 2 == 0: bl += [(o, .7, n('F1'), 118), (o + .75, .6, n('F1'), 100), (o + 2.5, 1.0, n('F1'), 110)]
        else: bl += [(o, .7, n('C1') + 12, 116), (o + .75, .6, n('Db1') + 12, 104), (o + 2.5, .5, n('Eb1') + 12, 106), (o + 3.0, .9, n('Db1') + 12, 110)]
    s.extra['bass'] = dsp.bass_808(bl, spb, s.length_s() + 4, decay=0.45)
    s.tracks.append(Track('bass', ('func', None), [], gain_db=-5, mono=True))
    s.balance = {'kick': 0.5, 'snare': 0, 'hats': -9, 'piano': -2, 'cello': -9, 'strings': -10, 'bass': -2.5}
    return s


# ---------------------------------------------------------------------------------------------- C
def concept_C(bars=8):
    bpm = 87.0; s = Song(bpm, bars, swing=70)
    spb = s.spb
    # 1) compose the 'record' we will sample: 2-bar jazz phrase, piano + upright + muted horn line (sax), C minor
    rec_song = Song(bpm, 2, swing=55)
    v1 = [n('Eb3'), n('G3'), n('B3'), n('D4')]         # Cm(maj7)9 (no root; bass plays C)
    v2 = [n('Gb3'), n('Bb3'), n('C4'), n('Eb4')]       # Abmaj7#11-ish over Ab bass
    v3 = [n('F3'), n('Ab3'), n('B3'), n('Db4')]        # G7b9 (rootless)
    pn = [Note(0, 1.6, p, 72) for p in v1] + [Note(1.75, .35, p, 66) for p in v1] + [Note(2.5, 1.4, p, 70) for p in v2] \
        + [Note(4, 1.0, p, 74) for p in v3] + [Note(5.5, .3, p, 64) for p in v3] + [Note(6.0, 1.9, p, 68) for p in v1]
    up = [Note(0, .9, n('C2'), 100), Note(1, .9, n('G1'), 92), Note(2.5, .9, n('Ab1'), 98), Note(3.5, .4, n('A1'), 84),
          Note(4, .9, n('G1'), 100), Note(5, .9, n('B1'), 90), Note(6, .9, n('C2'), 98), Note(7, .9, n('G1'), 88)]
    rec_song.tracks = [Track('p', ('sfz', kit('piano')), pn, gain_db=-4, humanize_ms=8, vel_jitter=6, send_reverb=0.25),
                       Track('u', ('sfz', kit('upright')), up, gain_db=-3, humanize_ms=6)]
    stems = {t.name: render_track(rec_song, t, tail_s=1.0) for t in rec_song.tracks}
    rec = mixdown(rec_song, stems)
    rec = rec[:int(rec_song.length_s() * SR)]
    # 'press the record': tape, band-limit, vinyl, then sample it into an SP-1200
    tape = pb.load_plugin('/usr/lib/vst3/CHOWTapeModel.vst3')
    rec = tape(rec.T.astype(np.float32), SR).T
    rec = dsp.bpf(rec, 90, 7000, order=2) + dsp.vinyl(len(rec), level_db=-34)
    rec = dsp.vintage(rec / (np.abs(rec).max() + 1e-9) * 0.8, 'sp1200')
    # 2) chop it: bar A = phrase bar 1 ; bar B = phrase bar 2 but with beat-3 stab repeated (the 'answer')
    L = int(4 * spb * SR); A, B = rec[:L], rec[L:2 * L].copy()
    beat = int(spb * SR); stab = rec[int(1.75 * spb * SR):int(1.75 * spb * SR) + beat // 2]
    B[2 * beat:2 * beat + len(stab)] = stab * np.hanning(len(stab))[:, None] ** 0.1
    B[int(2.75 * beat):int(2.75 * beat) + len(stab)] = stab[:len(B) - int(2.75 * beat)] * 0.9
    loop = np.concatenate([A, B]); full = np.concatenate([loop] * (bars // 2) + [np.zeros((int(4 * SR), 2))])
    M_, S_ = full.mean(1, keepdims=True), (full[:, :1] - full[:, 1:]) / 2
    full = np.concatenate([M_ + 0.25 * S_, M_ - 0.25 * S_], 1)   # 90s NY = near-mono (refs side-mid -24..-72 dB)
    full = dsp.hp(full, 110)                                       # the sub owns the bottom, not the sample
    s.extra = {'sample': full.astype(np.float32)}
    s.tracks.append(Track('sample', ('func', None), [], gain_db=-6, fx=None))
    # 3) drums: vintage-mic kit through SP-1200 + crush comp; busy chopped kick, hard snare, very late hats
    vk = kit('virt_vint')
    shots = {k: dsp.vintage(vk.render_note(k, v, 0.4) if vk.render_note(k, v, 0.4) is not None else kit('virt').render_note(k, v, 0.4), 'sp1200') for k, v in ((36, 125), (38, 124), (42, 88), (46, 80), (37, 90))}
    shots[36] = dsp.peq(shots[36], 60, 6, 0.9); shots[36] = dsp.sat(shots[36], 6)
    K, S, H = [], [], []
    for b in range(bars):
        o = b * 4
        K += [Note(o + x, .25, 36, 120) for x in ((0, 0.75, 1.75, 2.5) if b % 2 == 0 else (0, 1.5, 2.25, 2.5, 3.75))]
        S += [Note(o + 1, .25, 38, 124), Note(o + 3, .25, 38, 126)] + ([Note(o + 3.75, .25, 37, 70)] if b % 4 == 3 else [])
        H += [Note(o + i * .5, .25, 42, 92 if i % 2 == 0 else 64) for i in range(8)]
    crush = board(pb.Compressor(threshold_db=-20, ratio=6, attack_ms=10, release_ms=60), pb.Gain(4))
    s.tracks += [Track('kick', ('oneshot', shots), K, gain_db=-3, mono=True),
                 Track('snare', ('oneshot', shots), S, gain_db=-5, timing_ms=14, fx=crush, send_reverb=0.05),
                 Track('hats', ('oneshot', shots), H, gain_db=-15, humanize_ms=4, vel_jitter=6)]
    # sub under the sample (sample bass is thin after band-limiting)
    bl = []
    for b in range(bars):
        o = b * 4
        bl += [(o, 1.5, n('C1') + 12, 110), (o + 2.5, 1.2, n('Ab1') if b % 2 == 0 else n('G1'), 104)]
    s.extra['bass'] = dsp.bass_808(bl, spb, s.length_s() + 4, decay=0.7, drive_db=3)
    s.tracks.append(Track('bass', ('func', None), [], gain_db=-9, mono=True))
    s.balance = {'kick': 1.0, 'snare': 0, 'hats': -10, 'sample': -2.5, 'bass': -1.5}
    return s


def render(song, tag):
    stems = {}
    for tr in song.tracks:
        if tr.instrument[0] == 'func' and tr.name in getattr(song, 'extra', {}):
            x = song.extra[tr.name]
            if tr.fx: x = tr.fx(x)
            p = (tr.pan + 1) * np.pi / 4
            stems[tr.name] = (x * np.array([np.cos(p), np.sin(p)]) * np.sqrt(2) * 10 ** (tr.gain_db / 20)).astype(np.float32)
            song._sends = getattr(song, '_sends', {})
        else:
            stems[tr.name] = render_track(song, tr)
    n_ = int((song.length_s() + 2) * SR)
    for k in stems:
        s = stems[k][:n_]
        stems[k] = np.pad(s, ((0, n_ - len(s)), (0, 0)))
    if getattr(song, 'balance', None):
        stems, gains = auto_balance(stems, song.balance)
        print(tag, 'auto-balance gains dB:', gains)
    mix = mixdown(song, stems)
    m = master_chain(mix, target_lufs=-10.0)
    export(OUT + tag, m)
    for k, v in stems.items():
        export(OUT + f'{tag}_stems/{k}', v, mp3=False)
    return m, stems


def metrics(x):
    mono = x.mean(1); spec = np.abs(np.fft.rfft(mono)) ** 2; f = np.fft.rfftfreq(len(mono), 1 / SR)
    M, S = (x[:, 0] + x[:, 1]) / 2, (x[:, 0] - x[:, 1]) / 2
    return dict(lufs=round(dsp.lufs(x), 2), true_peak_dbtp=round(20 * np.log10(np.abs(dsp.resample_poly(x, 4, 1, axis=0)).max()), 2),
                crest_db=round(20 * np.log10(np.abs(mono).max() / np.sqrt(np.mean(mono ** 2))), 2),
                low_le150_pct=round(100 * spec[f <= 150].sum() / spec.sum(), 1), mid_250_2k_pct=round(100 * spec[(f > 250) & (f < 2000)].sum() / spec.sum(), 1),
                centroid_hz=round(float((spec * f).sum() / spec.sum()), 0), side_minus_mid_db=round(10 * np.log10(np.mean(S ** 2) / np.mean(M ** 2) + 1e-12), 1),
                lr_correlation=round(float(np.corrcoef(x[:, 0], x[:, 1])[0, 1]), 3))


if __name__ == '__main__':
    which = sys.argv[1:] or ['A', 'B', 'C']
    res = {}
    for w in which:
        song = {'A': concept_A, 'B': concept_B, 'C': concept_C}[w]()
        m, _ = render(song, f'concept_{w}')
        res[w] = metrics(m); print(w, res[w], flush=True)
    old = json.load(open(OUT + 'metrics.json')) if os.path.exists(OUT + 'metrics.json') else {}
    old.update(res); json.dump(old, open(OUT + 'metrics.json', 'w'), indent=1)
