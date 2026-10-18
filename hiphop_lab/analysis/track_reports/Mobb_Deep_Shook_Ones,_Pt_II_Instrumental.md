# Mobb Deep — Shook Ones, Pt. II (1995)

**Archetype:** Gritty underground NY (canonical)  ·  **Source file:** `references/raw/` (Mobb_Deep_Shook_Ones,_Pt_II_Instrumental)
**Evidence status:** measured by script; NOT listened to by the model. Every [hypothesis] needs the King's ear.

## 1. Identity & emotional character
Paranoid, cold, claustrophobic. G-minor, pitch profile spread (dissonant cluster) [measured/estimate].

**Production history:** Produced by Havoc; contains a sped/pitched Herbie Hancock 'Jessica' piano fragment and other jazz samples [documented, moderate confidence — verify]. 128 kbps source [measured].

## 2–3. Tempo, groove, timing
93.97 BPM; busy kick (x.x.xXX.x.X.xxX.) [measured] — the famous dense, stumbling kick pattern feel.

## 4–6. Drums, bass, harmony & texture
G-minor with a dissonant high piano figure [estimate]; Gm7/Cm7 sketches.

## 7–9. Structure, sections, layer changes
Intro 6 bars: drums/low enter and leave (b1–3 none, b4–5 partial, b6 none) [measured] → teasing intro; melody-off block b37–40 [measured].
Full per-bar map: `analysis/structural_maps/Mobb_Deep_Shook_Ones,_Pt_II_Instrumental.csv` · plot: `analysis/plots/Mobb_Deep_Shook_Ones,_Pt_II_Instrumental.png`

## 11. Vocal compatibility
Mid band quiet, the high piano stab sits above the vocal range [hypothesis].

## 12. Transferable principles
- Dissonant, tiny, high-register loop + heavy sub = paranoia.
- Intro that teases the drums before committing.
- Kick density as aggression (busy kick, plain snare).

## 13. Signature elements that must NOT be reproduced
- The piano fragment / sample
- The exact kick pattern

## 14. Open questions / needed evidence
- Sample sources (verify)

## Measured profile [measured — scripts/analyze_track.py → analysis/data/Mobb_Deep_Shook_Ones,_Pt_II_Instrumental.json]

| metric | value |
|---|---|
| duration | 276.74 s, 108 bars of 2.554 s |
| tempo | **93.971 BPM** (grid residual p90 6.9 ms; comb candidates [[4.353, 94.0], [3.969, 62.65], [3.27, 125.25]]; drift first→last third -0.008 %) |
| first downbeat | 0.718 s (bar-phase margin 0.376; snare backbeat ratio 0.99) |
| key | G minor [estimate, margin 0.198]; alternatives [['G major', 0.407], ['D# major', 0.318]] |
| loudness | -12.32 LUFS integrated, short-term p10/p90 [-12.9, -11.7], crest 12.03 dB, sample peak -1.09 dBFS |
| stereo | side−mid -21.6 dB overall, -21.4 dB below 150 Hz |
| spectrum | 81.0 % of energy ≤150 Hz; centroid 2060.0 Hz; HF content to ~10820 Hz |
| swing (hat 16ths) | 58.9 % (50 straight, 66.7 triplet); off-8th hat delay 20.2 ms |
| perc vs harmonic | -7.9 dB |
| harmonic loop similarity (bar lags) | {'1': -0.389, '2': 0.798, '3': -0.306, '4': 0.576, '8': 0.452} |

**16-step onset occupancy** (X strong, x present; whole track):
```
        1 e & a 2 e & a 3 e & a 4 e & a
kick    x . x . x X X . x . X . x x X .
snare   x . X . x . . . X . X . x . x .
hat     X . X . X . x . X . X . X . x .
```
Median micro-timing per step (ms, + = late): kick [19.3, -1.6, -0.7, 19.9, 36.9, 69.6, 23.9, -54.4, 20.6, 5.1, 25.3, -16.4, 27.4, 71.1, 32.0, None], snare [13.0, 29.6, 13.2, None, 32.5, None, 27.4, None, 14.5, 29.8, 13.1, None, 31.6, None, 26.5, 52.4], hat [18.3, 29.2, 15.4, None, 23.5, None, 25.1, None, 17.9, 27.8, 13.2, None, 23.4, None, 25.6, None]

**Layer timeline** (per bar vs. track median; NO-LOW = sub ≥6 dB down, NO-DRUMS = percussive ≥6 dB down):
b1:NO-LOW,NO-DRUMS,melody-off | b2-3:NO-LOW,NO-DRUMS | b4:NO-LOW | b5:low-thin | b6:NO-LOW,NO-DRUMS | b7-36:full | b37-40:melody-off | b41-47:full | b48:melody+ | b49:full | b50:melody+ | b51-83:full | b84:melody+ | b85:full | b86:melody+ | b87-89:full | b90:melody+ | b91:full | b92:melody+ | b93-102:full | b103:low-thin,melody-off | b104-108:NO-LOW,NO-DRUMS,no-hats,melody-off

**Bars 2–9 harmonic sketch** [estimate: chroma template + bass chroma; not a transcription]: [Gm7/Gm7 bass F#-F#-F-F] [Gm/Cm7 bass F-F-B-F#] [Gm7/C5 bass F#-F#-G-G] [Gm7/Cm7 bass G-G-G#-F#] [Gm7/Gm7 bass F#-F#-F-F] [Gmaj7/Gmaj7 bass G-G-G-G] [Gmaj7/Gm7 bass G-G-G-G] [Gm7/Gmaj7 bass G-G-G-G]

Pitch-class profile: {'C': 0.21, 'C#': 0.21, 'D': 0.22, 'D#': 0.23, 'E': 0.18, 'F': 0.35, 'F#': 0.45, 'G': 1.0, 'G#': 0.26, 'A': 0.31, 'A#': 0.36, 'B': 0.15}
Bass pitch-class profile: {'C': 0.17, 'C#': 0.19, 'D': 0.17, 'D#': 0.21, 'E': 0.18, 'F': 0.32, 'F#': 0.46, 'G': 1.0, 'G#': 0.25, 'A': 0.3, 'A#': 0.3, 'B': 0.14}
