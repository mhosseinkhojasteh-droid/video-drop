# 'Seen It All' (instrumental, attributed to DJ Premier in the filename)

**Archetype:** Dark mafioso / NY boom-bap  ·  **Source file:** `references/raw/` (DJ_Premier_-_Seen_it_All_(instrumental))
**Evidence status:** measured by script; NOT listened to by the model. Every [hypothesis] needs the King's ear.

## 1. Identity & emotional character
Dark, mafioso, steady (no drop-outs in 66 bars) [measured]. C#-minor centre with m7 colour; 80 % ≤150 Hz [measured].

**Production history:** [unknown] — record identity/credits not verified; the filename says DJ Premier.

## 2–3. Tempo, groove, timing
91.96 BPM, strong swing (72 % — beyond triplet, i.e. very late off-beat 16ths/hats) [measured; estimate of feel] → heavy laid-back walk.

## 4–6. Drums, bass, harmony & texture
C#m7 ↔ E / C#5 alternation; bass C#–B–B–B then C#–C#–G#–C# [estimate] → minor 2-bar loop with a descending whole-step in the bass (C#→B).

## 7–9. Structure, sections, layer changes
One continuous loop, no measured drop-outs until the end [measured] → arrangement presumably done by the vocal and subtle filtering [hypothesis].
Full per-bar map: `analysis/structural_maps/DJ_Premier_-_Seen_it_All_(instrumental).csv` · plot: `analysis/plots/DJ_Premier_-_Seen_it_All_(instrumental).png`

## 11. Vocal compatibility
Dark low-mid weighted bed; rapper sits above [hypothesis].

## 12. Transferable principles
- Mafioso darkness = minor i–♭VII bass motion + heavy swing + no brightness.
- A loop can run 60+ bars if its internal 2-bar phrase has tension and release.

## 13. Signature elements that must NOT be reproduced
- The specific chop/sample

## 14. Open questions / needed evidence
- Producer, sample, year

## Measured profile [measured — scripts/analyze_track.py → analysis/data/DJ_Premier_-_Seen_it_All_(instrumental).json]

| metric | value |
|---|---|
| duration | 180.4 s, 68 bars of 2.6097 s |
| tempo | **91.963 BPM** (grid residual p90 8.5 ms; comb candidates [[4.06, 91.95], [3.688, 61.3], [2.929, 73.55]]; drift first→last third -0.034 %) |
| first downbeat | 1.988 s (bar-phase margin 2.106; snare backbeat ratio 2.67) |
| key | C# minor [estimate, margin 0.028]; alternatives [['G# minor', 0.655], ['C# major', 0.531]] |
| loudness | -12.27 LUFS integrated, short-term p10/p90 [-12.6, -12.0], crest 13.92 dB, sample peak 0.11 dBFS |
| stereo | side−mid -72.8 dB overall, -120.0 dB below 150 Hz |
| spectrum | 80.0 % of energy ≤150 Hz; centroid 2097.0 Hz; HF content to ~10610 Hz |
| swing (hat 16ths) | 72.3 % (50 straight, 66.7 triplet); off-8th hat delay 27.5 ms |
| perc vs harmonic | 0.6 dB |
| harmonic loop similarity (bar lags) | {'1': -0.678, '2': 0.652, '3': -0.69, '4': 0.675, '8': 0.941} |

**16-step onset occupancy** (X strong, x present; whole track):
```
        1 e & a 2 e & a 3 e & a 4 e & a
kick    X . X . x . . . . . X . x . . .
snare   x . . . X . . . . . x . X . x .
hat     x . x . X . x . x . x . X . X .
```
Median micro-timing per step (ms, + = late): kick [19.9, -57.6, 21.9, -59.1, 28.9, -27.7, 60.3, 61.6, -26.4, 12.3, 21.0, -42.7, 30.0, 15.5, 42.0, -64.4], snare [25.0, 61.0, 22.0, None, 18.2, None, 37.8, None, 26.8, None, 25.7, None, 17.0, None, 34.0, 75.4], hat [23.2, 72.7, 21.6, None, 20.9, None, 36.3, None, 24.6, None, 23.3, None, 18.6, None, 31.7, None]

**Layer timeline** (per bar vs. track median; NO-LOW = sub ≥6 dB down, NO-DRUMS = percussive ≥6 dB down):
b1-66:full | b67:low-thin | b68:NO-LOW,NO-DRUMS,no-hats,melody-off

**Bars 2–9 harmonic sketch** [estimate: chroma template + bass chroma; not a transcription]: [C#m7/E bass C#-B-B-B] [C#m7/C#5 bass C#-C#-G#-C#] [C#m7/E bass C#-B-B-B] [C#m7/C#5 bass C#-C#-G#-C#] [C#m7/E bass C#-B-B-B] [C#m7/C#5 bass C#-C#-G#-C#] [Fm7/C#m7 bass D#-D#-C#-B] [C#m7/C#5 bass C#-C#-G#-C#]

Pitch-class profile: {'C': 0.59, 'C#': 1.0, 'D': 0.35, 'D#': 0.62, 'E': 0.6, 'F': 0.43, 'F#': 0.35, 'G': 0.36, 'G#': 0.92, 'A': 0.34, 'A#': 0.38, 'B': 0.78}
Bass pitch-class profile: {'C': 0.6, 'C#': 1.0, 'D': 0.37, 'D#': 0.52, 'E': 0.51, 'F': 0.45, 'F#': 0.36, 'G': 0.35, 'G#': 0.58, 'A': 0.34, 'A#': 0.38, 'B': 0.8}
