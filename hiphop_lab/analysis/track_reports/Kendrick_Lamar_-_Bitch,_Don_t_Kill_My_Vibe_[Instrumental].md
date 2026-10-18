# Kendrick Lamar — Bitch, Don't Kill My Vibe (2012)

**Archetype:** Soulful / laid-back modern West Coast  ·  **Source file:** `references/raw/` (Kendrick_Lamar_-_Bitch,_Don_t_Kill_My_Vibe_[Instrumental])
**Evidence status:** measured by script; NOT listened to by the model. Every [hypothesis] needs the King's ear.

## 1. Identity & emotional character
Dreamy, hazy, floating. 134.0 BPM in double-time = 67 BPM half-time feel [measured + interpretation]. Intro bars 1–22 have no drums/low end [measured].

**Production history:** Produced by Sounwave; sample: Boom Clap Bachelors 'Tiden Flyver' [documented, moderate confidence — verify].

## 2–3. Tempo, groove, timing
Kick on quarter notes in the double-time grid (X...X.x.X.x.X.x.) [measured] — reads as a half-time 67 BPM with 8th-note pulse.

## 4–6. Drums, bass, harmony & texture
C# major-7 centre with F#maj7 (IV) colour [estimate] → major-7 dream harmony (no minor darkness).

## 7–9. Structure, sections, layer changes
Long intro (22 bars in 134-grid = 11 bars half-time); repeated big drop-outs b57–70 (14 bars, no drums/low) [measured] — breakdowns around the hook.
Full per-bar map: `analysis/structural_maps/Kendrick_Lamar_-_Bitch,_Don_t_Kill_My_Vibe_[Instrumental].csv` · plot: `analysis/plots/Kendrick_Lamar_-_Bitch,_Don_t_Kill_My_Vibe_[Instrumental].png`

## 11. Vocal compatibility
84 % ≤150 Hz but hazy top; lots of space [measured + hypothesis].

## 12. Transferable principles
- Half-time at ~67 BPM gives 'vibe' — space for melodic flows.
- Maj7 (I–IV) harmony = calm confidence instead of menace.
- Long drumless passages as emotional reset.

## 13. Signature elements that must NOT be reproduced
- The Tiden Flyver sample/vocal chop

## 14. Open questions / needed evidence
- Sample treatment details

## Measured profile [measured — scripts/analyze_track.py → analysis/data/Kendrick_Lamar_-_Bitch,_Don_t_Kill_My_Vibe_[Instrumental].json]

| metric | value |
|---|---|
| duration | 308.01 s, 171 bars of 1.791 s |
| tempo | **134.003 BPM** (grid residual p90 11.3 ms; comb candidates [[3.405, 134.1], [3.283, 67.0], [3.034, 89.3]]; drift first→last third 0.021 %) |
| first downbeat | 1.442 s (bar-phase margin 0.02; snare backbeat ratio 3.04) |
| key | C# major [estimate, margin 0.118]; alternatives [['F# minor', 0.347], ['C# minor', 0.34]] |
| loudness | -13.02 LUFS integrated, short-term p10/p90 [-26.2, -10.8], crest 16.12 dB, sample peak 2.84 dBFS |
| stereo | side−mid -16.7 dB overall, -26.5 dB below 150 Hz |
| spectrum | 84.1 % of energy ≤150 Hz; centroid 2537.0 Hz; HF content to ~10782 Hz |
| swing (hat 16ths) | 47.1 % (50 straight, 66.7 triplet); off-8th hat delay 24.8 ms |
| perc vs harmonic | -2.1 dB |
| harmonic loop similarity (bar lags) | {'1': 0.224, '2': -0.109, '3': 0.092, '4': 0.65, '8': 0.471} |

**16-step onset occupancy** (X strong, x present; whole track):
```
        1 e & a 2 e & a 3 e & a 4 e & a
kick    X . . . X . x . X . x . X . x .
snare   . . . . x . x . . . . . X . . .
hat     X . x . X . X . x . x . X . x .
```
Median micro-timing per step (ms, + = late): kick [5.3, -14.4, 21.4, 19.5, 17.0, -31.6, 19.7, 14.7, 17.6, -26.5, 19.7, 3.3, 27.3, -24.2, 16.5, -0.7], snare [26.7, -10.0, 28.0, 25.7, 24.7, 45.5, 27.1, -0.4, 27.4, -37.1, 28.2, -7.6, 26.8, -27.3, 31.2, -12.5], hat [25.2, 3.4, 24.1, 27.6, 25.1, -14.1, 23.3, -9.2, 24.0, -25.0, 25.4, -3.9, 27.1, 15.4, 25.7, -9.8]

**Layer timeline** (per bar vs. track median; NO-LOW = sub ≥6 dB down, NO-DRUMS = percussive ≥6 dB down):
b1-22:NO-LOW,NO-DRUMS,no-hats | b23:NO-LOW | b24-25:hats+ | b26-28:full | b29:melody+ | b30:full | b31-32:hats+ | b33:full | b34:low-thin,no-hats | b35-37:no-hats | b38:low-thin,no-hats | b39:no-hats | b40:hats+ | b41:full | b42:melody-off | b43-45:full | b46:melody-off | b47:full | b48:hats+ | b49:full | b50-52:hats+ | b53:full | b54-56:hats+ | b57:NO-LOW,NO-DRUMS | b58-63:NO-LOW,NO-DRUMS,no-hats | b64:NO-LOW,NO-DRUMS | b65-70:NO-LOW,NO-DRUMS,no-hats | b71:NO-LOW | b72-73:hats+ | b74-76:full | b77:melody+ | b78:full | b79-80:hats+ | b81:full | b82:low-thin,no-hats | b83-85:no-hats | b86:low-thin,no-hats | b87:no-hats | b88:hats+ | b89:full | b90:melody-off | b91-93:full | b94:melody-off | b95:full | b96:hats+,melody+ | b97:melody+ | b98-100:hats+ | b101:full | b102-104:hats+ | b105:NO-LOW,NO-DRUMS | b106-111:NO-LOW,NO-DRUMS,no-hats | b112:NO-LOW,NO-DRUMS | b113-118:NO-LOW,NO-DRUMS,no-hats | b119:NO-LOW,hats+ | b120-121:hats+ | b122-124:full | b125:melody+ | b126:full | b127-128:hats+ | b129:NO-LOW,NO-DRUMS | b130:melody-off | b131-134:full | b135-136:hats+ | b137-142:NO-DRUMS | b143-144:hats+ | b145-147:full | b148-149:melody+ | b150-151:full | b152:low-thin,NO-DRUMS | b153:NO-LOW,NO-DRUMS,no-hats,melody+ | b154:NO-LOW,NO-DRUMS,no-hats | b155-157:NO-LOW,NO-DRUMS,no-hats,melody+ | b158-159:NO-LOW,NO-DRUMS,no-hats | b160:NO-DRUMS,no-hats | b161:NO-DRUMS,no-hats,melody+ | b162-163:NO-DRUMS,no-hats | b164-167:NO-DRUMS,no-hats,melody+ | b168:NO-LOW,NO-DRUMS,no-hats | b169-171:NO-LOW,NO-DRUMS,no-hats,melody-off

**Bars 2–9 harmonic sketch** [estimate: chroma template + bass chroma; not a transcription]: [C#5/C#5 bass C#-C#-C#-C#] [C#maj7/C#maj7 bass C#-C#-C#-A#] [F#maj7/C#maj7 bass F-F-G#-C] [C#maj7/C#maj7 bass C#-C#-C#-C#] [C#5/C#maj7 bass C#-C#-C#-C#] [C#maj7/C#maj7 bass C#-C#-C#-A#] [F#maj7/C#maj7 bass F-F-G#-C] [C#maj7/C#maj7 bass C#-C#-C#-C#]

Pitch-class profile: {'C': 0.5, 'C#': 1.0, 'D': 0.81, 'D#': 0.37, 'E': 0.26, 'F': 0.43, 'F#': 0.35, 'G': 0.37, 'G#': 0.56, 'A': 0.4, 'A#': 0.31, 'B': 0.25}
Bass pitch-class profile: {'C': 0.36, 'C#': 1.0, 'D': 1.0, 'D#': 0.37, 'E': 0.25, 'F': 0.36, 'F#': 0.39, 'G': 0.38, 'G#': 0.51, 'A': 0.42, 'A#': 0.4, 'B': 0.32}
