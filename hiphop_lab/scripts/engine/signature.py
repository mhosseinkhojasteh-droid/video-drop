"""GOLDEN V — the factory's signature tag (the King + THE GOD OF MUSIC).

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


def voice_chain(v, semis=-4.0):
    v = v / (np.abs(v).max() + 1e-9)
    st = np.stack([v, v], 1)
    b = pb.Pedalboard([pb.PitchShift(semitones=semis), pb.HighpassFilter(160), pb.LowpassFilter(7000),
                       pb.Compressor(threshold_db=-20, ratio=4, attack_ms=3, release_ms=80), pb.Distortion(drive_db=6)])
    y = b(st.T, SR).T
    # double: +-9 cents detune, 14 ms offset, panned
    d1 = pb.Pedalboard([pb.PitchShift(semitones=+0.09)])(y.T, SR).T; d2 = pb.Pedalboard([pb.PitchShift(semitones=-0.09)])(y.T, SR).T
    off = int(0.014 * SR)
    dbl = np.zeros_like(y); dbl[off:, 0] = d1[:-off, 0]; dbl[off:, 1] = d2[:-off, 1]
    return y + 0.45 * dbl


def golden_v_tag(bpm, chord_notes=None, piano=None, voice_wav=None, beats=2.0, seed=7):
    """Return (audio, lead_s): audio starts lead_s seconds before the target downbeat and its tail spills past it."""
    spb = 60.0 / bpm; lead = beats * spb; tail = 2.5
    N = int((lead + tail) * SR); out = np.zeros((N, 2), np.float32)
    d = int(lead * SR)  # downbeat index inside the buffer
    # 1) voice
    if voice_wav:
        v = _load(voice_wav)
    else:
        raw = _load(TAG_DIR + 'golden_raw.wav'); wh = _load(TAG_DIR + 'golden_whisper.wav')
        L = max(len(raw), len(wh)); v = np.zeros(L, np.float32); v[:len(raw)] += raw; v[:len(wh)] += 0.8 * wh[:L]
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
    # 2) gold shimmer: high bell partials (F6/C7/F7) with long decay, starts with the voice
    t = np.arange(int(2.2 * SR)) / SR
    bell = sum(a * np.sin(2 * np.pi * f * t) * np.exp(-t / dec) for f, a, dec in ((1396.9, 1.0, 1.1), (2093.0, .5, .7), (2793.8, .35, .5), (4186.0, .18, .3)))
    bell = dsp.hp(bell, 900) / np.abs(bell).max()
    bl = np.stack([bell, bell], 1).astype(np.float32)
    bl = pb.Pedalboard([pb.Reverb(room_size=0.85, wet_level=0.5, dry_level=0.6, width=1.0)])(bl.T, SR).T
    bs = max(0, st - int(0.12 * SR)); out[bs:bs + len(bl)] += bl[:N - bs] * 0.35
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
