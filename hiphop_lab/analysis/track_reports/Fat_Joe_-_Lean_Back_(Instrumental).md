# Terror Squad (Fat Joe) — Lean Back (2004)

**Archetype:** Storch-era club · Latin/East Coast  ·  **Source file:** `references/raw/` (Fat_Joe_-_Lean_Back_(Instrumental))
**Evidence status:** measured by script; NOT listened to by the model. Every [hypothesis] needs the King's ear.

## 1. Identity & emotional character
Swaggering, half-time-feel club groove. Intro 4 bars without drums [measured]. Bass/keys stab pattern with recurring 'low-thin' bars every 4 bars (b6, 14, 18, 22, 30…) [measured] → planned bass rests.

**Production history:** Produced by Scott Storch [documented].

## 2–3. Tempo, groove, timing
95.1 BPM; kick only on 1 and 3 (X.........X.....) [measured] — extremely sparse kick; snare/claps carry the rhythm.

## 4–6. Drums, bass, harmony & texture
G#/D# centre with A natural colour (Amaj7 vs G# bars) [estimate] → semitone shift (♭2 colour again, Storch habit).

## 7–9. Structure, sections, layer changes
4-bar intro; then a 4-bar cell where bar 2 drops the low end — the 'lean back' space [measured + hypothesis].
Full per-bar map: `analysis/structural_maps/Fat_Joe_-_Lean_Back_(Instrumental).csv` · plot: `analysis/plots/Fat_Joe_-_Lean_Back_(Instrumental).png`

## 11. Vocal compatibility
Sparse kick + bass rests = room for call-and-response chant hooks [hypothesis].

## 12. Transferable principles
- Two kicks per bar can be enough if the snare/clap and bass hits are syncopated.
- Planned bass rests every 4 bars create a dance 'move' moment.
- Storch ♭2 semitone colour reappears (Candy Shop, Lean Back).

## 13. Signature elements that must NOT be reproduced
- The Lean Back stab rhythm and melodic figure

## 14. Open questions / needed evidence
- Instrument identities

## Measured profile [measured — scripts/analyze_track.py → analysis/data/Fat_Joe_-_Lean_Back_(Instrumental).json]

| metric | value |
|---|---|
| duration | 253.59 s, 100 bars of 2.5228 s |
| tempo | **95.132 BPM** (grid residual p90 36.9 ms; comb candidates [[3.197, 95.15], [2.788, 63.4], [2.553, 126.9]]; drift first→last third None %) |
| first downbeat | 0.501 s (bar-phase margin 2.558; snare backbeat ratio 1.76) |
| key | G# major [estimate, margin 0.075]; alternatives [['G# minor', 0.467], ['C# minor', 0.424]] |
| loudness | -10.5 LUFS integrated, short-term p10/p90 [-11.5, -9.6], crest 13.54 dB, sample peak 1.1 dBFS |
| stereo | side−mid -12.8 dB overall, -16.7 dB below 150 Hz |
| spectrum | 73.6 % of energy ≤150 Hz; centroid 1982.0 Hz; HF content to ~10798 Hz |
| swing (hat 16ths) | 37.9 % (50 straight, 66.7 triplet); off-8th hat delay 0.2 ms |
| perc vs harmonic | 0.4 dB |
| harmonic loop similarity (bar lags) | {'1': -0.383, '2': 0.328, '3': -0.382, '4': 0.324, '8': 0.923} |

**16-step onset occupancy** (X strong, x present; whole track):
```
        1 e & a 2 e & a 3 e & a 4 e & a
kick    X . . . . . . . . . X . . . . .
snare   . . X . X . . x . x . . X . . .
hat     . . X . X . . X . X . . X . . X
```
Median micro-timing per step (ms, + = late): kick [-30.0, -8.6, -2.7, -24.7, -24.2, -7.2, -9.9, -30.7, 14.4, -24.4, -20.2, -18.6, -6.9, -15.8, -8.7, -18.2], snare [-28.2, -34.4, -39.2, -7.2, -35.2, None, -19.7, -37.0, 2.4, -35.9, -21.5, -18.8, -37.0, None, 15.2, -35.7], hat [-13.1, -12.6, -40.4, None, -35.2, None, 33.5, -38.1, 16.3, -40.0, -25.5, -23.3, -37.0, None, 26.0, -38.7]

**Layer timeline** (per bar vs. track median; NO-LOW = sub ≥6 dB down, NO-DRUMS = percussive ≥6 dB down):
b1:NO-DRUMS,hats+,melody+ | b2:NO-DRUMS,hats+ | b3-4:NO-DRUMS,hats+,melody+ | b5:full | b6:low-thin | b7-11:full | b12:hats+ | b13:full | b14:low-thin | b15-17:full | b18:low-thin | b19:full | b20:melody+ | b21:full | b22:low-thin | b23-27:full | b28:hats+,melody+ | b29:full | b30:low-thin | b31-33:full | b34:low-thin | b35:full | b36:hats+,melody+ | b37-43:full | b44:melody+ | b45:full | b46:low-thin | b47-49:full | b50:low-thin | b51:full | b52:hats+,melody+ | b53:full | b54:low-thin | b55-57:full | b58:low-thin | b59:full | b60:hats+,melody+ | b61:full | b62:low-thin | b63-65:full | b66:low-thin | b67:full | b68:melody+ | b69:full | b70:low-thin | b71-73:full | b74:low-thin | b75:full | b76:hats+,melody+ | b77:full | b78:low-thin | b79-81:full | b82:low-thin | b83:full | b84:hats+,melody+ | b85:full | b86:low-thin | b87-89:full | b90:low-thin | b91:full | b92:melody+ | b93:full | b94:low-thin | b95:low-thin,melody-off | b96-100:NO-LOW,NO-DRUMS,no-hats,melody-off

**Bars 2–9 harmonic sketch** [estimate: chroma template + bass chroma; not a transcription]: [D#maj7/D#maj7 bass D#-D#-D#-D#] [D#m7/A#dim bass D#-C#-E-C#] [G#5/G#5 bass D#-D#-D#-D#] [G#5/Emaj7 bass G#-G#-G#-F] [Amaj7/Amaj7 bass G#-C#-G#-G#] [C#5/Fmaj7 bass G#-G#-G#-A#] [Amaj7/G#maj7 bass A-C#-G#-G#] [G#5/G#7 bass G#-G#-G#-G#]

Pitch-class profile: {'C': 0.49, 'C#': 0.47, 'D': 0.35, 'D#': 0.65, 'E': 0.57, 'F': 0.48, 'F#': 0.53, 'G': 0.64, 'G#': 1.0, 'A': 0.69, 'A#': 0.5, 'B': 0.37}
Bass pitch-class profile: {'C': 0.47, 'C#': 0.46, 'D': 0.3, 'D#': 0.48, 'E': 0.47, 'F': 0.48, 'F#': 0.47, 'G': 0.58, 'G#': 1.0, 'A': 0.7, 'A#': 0.57, 'B': 0.32}
