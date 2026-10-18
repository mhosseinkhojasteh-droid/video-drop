# 50 Cent — Candy Shop (2005)

**Archetype:** G-Unit/Storch club · exotic-minor seduction  ·  **Source file:** `references/raw/` (50_Cent_-_Candy_Shop_instrumental)
**Evidence status:** measured by script; NOT listened to by the model. Every [hypothesis] needs the King's ear.

## 1. Identity & emotional character
Seductive, exotic, minimal club record. 85 % of energy ≤150 Hz [measured] — the sub owns it; the melodic hook is sparse and modal.

**Production history:** Produced by Scott Storch [documented]. The Massacre; features Olivia.

## 2–3. Tempo, groove, timing
98.0 BPM [measured]. Hat occupancy concentrated on beat 2 and 3-and (sparse) [measured]; a call-and-response between hook stabs and sub hits [hypothesis].

## 4–6. Drums, bass, harmony & texture
F#-minor centre with the G (flat-2) prominent: bars alternate G-ish / F#-ish (Gmaj7/F#5 sketches) [estimate] → Phrygian colour (♭2 over the tonic) = the 'Middle-Eastern' flavour [hypothesis consistent with chroma].

## 7–9. Structure, sections, layer changes
4-bar cycle of variation: 'melody+' and 'hats+' bars recur every 4 bars (b9, 13, 33, 37, 41…; hats+ b6, 10, 14…) [measured] → ear-candy every 4th bar keeps a static loop alive.
Full per-bar map: `analysis/structural_maps/50_Cent_-_Candy_Shop_instrumental.csv` · plot: `analysis/plots/50_Cent_-_Candy_Shop_instrumental.png`

## 11. Vocal compatibility
Mid band nearly empty [measured] → vocals and the female hook sit on top.

## 12. Transferable principles
- Phrygian ♭2 against the tonic = instant exotic tension (and a Persian-friendly scale).
- Change something every 4th bar (fill, extra hat, hook stab) without changing the loop.
- Let the sub carry the groove; the melody only punctuates.

## 13. Signature elements that must NOT be reproduced
- The Candy Shop hook motif and its rhythmic placement

## 14. Open questions / needed evidence
- Exact instrument (synth vs. sampled ethnic instrument)

## Measured profile [measured — scripts/analyze_track.py → analysis/data/50_Cent_-_Candy_Shop_instrumental.json]

| metric | value |
|---|---|
| duration | 209.73 s, 85 bars of 2.4487 s |
| tempo | **98.01 BPM** (grid residual p90 7.6 ms; comb candidates [[3.063, 98.0], [2.269, 65.35], [1.739, 130.7]]; drift first→last third -0.009 %) |
| first downbeat | 1.45 s (bar-phase margin 0.085; snare backbeat ratio 5.63) |
| key | F# minor [estimate, margin 0.034]; alternatives [['F# major', 0.319], ['D major', 0.25]] |
| loudness | -9.9 LUFS integrated, short-term p10/p90 [-10.5, -9.3], crest 11.6 dB, sample peak 1.17 dBFS |
| stereo | side−mid -14.8 dB overall, -21.1 dB below 150 Hz |
| spectrum | 84.7 % of energy ≤150 Hz; centroid 1791.0 Hz; HF content to ~10777 Hz |
| swing (hat 16ths) | 44.7 % (50 straight, 66.7 triplet); off-8th hat delay 39.8 ms |
| perc vs harmonic | 0.0 dB |
| harmonic loop similarity (bar lags) | {'1': -0.086, '2': 0.292, '3': -0.124, '4': 0.602, '8': 0.505} |

**16-step onset occupancy** (X strong, x present; whole track):
```
        1 e & a 2 e & a 3 e & a 4 e & a
kick    X . . X . . . . X . . . . . . .
snare   x . . . X . . . . . . x . . x .
hat     . . . . X . . . . . . x . . . .
```
Median micro-timing per step (ms, + = late): kick [15.7, -37.8, 22.0, 15.7, -38.3, 65.6, 6.9, -15.8, 14.3, -5.3, 47.6, 24.4, 19.7, None, 27.5, -19.8], snare [45.4, 37.3, 29.5, 19.9, 14.5, 33.1, 24.2, None, 35.2, None, None, 15.3, 30.8, None, 32.3, -49.1], hat [52.5, -3.1, 37.6, 39.6, 14.0, None, 43.2, -30.4, 37.6, -70.8, None, 26.4, 32.6, None, 39.8, -29.6]

**Layer timeline** (per bar vs. track median; NO-LOW = sub ≥6 dB down, NO-DRUMS = percussive ≥6 dB down):
b1:NO-LOW,NO-DRUMS,no-hats,melody+ | b2:low-thin,NO-DRUMS | b3:melody-off | b4-5:full | b6:hats+ | b7-8:full | b9:melody+ | b10:hats+ | b11-12:full | b13:melody+ | b14:hats+ | b15:melody-off | b16-17:full | b18:hats+ | b19:melody-off | b20-21:full | b22:hats+ | b23-25:full | b26:hats+ | b27:melody-off | b28-29:full | b30:hats+ | b31-32:full | b33:melody+ | b34:hats+ | b35-36:full | b37:melody+ | b38:hats+ | b39-40:full | b41:melody+ | b42:hats+ | b43:melody-off | b44-45:full | b46:hats+ | b47:melody-off | b48-49:full | b50:hats+ | b51-53:full | b54:hats+ | b55:melody-off | b56-57:full | b58:hats+ | b59-60:full | b61:melody+ | b62:hats+ | b63-64:full | b65:melody+ | b66:hats+ | b67-69:full | b70:hats+ | b71-73:full | b74:hats+ | b75-77:melody+ | b78:hats+,melody+ | b79:melody+ | b80:low-thin | b81:NO-LOW,NO-DRUMS,no-hats | b82-85:NO-LOW,NO-DRUMS,no-hats,melody-off

**Bars 2–9 harmonic sketch** [estimate: chroma template + bass chroma; not a transcription]: [B5/Gmaj7 bass B-B-F#-F#] [Gmaj7/Gmaj7 bass G-F#-F#-F#] [Gmaj7/Gmaj7 bass G-F#-F#-F#] [Gmaj7/F#5 bass G-F#-F#-F#] [Gmaj7/Gmaj7 bass G-F#-F#-F#] [Gmaj7/Gmaj7 bass G-F#-F#-F#] [Gmaj7/F#maj7 bass G-F#-F#-F#] [Gmaj7/F#5 bass G-F#-F#-F#]

Pitch-class profile: {'C': 0.08, 'C#': 0.13, 'D': 0.13, 'D#': 0.18, 'E': 0.27, 'F': 0.41, 'F#': 1.0, 'G': 0.6, 'G#': 0.27, 'A': 0.18, 'A#': 0.14, 'B': 0.1}
Bass pitch-class profile: {'C': 0.08, 'C#': 0.1, 'D': 0.12, 'D#': 0.19, 'E': 0.28, 'F': 0.45, 'F#': 1.0, 'G': 0.6, 'G#': 0.27, 'A': 0.19, 'A#': 0.12, 'B': 0.07}
