## Measured profile [measured — scripts/analyze_track.py → analysis/data/Wu_Tang_Clan_-_Triumph_Instrumental.json]

| metric | value |
|---|---|
| duration | 338.78 s, 127 bars of 2.6371 s |
| tempo | **91.009 BPM** (grid residual p90 14.7 ms; comb candidates [[3.174, 91.0], [2.617, 60.65], [2.012, 121.2]]; drift first→last third -0.004 %) |
| first downbeat | 1.566 s (bar-phase margin 0.123; snare backbeat ratio 3.38) |
| key | D minor [estimate, margin 0.036]; alternatives [['D major', 0.482], ['B minor', 0.305]] |
| loudness | -16.05 LUFS integrated, short-term p10/p90 [-16.4, -15.7], crest 14.87 dB, sample peak -2.72 dBFS |
| stereo | side−mid -71.8 dB overall, -120.0 dB below 150 Hz |
| spectrum | 70.6 % of energy ≤150 Hz; centroid 1762.0 Hz; HF content to ~10691 Hz |
| swing (hat 16ths) | 64.3 % (50 straight, 66.7 triplet); off-8th hat delay 29.5 ms |
| perc vs harmonic | -0.7 dB |
| harmonic loop similarity (bar lags) | {'1': 0.464, '2': 0.355, '3': 0.305, '4': 0.456, '8': 0.343} |

**16-step onset occupancy** (X strong, x present; whole track):
```
        1 e & a 2 e & a 3 e & a 4 e & a
kick    X . X . X . X . X . . . x . . .
snare   x . x . X . x . x . x . X . x .
hat     x . x . X . x . x . x . X . X .
```
Median micro-timing per step (ms, + = late): kick [-4.6, None, 3.8, None, 1.7, 70.1, 2.9, None, -2.4, -14.7, 27.3, -69.0, 32.9, None, 22.2, -56.5], snare [20.6, None, 37.8, 49.8, 24.2, None, 32.7, 46.8, 12.2, None, 24.9, 49.3, 23.1, None, 21.8, -40.8], hat [30.5, None, 45.6, 48.1, 22.4, None, 34.6, 46.4, 14.7, None, 24.4, 48.9, 23.5, None, 22.4, -37.2]

**Layer timeline** (per bar vs. track median; NO-LOW = sub ≥6 dB down, NO-DRUMS = percussive ≥6 dB down):
b1-8:melody+ | b9-30:full | b31:low-thin | b32-35:full | b36:melody+ | b37-40:full | b41:melody+ | b42-47:full | b48:melody+ | b49:melody-off | b50-54:full | b55:NO-LOW,no-hats | b56:low-thin | b57-58:full | b59-60:melody+ | b61-62:full | b63:melody+ | b64-84:full | b85:melody-off | b86-87:full | b88-91:melody-off | b92-102:full | b103:melody-off | b104:full | b105:melody-off | b106-127:full

**Bars 2–9 harmonic sketch** [estimate: chroma template + bass chroma; not a transcription]: [D5/G5 bass D-D-D-D] [G5/G5 bass D-D-D-D] [G5/G5 bass D-D-D-D] [G5/D5 bass D-D-D-D] [D5/G5 bass D-D-D-D] [G5/G5 bass D-D-D-D] [G5/D5 bass D-D-D-D] [D5/D5 bass D-D-D-D]

Pitch-class profile: {'C': 0.16, 'C#': 0.34, 'D': 1.0, 'D#': 0.27, 'E': 0.19, 'F': 0.14, 'F#': 0.07, 'G': 0.07, 'G#': 0.05, 'A': 0.11, 'A#': 0.07, 'B': 0.1}
Bass pitch-class profile: {'C': 0.16, 'C#': 0.59, 'D': 1.0, 'D#': 0.3, 'E': 0.2, 'F': 0.12, 'F#': 0.07, 'G': 0.07, 'G#': 0.05, 'A': 0.07, 'A#': 0.08, 'B': 0.12}
