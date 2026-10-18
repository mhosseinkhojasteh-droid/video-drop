## Measured profile [measured — scripts/analyze_track.py → analysis/data/Dr._Dre_-_The_Next_Episode_(Instrumental).json]

| metric | value |
|---|---|
| duration | 161.6 s, 64 bars of 2.5149 s |
| tempo | **95.431 BPM** (grid residual p90 7.5 ms; comb candidates [[3.945, 95.45], [3.687, 63.6], [3.076, 127.3]]; drift first→last third -0.006 %) |
| first downbeat | 0.143 s (bar-phase margin 0.254; snare backbeat ratio 1.84) |
| key | F# major [estimate, margin 0.138]; alternatives [['D# minor', 0.56], ['B major', 0.503]] |
| loudness | -9.19 LUFS integrated, short-term p10/p90 [-11.4, -7.9], crest 13.52 dB, sample peak 2.48 dBFS |
| stereo | side−mid -21.4 dB overall, -23.0 dB below 150 Hz |
| spectrum | 60.7 % of energy ≤150 Hz; centroid 2803.0 Hz; HF content to ~10809 Hz |
| swing (hat 16ths) | None % (50 straight, 66.7 triplet); off-8th hat delay 21.4 ms |
| perc vs harmonic | 2.1 dB |
| harmonic loop similarity (bar lags) | {'1': 0.199, '2': 0.744, '3': 0.093, '4': 0.589, '8': 0.55} |

**16-step onset occupancy** (X strong, x present; whole track):
```
        1 e & a 2 e & a 3 e & a 4 e & a
kick    X . . . x . X . x . X . x . X .
snare   X . . . X . . . x . x . X . . .
hat     X . x . X . X . X . x . X . X .
```
Median micro-timing per step (ms, + = late): kick [13.5, -21.4, -59.1, 29.8, 24.2, None, 22.9, None, 29.6, 17.0, 14.4, -4.2, 27.4, 23.8, 17.6, -66.9], snare [17.5, None, 29.8, None, 15.3, None, 27.1, None, 34.9, None, 18.4, None, 15.1, None, 22.0, None], hat [19.3, None, 22.5, None, 23.7, None, 19.2, None, 17.0, None, 27.3, None, 24.0, None, 20.2, None]

**Layer timeline** (per bar vs. track median; NO-LOW = sub ≥6 dB down, NO-DRUMS = percussive ≥6 dB down):
b1-3:NO-DRUMS,no-hats,melody+ | b4:NO-DRUMS,melody+ | b5-6:full | b7:melody+ | b8-13:full | b14:melody-off | b15-28:full | b29-32:NO-DRUMS,no-hats,melody+ | b33-37:full | b38:melody-off | b39-41:full | b42:melody-off | b43-45:full | b46:melody-off | b47-49:full | b50:melody-off | b51-53:full | b54:melody-off | b55-57:full | b58:melody-off | b59-60:full | b61:NO-LOW | b62-64:NO-LOW,NO-DRUMS,no-hats,melody-off

**Bars 2–9 harmonic sketch** [estimate: chroma template + bass chroma; not a transcription]: [D#5/D#5 bass D#-D#-D#-D#] [B5/B5 bass B-B-B-B] [D#5/D#5 bass D#-D#-D#-D#] [D#m7/F#maj7 bass D#-F#-F#-F#] [D7/F#maj7 bass F#-C-A#-A#] [D#m7/F#maj7 bass D#-F#-F#-F#] [D7/F#maj7 bass F#-C-A#-A#] [D#m7/F#maj7 bass D#-F#-F#-F#]

Pitch-class profile: {'C': 0.91, 'C#': 0.88, 'D': 0.72, 'D#': 0.9, 'E': 0.69, 'F': 0.71, 'F#': 1.0, 'G': 0.71, 'G#': 0.73, 'A': 0.78, 'A#': 0.96, 'B': 0.9}
Bass pitch-class profile: {'C': 0.96, 'C#': 0.87, 'D': 0.75, 'D#': 0.87, 'E': 0.7, 'F': 0.67, 'F#': 1.0, 'G': 0.69, 'G#': 0.69, 'A': 0.77, 'A#': 0.93, 'B': 0.87}
