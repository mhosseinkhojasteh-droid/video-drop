## Measured profile [measured — scripts/analyze_track.py → analysis/data/50_Cent_-_In_Da_Club.json]

| metric | value |
|---|---|
| duration | 220.39 s, 81 bars of 2.6696 s |
| tempo | **89.902 BPM** (grid residual p90 5.4 ms; comb candidates [[4.109, 89.85], [3.669, 179.75], [2.924, 119.8]]; drift first→last third -0.008 %) |
| first downbeat | 1.994 s (bar-phase margin 0.816; snare backbeat ratio 0.56) |
| key | C# minor [estimate, margin 0.12]; alternatives [['A major', 0.243], ['D major', 0.189]] |
| loudness | -14.71 LUFS integrated, short-term p10/p90 [-15.3, -14.2], crest 15.64 dB, sample peak 0.37 dBFS |
| stereo | side−mid -13.7 dB overall, -14.4 dB below 150 Hz |
| spectrum | 73.9 % of energy ≤150 Hz; centroid 2058.0 Hz; HF content to ~10766 Hz |
| swing (hat 16ths) | 66.3 % (50 straight, 66.7 triplet); off-8th hat delay -10.6 ms |
| perc vs harmonic | 3.4 dB |
| harmonic loop similarity (bar lags) | {'1': -0.754, '2': 0.753, '3': -0.765, '4': 0.869, '8': 0.853} |

**16-step onset occupancy** (X strong, x present; whole track):
```
        1 e & a 2 e & a 3 e & a 4 e & a
kick    X . x . . X . . X . . . . X . .
snare   X . X . x X . . X . X . x X x .
hat     x . X . X . X . x . X . X . X .
```
Median micro-timing per step (ms, + = late): kick [14.6, 71.0, 9.4, None, 45.1, 17.7, -15.9, 56.3, 17.6, 61.3, 11.1, 73.5, 62.3, 23.0, -17.5, 80.5], snare [10.2, 50.7, -48.1, 53.0, 37.0, 24.2, 16.6, 52.3, 11.8, 57.5, -35.6, 54.1, 34.7, 23.8, 15.8, 49.0], hat [16.7, 54.4, -44.3, 54.5, 29.0, 34.2, 15.0, 53.2, 16.8, 54.1, -34.0, 54.8, 28.2, 34.7, 12.8, 54.6]

**Layer timeline** (per bar vs. track median; NO-LOW = sub ≥6 dB down, NO-DRUMS = percussive ≥6 dB down):
b1-5:melody-off | b6-14:full | b15-21:melody-off | b22-31:full | b32:melody+ | b33-35:full | b36:melody+ | b37:full | b38-41:melody+ | b42:full | b43-45:melody-off | b46-50:full | b51-53:melody-off | b54-55:full | b56:melody+ | b57-59:full | b60:melody+ | b61-67:full | b68:melody+ | b69-79:full | b80:low-thin,melody-off | b81:NO-LOW,NO-DRUMS,no-hats,melody-off

**Bars 2–9 harmonic sketch** [estimate: chroma template + bass chroma; not a transcription]: [D#maj7/C#5 bass E-D-C#-C#] [D#maj7/D#m7 bass D-D#-D#-F#] [Em7/Dmaj7 bass D-D-C#-C#] [D#maj7/D#m7 bass D-E-D#-F#] [D#maj7/Dmaj7 bass E-D-C#-C#] [D#maj7/D#m7 bass D-D-D#-F#] [E7/C#5 bass E-E-C#-C#] [D#maj7/D#m7 bass D-E-D#-F#]

Pitch-class profile: {'C': 0.3, 'C#': 0.9, 'D': 1.0, 'D#': 0.86, 'E': 0.69, 'F': 0.36, 'F#': 0.36, 'G': 0.23, 'G#': 0.31, 'A': 0.17, 'A#': 0.1, 'B': 0.13}
Bass pitch-class profile: {'C': 0.36, 'C#': 0.94, 'D': 1.0, 'D#': 0.87, 'E': 0.66, 'F': 0.33, 'F#': 0.36, 'G': 0.19, 'G#': 0.19, 'A': 0.1, 'A#': 0.09, 'B': 0.09}
