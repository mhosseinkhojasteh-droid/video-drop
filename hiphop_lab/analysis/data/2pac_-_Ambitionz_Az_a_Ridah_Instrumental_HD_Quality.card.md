## Measured profile [measured — scripts/analyze_track.py → analysis/data/2pac_-_Ambitionz_Az_a_Ridah_Instrumental_HD_Quality.json]

| metric | value |
|---|---|
| duration | 276.98 s, 100 bars of 2.7499 s |
| tempo | **87.275 BPM** (grid residual p90 8.7 ms; comb candidates [[3.769, 87.3], [3.569, 174.6], [3.13, 69.85]]; drift first→last third -0.006 %) |
| first downbeat | 0.502 s (bar-phase margin 0.568; snare backbeat ratio 1.81) |
| key | G minor [estimate, margin 0.03]; alternatives [['D major', 0.276], ['F# minor', 0.225]] |
| loudness | -13.12 LUFS integrated, short-term p10/p90 [-13.3, -13.0], crest 14.77 dB, sample peak 0.66 dBFS |
| stereo | side−mid -17.9 dB overall, -21.5 dB below 150 Hz |
| spectrum | 81.5 % of energy ≤150 Hz; centroid 1652.0 Hz; HF content to ~10777 Hz |
| swing (hat 16ths) | 56.9 % (50 straight, 66.7 triplet); off-8th hat delay 17.5 ms |
| perc vs harmonic | -0.4 dB |
| harmonic loop similarity (bar lags) | {'1': 0.468, '2': 0.451, '3': 0.401, '4': 0.562, '8': 0.583} |

**16-step onset occupancy** (X strong, x present; whole track):
```
        1 e & a 2 e & a 3 e & a 4 e & a
kick    X x . . . X . X X . . . . X x .
snare   x . x . x . . . x . X . . . . .
hat     X . X . x X . x X . X . x x . .
```
Median micro-timing per step (ms, + = late): kick [4.3, 17.7, 19.7, None, 48.0, 11.6, -34.2, 12.5, 14.1, 45.4, 27.7, 34.6, None, 10.7, 6.1, None], snare [15.6, 54.9, 18.5, None, 30.7, 18.7, 35.4, 15.2, 10.9, None, 15.4, None, 32.9, 18.3, 13.8, None], hat [18.9, 59.4, 17.1, None, 22.3, 21.4, None, 11.7, 20.3, None, 17.5, None, 21.7, 23.8, 21.5, 44.5]

**Layer timeline** (per bar vs. track median; NO-LOW = sub ≥6 dB down, NO-DRUMS = percussive ≥6 dB down):
b1:NO-LOW,NO-DRUMS,no-hats,melody-off | b2:NO-LOW,NO-DRUMS,no-hats | b3-18:full | b19:low-thin,NO-DRUMS,no-hats | b20-54:full | b55:low-thin,NO-DRUMS,no-hats | b56-90:full | b91:low-thin,NO-DRUMS,no-hats | b92-98:full | b99:NO-LOW,NO-DRUMS,no-hats | b100:NO-LOW,NO-DRUMS,no-hats,melody-off

**Bars 2–9 harmonic sketch** [estimate: chroma template + bass chroma; not a transcription]: [A#maj7/A#7 bass A-A-A#-G#] [Gmaj7/Gmaj7 bass F-G-G#-G#] [Gmaj7/Gmaj7 bass F-G-G#-G#] [Gmaj7/Gmaj7 bass F-G-G#-G#] [Gmaj7/Gmaj7 bass F-G-G#-G#] [Gmaj7/Gmaj7 bass F-G-G#-G#] [A#maj7/A#7 bass F-A-A#-G#] [Gmaj7/Gmaj7 bass F-G-G#-G#]

Pitch-class profile: {'C': 0.27, 'C#': 0.27, 'D': 0.65, 'D#': 0.33, 'E': 0.37, 'F': 0.64, 'F#': 0.98, 'G': 1.0, 'G#': 0.99, 'A': 0.6, 'A#': 0.52, 'B': 0.25}
Bass pitch-class profile: {'C': 0.25, 'C#': 0.25, 'D': 0.53, 'D#': 0.37, 'E': 0.3, 'F': 0.5, 'F#': 0.89, 'G': 0.99, 'G#': 1.0, 'A': 0.52, 'A#': 0.5, 'B': 0.25}
