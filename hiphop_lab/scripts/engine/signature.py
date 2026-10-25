"""GOLDEN V — the factory's signature tag. v2 (King 25 Oct): Kanye-style — very low (−10 st), dark (LP 2.3 kHz), saturated, the word only readable if you know it; NO bell.
v1 notes: (the King + THE GOD OF MUSIC).

Placed in the last 2 beats before the first big drop: [gold shimmer] + ["Golden V" voice, dark, doubled] + [reversed piano swell
of the record's own chord] -> 1/16 of silence -> BOOM (the song's impact + kick + 808).
The voice is espeak-ng (offline TTS), pitched down and processed. It is a PLACEHOLDER: record the King saying "Golden V"
(dry, close, 48 kHz WAV) and pass it as `voice_wav` — the chain is built for a real voice.
"""
import numpy as np, soundfile as sf, pedalboard as pb
from scipy.signal import resample_poly
import dsp
from dsp import SR

TAG_DIR = 'assets/tag/'


def _load(p):
    x, sr = sf.read(p, always_2d=True, dtype='float32')
    x = x.mean(1)
    if sr != SR: x = resample_poly(x, SR, sr).astype(np.float32)
    return x


def voice_chain(v, semis=-10.0, lp_hz=2300, drive_db=9.0):
    v = v / (np.abs(v).max() + 1e-9)
    st = np.stack([v, v], 1)
    b = pb.Pedalboard([pb.PitchShift(semitones=semis), pb.HighpassFilter(70), pb.LowpassFilter(lp_hz),
                       pb.Compressor(threshold_db=-22, ratio=4, attack_ms=5, release_ms=90), pb.Distortion(drive_db=drive_db), pb.LowpassFilter(lp_hz)])
    y = b(st.T, SR).T
    # double: +-9 cents detune, 14 ms offset, panned
    d1 = pb.Pedalboard([pb.PitchShift(semitones=+0.09)])(y.T, SR).T; d2 = pb.Pedalboard([pb.PitchShift(semitones=-0.09)])(y.T, SR).T
    off = int(0.014 * SR)
    dbl = np.zeros_like(y); dbl[off:, 0] = d1[:-off, 0]; dbl[off:, 1] = d2[:-off, 1]
    return y + 0.45 * dbl


def golden_v_tag(bpm, chord_notes=None, piano=None, voice_wav=None, beats=2.0, seed=7, style='dark'):
    """style='dark' (v7, Kanye-low, saturated) or 'soft' (v8, King 25 Oct: for soft/artistic beats — warm whisper, −5 st, no distortion, halo reverb)."""
    """Return (audio, lead_s): audio starts lead_s seconds before the target downbeat and its tail spills past it."""
    spb = 60.0 / bpm; lead = beats * spb; tail = 2.5
    N = int((lead + tail) * SR); out = np.zeros((N, 2), np.float32)
    d = int(lead * SR)  # downbeat index inside the buffer
    # 1) voice
    if voice_wav:
        v = _load(voice_wav)
    else:
        raw = _load(TAG_DIR + 'golden_raw.wav'); wh = _load(TAG_DIR + 'golden_whisper.wav')
        if style == 'soft':
            v = wh
        else:
            L = max(len(raw), len(wh)); v = np.zeros(L, np.float32); v[:len(raw)] += raw; v[:len(wh)] += 0.8 * wh[:L]
    if style == 'soft':
        vc = voice_chain(v, semis=-5.0, lp_hz=3600, drive_db=0.0)
        halo = pb.Pedalboard([pb.Reverb(room_size=0.75, damping=0.6, wet_level=0.35, dry_level=0.8, width=1.0)])
        vc = halo(np.pad(vc, ((0, int(0.4 * SR)), (0, 0))).T, SR).T
    else:
        vc = voice_chain(v)
    # trim silence, fit the phrase so it ends 1/16 before the downbeat
    env = np.abs(vc).max(1); idx = np.where(env > 0.02 * env.max())[0]; vc = vc[idx[0]:idx[-1] + int(0.05 * SR)]
    room = d - int(spb / 4 * SR) - int(0.15 * spb * SR)
    if len(vc) > room:
        r = len(vc) / room
        vc = np.stack([np.interp(np.arange(0, len(vc) - 1, r), np.arange(len(vc)), vc[:, c]) for c in range(2)], 1)
    st = d - int(spb / 4 * SR) - len(vc)
    out[st:st + len(vc)] += vc * 0.9
    # echo throw of the last 250 ms ("...V") across the downbeat, darkening
    throw = vc[-int(0.25 * SR):]; dly = int(0.75 * spb * SR); g = 0.45
    for k in range(1, 5):
        p = st + len(vc) - len(throw) + k * dly
        if p + len(throw) > N: break
        out[p:p + len(throw)] += dsp.lp(throw, 4000 / k, order=2) * g; g *= 0.55
    # 2) dark air: the voice's own reversed reverb swells INTO the word (no bell, no beep)
    wet = pb.Pedalboard([pb.Reverb(room_size=0.9, damping=0.8, wet_level=1.0, dry_level=0.0, width=1.0)])(np.pad(vc, ((0, int(1.5 * SR)), (0, 0))).T, SR).T
    rv = dsp.lp(wet[::-1], 1500, order=2)[-int(min(len(wet), st)):]
    rv = rv * np.linspace(0, 1, len(rv))[:, None] ** 2
    out[st - len(rv):st] += rv * 0.35
    # 3) reversed piano swell of the song's chord, landing exactly on the downbeat
    if piano is not None and chord_notes:
        ch = None
        for k, m in enumerate(chord_notes):
            x = piano.render_note(m, 92 - 4 * k, 2.5)
            if x is None: continue
            ch = x if ch is None else (np.pad(ch, ((0, max(0, len(x) - len(ch))), (0, 0))) + np.pad(x, ((0, max(0, len(ch) - len(x))), (0, 0))))
        rev = ch[::-1][-int(lead * SR):] if len(ch) > lead * SR else ch[::-1]
        rev = rev * np.linspace(0, 1, len(rev))[:, None] ** 2.5
        out[d - len(rev):d] += dsp.hp(rev, 200) * 0.6
    out[d - int(spb / 16 * SR):d] = 0.0  # the breath before the boom: 1/16 of total silence
    return out, lead


if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'scripts/engine')
    from sfz import SFZ
    pno = SFZ('sound_library/incoming/SalamanderGrandPiano/Salamander Grand Piano V3.sfz')
    tag, lead = golden_v_tag(90, [29, 41, 48, 56, 67, 72], pno)
    sf.write(TAG_DIR + 'golden_v_tag_preview.wav', tag / np.abs(tag).max() * 0.9, SR, subtype='PCM_24')
    print('tag', tag.shape, 'lead_s', round(lead, 3))
