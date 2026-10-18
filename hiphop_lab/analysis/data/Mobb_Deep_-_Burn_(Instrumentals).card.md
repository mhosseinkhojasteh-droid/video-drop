## Measured profile [measured — scripts/analyze_track.py → analysis/data/Mobb_Deep_-_Burn_(Instrumentals).json]

| metric | value |
|---|---|
| duration | 257.44 s, 101 bars of 2.5118 s |
| tempo | **95.551 BPM** (grid residual p90 8.5 ms; comb candidates [[3.899, 95.55], [3.228, 63.7], [2.405, 76.45]]; drift first→last third -0.025 %) |
| first downbeat | 1.395 s (bar-phase margin 0.064; snare backbeat ratio 11.42) |
| key | C major [estimate, margin 0.082]; alternatives [['G major', 0.516], ['F major', 0.427]] |
| loudness | -9.06 LUFS integrated, short-term p10/p90 [-10.2, -7.9], crest 12.16 dB, sample peak 2.34 dBFS |
| stereo | side−mid -20.8 dB overall, -36.2 dB below 150 Hz |
| spectrum | 86.7 % of energy ≤150 Hz; centroid 3796.0 Hz; HF content to ~10809 Hz |
| swing (hat 16ths) | None % (50 straight, 66.7 triplet); off-8th hat delay 55.9 ms |
| perc vs harmonic | 1.5 dB |
| harmonic loop similarity (bar lags) | {'1': -0.228, '2': -0.47, '3': -0.232, '4': 0.972, '8': 0.97} |

**16-step onset occupancy** (X strong, x present; whole track):
```
        1 e & a 2 e & a 3 e & a 4 e & a
kick    X . . . x . . x X . X . x . . .
snare   . . x . X . . . . . . . X . . .
hat     . . x . X . x . . . x . X . x .
```
Median micro-timing per step (ms, + = late): kick [13.8, -56.4, -4.7, -61.9, 22.9, -75.0, -59.3, 37.2, 15.4, -54.8, 13.9, 69.6, 18.2, -43.5, -60.5, -64.3], snare [50.0, 49.7, 48.4, None, 18.5, None, 53.6, None, 50.9, 44.7, 47.4, None, 18.1, None, 53.4, 74.1], hat [55.4, None, 48.9, None, 20.9, None, 56.4, None, 57.8, None, 55.5, None, 21.3, None, 56.2, None]

**Layer timeline** (per bar vs. track median; NO-LOW = sub ≥6 dB down, NO-DRUMS = percussive ≥6 dB down):
b1-94:full | b95:no-hats,melody-off | b96-101:NO-LOW,NO-DRUMS,no-hats,melody-off

**Bars 2–9 harmonic sketch** [estimate: chroma template + bass chroma; not a transcription]: [G7/C#maj7 bass A-G-D-C] [Fmaj7/A7 bass F-F-D-A] [G7/Fm7 bass A-G-D#-G#] [E7/A7 bass C-E-D-A] [G7/C#maj7 bass A-G-D-C] [Fmaj7/A7 bass F-F-D-A] [G7/Fm7 bass A-G-D#-G#] [Cmaj7/A7 bass C-E-D-A]

Pitch-class profile: {'C': 0.74, 'C#': 0.73, 'D': 0.75, 'D#': 0.63, 'E': 0.75, 'F': 0.86, 'F#': 0.51, 'G': 1.0, 'G#': 0.74, 'A': 0.86, 'A#': 0.6, 'B': 0.81}
Bass pitch-class profile: {'C': 0.96, 'C#': 0.87, 'D': 0.94, 'D#': 0.87, 'E': 0.93, 'F': 0.96, 'F#': 0.72, 'G': 1.0, 'G#': 0.92, 'A': 0.98, 'A#': 0.78, 'B': 0.79}
