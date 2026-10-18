## Measured profile [measured — scripts/analyze_track.py → analysis/data/Nas_-_Nas_Is_Like_(Instrumental)_-_HQ.json]

| metric | value |
|---|---|
| duration | 241.07 s, 94 bars of 2.54 s |
| tempo | **94.488 BPM** (grid residual p90 6.6 ms; comb candidates [[3.492, 94.5], [2.941, 63.0], [2.17, 126.1]]; drift first→last third -0.001 %) |
| first downbeat | 0.356 s (bar-phase margin 0.953; snare backbeat ratio 2.62) |
| key | F# minor [estimate, margin 0.096]; alternatives [['C# minor', 0.477], ['C# major', 0.351]] |
| loudness | -15.03 LUFS integrated, short-term p10/p90 [-16.1, -14.3], crest 14.75 dB, sample peak -1.7 dBFS |
| stereo | side−mid -25.8 dB overall, -25.1 dB below 150 Hz |
| spectrum | 75.6 % of energy ≤150 Hz; centroid 2350.0 Hz; HF content to ~10755 Hz |
| swing (hat 16ths) | 74.2 % (50 straight, 66.7 triplet); off-8th hat delay 33.4 ms |
| perc vs harmonic | 0.3 dB |
| harmonic loop similarity (bar lags) | {'1': -0.678, '2': 0.861, '3': -0.712, '4': 0.822, '8': 0.771} |

**16-step onset occupancy** (X strong, x present; whole track):
```
        1 e & a 2 e & a 3 e & a 4 e & a
kick    X . X . X . . . x . X . x . . .
snare   x . . . X . x . X . . . X . . .
hat     x . x . X . x . X . x . X . x .
```
Median micro-timing per step (ms, + = late): kick [25.5, -40.1, 24.7, -40.3, 12.6, None, None, 43.4, 34.1, 13.2, 24.2, -42.2, 34.6, -60.2, 10.4, -54.2], snare [24.3, None, 24.3, None, 17.0, None, 45.7, None, 23.6, None, 24.4, None, 17.9, None, 47.6, 76.8], hat [26.9, None, 24.0, None, 17.8, None, 42.7, None, 23.5, None, 22.0, None, 17.5, None, 43.3, 76.8]

**Layer timeline** (per bar vs. track median; NO-LOW = sub ≥6 dB down, NO-DRUMS = percussive ≥6 dB down):
b1-3:low-thin,melody-off | b4:melody-off | b5-8:low-thin,melody-off | b9-27:full | b28:NO-LOW,NO-DRUMS,no-hats,melody-off | b29-57:full | b58:no-hats | b59-81:full | b82:NO-LOW,no-hats,melody-off | b83-90:full | b91:melody-off | b92:low-thin,melody-off | b93:NO-LOW,no-hats,melody-off | b94:NO-LOW,NO-DRUMS,no-hats,melody-off

**Bars 2–9 harmonic sketch** [estimate: chroma template + bass chroma; not a transcription]: [Amaj7/A#7 bass G#-C#-G#-G] [G#maj7/Amaj7 bass G#-G-G#-G#] [Amaj7/A#7 bass G#-C#-G#-G#] [G#maj7/Amaj7 bass G#-G-G#-G#] [Amaj7/A#m7 bass G#-G#-G#-G#] [A#m7/Amaj7 bass G#-G-G#-G#] [Amaj7/A#maj7 bass G#-G-G#-A] [Gmaj7/Amaj7 bass F#-F#-F#-G#]

Pitch-class profile: {'C': 0.48, 'C#': 0.83, 'D': 0.38, 'D#': 0.3, 'E': 0.48, 'F': 0.42, 'F#': 0.8, 'G': 0.76, 'G#': 1.0, 'A': 0.79, 'A#': 0.48, 'B': 0.59}
Bass pitch-class profile: {'C': 0.6, 'C#': 0.73, 'D': 0.4, 'D#': 0.28, 'E': 0.3, 'F': 0.53, 'F#': 0.85, 'G': 0.86, 'G#': 1.0, 'A': 0.78, 'A#': 0.52, 'B': 0.57}
