# Dr. Dre — Still D.R.E. (1999)

**Archetype:** West Coast 2001-era (piano-led)  ·  **Source file:** `references/raw/` (Dr_Dre-_Still_Dre_instrumental)
**Evidence status:** measured by script; NOT listened to by the model. Every [hypothesis] needs the King's ear.

## 1. Identity & emotional character
Iconic, regal, minimal. Piano-only intro bars 1–3 (hats −42 dB → −29 dB at bar 5) [measured]. 105 bars with essentially no arrangement changes [measured] — the riff carries the whole record.

**Production history:** Produced by Dr. Dre and Mel-Man; the piano riff played by Scott Storch [documented].

## 2–3. Tempo, groove, timing
93.43 BPM; snare 2 & 4; strong late off-beats (swing ≈ 72.9 % on 16ths) [measured; estimate of feel].

## 4–6. Drums, bass, harmony & texture
Strict 1-bar alternation of two pitch-sets (chroma flips A#/F ↔ E/A every bar) [measured on chroma plot] → a 2-bar riff of staccato piano chords.

## 7–9. Structure, sections, layer changes
Intro 4 bars piano (+strings) → full from bar 5 → no changes until outro [measured].
Full per-bar map: `analysis/structural_maps/Dr_Dre-_Still_Dre_instrumental.csv` · plot: `analysis/plots/Dr_Dre-_Still_Dre_instrumental.png`

## 11. Vocal compatibility
Piano occupies 500 Hz–2 kHz (15.9 % — highest mid share of batch 1) but in short staccato hits, leaving gaps [measured + hypothesis].

## 12. Transferable principles
- A staccato chord riff with rests can fill the mids without masking vocals.
- No arrangement needed if the 2-bar riff is strong enough — minimalism as confidence.
- Piano intro before drums: 4 bars.

## 13. Signature elements that must NOT be reproduced
- The Still D.R.E. piano riff (chord voicings + rhythm)
- Its string line

## 14. Open questions / needed evidence
- Exact voicings (needs transcription)

## Measured profile [measured — scripts/analyze_track.py → analysis/data/Dr_Dre-_Still_Dre_instrumental.json]

| metric | value |
|---|---|
| duration | 271.96 s, 105 bars of 2.5688 s |
| tempo | **93.428 BPM** (grid residual p90 9.4 ms; comb candidates [[4.046, 93.4], [3.783, 62.25], [3.059, 124.5]]; drift first→last third 0.017 %) |
| first downbeat | 0.864 s (bar-phase margin 0.105; snare backbeat ratio 3.21) |
| key | F major [estimate, margin 0.142]; alternatives [['F minor', 0.498], ['A# minor', 0.439]] |
| loudness | -11.33 LUFS integrated, short-term p10/p90 [-11.9, -10.8], crest 13.13 dB, sample peak 0.69 dBFS |
| stereo | side−mid -16.5 dB overall, -18.9 dB below 150 Hz |
| spectrum | 66.9 % of energy ≤150 Hz; centroid 2137.0 Hz; HF content to ~10815 Hz |
| swing (hat 16ths) | 72.9 % (50 straight, 66.7 triplet); off-8th hat delay 28.8 ms |
| perc vs harmonic | -0.8 dB |
| harmonic loop similarity (bar lags) | {'1': -0.884, '2': 0.857, '3': -0.891, '4': 0.944, '8': 0.927} |

**16-step onset occupancy** (X strong, x present; whole track):
```
        1 e & a 2 e & a 3 e & a 4 e & a
kick    x . . . . X . . X . . . X . . .
snare   x . x . X . x . X . x . X . x .
hat     X . x . x . X . X . x . x . x .
```
Median micro-timing per step (ms, + = late): kick [9.7, -56.1, 19.5, -42.6, 14.3, 70.0, -3.7, None, -0.8, -55.6, 64.6, -46.7, 17.0, -71.7, 53.3, -25.4], snare [22.4, 69.0, 43.3, None, 24.4, 77.2, 25.5, -64.0, 20.2, -60.4, 49.5, 66.9, 22.6, 69.7, 36.7, 67.7], hat [19.6, 69.6, 37.3, None, 25.9, 77.6, 12.2, None, 18.1, None, 37.2, None, 25.9, 78.1, 20.3, 67.7]

**Layer timeline** (per bar vs. track median; NO-LOW = sub ≥6 dB down, NO-DRUMS = percussive ≥6 dB down):
b1-3:NO-DRUMS,no-hats | b4:low-thin,NO-DRUMS | b5-103:full | b104:low-thin,no-hats,melody-off | b105:NO-LOW,NO-DRUMS,no-hats,melody-off

**Bars 2–9 harmonic sketch** [estimate: chroma template + bass chroma; not a transcription]: [Fmaj7/Fmaj7 bass E-F-E-E] [A#maj7/Cmaj7 bass A#-A#-A#-B] [Fmaj7/Fmaj7 bass E-E-D#-A] [A#maj7/Cmaj7 bass A#-A-C-B] [Fmaj7/Fmaj7 bass F-E-E-E] [A#maj7/Cmaj7 bass A-A-C-B] [Fmaj7/Fmaj7 bass E-E-A-A] [A#maj7/Cmaj7 bass A#-A#-C-B]

Pitch-class profile: {'C': 0.77, 'C#': 0.52, 'D': 0.41, 'D#': 0.5, 'E': 0.91, 'F': 1.0, 'F#': 0.36, 'G': 0.36, 'G#': 0.5, 'A': 0.64, 'A#': 0.86, 'B': 0.52}
Bass pitch-class profile: {'C': 0.69, 'C#': 0.49, 'D': 0.58, 'D#': 0.66, 'E': 1.0, 'F': 0.82, 'F#': 0.45, 'G': 0.35, 'G#': 0.4, 'A': 0.72, 'A#': 0.72, 'B': 0.59}
