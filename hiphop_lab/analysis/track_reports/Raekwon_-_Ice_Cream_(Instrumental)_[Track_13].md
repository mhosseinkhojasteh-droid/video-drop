# Raekwon — Ice Cream (1995)

**Archetype:** Wu-Tang mafioso / soulful-dark  ·  **Source file:** `references/raw/` (Raekwon_-_Ice_Cream_(Instrumental)_[Track_13])
**Evidence status:** measured by script; NOT listened to by the model. Every [hypothesis] needs the King's ear.

## 1. Identity & emotional character
Smooth-menacing, mafioso cool. Essentially MONO (side−mid −40 dB) [measured] — 90s Wu mixes are mono-centred; percussion 9.3 dB above harmonic content [measured] → drums dominate.

**Production history:** Produced by RZA [documented]. Only Built 4 Cuban Linx… Sample attributions not verified here.

## 2–3. Tempo, groove, timing
89.6 BPM, swing 66 % (triplet) [measured]; hats 26 ms late on off-8ths [measured].

## 4–6. Drums, bass, harmony & texture
C#-minor area with dominant-7 colours (D#7, F#7, A7) [estimate] → soul-sample chords.

## 7–9. Structure, sections, layer changes
Single/two-bar full drop-outs at b47, b68–69, b83 [measured] (section markers); many single 'melody+' bars every 4 bars [measured] → sample phrase accent on bar 4.
Full per-bar map: `analysis/structural_maps/Raekwon_-_Ice_Cream_(Instrumental)_[Track_13].csv` · plot: `analysis/plots/Raekwon_-_Ice_Cream_(Instrumental)_[Track_13].png`

## 11. Vocal compatibility
Mono, mid-quiet bed; vocals centre [hypothesis].

## 12. Transferable principles
- Mono-centred mix = old-school weight; width is not required for impact.
- Drums louder than the sample (+9 dB perc vs harmonic) = RZA grit.
- Drop-out bars as section markers.

## 13. Signature elements that must NOT be reproduced
- The sample and its chop

## 14. Open questions / needed evidence
- Sample sources

## Measured profile [measured — scripts/analyze_track.py → analysis/data/Raekwon_-_Ice_Cream_(Instrumental)_[Track_13].json]

| metric | value |
|---|---|
| duration | 299.1 s, 111 bars of 2.6794 s |
| tempo | **89.571 BPM** (grid residual p90 14.3 ms; comb candidates [[2.974, 89.55], [2.681, 178.95], [2.084, 119.45]]; drift first→last third 0.008 %) |
| first downbeat | 1.442 s (bar-phase margin 0.042; snare backbeat ratio 1.65) |
| key | C# minor [estimate, margin 0.104]; alternatives [['C# major', 0.605], ['G# minor', 0.398]] |
| loudness | -13.26 LUFS integrated, short-term p10/p90 [-14.3, -12.4], crest 14.0 dB, sample peak -0.47 dBFS |
| stereo | side−mid -40.2 dB overall, -51.9 dB below 150 Hz |
| spectrum | 69.2 % of energy ≤150 Hz; centroid 2168.0 Hz; HF content to ~10761 Hz |
| swing (hat 16ths) | 66.4 % (50 straight, 66.7 triplet); off-8th hat delay 26.1 ms |
| perc vs harmonic | 9.3 dB |
| harmonic loop similarity (bar lags) | {'1': 0.109, '2': 0.183, '3': -0.05, '4': 0.43, '8': 0.305} |

**16-step onset occupancy** (X strong, x present; whole track):
```
        1 e & a 2 e & a 3 e & a 4 e & a
kick    x . X . . . . X x . . . . . . X
snare   x . . . X . X . x . X . x x . x
hat     x . x . X . x . x . X . . . x .
```
Median micro-timing per step (ms, + = late): kick [10.8, None, 5.1, 19.5, 29.1, 1.2, 14.5, 21.0, 10.0, -31.2, 16.5, -4.5, 40.1, 73.6, -78.5, 19.6], snare [28.3, 71.6, 33.0, 69.2, 17.1, None, -3.9, 39.4, 12.9, 57.6, 19.8, None, 32.1, 74.4, 29.2, 34.7], hat [34.8, 75.5, 37.4, 77.3, 14.9, None, 16.1, 52.4, 16.0, 28.2, 19.0, 40.1, 40.4, 78.1, 33.1, 54.9]

**Layer timeline** (per bar vs. track median; NO-LOW = sub ≥6 dB down, NO-DRUMS = percussive ≥6 dB down):
b1:melody+ | b2:full | b3:hats+ | b4:hats+,melody+ | b5-16:full | b17:melody+ | b18-23:full | b24:low-thin | b25:melody+ | b26-27:full | b28:hats+ | b29-30:hats+,melody+ | b31-44:full | b45:hats+,melody+ | b46:low-thin,melody+ | b47:NO-LOW,NO-DRUMS | b48-60:full | b61:melody+ | b62-64:full | b65:melody+ | b66:full | b67:low-thin | b68:NO-LOW,NO-DRUMS | b69:NO-LOW,NO-DRUMS,no-hats | b70-71:full | b72-74:melody+ | b75-76:full | b77:melody+ | b78-80:full | b81:melody+ | b82:full | b83:NO-LOW,NO-DRUMS | b84-88:full | b89:melody+ | b90-92:full | b93:melody+ | b94-96:full | b97:melody+ | b98-100:full | b101:melody+ | b102-104:full | b105:melody+ | b106-107:full | b108-111:NO-LOW,NO-DRUMS,no-hats,melody-off

**Bars 2–9 harmonic sketch** [estimate: chroma template + bass chroma; not a transcription]: [D#maj7/C#m bass D-G-D#-D#] [F#7/Emaj7 bass F#-F#-D#-D#] [D#7/C#m bass F-G-D#-D#] [A7/Amaj7 bass D-G-D#-D] [D#7/C#m bass F-G-D#-D#] [F#7/C#m bass F#-F#-D#-C#] [D#7/C#m bass F-G-D#-D#] [Amaj7/Amaj7 bass F-G-D#-D]

Pitch-class profile: {'C': 0.38, 'C#': 0.9, 'D': 0.55, 'D#': 0.7, 'E': 0.78, 'F': 0.51, 'F#': 0.73, 'G': 0.57, 'G#': 1.0, 'A': 0.56, 'A#': 0.68, 'B': 0.29}
Bass pitch-class profile: {'C': 0.6, 'C#': 0.82, 'D': 0.84, 'D#': 1.0, 'E': 0.83, 'F': 0.91, 'F#': 0.81, 'G': 0.89, 'G#': 0.85, 'A': 0.71, 'A#': 0.67, 'B': 0.27}
