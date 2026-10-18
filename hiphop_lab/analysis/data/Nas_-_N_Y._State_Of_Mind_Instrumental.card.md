## Measured profile [measured — scripts/analyze_track.py → analysis/data/Nas_-_N_Y._State_Of_Mind_Instrumental.json]

| metric | value |
|---|---|
| duration | 297.33 s, 104 bars of 2.841 s |
| tempo | **84.476 BPM** (grid residual p90 30.8 ms; comb candidates [[3.37, 84.5], [2.874, 169.05], [2.107, 112.65]]; drift first→last third -0.004 %) |
| first downbeat | 0.171 s (bar-phase margin 1.573; snare backbeat ratio 3.24) |
| key | C# major [estimate, margin 0.147]; alternatives [['C# minor', 0.427], ['F# minor', 0.414]] |
| loudness | -11.39 LUFS integrated, short-term p10/p90 [-12.9, -10.8], crest 12.7 dB, sample peak -0.3 dBFS |
| stereo | side−mid -24.3 dB overall, -23.1 dB below 150 Hz |
| spectrum | 65.2 % of energy ≤150 Hz; centroid 1788.0 Hz; HF content to ~10691 Hz |
| swing (hat 16ths) | 69.3 % (50 straight, 66.7 triplet); off-8th hat delay 44.4 ms |
| perc vs harmonic | -2.6 dB |
| harmonic loop similarity (bar lags) | {'1': -0.296, '2': 0.813, '3': -0.38, '4': 0.685, '8': 0.613} |

**16-step onset occupancy** (X strong, x present; whole track):
```
        1 e & a 2 e & a 3 e & a 4 e & a
kick    X . x x x . . . . x X . x . . X
snare   X . x . X . . . x X . . X . x .
hat     X . x . X . x . X X . . X . x .
```
Median micro-timing per step (ms, + = late): kick [15.7, -40.5, 11.7, 65.7, 18.6, 16.0, -18.0, 69.9, -58.7, 74.6, 8.0, 23.0, 12.6, 21.2, 43.7, 43.3], snare [7.5, 70.9, 12.1, 72.5, 5.4, 56.6, 46.7, 82.1, 64.1, 62.0, None, 63.1, 7.3, 74.2, 40.1, 76.1], hat [8.7, 78.5, 47.1, 45.2, 5.6, 52.5, 41.6, 72.3, 66.3, 64.8, 67.0, 61.7, 8.1, 72.0, 36.7, 72.4]

**Layer timeline** (per bar vs. track median; NO-LOW = sub ≥6 dB down, NO-DRUMS = percussive ≥6 dB down):
b1:low-thin | b2:full | b3:low-thin | b4:full | b5:low-thin | b6-48:full | b49-52:hats+ | b53:low-thin | b54:melody-off | b55:low-thin | b56-78:full | b79:low-thin,melody-off | b80:melody-off | b81-88:full | b89-97:hats+ | b98:hats+,melody-off | b99:low-thin,hats+,melody-off | b100:low-thin,melody-off | b101-104:NO-LOW,NO-DRUMS,no-hats,melody-off

**Bars 2–9 harmonic sketch** [estimate: chroma template + bass chroma; not a transcription]: [F#maj7/F#maj7 bass F-E-F-F] [F#maj7/F#maj7 bass F-F#-F-F] [F#maj7/F#maj7 bass F-F#-F-G] [A#m7/C#7 bass F-G#-C#-F] [Ddim/C#7 bass F-G#-G#-B] [C#5/C#7 bass C#-G#-G#-B] [Ddim/C#7 bass E-G#-G#-B] [C#5/C#7 bass C#-G#-G#-B]

Pitch-class profile: {'C': 0.39, 'C#': 0.68, 'D': 0.45, 'D#': 0.34, 'E': 0.52, 'F': 0.69, 'F#': 0.67, 'G': 0.54, 'G#': 1.0, 'A': 0.45, 'A#': 0.36, 'B': 0.57}
Bass pitch-class profile: {'C': 0.52, 'C#': 0.71, 'D': 0.45, 'D#': 0.37, 'E': 0.68, 'F': 0.76, 'F#': 0.68, 'G': 0.78, 'G#': 1.0, 'A': 0.43, 'A#': 0.44, 'B': 0.56}
