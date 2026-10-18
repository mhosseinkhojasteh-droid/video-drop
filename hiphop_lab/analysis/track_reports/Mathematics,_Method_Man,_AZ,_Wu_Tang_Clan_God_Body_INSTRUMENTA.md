# Mathematics feat. Method Man & AZ — God Body (Wu-Tang family)

**Archetype:** Wu-Tang / gritty NY  ·  **Source file:** `references/raw/` (Mathematics,_Method_Man,_AZ,_Wu_Tang_Clan_God_Body_INSTRUMENTA)
**Evidence status:** measured by script; NOT listened to by the model. Every [hypothesis] needs the King's ear.

## 1. Identity & emotional character
Gritty, dense, loud (−8.6 LUFS, crest 10.8) [measured]. Runs bars 2–63 without any layer change [measured].

**Production history:** Producer Mathematics [documented as artist; production credit not verified here].

## 2–3. Tempo, groove, timing
81.0 BPM — slowest of the set [measured]. Swing 59.5 % [measured]. Kick syncopated off the 1 (..x.X..X..X.x.xx) [measured; downbeat phase margin should be checked].

## 4–6. Drums, bass, harmony & texture
D minor area with Eb (♭2) colour (D#maj7/Em7 alternation) [estimate] → semitone-shifted sample = Wu dissonance.

## 7–9. Structure, sections, layer changes
Continuous loop [measured].
Full per-bar map: `analysis/structural_maps/Mathematics,_Method_Man,_AZ,_Wu_Tang_Clan_God_Body_INSTRUMENTA.csv` · plot: `analysis/plots/Mathematics,_Method_Man,_AZ,_Wu_Tang_Clan_God_Body_INSTRUMENTA.png`

## 11. Vocal compatibility
Dense bed; the vocal must be bright and forward [hypothesis].

## 12. Transferable principles
- 81 BPM + ♭2 dissonance + grit = Wu weight.
- One loop for 60+ bars with three MCs carrying the variation.

## 13. Signature elements that must NOT be reproduced
- The sample

## 14. Open questions / needed evidence
- Sample source
- Exact bar phase (syncopated kick)

## Measured profile [measured — scripts/analyze_track.py → analysis/data/Mathematics,_Method_Man,_AZ,_Wu_Tang_Clan_God_Body_INSTRUMENTA.json]

| metric | value |
|---|---|
| duration | 192.86 s, 64 bars of 2.963 s |
| tempo | **80.999 BPM** (grid residual p90 5.6 ms; comb candidates [[4.182, 81.0], [4.091, 162.1], [3.29, 64.8]]; drift first→last third 0.001 %) |
| first downbeat | 2.957 s (bar-phase margin 0.025; snare backbeat ratio 2.28) |
| key | D minor [estimate, margin 0.048]; alternatives [['B minor', 0.295], ['D major', 0.26]] |
| loudness | -8.62 LUFS integrated, short-term p10/p90 [-8.8, -8.3], crest 10.78 dB, sample peak 1.8 dBFS |
| stereo | side−mid -12.8 dB overall, -19.3 dB below 150 Hz |
| spectrum | 78.5 % of energy ≤150 Hz; centroid 1812.0 Hz; HF content to ~10788 Hz |
| swing (hat 16ths) | 59.5 % (50 straight, 66.7 triplet); off-8th hat delay 21.1 ms |
| perc vs harmonic | -2.6 dB |
| harmonic loop similarity (bar lags) | {'1': -0.57, '2': 0.558, '3': -0.554, '4': 0.453, '8': 0.869} |

**16-step onset occupancy** (X strong, x present; whole track):
```
        1 e & a 2 e & a 3 e & a 4 e & a
kick    . . x . X . . X . . X . x . x x
snare   x . . . X . x . . . . . X . x .
hat     X . x . X . X . x . x . X . X .
```
Median micro-timing per step (ms, + = late): kick [-9.8, -0.7, 8.4, -28.1, 38.9, -72.5, 40.3, 25.7, -6.7, 7.8, 21.5, 49.4, 42.5, 13.4, 27.9, 62.3], snare [24.4, -55.9, 19.2, None, 20.1, None, 20.3, 32.1, 35.0, None, 17.7, None, 20.6, None, 21.3, 54.3], hat [19.0, None, 22.5, None, 19.8, None, 19.6, 35.1, 22.3, None, 23.2, None, 18.7, None, 19.3, None]

**Layer timeline** (per bar vs. track median; NO-LOW = sub ≥6 dB down, NO-DRUMS = percussive ≥6 dB down):
b1:NO-LOW,melody+ | b2-63:full | b64:NO-LOW,NO-DRUMS,no-hats,melody-off

**Bars 2–9 harmonic sketch** [estimate: chroma template + bass chroma; not a transcription]: [D#maj7/Em7 bass D-D#-D-D] [D#maj7/Em7 bass A#-D-E-D] [Dmaj7/Gmaj7 bass D-D-D-F#] [D#maj7/Dmaj7 bass A#-D-E-F#] [Em7/Gmaj7 bass D-D-D-F#] [D#maj7/G7 bass A#-D-F-G] [Dmaj7/Em7 bass D-D-D-F#] [D#maj7/G7 bass A#-D-E-F#]

Pitch-class profile: {'C': 0.7, 'C#': 0.81, 'D': 1.0, 'D#': 0.76, 'E': 0.74, 'F': 0.72, 'F#': 0.67, 'G': 0.64, 'G#': 0.49, 'A': 0.5, 'A#': 0.6, 'B': 0.62}
Bass pitch-class profile: {'C': 0.71, 'C#': 0.81, 'D': 1.0, 'D#': 0.78, 'E': 0.79, 'F': 0.76, 'F#': 0.66, 'G': 0.65, 'G#': 0.49, 'A': 0.51, 'A#': 0.56, 'B': 0.64}
