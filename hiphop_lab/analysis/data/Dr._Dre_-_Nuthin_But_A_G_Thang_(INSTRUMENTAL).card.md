## Measured profile [measured — scripts/analyze_track.py → analysis/data/Dr._Dre_-_Nuthin_But_A_G_Thang_(INSTRUMENTAL).json]

| metric | value |
|---|---|
| duration | 240.9 s, 94 bars of 2.5349 s |
| tempo | **94.678 BPM** (grid residual p90 16.5 ms; comb candidates [[3.091, 94.7], [2.585, 63.1], [1.93, 126.5]]; drift first→last third 0.0 %) |
| first downbeat | 0.135 s (bar-phase margin 0.174; snare backbeat ratio 3.46) |
| key | B minor [estimate, margin 0.153]; alternatives [['B major', 0.498], ['E minor', 0.438]] |
| loudness | -19.77 LUFS integrated, short-term p10/p90 [-20.8, -19.0], crest 19.31 dB, sample peak -1.75 dBFS |
| stereo | side−mid -6.0 dB overall, -10.2 dB below 150 Hz |
| spectrum | 64.1 % of energy ≤150 Hz; centroid 2772.0 Hz; HF content to ~10788 Hz |
| swing (hat 16ths) | 60.6 % (50 straight, 66.7 triplet); off-8th hat delay 26.1 ms |
| perc vs harmonic | -0.7 dB |
| harmonic loop similarity (bar lags) | {'1': -0.228, '2': 0.711, '3': -0.276, '4': 0.582, '8': 0.396} |

**16-step onset occupancy** (X strong, x present; whole track):
```
        1 e & a 2 e & a 3 e & a 4 e & a
kick    x . . . . . X . x . x . . . X .
snare   x . . . X . . . x . . . X . . .
hat     X . . . X . x . X . x . X . x .
```
Median micro-timing per step (ms, + = late): kick [4.2, 56.3, 26.8, 31.4, 23.8, None, 17.4, -51.2, 22.8, None, 19.0, 41.5, 23.5, None, 23.8, -33.9], snare [20.2, None, 29.4, 33.9, 15.3, None, 29.0, 44.6, 25.3, None, 13.9, -33.2, 28.0, None, 34.4, 9.1], hat [20.6, None, 25.3, 47.0, 17.9, 33.6, 25.7, 30.3, 18.5, None, 28.4, None, 29.6, 45.2, 26.6, 31.5]

**Layer timeline** (per bar vs. track median; NO-LOW = sub ≥6 dB down, NO-DRUMS = percussive ≥6 dB down):
b1:NO-LOW | b2:low-thin | b3:NO-LOW,melody+ | b4:low-thin,melody+ | b5-26:full | b27-30:melody+ | b31-42:full | b43-50:melody+ | b51:NO-LOW | b52:low-thin | b53:NO-LOW | b54:low-thin | b55-58:full | b59-62:melody+ | b63:NO-LOW | b64:low-thin | b65:NO-LOW | b66:low-thin | b67:NO-LOW | b68:low-thin | b69:NO-LOW | b70:low-thin | b71-78:full | b79-94:melody+

**Bars 2–9 harmonic sketch** [estimate: chroma template + bass chroma; not a transcription]: [Cmaj7/Gmaj7 bass F#-G-G-A#] [Bm7/Cmaj7 bass B-A#-B-B] [F#m7/Gmaj7 bass B-G-G-B] [Bm7/Fmaj7 bass B-B-E-F#] [Fmaj7/Bmaj7 bass E-G-B-B] [Bm7/Fmaj7 bass B-B-E-F#] [Fmaj7/Bmaj7 bass E-G-B-B] [Bm7/F#7 bass B-B-E-F#]

Pitch-class profile: {'C': 0.64, 'C#': 0.48, 'D': 0.5, 'D#': 0.35, 'E': 0.61, 'F': 0.56, 'F#': 0.79, 'G': 0.46, 'G#': 0.38, 'A': 0.54, 'A#': 0.6, 'B': 1.0}
Bass pitch-class profile: {'C': 0.66, 'C#': 0.47, 'D': 0.39, 'D#': 0.37, 'E': 0.52, 'F': 0.6, 'F#': 0.74, 'G': 0.53, 'G#': 0.44, 'A': 0.53, 'A#': 0.68, 'B': 1.0}
