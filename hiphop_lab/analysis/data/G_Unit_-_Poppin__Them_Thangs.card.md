## Measured profile [measured — scripts/analyze_track.py → analysis/data/G_Unit_-_Poppin__Them_Thangs.json]

| metric | value |
|---|---|
| duration | 272.45 s, 99 bars of 2.7269 s |
| tempo | **88.012 BPM** (grid residual p90 6.3 ms; comb candidates [[4.097, 88.0], [4.091, 176.1], [3.374, 117.35]]; drift first→last third -0.001 %) |
| first downbeat | 0.294 s (bar-phase margin 0.063; snare backbeat ratio 3.25) |
| key | F# minor [estimate, margin 0.254]; alternatives [['F# major', 0.556], ['A major', 0.405]] |
| loudness | -8.01 LUFS integrated, short-term p10/p90 [-8.6, -7.6], crest 12.84 dB, sample peak 2.45 dBFS |
| stereo | side−mid -12.7 dB overall, -23.8 dB below 150 Hz |
| spectrum | 30.6 % of energy ≤150 Hz; centroid 2152.0 Hz; HF content to ~10766 Hz |
| swing (hat 16ths) | 66.0 % (50 straight, 66.7 triplet); off-8th hat delay 22.0 ms |
| perc vs harmonic | -0.3 dB |
| harmonic loop similarity (bar lags) | {'1': 0.017, '2': 0.495, '3': -0.174, '4': 0.394, '8': 0.528} |

**16-step onset occupancy** (X strong, x present; whole track):
```
        1 e & a 2 e & a 3 e & a 4 e & a
kick    x . . . x . . . X . . . x . x .
snare   . . . x X . x . x . x . X . X .
hat     x . X . X . X . X . X . X . X .
```
Median micro-timing per step (ms, + = late): kick [7.7, -38.9, 58.7, 54.9, 22.2, 57.9, 22.9, 28.3, 5.6, -76.7, 45.0, 44.6, 32.9, None, 4.4, 65.5], snare [27.4, None, 29.4, 55.2, 23.7, 55.6, 25.3, 27.2, 24.7, 44.6, 24.6, 55.8, 22.9, 60.2, 25.0, 23.8], hat [24.2, None, 23.2, 54.6, 22.5, None, 21.9, None, 22.7, 39.5, 21.8, 54.5, 21.6, 65.5, 22.1, 22.8]

**Layer timeline** (per bar vs. track median; NO-LOW = sub ≥6 dB down, NO-DRUMS = percussive ≥6 dB down):
b1-8:full | b9:hats+ | b10-57:full | b58:low-thin | b59:full | b60:low-thin | b61-94:full | b95:NO-LOW,no-hats,melody-off | b96-99:NO-LOW,NO-DRUMS,no-hats,melody-off

**Bars 2–9 harmonic sketch** [estimate: chroma template + bass chroma; not a transcription]: [F#m/F#m7 bass F#-F#-E-E] [F#m/Bm7 bass F#-F-D#-B] [F#m/F#m7 bass F#-D#-E-E] [F#m/Bm7 bass F#-F#-D#-B] [F#m/F#m7 bass F#-F-D#-E] [F#m/Bm7 bass F#-F#-D#-B] [F#m/F#m7 bass F#-F-E-E] [F#m/Bm7 bass F#-F#-F#-B]

Pitch-class profile: {'C': 0.15, 'C#': 0.59, 'D': 0.23, 'D#': 0.25, 'E': 0.37, 'F': 0.39, 'F#': 1.0, 'G': 0.28, 'G#': 0.25, 'A': 0.54, 'A#': 0.21, 'B': 0.29}
Bass pitch-class profile: {'C': 0.23, 'C#': 0.3, 'D': 0.4, 'D#': 0.56, 'E': 0.69, 'F': 0.73, 'F#': 1.0, 'G': 0.45, 'G#': 0.29, 'A': 0.24, 'A#': 0.19, 'B': 0.29}
