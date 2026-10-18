# Ice Cube — Why We Thugs (2006)

**Archetype:** G-Unit/Storch-era street-club · West Coast attitude  ·  **Source file:** `references/raw/` (Ice_Cube_Why_We_Thugs_Instrumental)
**Evidence status:** measured by script; NOT listened to by the model. Every [hypothesis] needs the King's ear.

## 1. Identity & emotional character
Hard, bright, loop-driven street anthem. Constant energy (LUFS spread tiny), dense low end (77 % ≤150 Hz) [measured]. Emotion: defiance, swagger [hypothesis].

**Production history:** Produced by Scott Storch [documented]. Laugh Now, Cry Later era.

## 2–3. Tempo, groove, timing
99.0 BPM, very stable grid; kick on 1 and around beat 3 region with snare on 2 & 4 [measured]. Hats sparse in occupancy → the rhythmic drive is carried by the melodic synth riff, not by a busy hat [hypothesis from occupancy + melody+ bars].

## 4–6. Drums, bass, harmony & texture
Two-chord pendulum in the A–B–C area (chroma alternates A-minor-ish / B-ish every half bar) [estimate]. Storch signature: a single repeated synth/keys hook carrying the whole tension.

## 7–9. Structure, sections, layer changes
Arrangement by 8-bar 'melody+' blocks: bars 5–12, 29–36, 53–60, 77–84 add a melodic layer (hook sections) on a 24-bar cycle (16 verse + 8 hook) [measured timeline; section function = hypothesis].
Full per-bar map: `analysis/structural_maps/Ice_Cube_Why_We_Thugs_Instrumental.csv` · plot: `analysis/plots/Ice_Cube_Why_We_Thugs_Instrumental.png`

## 11. Vocal compatibility
Mids are left open in verses (melody layer drops out), which is where the rapper sits; hooks add the lead synth [hypothesis].

## 12. Transferable principles
- One unforgettable riff + constant drums; arrangement = adding/removing that riff in 8-bar blocks.
- Keep a 24-bar verse+hook cycle with no dead bars.
- Loud but not crushed: −9.4 LUFS with 11 dB crest.

## 13. Signature elements that must NOT be reproduced
- The riff's exact interval/rhythm sequence
- Its specific synth timbre combination

## 14. Open questions / needed evidence
- Exact instrument identities
- Whether the hook layer is strings, synth brass or keys

## Measured profile [measured — scripts/analyze_track.py → analysis/data/Ice_Cube_Why_We_Thugs_Instrumental.json]

| metric | value |
|---|---|
| duration | 228.09 s, 93 bars of 2.4242 s |
| tempo | **99.002 BPM** (grid residual p90 8.3 ms; comb candidates [[3.771, 99.0], [2.968, 66.0], [2.23, 79.2]]; drift first→last third -0.001 %) |
| first downbeat | 0.221 s (bar-phase margin 0.002; snare backbeat ratio 6.78) |
| key | B major [estimate, margin 0.012]; alternatives [['E minor', 0.458], ['B minor', 0.376]] |
| loudness | -9.35 LUFS integrated, short-term p10/p90 [-9.8, -9.0], crest 11.17 dB, sample peak 0.78 dBFS |
| stereo | side−mid -19.3 dB overall, -23.4 dB below 150 Hz |
| spectrum | 76.9 % of energy ≤150 Hz; centroid 1043.0 Hz; HF content to ~10782 Hz |
| swing (hat 16ths) | 35.0 % (50 straight, 66.7 triplet); off-8th hat delay 44.5 ms |
| perc vs harmonic | 0.0 dB |
| harmonic loop similarity (bar lags) | {'1': -0.507, '2': 0.488, '3': -0.579, '4': 0.524, '8': 0.77} |

**16-step onset occupancy** (X strong, x present; whole track):
```
        1 e & a 2 e & a 3 e & a 4 e & a
kick    X . . . . . X . x . . . x . . .
snare   x . . . X . . . . . . . X . . .
hat     x . . . X . . . . . . . X . . .
```
Median micro-timing per step (ms, + = late): kick [-5.3, -16.7, 29.8, -3.8, -39.1, -59.8, 20.2, -29.0, 32.7, 36.3, None, None, 15.7, -56.9, 58.5, None], snare [15.7, -55.4, 22.6, -60.0, 20.2, None, 47.9, -55.5, 24.5, -40.3, None, None, 19.1, None, None, -39.4], hat [27.7, -10.5, 30.3, -57.5, 12.1, None, 58.8, -45.5, 39.3, None, None, None, 11.7, None, None, None]

**Layer timeline** (per bar vs. track median; NO-LOW = sub ≥6 dB down, NO-DRUMS = percussive ≥6 dB down):
b1-4:full | b5-12:melody+ | b13-28:full | b29-36:melody+ | b37-43:full | b44:melody-off | b45-52:full | b53-60:melody+ | b61-62:melody-off | b63-76:full | b77-84:melody+ | b85-92:full | b93:NO-LOW,NO-DRUMS,no-hats,melody-off

**Bars 2–9 harmonic sketch** [estimate: chroma template + bass chroma; not a transcription]: [Amaj7/Cmaj7 bass A-C-B-C] [B/Cmaj7 bass B-B-B-B] [Am7/G#7 bass A-A-B-C] [B5/Cmaj7 bass B-B-B-C#] [Am7/B7 bass A-A-B-C] [B5/Gmaj7 bass B-B-B-B] [Am7/Fmaj7 bass A-D-A-C] [B/C bass B-B-C-C]

Pitch-class profile: {'C': 0.91, 'C#': 0.72, 'D': 0.53, 'D#': 0.64, 'E': 0.65, 'F': 0.52, 'F#': 0.76, 'G': 0.56, 'G#': 0.51, 'A': 0.62, 'A#': 0.44, 'B': 1.0}
Bass pitch-class profile: {'C': 1.0, 'C#': 0.79, 'D': 0.58, 'D#': 0.72, 'E': 0.66, 'F': 0.58, 'F#': 0.59, 'G': 0.42, 'G#': 0.57, 'A': 0.68, 'A#': 0.47, 'B': 0.97}
