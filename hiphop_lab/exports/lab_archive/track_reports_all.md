=== FILE: analysis/track_reports/2pac_-_Ambitionz_Az_a_Ridah_Instrumental_HD_Quality.md ===
# 2Pac — Ambitionz Az a Ridah (1996)

**Archetype:** West Coast · dark G-funk-adjacent, ominous  ·  **Source file:** `references/raw/` (2pac_-_Ambitionz_Az_a_Ridah_Instrumental_HD_Quality)
**Evidence status:** measured by script; NOT listened to by the model. Every [hypothesis] needs the King's ear.

## 1. Identity & emotional character
Ominous, menacing West Coast. Chromatic pitch cluster (F#–G–G# all near max in the pitch-class profile and the bass profile) [measured] → a semitone-rubbing motif that creates dread [hypothesis].

**Production history:** Produced by Daz Dillinger [documented]. All Eyez on Me.

## 2–3. Tempo, groove, timing
87.3 BPM (tracker aliased to 118.6 = 4/3; corrected by comb) [measured]. Moderate swing 56.9 % with hats ~18–24 ms late on off-beats [measured] — laid-back West Coast pocket.

## 4–6. Drums, bass, harmony & texture
Static tonal centre around G with chromatic neighbour tones (G–G#–F#) rather than chord changes [estimate]. Tension from half-steps, not from progressions.

## 7–9. Structure, sections, layer changes
Intro 2 bars without drums/low end; then the loop runs with single-bar full drop-outs (drums+hats removed) at bars 19, 55, 91 — a 36-bar period [measured] that marks section starts.
Full per-bar map: `analysis/structural_maps/2pac_-_Ambitionz_Az_a_Ridah_Instrumental_HD_Quality.csv` · plot: `analysis/plots/2pac_-_Ambitionz_Az_a_Ridah_Instrumental_HD_Quality.png`

## 11. Vocal compatibility
Very low mid energy (250 Hz–2 kHz ≈ 4 %) [measured] → huge vocal space; the beat lives in sub-bass and top.

## 12. Transferable principles
- Dread from semitone motion over a pedal tone.
- Single-bar total drop-out as the section marker (the MC enters alone).
- 87 BPM + light swing = menace without rush.

## 13. Signature elements that must NOT be reproduced
- The specific chromatic synth line and its rhythm

## 14. Open questions / needed evidence
- Synth source
- Exact bar/section functions (no vocal reference)

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

=== FILE: analysis/track_reports/50_Cent_-_Candy_Shop_instrumental.md ===
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

=== FILE: analysis/track_reports/50_Cent_-_In_Da_Club.md ===
# 50 Cent — In Da Club (2003)

**Archetype:** G-Unit/Dre club anthem  ·  **Source file:** `references/raw/` (50_Cent_-_In_Da_Club)
**Evidence status:** measured by script; NOT listened to by the model. Every [hypothesis] needs the King's ear.

## 1. Identity & emotional character
Sparse, bouncy, confident. Dynamic for a club record (−14.7 LUFS, crest 15.6 dB) [measured] — this rip is quieter than the others; don't copy its loudness.

**Production history:** Produced by Dr. Dre with Mike Elizondo [documented]. Filename has no 'instrumental' → vocal presence NOT verified [unknown].

## 2–3. Tempo, groove, timing
89.9 BPM, hat swing ≈ 66 % (near triplet) [measured] → the famous bounce. Kick pattern dense around beat 1 and 2-and/3 [measured].

## 4–6. Drums, bass, harmony & texture
C#-minor-ish centre, chroma moves D#–E–D around C# (bass E-D-C# walk) [estimate]; strings/keys stab figure.

## 7–9. Structure, sections, layer changes
Melody layer absent bars 1–5 and 15–21, 43–45, 51–53 [measured] → the hook instrumentation is switched off under verses — classic Dre subtraction arrangement.
Full per-bar map: `analysis/structural_maps/50_Cent_-_In_Da_Club.csv` · plot: `analysis/plots/50_Cent_-_In_Da_Club.png`

## 11. Vocal compatibility
Vocal space created by removing the melodic stab in verses [hypothesis from timeline].

## 12. Transferable principles
- Near-triplet hat swing (≈66 %) over straight kicks = bounce.
- Dre subtraction: same drums all song, melodic layer on/off defines verse vs hook.
- Few elements, each with its own frequency lane.

## 13. Signature elements that must NOT be reproduced
- The In Da Club string/synth stab figure and kick pattern combination

## 14. Open questions / needed evidence
- Whether vocals are present in this file
- Section labels

## Measured profile [measured — scripts/analyze_track.py → analysis/data/50_Cent_-_In_Da_Club.json]

| metric | value |
|---|---|
| duration | 220.39 s, 81 bars of 2.6696 s |
| tempo | **89.902 BPM** (grid residual p90 5.4 ms; comb candidates [[4.109, 89.85], [3.669, 179.75], [2.924, 119.8]]; drift first→last third -0.008 %) |
| first downbeat | 1.994 s (bar-phase margin 0.816; snare backbeat ratio 0.56) |
| key | C# minor [estimate, margin 0.12]; alternatives [['A major', 0.243], ['D major', 0.189]] |
| loudness | -14.71 LUFS integrated, short-term p10/p90 [-15.3, -14.2], crest 15.64 dB, sample peak 0.37 dBFS |
| stereo | side−mid -13.7 dB overall, -14.4 dB below 150 Hz |
| spectrum | 73.9 % of energy ≤150 Hz; centroid 2058.0 Hz; HF content to ~10766 Hz |
| swing (hat 16ths) | 66.3 % (50 straight, 66.7 triplet); off-8th hat delay -10.6 ms |
| perc vs harmonic | 3.4 dB |
| harmonic loop similarity (bar lags) | {'1': -0.754, '2': 0.753, '3': -0.765, '4': 0.869, '8': 0.853} |

**16-step onset occupancy** (X strong, x present; whole track):
```
        1 e & a 2 e & a 3 e & a 4 e & a
kick    X . x . . X . . X . . . . X . .
snare   X . X . x X . . X . X . x X x .
hat     x . X . X . X . x . X . X . X .
```
Median micro-timing per step (ms, + = late): kick [14.6, 71.0, 9.4, None, 45.1, 17.7, -15.9, 56.3, 17.6, 61.3, 11.1, 73.5, 62.3, 23.0, -17.5, 80.5], snare [10.2, 50.7, -48.1, 53.0, 37.0, 24.2, 16.6, 52.3, 11.8, 57.5, -35.6, 54.1, 34.7, 23.8, 15.8, 49.0], hat [16.7, 54.4, -44.3, 54.5, 29.0, 34.2, 15.0, 53.2, 16.8, 54.1, -34.0, 54.8, 28.2, 34.7, 12.8, 54.6]

**Layer timeline** (per bar vs. track median; NO-LOW = sub ≥6 dB down, NO-DRUMS = percussive ≥6 dB down):
b1-5:melody-off | b6-14:full | b15-21:melody-off | b22-31:full | b32:melody+ | b33-35:full | b36:melody+ | b37:full | b38-41:melody+ | b42:full | b43-45:melody-off | b46-50:full | b51-53:melody-off | b54-55:full | b56:melody+ | b57-59:full | b60:melody+ | b61-67:full | b68:melody+ | b69-79:full | b80:low-thin,melody-off | b81:NO-LOW,NO-DRUMS,no-hats,melody-off

**Bars 2–9 harmonic sketch** [estimate: chroma template + bass chroma; not a transcription]: [D#maj7/C#5 bass E-D-C#-C#] [D#maj7/D#m7 bass D-D#-D#-F#] [Em7/Dmaj7 bass D-D-C#-C#] [D#maj7/D#m7 bass D-E-D#-F#] [D#maj7/Dmaj7 bass E-D-C#-C#] [D#maj7/D#m7 bass D-D-D#-F#] [E7/C#5 bass E-E-C#-C#] [D#maj7/D#m7 bass D-E-D#-F#]

Pitch-class profile: {'C': 0.3, 'C#': 0.9, 'D': 1.0, 'D#': 0.86, 'E': 0.69, 'F': 0.36, 'F#': 0.36, 'G': 0.23, 'G#': 0.31, 'A': 0.17, 'A#': 0.1, 'B': 0.13}
Bass pitch-class profile: {'C': 0.36, 'C#': 0.94, 'D': 1.0, 'D#': 0.87, 'E': 0.66, 'F': 0.33, 'F#': 0.36, 'G': 0.19, 'G#': 0.19, 'A': 0.1, 'A#': 0.09, 'B': 0.09}

=== FILE: analysis/track_reports/DJ_Premier_-_Classic_(instrumental).md ===
# DJ Premier — Classic (2007, Nike Air Force 1 anniversary)

**Archetype:** NY boom-bap (Premier)  ·  **Source file:** `references/raw/` (DJ_Premier_-_Classic_(instrumental))
**Evidence status:** measured by script; NOT listened to by the model. Every [hypothesis] needs the King's ear.

## 1. Identity & emotional character
Triumphant, ceremonial boom-bap. Loudest reference (−8.5 LUFS, crest 10.7) [measured] — a modern Premier master.

**Production history:** Produced by DJ Premier for Rakim, Nas, KRS-One and Kanye West [documented].

## 2–3. Tempo, groove, timing
99.99 BPM — drum-machine exact [measured]. Hats and melody alternate in a strict 2-bar call/response (bars even: hats+ melody+) [measured] → the classic Premier 2-bar chop.

## 4–6. Drums, bass, harmony & texture
Minor-7 colour around B/F# (Bm7 ↔ F#maj7 alternation) [estimate] — chopped sample phrase.

## 7–9. Structure, sections, layer changes
Strict 2-bar alternation all the way (b3 full, b4 hats+melody+, …) [measured] — the arrangement is the chop itself.
Full per-bar map: `analysis/structural_maps/DJ_Premier_-_Classic_(instrumental).csv` · plot: `analysis/plots/DJ_Premier_-_Classic_(instrumental).png`

## 11. Vocal compatibility
Mid band relatively busy (centroid higher) but the 2-bar call/response leaves 'answer' gaps for the rapper [hypothesis].

## 12. Transferable principles
- The 2-bar chop: bar A states, bar B answers — the loop is a conversation.
- Machine-tight tempo, swing lives in the chop placement.
- Modern Premier masters are loud (−8.5 LUFS) yet keep ~10.7 dB crest.

## 13. Signature elements that must NOT be reproduced
- The specific sample phrase / chop points

## 14. Open questions / needed evidence
- Original sample source

## Measured profile [measured — scripts/analyze_track.py → analysis/data/DJ_Premier_-_Classic_(instrumental).json]

| metric | value |
|---|---|
| duration | 286.56 s, 118 bars of 2.4002 s |
| tempo | **99.993 BPM** (grid residual p90 12.0 ms; comb candidates [[2.883, 100.0], [2.266, 66.7], [1.7, 133.35]]; drift first→last third 0.022 %) |
| first downbeat | 1.705 s (bar-phase margin 1.541; snare backbeat ratio 2.96) |
| key | F# major [estimate, margin 0.022]; alternatives [['F# minor', 0.476], ['B minor', 0.338]] |
| loudness | -8.53 LUFS integrated, short-term p10/p90 [-9.3, -8.0], crest 10.74 dB, sample peak 0.53 dBFS |
| stereo | side−mid -54.5 dB overall, -120.0 dB below 150 Hz |
| spectrum | 68.9 % of energy ≤150 Hz; centroid 2165.0 Hz; HF content to ~10481 Hz |
| swing (hat 16ths) | 39.9 % (50 straight, 66.7 triplet); off-8th hat delay 28.5 ms |
| perc vs harmonic | -0.8 dB |
| harmonic loop similarity (bar lags) | {'1': -0.841, '2': 0.839, '3': -0.844, '4': 0.837, '8': 0.851} |

**16-step onset occupancy** (X strong, x present; whole track):
```
        1 e & a 2 e & a 3 e & a 4 e & a
kick    x x . . x . x . . . X . x . . x
snare   . x . . X . . . . . . . x . . .
hat     x x X . X . . . x . x . x . x .
```
Median micro-timing per step (ms, + = late): kick [29.2, 47.9, 45.9, -52.0, 23.5, 64.7, 14.0, 5.7, -61.4, -55.7, 16.3, -13.2, 27.6, 30.5, 66.4, -24.9], snare [29.4, 45.3, 40.8, None, 14.9, None, 22.0, 41.9, 39.4, 41.5, 21.4, -28.9, 19.0, None, 35.6, -54.3], hat [-5.7, 35.2, 35.2, None, 15.9, None, 25.1, 30.9, 29.0, -58.0, 20.9, -30.3, 20.1, None, 31.8, -68.8]

**Layer timeline** (per bar vs. track median; NO-LOW = sub ≥6 dB down, NO-DRUMS = percussive ≥6 dB down):
b1:NO-LOW,NO-DRUMS,melody-off | b2:NO-LOW,NO-DRUMS,no-hats,melody-off | b3:full | b4:hats+,melody+ | b5:full | b6:hats+,melody+ | b7:full | b8:hats+,melody+ | b9:full | b10:hats+,melody+ | b11:full | b12:hats+,melody+ | b13:full | b14:hats+,melody+ | b15:full | b16:hats+,melody+ | b17:full | b18:hats+ | b19:full | b20:hats+,melody+ | b21:full | b22:hats+,melody+ | b23:full | b24:hats+,melody+ | b25-27:full | b28:hats+,melody+ | b29:full | b30:hats+,melody+ | b31:full | b32:hats+,melody+ | b33:full | b34:hats+,melody+ | b35:full | b36:hats+,melody+ | b37:full | b38:hats+,melody+ | b39:full | b40:hats+,melody+ | b41:full | b42:hats+,melody+ | b43:full | b44:hats+,melody+ | b45:full | b46:hats+,melody+ | b47:full | b48:hats+,melody+ | b49:full | b50:hats+,melody+ | b51:full | b52:hats+,melody+ | b53-55:full | b56:hats+,melody+ | b57:full | b58:hats+,melody+ | b59:full | b60:hats+,melody+ | b61:full | b62:NO-LOW,NO-DRUMS,melody-off | b63:full | b64:hats+,melody+ | b65:full | b66:hats+,melody+ | b67:full | b68:hats+,melody+ | b69:full | b70:hats+,melody+ | b71:full | b72:hats+,melody+ | b73:full | b74:hats+,melody+ | b75:full | b76:hats+,melody+ | b77:full | b78:hats+,melody+ | b79:full | b80:hats+,melody+ | b81:full | b82:hats+,melody+ | b83:full | b84:hats+,melody+ | b85:full | b86:low-thin,hats+,melody+ | b87:full | b88:hats+,melody+ | b89:full | b90:hats+,melody+ | b91:full | b92:hats+,melody+ | b93:full | b94:hats+,melody+ | b95:full | b96:hats+,melody+ | b97:full | b98:hats+,melody+ | b99:full | b100:hats+,melody+ | b101:full | b102:NO-LOW,NO-DRUMS,hats+,melody+ | b103:full | b104:hats+,melody+ | b105:full | b106:hats+,melody+ | b107:full | b108:hats+,melody+ | b109:full | b110:hats+,melody+ | b111:full | b112:hats+,melody+ | b113:full | b114:hats+,melody+ | b115:full | b116:NO-LOW,NO-DRUMS | b117-118:NO-LOW,NO-DRUMS,no-hats,melody-off

**Bars 2–9 harmonic sketch** [estimate: chroma template + bass chroma; not a transcription]: [Dm7/F#maj7 bass D-D-E-G] [F#maj7/F#m7 bass A#-F-E-F#] [Bm7/Bm7 bass B-G-G-A#] [Bmaj7/F#maj7 bass A#-F-F-F#] [Bm7/Bm7 bass B-G#-G-A#] [Bmaj7/F#maj7 bass A#-F-F-F#] [Bm7/Bm7 bass B-G-G-A#] [Bmaj7/Emaj7 bass A#-F-D#-F]

Pitch-class profile: {'C': 0.46, 'C#': 0.54, 'D': 0.47, 'D#': 0.4, 'E': 0.53, 'F': 0.7, 'F#': 1.0, 'G': 0.68, 'G#': 0.74, 'A': 0.78, 'A#': 0.8, 'B': 0.82}
Bass pitch-class profile: {'C': 0.42, 'C#': 0.39, 'D': 0.42, 'D#': 0.42, 'E': 0.57, 'F': 0.8, 'F#': 1.0, 'G': 0.95, 'G#': 0.92, 'A': 0.87, 'A#': 0.91, 'B': 0.82}

=== FILE: analysis/track_reports/DJ_Premier_-_Seen_it_All_(instrumental).md ===
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

=== FILE: analysis/track_reports/Dr._Dre_-_Nuthin_But_A_G_Thang_(INSTRUMENTAL).md ===
# Dr. Dre — Nuthin' but a 'G' Thang (1992)

**Archetype:** West Coast G-funk (canonical)  ·  **Source file:** `references/raw/` (Dr._Dre_-_Nuthin_But_A_G_Thang_(INSTRUMENTAL))
**Evidence status:** measured by script; NOT listened to by the model. Every [hypothesis] needs the King's ear.

## 1. Identity & emotional character
Relaxed, sunny, funky. Very dynamic (crest 19.3 dB, −19.8 LUFS) [measured] — 1992 mastering, quieter era.

**Production history:** Produced by Dr. Dre; built on Leon Haywood 'I Want'a Do Something Freaky to You' (interpolated/sampled) [documented]. The Chronic.

## 2–3. Tempo, groove, timing
94.7 BPM, swing ≈ 60.6 % [measured] → loose funk pocket. Snare on 2 & 4 clean; hats on 8ths [measured].

## 4–6. Drums, bass, harmony & texture
Major-7/minor-7 movement around B/F#/C (Bm7–Fmaj7 style alternation) [estimate] — soulful extended chords typical of G-funk.

## 7–9. Structure, sections, layer changes
Bars 51–54 and 63–70 alternate NO-LOW / low-thin [measured] → bass removed on alternating bars = a breakdown device. 'melody+' blocks at 27–30, 43–50, 59–62, 79–94 [measured] (G-funk lead / keys entries) [hypothesis].
Full per-bar map: `analysis/structural_maps/Dr._Dre_-_Nuthin_But_A_G_Thang_(INSTRUMENTAL).csv` · plot: `analysis/plots/Dr._Dre_-_Nuthin_But_A_G_Thang_(INSTRUMENTAL).png`

## 11. Vocal compatibility
Mid-heavy for G-funk (64 % low) — keys and lead share the vocal range, so the lead plays only between/after lines [hypothesis].

## 12. Transferable principles
- G-funk = extended chords (m7/maj7/9) + funk bass + whiny portamento lead used sparingly.
- Breakdown by removing the bass on alternate bars.
- Swing ~60 %: loose but not triplet.

## 13. Signature elements that must NOT be reproduced
- The Leon Haywood-derived progression + bass line
- The lead melody

## 14. Open questions / needed evidence
- Exact chord qualities (needs transcription)

## Measured profile [measured — scripts/analyze_track.py → analysis/data/Dr._Dre_-_Nuthin_But_A_G_Thang_(INSTRUMENTAL).json]

| metric | value |
|---|---|
| duration | 240.9 s, 94 bars of 2.5349 s |
| tempo | **94.678 BPM** (grid residual p90 16.5 ms; comb candidates [[3.091, 94.7], [2.585, 63.1], [1.93, 126.5]]; drift first→last third 0.0 %) |
| first downbeat | 0.135 s (bar-phase margin 0.174; snare backbeat ratio 3.46) |
| key | B minor [estimate, margin 0.153]; alternatives [['B major', 0.498], ['E minor', 0.438]] |
| loudness | -19.77 LUFS integrated, short-term p10/p90 [-20.8, -19.0], crest 19.31 dB, sample peak -1.75 dBFS |
| stereo | side−mid -6.0 dB overall, -10.2 dB below 150 Hz |
| spectrum | 64.1 % of energy ≤150 Hz; centroid 2772.0 Hz; HF content to ~10788 Hz |
| swing (hat 16ths) | 60.6 % (50 straight, 66.7 triplet); off-8th hat delay 26.1 ms |
| perc vs harmonic | -0.7 dB |
| harmonic loop similarity (bar lags) | {'1': -0.228, '2': 0.711, '3': -0.276, '4': 0.582, '8': 0.396} |

**16-step onset occupancy** (X strong, x present; whole track):
```
        1 e & a 2 e & a 3 e & a 4 e & a
kick    x . . . . . X . x . x . . . X .
snare   x . . . X . . . x . . . X . . .
hat     X . . . X . x . X . x . X . x .
```
Median micro-timing per step (ms, + = late): kick [4.2, 56.3, 26.8, 31.4, 23.8, None, 17.4, -51.2, 22.8, None, 19.0, 41.5, 23.5, None, 23.8, -33.9], snare [20.2, None, 29.4, 33.9, 15.3, None, 29.0, 44.6, 25.3, None, 13.9, -33.2, 28.0, None, 34.4, 9.1], hat [20.6, None, 25.3, 47.0, 17.9, 33.6, 25.7, 30.3, 18.5, None, 28.4, None, 29.6, 45.2, 26.6, 31.5]

**Layer timeline** (per bar vs. track median; NO-LOW = sub ≥6 dB down, NO-DRUMS = percussive ≥6 dB down):
b1:NO-LOW | b2:low-thin | b3:NO-LOW,melody+ | b4:low-thin,melody+ | b5-26:full | b27-30:melody+ | b31-42:full | b43-50:melody+ | b51:NO-LOW | b52:low-thin | b53:NO-LOW | b54:low-thin | b55-58:full | b59-62:melody+ | b63:NO-LOW | b64:low-thin | b65:NO-LOW | b66:low-thin | b67:NO-LOW | b68:low-thin | b69:NO-LOW | b70:low-thin | b71-78:full | b79-94:melody+

**Bars 2–9 harmonic sketch** [estimate: chroma template + bass chroma; not a transcription]: [Cmaj7/Gmaj7 bass F#-G-G-A#] [Bm7/Cmaj7 bass B-A#-B-B] [F#m7/Gmaj7 bass B-G-G-B] [Bm7/Fmaj7 bass B-B-E-F#] [Fmaj7/Bmaj7 bass E-G-B-B] [Bm7/Fmaj7 bass B-B-E-F#] [Fmaj7/Bmaj7 bass E-G-B-B] [Bm7/F#7 bass B-B-E-F#]

Pitch-class profile: {'C': 0.64, 'C#': 0.48, 'D': 0.5, 'D#': 0.35, 'E': 0.61, 'F': 0.56, 'F#': 0.79, 'G': 0.46, 'G#': 0.38, 'A': 0.54, 'A#': 0.6, 'B': 1.0}
Bass pitch-class profile: {'C': 0.66, 'C#': 0.47, 'D': 0.39, 'D#': 0.37, 'E': 0.52, 'F': 0.6, 'F#': 0.74, 'G': 0.53, 'G#': 0.44, 'A': 0.53, 'A#': 0.68, 'B': 1.0}

=== FILE: analysis/track_reports/Dr._Dre_-_The_Next_Episode_(Instrumental).md ===
# Dr. Dre — The Next Episode (1999)

**Archetype:** West Coast 2001-era (cinematic G-funk)  ·  **Source file:** `references/raw/` (Dr._Dre_-_The_Next_Episode_(Instrumental))
**Evidence status:** measured by script; NOT listened to by the model. Every [hypothesis] needs the King's ear.

## 1. Identity & emotional character
Cinematic, cocky, iconic guitar/bass figure. Intro bars 1–4 without drums (melody only) [measured].

**Production history:** Produced by Dr. Dre with Mel-Man; based on David McCallum's 'The Edge' [documented].

## 2–3. Tempo, groove, timing
95.4 BPM; kick on 1 with a dense 8th-ish kick pattern later in the bar [measured]; swing value not computed (insufficient off-beat hat onsets) [measured].

## 4–6. Drums, bass, harmony & texture
D#/B power-chord bars then D#m7 ↔ F#maj7 alternation [estimate] — minor i ↔ relative major motion.

## 7–9. Structure, sections, layer changes
Intro 4 bars (no drums) → drums at bar 5; bars 29–32 drop drums again (break) [measured]; then every 4th bar 'melody-off' (b38, 42, 46…) [measured] → the riff rests on bar 4 of every 4-bar phrase, leaving a hole for the rapper's punchline.
Full per-bar map: `analysis/structural_maps/Dr._Dre_-_The_Next_Episode_(Instrumental).csv` · plot: `analysis/plots/Dr._Dre_-_The_Next_Episode_(Instrumental).png`

## 11. Vocal compatibility
The 4-bar riff with a built-in rest bar = a punchline slot [hypothesis].

## 12. Transferable principles
- Build the riff with a rest in bar 4 — the beat 'breathes' for the punchline.
- Drums-out break mid-song (4 bars) resets attention.
- Minor i ↔ relative major alternation = cool tension.

## 13. Signature elements that must NOT be reproduced
- The McCallum-derived riff
- The exact bass/guitar figure

## 14. Open questions / needed evidence
- Instrumentation split (guitar vs. bass vs. keys)

## Measured profile [measured — scripts/analyze_track.py → analysis/data/Dr._Dre_-_The_Next_Episode_(Instrumental).json]

| metric | value |
|---|---|
| duration | 161.6 s, 64 bars of 2.5149 s |
| tempo | **95.431 BPM** (grid residual p90 7.5 ms; comb candidates [[3.945, 95.45], [3.687, 63.6], [3.076, 127.3]]; drift first→last third -0.006 %) |
| first downbeat | 0.143 s (bar-phase margin 0.254; snare backbeat ratio 1.84) |
| key | F# major [estimate, margin 0.138]; alternatives [['D# minor', 0.56], ['B major', 0.503]] |
| loudness | -9.19 LUFS integrated, short-term p10/p90 [-11.4, -7.9], crest 13.52 dB, sample peak 2.48 dBFS |
| stereo | side−mid -21.4 dB overall, -23.0 dB below 150 Hz |
| spectrum | 60.7 % of energy ≤150 Hz; centroid 2803.0 Hz; HF content to ~10809 Hz |
| swing (hat 16ths) | None % (50 straight, 66.7 triplet); off-8th hat delay 21.4 ms |
| perc vs harmonic | 2.1 dB |
| harmonic loop similarity (bar lags) | {'1': 0.199, '2': 0.744, '3': 0.093, '4': 0.589, '8': 0.55} |

**16-step onset occupancy** (X strong, x present; whole track):
```
        1 e & a 2 e & a 3 e & a 4 e & a
kick    X . . . x . X . x . X . x . X .
snare   X . . . X . . . x . x . X . . .
hat     X . x . X . X . X . x . X . X .
```
Median micro-timing per step (ms, + = late): kick [13.5, -21.4, -59.1, 29.8, 24.2, None, 22.9, None, 29.6, 17.0, 14.4, -4.2, 27.4, 23.8, 17.6, -66.9], snare [17.5, None, 29.8, None, 15.3, None, 27.1, None, 34.9, None, 18.4, None, 15.1, None, 22.0, None], hat [19.3, None, 22.5, None, 23.7, None, 19.2, None, 17.0, None, 27.3, None, 24.0, None, 20.2, None]

**Layer timeline** (per bar vs. track median; NO-LOW = sub ≥6 dB down, NO-DRUMS = percussive ≥6 dB down):
b1-3:NO-DRUMS,no-hats,melody+ | b4:NO-DRUMS,melody+ | b5-6:full | b7:melody+ | b8-13:full | b14:melody-off | b15-28:full | b29-32:NO-DRUMS,no-hats,melody+ | b33-37:full | b38:melody-off | b39-41:full | b42:melody-off | b43-45:full | b46:melody-off | b47-49:full | b50:melody-off | b51-53:full | b54:melody-off | b55-57:full | b58:melody-off | b59-60:full | b61:NO-LOW | b62-64:NO-LOW,NO-DRUMS,no-hats,melody-off

**Bars 2–9 harmonic sketch** [estimate: chroma template + bass chroma; not a transcription]: [D#5/D#5 bass D#-D#-D#-D#] [B5/B5 bass B-B-B-B] [D#5/D#5 bass D#-D#-D#-D#] [D#m7/F#maj7 bass D#-F#-F#-F#] [D7/F#maj7 bass F#-C-A#-A#] [D#m7/F#maj7 bass D#-F#-F#-F#] [D7/F#maj7 bass F#-C-A#-A#] [D#m7/F#maj7 bass D#-F#-F#-F#]

Pitch-class profile: {'C': 0.91, 'C#': 0.88, 'D': 0.72, 'D#': 0.9, 'E': 0.69, 'F': 0.71, 'F#': 1.0, 'G': 0.71, 'G#': 0.73, 'A': 0.78, 'A#': 0.96, 'B': 0.9}
Bass pitch-class profile: {'C': 0.96, 'C#': 0.87, 'D': 0.75, 'D#': 0.87, 'E': 0.7, 'F': 0.67, 'F#': 1.0, 'G': 0.69, 'G#': 0.69, 'A': 0.77, 'A#': 0.93, 'B': 0.87}

=== FILE: analysis/track_reports/Dr_Dre-_Still_Dre_instrumental.md ===
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

=== FILE: analysis/track_reports/Fat_Joe_-_Lean_Back_(Instrumental).md ===
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

=== FILE: analysis/track_reports/G_Unit_-_Poppin__Them_Thangs.md ===
# G-Unit — Poppin' Them Thangs (2003)

**Archetype:** G-Unit street anthem (piano-led, aggressive)  ·  **Source file:** `references/raw/` (G_Unit_-_Poppin__Them_Thangs)
**Evidence status:** measured by script; NOT listened to by the model. Every [hypothesis] needs the King's ear.

## 1. Identity & emotional character
Aggressive, militant, piano-driven. Lowest low-end share of all (30.6 % ≤150 Hz) [measured] → mid-forward record: the piano/keys hit hard in the mids. Loud (−8.0 LUFS) [measured].

**Production history:** Produced by Scott Storch [documented, moderate confidence — verify].

## 2–3. Tempo, groove, timing
88.0 BPM, swing 66 % (triplet feel) [measured]. 8th hats straight-through [measured].

## 4–6. Drums, bass, harmony & texture
F#-minor, bars alternate F#m ↔ Bm7 with bass F#–F–E / F#–D#–B descent [estimate] → chromatic descending bass under a minor i–iv = menace.

## 7–9. Structure, sections, layer changes
Almost no layer changes (b1–94 full) [measured] → the drama is in the riff, not the arrangement.
Full per-bar map: `analysis/structural_maps/G_Unit_-_Poppin__Them_Thangs.csv` · plot: `analysis/plots/G_Unit_-_Poppin__Them_Thangs.png`

## 11. Vocal compatibility
Mid-forward beat → vocals must be EQ'd to cut through, or the piano must leave rhythmic gaps [hypothesis].

## 12. Transferable principles
- Chromatic descending bass line under i–iv minor = street menace.
- Aggression can come from mid-range piano hits instead of sub.
- Triplet-swung hats at 88 BPM.

## 13. Signature elements that must NOT be reproduced
- The piano riff

## 14. Open questions / needed evidence
- Producer verification
- Exact piano voicings

## Measured profile [measured — scripts/analyze_track.py → analysis/data/G_Unit_-_Poppin__Them_Thangs.json]

| metric | value |
|---|---|
| duration | 272.45 s, 99 bars of 2.7269 s |
| tempo | **88.012 BPM** (grid residual p90 6.3 ms; comb candidates [[4.097, 88.0], [4.091, 176.1], [3.374, 117.35]]; drift first→last third -0.001 %) |
| first downbeat | 0.294 s (bar-phase margin 0.063; snare backbeat ratio 3.25) |
| key | F# minor [estimate, margin 0.254]; alternatives [['F# major', 0.556], ['A major', 0.405]] |
| loudness | -8.01 LUFS integrated, short-term p10/p90 [-8.6, -7.6], crest 12.84 dB, sample peak 2.45 dBFS |
| stereo | side−mid -12.7 dB overall, -23.8 dB below 150 Hz |
| spectrum | 30.6 % of energy ≤150 Hz; centroid 2152.0 Hz; HF content to ~10766 Hz |
| swing (hat 16ths) | 66.0 % (50 straight, 66.7 triplet); off-8th hat delay 22.0 ms |
| perc vs harmonic | -0.3 dB |
| harmonic loop similarity (bar lags) | {'1': 0.017, '2': 0.495, '3': -0.174, '4': 0.394, '8': 0.528} |

**16-step onset occupancy** (X strong, x present; whole track):
```
        1 e & a 2 e & a 3 e & a 4 e & a
kick    x . . . x . . . X . . . x . x .
snare   . . . x X . x . x . x . X . X .
hat     x . X . X . X . X . X . X . X .
```
Median micro-timing per step (ms, + = late): kick [7.7, -38.9, 58.7, 54.9, 22.2, 57.9, 22.9, 28.3, 5.6, -76.7, 45.0, 44.6, 32.9, None, 4.4, 65.5], snare [27.4, None, 29.4, 55.2, 23.7, 55.6, 25.3, 27.2, 24.7, 44.6, 24.6, 55.8, 22.9, 60.2, 25.0, 23.8], hat [24.2, None, 23.2, 54.6, 22.5, None, 21.9, None, 22.7, 39.5, 21.8, 54.5, 21.6, 65.5, 22.1, 22.8]

**Layer timeline** (per bar vs. track median; NO-LOW = sub ≥6 dB down, NO-DRUMS = percussive ≥6 dB down):
b1-8:full | b9:hats+ | b10-57:full | b58:low-thin | b59:full | b60:low-thin | b61-94:full | b95:NO-LOW,no-hats,melody-off | b96-99:NO-LOW,NO-DRUMS,no-hats,melody-off

**Bars 2–9 harmonic sketch** [estimate: chroma template + bass chroma; not a transcription]: [F#m/F#m7 bass F#-F#-E-E] [F#m/Bm7 bass F#-F-D#-B] [F#m/F#m7 bass F#-D#-E-E] [F#m/Bm7 bass F#-F#-D#-B] [F#m/F#m7 bass F#-F-D#-E] [F#m/Bm7 bass F#-F#-D#-B] [F#m/F#m7 bass F#-F-E-E] [F#m/Bm7 bass F#-F#-F#-B]

Pitch-class profile: {'C': 0.15, 'C#': 0.59, 'D': 0.23, 'D#': 0.25, 'E': 0.37, 'F': 0.39, 'F#': 1.0, 'G': 0.28, 'G#': 0.25, 'A': 0.54, 'A#': 0.21, 'B': 0.29}
Bass pitch-class profile: {'C': 0.23, 'C#': 0.3, 'D': 0.4, 'D#': 0.56, 'E': 0.69, 'F': 0.73, 'F#': 1.0, 'G': 0.45, 'G#': 0.29, 'A': 0.24, 'A#': 0.19, 'B': 0.29}

=== FILE: analysis/track_reports/Ice_Cube_Why_We_Thugs_Instrumental.md ===
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

=== FILE: analysis/track_reports/Jay-Z_-_Blueprint_2_(Instrumental).md ===
# Jay-Z — Blueprint² (title track, 2002)

**Archetype:** Soulful/cinematic East Coast  ·  **Source file:** `references/raw/` (Jay-Z_-_Blueprint_2_(Instrumental))
**Evidence status:** measured by script; NOT listened to by the model. Every [hypothesis] needs the King's ear.

## 1. Identity & emotional character
Reflective, grand. Long intro: bars 1–16 have no drums and no low end [measured] (sample breathing alone). Dynamic master (−15.7 LUFS, crest 17.4) [measured].

**Production history:** [unknown] producer not verified here.

## 2–3. Tempo, groove, timing
90.0 BPM, swing ≈ 72 % [measured]. Kick pattern X...x..X..X.x..x [measured].

## 4–6. Drums, bass, harmony & texture
Static C-major-7 / E-bass colour for the first bars (Cmaj7 over E) [estimate] → a suspended, unresolved soul sample.

## 7–9. Structure, sections, layer changes
16-bar drumless intro; then melody+ blocks of 2–4 bars alternating with full bars (b17–18, 21–26, 29–32, 49–50, 53–56, 73–74, 77–80) [measured].
Full per-bar map: `analysis/structural_maps/Jay-Z_-_Blueprint_2_(Instrumental).csv` · plot: `analysis/plots/Jay-Z_-_Blueprint_2_(Instrumental).png`

## 11. Vocal compatibility
Low-end only half the energy (50 % ≤150 Hz) → mids carry the sample; vocal competes, so the sample must duck or thin under verses [hypothesis].

## 12. Transferable principles
- A long drumless intro (16 bars) is legitimate when the sample has narrative weight.
- Maj7-over-3rd voicing = unresolved, reflective.

## 13. Signature elements that must NOT be reproduced
- The sample/chop

## 14. Open questions / needed evidence
- Producer and sample source

## Measured profile [measured — scripts/analyze_track.py → analysis/data/Jay-Z_-_Blueprint_2_(Instrumental).json]

| metric | value |
|---|---|
| duration | 278.4 s, 104 bars of 2.6668 s |
| tempo | **89.996 BPM** (grid residual p90 13.0 ms; comb candidates [[4.172, 90.0], [4.132, 180.0], [4.017, 60.0]]; drift first→last third -0.017 %) |
| first downbeat | 1.018 s (bar-phase margin 1.524; snare backbeat ratio 2.01) |
| key | A minor [estimate, margin 0.064]; alternatives [['C major', 0.776], ['E minor', 0.579]] |
| loudness | -15.68 LUFS integrated, short-term p10/p90 [-21.0, -14.1], crest 17.37 dB, sample peak -0.54 dBFS |
| stereo | side−mid -12.4 dB overall, -10.8 dB below 150 Hz |
| spectrum | 50.1 % of energy ≤150 Hz; centroid 1595.0 Hz; HF content to ~10809 Hz |
| swing (hat 16ths) | 71.9 % (50 straight, 66.7 triplet); off-8th hat delay 21.1 ms |
| perc vs harmonic | -1.8 dB |
| harmonic loop similarity (bar lags) | {'1': -0.037, '2': -0.071, '3': 0.066, '4': 0.402, '8': 0.782} |

**16-step onset occupancy** (X strong, x present; whole track):
```
        1 e & a 2 e & a 3 e & a 4 e & a
kick    X . . . x . . X . . X . x . . x
snare   X . . . X . x x x . x . X . X .
hat     x . x . X . X x X . x . X . X .
```
Median micro-timing per step (ms, + = late): kick [20.3, 34.7, 33.6, 43.2, 20.1, 36.9, 33.6, 18.2, -49.4, 37.5, 19.1, -44.4, 24.4, 42.0, 33.5, 24.9], snare [25.2, 27.7, 27.3, 32.1, 21.4, 25.1, 22.4, 27.1, 23.3, 32.8, 25.6, 35.7, 21.6, 33.6, 22.7, 26.0], hat [24.0, None, 22.8, 74.1, 17.9, None, 19.1, 25.3, 20.6, 78.1, 20.7, 77.2, 16.4, 72.1, 21.6, 27.9]

**Layer timeline** (per bar vs. track median; NO-LOW = sub ≥6 dB down, NO-DRUMS = percussive ≥6 dB down):
b1:NO-LOW,NO-DRUMS,no-hats,melody+ | b2:NO-LOW,NO-DRUMS,no-hats | b3:NO-LOW,NO-DRUMS,no-hats,melody+ | b4:NO-LOW,NO-DRUMS,no-hats | b5:NO-LOW,NO-DRUMS,no-hats,melody+ | b6:NO-LOW,NO-DRUMS,no-hats | b7:NO-LOW,NO-DRUMS,no-hats,melody+ | b8:NO-LOW,NO-DRUMS,no-hats | b9:NO-LOW,NO-DRUMS,no-hats,melody+ | b10:NO-LOW,NO-DRUMS,no-hats | b11:NO-LOW,NO-DRUMS,no-hats,melody+ | b12-13:NO-LOW,NO-DRUMS,no-hats | b14:NO-LOW,NO-DRUMS | b15:NO-LOW,NO-DRUMS,no-hats | b16:NO-LOW | b17-18:melody+ | b19-20:full | b21-26:melody+ | b27-28:full | b29-32:melody+ | b33-48:full | b49-50:melody+ | b51-52:full | b53-56:melody+ | b57-72:full | b73-74:melody+ | b75-76:full | b77-80:melody+ | b81-101:full | b102:NO-LOW,NO-DRUMS,melody-off | b103-104:NO-LOW,NO-DRUMS,no-hats,melody-off

**Bars 2–9 harmonic sketch** [estimate: chroma template + bass chroma; not a transcription]: [Cmaj7/Cmaj7 bass E-E-E-E] [Cmaj7/Cmaj7 bass E-E-E-E] [Cmaj7/Cmaj7 bass E-E-E-E] [Cmaj7/Cmaj7 bass B-E-E-E] [Cmaj7/Cmaj7 bass E-E-E-E] [Cmaj7/Cmaj7 bass E-E-E-E] [Cmaj7/Cmaj7 bass E-E-E-E] [Cmaj7/Cmaj7 bass E-E-E-E]

Pitch-class profile: {'C': 1.0, 'C#': 0.39, 'D': 0.54, 'D#': 0.33, 'E': 0.86, 'F': 0.49, 'F#': 0.26, 'G': 0.55, 'G#': 0.28, 'A': 0.81, 'A#': 0.4, 'B': 0.72}
Bass pitch-class profile: {'C': 1.0, 'C#': 0.46, 'D': 0.67, 'D#': 0.45, 'E': 0.91, 'F': 0.68, 'F#': 0.32, 'G': 0.63, 'G#': 0.36, 'A': 0.93, 'A#': 0.54, 'B': 0.76}

=== FILE: analysis/track_reports/Kendrick_Lamar_-_Bitch,_Don_t_Kill_My_Vibe_[Instrumental].md ===
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

=== FILE: analysis/track_reports/Mathematics,_Method_Man,_AZ,_Wu_Tang_Clan_God_Body_INSTRUMENTA.md ===
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

=== FILE: analysis/track_reports/Mobb_Deep_-_Burn_(Instrumentals).md ===
# Mobb Deep — Burn (Infamy era, 2001)

**Archetype:** Dark NY / mafioso  ·  **Source file:** `references/raw/` (Mobb_Deep_-_Burn_(Instrumentals))
**Evidence status:** measured by script; NOT listened to by the model. Every [hypothesis] needs the King's ear.

## 1. Identity & emotional character
Dark, steady, heavy low end (86.7 % ≤150 Hz — highest) [measured]. No layer changes bars 1–94 [measured].

**Production history:** Mobb Deep record; production credit not verified here (likely Havoc) [unknown].

## 2–3. Tempo, groove, timing
95.6 BPM; kick X...x..xX.X.x... [measured].

## 4–6. Drums, bass, harmony & texture
Dominant-7 colours (G7, A7, E7) with chromatic bass A–G–D–C / F–F–D–A [estimate] → bluesy, unresolved dominant chain.

## 7–9. Structure, sections, layer changes
Continuous loop, outro drop at b96 [measured].
Full per-bar map: `analysis/structural_maps/Mobb_Deep_-_Burn_(Instrumentals).csv` · plot: `analysis/plots/Mobb_Deep_-_Burn_(Instrumentals).png`

## 11. Vocal compatibility
Huge sub, quiet mids → vocals sit easily [hypothesis].

## 12. Transferable principles
- Dominant-7 chains without resolution = unease.
- When the sub carries 87 % of the energy, every other element must be thin and dark.

## 13. Signature elements that must NOT be reproduced
- The loop

## 14. Open questions / needed evidence
- Producer, sample

## Measured profile [measured — scripts/analyze_track.py → analysis/data/Mobb_Deep_-_Burn_(Instrumentals).json]

| metric | value |
|---|---|
| duration | 257.44 s, 101 bars of 2.5118 s |
| tempo | **95.551 BPM** (grid residual p90 8.5 ms; comb candidates [[3.899, 95.55], [3.228, 63.7], [2.405, 76.45]]; drift first→last third -0.025 %) |
| first downbeat | 1.395 s (bar-phase margin 0.064; snare backbeat ratio 11.42) |
| key | C major [estimate, margin 0.082]; alternatives [['G major', 0.516], ['F major', 0.427]] |
| loudness | -9.06 LUFS integrated, short-term p10/p90 [-10.2, -7.9], crest 12.16 dB, sample peak 2.34 dBFS |
| stereo | side−mid -20.8 dB overall, -36.2 dB below 150 Hz |
| spectrum | 86.7 % of energy ≤150 Hz; centroid 3796.0 Hz; HF content to ~10809 Hz |
| swing (hat 16ths) | None % (50 straight, 66.7 triplet); off-8th hat delay 55.9 ms |
| perc vs harmonic | 1.5 dB |
| harmonic loop similarity (bar lags) | {'1': -0.228, '2': -0.47, '3': -0.232, '4': 0.972, '8': 0.97} |

**16-step onset occupancy** (X strong, x present; whole track):
```
        1 e & a 2 e & a 3 e & a 4 e & a
kick    X . . . x . . x X . X . x . . .
snare   . . x . X . . . . . . . X . . .
hat     . . x . X . x . . . x . X . x .
```
Median micro-timing per step (ms, + = late): kick [13.8, -56.4, -4.7, -61.9, 22.9, -75.0, -59.3, 37.2, 15.4, -54.8, 13.9, 69.6, 18.2, -43.5, -60.5, -64.3], snare [50.0, 49.7, 48.4, None, 18.5, None, 53.6, None, 50.9, 44.7, 47.4, None, 18.1, None, 53.4, 74.1], hat [55.4, None, 48.9, None, 20.9, None, 56.4, None, 57.8, None, 55.5, None, 21.3, None, 56.2, None]

**Layer timeline** (per bar vs. track median; NO-LOW = sub ≥6 dB down, NO-DRUMS = percussive ≥6 dB down):
b1-94:full | b95:no-hats,melody-off | b96-101:NO-LOW,NO-DRUMS,no-hats,melody-off

**Bars 2–9 harmonic sketch** [estimate: chroma template + bass chroma; not a transcription]: [G7/C#maj7 bass A-G-D-C] [Fmaj7/A7 bass F-F-D-A] [G7/Fm7 bass A-G-D#-G#] [E7/A7 bass C-E-D-A] [G7/C#maj7 bass A-G-D-C] [Fmaj7/A7 bass F-F-D-A] [G7/Fm7 bass A-G-D#-G#] [Cmaj7/A7 bass C-E-D-A]

Pitch-class profile: {'C': 0.74, 'C#': 0.73, 'D': 0.75, 'D#': 0.63, 'E': 0.75, 'F': 0.86, 'F#': 0.51, 'G': 1.0, 'G#': 0.74, 'A': 0.86, 'A#': 0.6, 'B': 0.81}
Bass pitch-class profile: {'C': 0.96, 'C#': 0.87, 'D': 0.94, 'D#': 0.87, 'E': 0.93, 'F': 0.96, 'F#': 0.72, 'G': 1.0, 'G#': 0.92, 'A': 0.98, 'A#': 0.78, 'B': 0.79}

=== FILE: analysis/track_reports/Mobb_Deep_Shook_Ones,_Pt_II_Instrumental.md ===
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

=== FILE: analysis/track_reports/Mobb_Deep_Survival_Of_The_Fittest_Instrumental.md ===
# Mobb Deep — Survival of the Fittest (1995)

**Archetype:** Gritty underground NY  ·  **Source file:** `references/raw/` (Mobb_Deep_Survival_Of_The_Fittest_Instrumental)
**Evidence status:** measured by script; NOT listened to by the model. Every [hypothesis] needs the King's ear.

## 1. Identity & emotional character
Bleak, haunting. Intro bars 1–6 with no drums [measured]; then a strict 2-bar alternation (odd bars full, even bars melody+) [measured] — a 2-bar sample phrase where bar 2 carries the melodic tail.

**Production history:** Produced by Mobb Deep (Havoc) [documented]; jazz piano sample (reportedly Barry Harris 'Skylark') [documented, moderate confidence — verify]. 128 kbps source.

## 2–3. Tempo, groove, timing
95.15 BPM; kick X.X....xX.x....x, snare on 2 & 4 [measured].

## 4–6. Drums, bass, harmony & texture
E/F semitone (Fmaj7 chroma over E bass) [estimate] → ♭2 over the bass = haunted.

## 7–9. Structure, sections, layer changes
6-bar drumless intro, then the 2-bar call/response loop for the whole song [measured].
Full per-bar map: `analysis/structural_maps/Mobb_Deep_Survival_Of_The_Fittest_Instrumental.csv` · plot: `analysis/plots/Mobb_Deep_Survival_Of_The_Fittest_Instrumental.png`

## 11. Vocal compatibility
Bass pedal on E keeps the floor fixed while the sample moves above [hypothesis].

## 12. Transferable principles
- ♭II over the root (F over E) = haunting.
- 2-bar sample phrase where bar 2 'answers' — loop as a sentence.
- 6-bar drumless intro for mood.

## 13. Signature elements that must NOT be reproduced
- The piano sample

## 14. Open questions / needed evidence
- Sample verification

## Measured profile [measured — scripts/analyze_track.py → analysis/data/Mobb_Deep_Survival_Of_The_Fittest_Instrumental.json]

| metric | value |
|---|---|
| duration | 216.87 s, 85 bars of 2.5223 s |
| tempo | **95.15 BPM** (grid residual p90 7.2 ms; comb candidates [[4.29, 95.2], [4.138, 63.45], [3.414, 126.9]]; drift first→last third -0.021 %) |
| first downbeat | 2.105 s (bar-phase margin 0.146; snare backbeat ratio 6.23) |
| key | E minor [estimate, margin 0.087]; alternatives [['E major', 0.311], ['C major', 0.311]] |
| loudness | -11.42 LUFS integrated, short-term p10/p90 [-12.7, -10.8], crest 12.38 dB, sample peak 1.49 dBFS |
| stereo | side−mid -19.6 dB overall, -22.8 dB below 150 Hz |
| spectrum | 78.1 % of energy ≤150 Hz; centroid 1637.0 Hz; HF content to ~10782 Hz |
| swing (hat 16ths) | None % (50 straight, 66.7 triplet); off-8th hat delay 20.4 ms |
| perc vs harmonic | -5.2 dB |
| harmonic loop similarity (bar lags) | {'1': -0.642, '2': 0.852, '3': -0.675, '4': 0.861, '8': 0.829} |

**16-step onset occupancy** (X strong, x present; whole track):
```
        1 e & a 2 e & a 3 e & a 4 e & a
kick    X . X . . . . x X . x . . . . x
snare   . . . . X . . . . . x . X . . .
hat     x . x . X . x . x . X . X . x .
```
Median micro-timing per step (ms, + = late): kick [28.2, -7.1, 23.6, -8.1, 17.4, -65.1, 26.0, 70.0, 30.3, -5.4, 24.5, -2.6, 21.6, -68.0, -46.2, -52.5], snare [22.2, -12.4, 22.1, -22.8, 17.1, None, 32.2, None, 22.9, -29.4, 23.4, None, 16.2, None, 31.5, 26.5], hat [20.1, None, 19.9, None, 18.3, None, 21.0, None, 21.4, None, 20.5, None, 18.5, None, 20.3, None]

**Layer timeline** (per bar vs. track median; NO-LOW = sub ≥6 dB down, NO-DRUMS = percussive ≥6 dB down):
b1:NO-LOW,NO-DRUMS,no-hats | b2:NO-LOW,NO-DRUMS,no-hats,melody+ | b3:NO-DRUMS,no-hats | b4:NO-DRUMS,no-hats,melody+ | b5:NO-DRUMS,no-hats | b6:NO-DRUMS,no-hats,melody+ | b7:no-hats | b8:melody+ | b9:full | b10:melody+ | b11:full | b12:melody+ | b13:full | b14:melody+ | b15:full | b16:melody+ | b17:full | b18:melody+ | b19:low-thin | b20:melody+ | b21:full | b22:melody+ | b23:full | b24:melody+ | b25:full | b26:melody+ | b27:full | b28:melody+ | b29:full | b30:melody+ | b31:full | b32:melody+ | b33:full | b34:melody+ | b35:full | b36:melody+ | b37:full | b38:melody+ | b39:full | b40:melody+ | b41:full | b42:melody+ | b43:full | b44:melody+ | b45:full | b46:melody+ | b47:full | b48:melody+ | b49:full | b50:melody+ | b51:full | b52:melody+ | b53:full | b54:melody+ | b55:full | b56:melody+ | b57:full | b58:melody+ | b59:full | b60:melody+ | b61:full | b62:melody+ | b63:full | b64:melody+ | b65:full | b66:melody+ | b67:full | b68:melody+ | b69:full | b70:melody+ | b71-73:full | b74:melody+ | b75:full | b76:melody+ | b77:full | b78:melody+ | b79:full | b80:melody+ | b81:NO-LOW,NO-DRUMS | b82:NO-LOW,NO-DRUMS,melody+ | b83:full | b84-85:NO-LOW,NO-DRUMS,no-hats,melody-off

**Bars 2–9 harmonic sketch** [estimate: chroma template + bass chroma; not a transcription]: [Fmaj7/Cmaj7 bass E-E-C-G] [Fmaj7/Fmaj7 bass E-E-E-E] [Fmaj7/Em7 bass E-E-E-E] [Fmaj7/Fmaj7 bass E-E-E-E] [Fmaj7/Em7 bass E-E-E-E] [Fmaj7/Fmaj7 bass E-E-E-E] [Fmaj7/Em7 bass E-E-E-E] [Fmaj7/Fmaj7 bass E-E-E-E]

Pitch-class profile: {'C': 0.15, 'C#': 0.16, 'D': 0.23, 'D#': 0.26, 'E': 1.0, 'F': 0.67, 'F#': 0.42, 'G': 0.37, 'G#': 0.26, 'A': 0.22, 'A#': 0.16, 'B': 0.14}
Bass pitch-class profile: {'C': 0.12, 'C#': 0.16, 'D': 0.2, 'D#': 0.24, 'E': 1.0, 'F': 0.44, 'F#': 0.34, 'G': 0.31, 'G#': 0.2, 'A': 0.18, 'A#': 0.13, 'B': 0.1}

=== FILE: analysis/track_reports/Nas_-_N_Y._State_Of_Mind_Instrumental.md ===
# Nas — N.Y. State of Mind (1994)

**Archetype:** DJ Premier NY boom-bap (canonical)  ·  **Source file:** `references/raw/` (Nas_-_N_Y._State_Of_Mind_Instrumental)
**Evidence status:** measured by script; NOT listened to by the model. Every [hypothesis] needs the King's ear.

## 1. Identity & emotional character
Tense, nocturnal, cinematic street noir. 84.5 BPM [measured].

**Production history:** Produced by DJ Premier; samples Joe Chambers 'Mind Rain' (piano) and Donald Byrd 'Flight Time' [documented].

## 2–3. Tempo, groove, timing
84.48 BPM; swing 69 % [measured]. Kick X.xxx....xX.x..X (chopped, irregular) [measured] → Premier's syncopated, chopped-break feel.

## 4–6. Drums, bass, harmony & texture
F#/C# area with diminished colour (Ddim/C#7 sketches) [estimate] → dark jazz piano dissonance.

## 7–9. Structure, sections, layer changes
Intro alternating low-thin/full bars (b1–5) [measured]; hats+ blocks b49–52 and b89–99 [measured] → hat density raised in later sections.
Full per-bar map: `analysis/structural_maps/Nas_-_N_Y._State_Of_Mind_Instrumental.csv` · plot: `analysis/plots/Nas_-_N_Y._State_Of_Mind_Instrumental.png`

## 11. Vocal compatibility
Mid 65 % low share; the jazz piano sits in short stabs [hypothesis].

## 12. Transferable principles
- Jazz dissonance (dim/7♭9) chopped into short stabs = noir.
- 84 BPM + 69 % swing = heavy walking pocket.
- Raise hat density for later verses instead of adding instruments.

## 13. Signature elements that must NOT be reproduced
- The Mind Rain piano chop
- Flight Time bass

## 14. Open questions / needed evidence
- Exact chop points

## Measured profile [measured — scripts/analyze_track.py → analysis/data/Nas_-_N_Y._State_Of_Mind_Instrumental.json]

| metric | value |
|---|---|
| duration | 297.33 s, 104 bars of 2.841 s |
| tempo | **84.476 BPM** (grid residual p90 30.8 ms; comb candidates [[3.37, 84.5], [2.874, 169.05], [2.107, 112.65]]; drift first→last third -0.004 %) |
| first downbeat | 0.171 s (bar-phase margin 1.573; snare backbeat ratio 3.24) |
| key | C# major [estimate, margin 0.147]; alternatives [['C# minor', 0.427], ['F# minor', 0.414]] |
| loudness | -11.39 LUFS integrated, short-term p10/p90 [-12.9, -10.8], crest 12.7 dB, sample peak -0.3 dBFS |
| stereo | side−mid -24.3 dB overall, -23.1 dB below 150 Hz |
| spectrum | 65.2 % of energy ≤150 Hz; centroid 1788.0 Hz; HF content to ~10691 Hz |
| swing (hat 16ths) | 69.3 % (50 straight, 66.7 triplet); off-8th hat delay 44.4 ms |
| perc vs harmonic | -2.6 dB |
| harmonic loop similarity (bar lags) | {'1': -0.296, '2': 0.813, '3': -0.38, '4': 0.685, '8': 0.613} |

**16-step onset occupancy** (X strong, x present; whole track):
```
        1 e & a 2 e & a 3 e & a 4 e & a
kick    X . x x x . . . . x X . x . . X
snare   X . x . X . . . x X . . X . x .
hat     X . x . X . x . X X . . X . x .
```
Median micro-timing per step (ms, + = late): kick [15.7, -40.5, 11.7, 65.7, 18.6, 16.0, -18.0, 69.9, -58.7, 74.6, 8.0, 23.0, 12.6, 21.2, 43.7, 43.3], snare [7.5, 70.9, 12.1, 72.5, 5.4, 56.6, 46.7, 82.1, 64.1, 62.0, None, 63.1, 7.3, 74.2, 40.1, 76.1], hat [8.7, 78.5, 47.1, 45.2, 5.6, 52.5, 41.6, 72.3, 66.3, 64.8, 67.0, 61.7, 8.1, 72.0, 36.7, 72.4]

**Layer timeline** (per bar vs. track median; NO-LOW = sub ≥6 dB down, NO-DRUMS = percussive ≥6 dB down):
b1:low-thin | b2:full | b3:low-thin | b4:full | b5:low-thin | b6-48:full | b49-52:hats+ | b53:low-thin | b54:melody-off | b55:low-thin | b56-78:full | b79:low-thin,melody-off | b80:melody-off | b81-88:full | b89-97:hats+ | b98:hats+,melody-off | b99:low-thin,hats+,melody-off | b100:low-thin,melody-off | b101-104:NO-LOW,NO-DRUMS,no-hats,melody-off

**Bars 2–9 harmonic sketch** [estimate: chroma template + bass chroma; not a transcription]: [F#maj7/F#maj7 bass F-E-F-F] [F#maj7/F#maj7 bass F-F#-F-F] [F#maj7/F#maj7 bass F-F#-F-G] [A#m7/C#7 bass F-G#-C#-F] [Ddim/C#7 bass F-G#-G#-B] [C#5/C#7 bass C#-G#-G#-B] [Ddim/C#7 bass E-G#-G#-B] [C#5/C#7 bass C#-G#-G#-B]

Pitch-class profile: {'C': 0.39, 'C#': 0.68, 'D': 0.45, 'D#': 0.34, 'E': 0.52, 'F': 0.69, 'F#': 0.67, 'G': 0.54, 'G#': 1.0, 'A': 0.45, 'A#': 0.36, 'B': 0.57}
Bass pitch-class profile: {'C': 0.52, 'C#': 0.71, 'D': 0.45, 'D#': 0.37, 'E': 0.68, 'F': 0.76, 'F#': 0.68, 'G': 0.78, 'G#': 1.0, 'A': 0.43, 'A#': 0.44, 'B': 0.56}

=== FILE: analysis/track_reports/Nas_-_Nas_Is_Like_(Instrumental)_-_HQ.md ===
# Nas — Nas Is Like (1999)

**Archetype:** DJ Premier NY boom-bap  ·  **Source file:** `references/raw/` (Nas_-_Nas_Is_Like_(Instrumental)_-_HQ)
**Evidence status:** measured by script; NOT listened to by the model. Every [hypothesis] needs the King's ear.

## 1. Identity & emotional character
Ceremonial, stately. Intro bars 1–8 low-thin/melody-off [measured] → 8-bar intro with the cut/scratch or thin sample before full drums.

**Production history:** Produced by DJ Premier [documented]. I Am… era.

## 2–3. Tempo, groove, timing
94.5 BPM; swing 74 % (very late hats) [measured; estimate of feel].

## 4–6. Drums, bass, harmony & texture
Semitone neighbour A ↔ A# / G# ↔ A alternation (Amaj7/A#7) [estimate] → Premier's chromatic chop shift.

## 7–9. Structure, sections, layer changes
Full drop-outs at b28 and b82 (single bars) [measured] → classic one-bar break before a new section; melody-off b91–93 into the outro [measured].
Full per-bar map: `analysis/structural_maps/Nas_-_Nas_Is_Like_(Instrumental)_-_HQ.csv` · plot: `analysis/plots/Nas_-_Nas_Is_Like_(Instrumental)_-_HQ.png`

## 11. Vocal compatibility
Premier leaves space for scratched hooks (cuts) [documented habit; hypothesis here].

## 12. Transferable principles
- One-bar full stop before the hook/verse = punctuation.
- Chromatic semitone chop shift (A ↔ A#) as the 'turn' of the loop.
- 8-bar intro.

## 13. Signature elements that must NOT be reproduced
- The sample chop

## 14. Open questions / needed evidence
- Sample source

## Measured profile [measured — scripts/analyze_track.py → analysis/data/Nas_-_Nas_Is_Like_(Instrumental)_-_HQ.json]

| metric | value |
|---|---|
| duration | 241.07 s, 94 bars of 2.54 s |
| tempo | **94.488 BPM** (grid residual p90 6.6 ms; comb candidates [[3.492, 94.5], [2.941, 63.0], [2.17, 126.1]]; drift first→last third -0.001 %) |
| first downbeat | 0.356 s (bar-phase margin 0.953; snare backbeat ratio 2.62) |
| key | F# minor [estimate, margin 0.096]; alternatives [['C# minor', 0.477], ['C# major', 0.351]] |
| loudness | -15.03 LUFS integrated, short-term p10/p90 [-16.1, -14.3], crest 14.75 dB, sample peak -1.7 dBFS |
| stereo | side−mid -25.8 dB overall, -25.1 dB below 150 Hz |
| spectrum | 75.6 % of energy ≤150 Hz; centroid 2350.0 Hz; HF content to ~10755 Hz |
| swing (hat 16ths) | 74.2 % (50 straight, 66.7 triplet); off-8th hat delay 33.4 ms |
| perc vs harmonic | 0.3 dB |
| harmonic loop similarity (bar lags) | {'1': -0.678, '2': 0.861, '3': -0.712, '4': 0.822, '8': 0.771} |

**16-step onset occupancy** (X strong, x present; whole track):
```
        1 e & a 2 e & a 3 e & a 4 e & a
kick    X . X . X . . . x . X . x . . .
snare   x . . . X . x . X . . . X . . .
hat     x . x . X . x . X . x . X . x .
```
Median micro-timing per step (ms, + = late): kick [25.5, -40.1, 24.7, -40.3, 12.6, None, None, 43.4, 34.1, 13.2, 24.2, -42.2, 34.6, -60.2, 10.4, -54.2], snare [24.3, None, 24.3, None, 17.0, None, 45.7, None, 23.6, None, 24.4, None, 17.9, None, 47.6, 76.8], hat [26.9, None, 24.0, None, 17.8, None, 42.7, None, 23.5, None, 22.0, None, 17.5, None, 43.3, 76.8]

**Layer timeline** (per bar vs. track median; NO-LOW = sub ≥6 dB down, NO-DRUMS = percussive ≥6 dB down):
b1-3:low-thin,melody-off | b4:melody-off | b5-8:low-thin,melody-off | b9-27:full | b28:NO-LOW,NO-DRUMS,no-hats,melody-off | b29-57:full | b58:no-hats | b59-81:full | b82:NO-LOW,no-hats,melody-off | b83-90:full | b91:melody-off | b92:low-thin,melody-off | b93:NO-LOW,no-hats,melody-off | b94:NO-LOW,NO-DRUMS,no-hats,melody-off

**Bars 2–9 harmonic sketch** [estimate: chroma template + bass chroma; not a transcription]: [Amaj7/A#7 bass G#-C#-G#-G] [G#maj7/Amaj7 bass G#-G-G#-G#] [Amaj7/A#7 bass G#-C#-G#-G#] [G#maj7/Amaj7 bass G#-G-G#-G#] [Amaj7/A#m7 bass G#-G#-G#-G#] [A#m7/Amaj7 bass G#-G-G#-G#] [Amaj7/A#maj7 bass G#-G-G#-A] [Gmaj7/Amaj7 bass F#-F#-F#-G#]

Pitch-class profile: {'C': 0.48, 'C#': 0.83, 'D': 0.38, 'D#': 0.3, 'E': 0.48, 'F': 0.42, 'F#': 0.8, 'G': 0.76, 'G#': 1.0, 'A': 0.79, 'A#': 0.48, 'B': 0.59}
Bass pitch-class profile: {'C': 0.6, 'C#': 0.73, 'D': 0.4, 'D#': 0.28, 'E': 0.3, 'F': 0.53, 'F#': 0.85, 'G': 0.86, 'G#': 1.0, 'A': 0.78, 'A#': 0.52, 'B': 0.57}

=== FILE: analysis/track_reports/Raekwon_-_Ice_Cream_(Instrumental)_[Track_13].md ===
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

=== FILE: analysis/track_reports/Wu_Tang_Clan_-_Triumph_Instrumental.md ===
# Wu-Tang Clan — Triumph (1997)

**Archetype:** Wu-Tang / martial-arts cinematic  ·  **Source file:** `references/raw/` (Wu_Tang_Clan_-_Triumph_Instrumental)
**Evidence status:** measured by script; NOT listened to by the model. Every [hypothesis] needs the King's ear.

## 1. Identity & emotional character
Epic, militant, cinematic. MONO file (side−mid −72 dB) [measured]. Very dynamic (−16 LUFS, crest 14.9) [measured]. 127 bars, longest reference.

**Production history:** Produced by RZA [documented]. Wu-Tang Forever.

## 2–3. Tempo, groove, timing
91.0 BPM, swing 64 % [measured]. Kick on every quarter in the first half (X.X.X.X.X...) [measured] — marching.

## 4–6. Drums, bass, harmony & texture
Power-fifth sketches D5/G5 with a D bass pedal [estimate] → modal (no 3rds) = martial/medieval.

## 7–9. Structure, sections, layer changes
Intro bars 1–8 melody+ (string/horn statement) [measured]; then long continuous verse sections with melody-off pockets (b85, 88–91, 103, 105) [measured] — 9 MCs, the arrangement is the verse order.
Full per-bar map: `analysis/structural_maps/Wu_Tang_Clan_-_Triumph_Instrumental.csv` · plot: `analysis/plots/Wu_Tang_Clan_-_Triumph_Instrumental.png`

## 11. Vocal compatibility
Modal, open fifths leave all harmonic room for vocals [hypothesis].

## 12. Transferable principles
- Open fifths + pedal bass = martial/cinematic (no major/minor commitment).
- Marching quarter-note kick for militancy.
- 8-bar orchestral intro statement.

## 13. Signature elements that must NOT be reproduced
- The sample/horn line

## 14. Open questions / needed evidence
- Sample source; exact instrumentation

## Measured profile [measured — scripts/analyze_track.py → analysis/data/Wu_Tang_Clan_-_Triumph_Instrumental.json]

| metric | value |
|---|---|
| duration | 338.78 s, 127 bars of 2.6371 s |
| tempo | **91.009 BPM** (grid residual p90 14.7 ms; comb candidates [[3.174, 91.0], [2.617, 60.65], [2.012, 121.2]]; drift first→last third -0.004 %) |
| first downbeat | 1.566 s (bar-phase margin 0.123; snare backbeat ratio 3.38) |
| key | D minor [estimate, margin 0.036]; alternatives [['D major', 0.482], ['B minor', 0.305]] |
| loudness | -16.05 LUFS integrated, short-term p10/p90 [-16.4, -15.7], crest 14.87 dB, sample peak -2.72 dBFS |
| stereo | side−mid -71.8 dB overall, -120.0 dB below 150 Hz |
| spectrum | 70.6 % of energy ≤150 Hz; centroid 1762.0 Hz; HF content to ~10691 Hz |
| swing (hat 16ths) | 64.3 % (50 straight, 66.7 triplet); off-8th hat delay 29.5 ms |
| perc vs harmonic | -0.7 dB |
| harmonic loop similarity (bar lags) | {'1': 0.464, '2': 0.355, '3': 0.305, '4': 0.456, '8': 0.343} |

**16-step onset occupancy** (X strong, x present; whole track):
```
        1 e & a 2 e & a 3 e & a 4 e & a
kick    X . X . X . X . X . . . x . . .
snare   x . x . X . x . x . x . X . x .
hat     x . x . X . x . x . x . X . X .
```
Median micro-timing per step (ms, + = late): kick [-4.6, None, 3.8, None, 1.7, 70.1, 2.9, None, -2.4, -14.7, 27.3, -69.0, 32.9, None, 22.2, -56.5], snare [20.6, None, 37.8, 49.8, 24.2, None, 32.7, 46.8, 12.2, None, 24.9, 49.3, 23.1, None, 21.8, -40.8], hat [30.5, None, 45.6, 48.1, 22.4, None, 34.6, 46.4, 14.7, None, 24.4, 48.9, 23.5, None, 22.4, -37.2]

**Layer timeline** (per bar vs. track median; NO-LOW = sub ≥6 dB down, NO-DRUMS = percussive ≥6 dB down):
b1-8:melody+ | b9-30:full | b31:low-thin | b32-35:full | b36:melody+ | b37-40:full | b41:melody+ | b42-47:full | b48:melody+ | b49:melody-off | b50-54:full | b55:NO-LOW,no-hats | b56:low-thin | b57-58:full | b59-60:melody+ | b61-62:full | b63:melody+ | b64-84:full | b85:melody-off | b86-87:full | b88-91:melody-off | b92-102:full | b103:melody-off | b104:full | b105:melody-off | b106-127:full

**Bars 2–9 harmonic sketch** [estimate: chroma template + bass chroma; not a transcription]: [D5/G5 bass D-D-D-D] [G5/G5 bass D-D-D-D] [G5/G5 bass D-D-D-D] [G5/D5 bass D-D-D-D] [D5/G5 bass D-D-D-D] [G5/G5 bass D-D-D-D] [G5/D5 bass D-D-D-D] [D5/D5 bass D-D-D-D]

Pitch-class profile: {'C': 0.16, 'C#': 0.34, 'D': 1.0, 'D#': 0.27, 'E': 0.19, 'F': 0.14, 'F#': 0.07, 'G': 0.07, 'G#': 0.05, 'A': 0.11, 'A#': 0.07, 'B': 0.1}
Bass pitch-class profile: {'C': 0.16, 'C#': 0.59, 'D': 1.0, 'D#': 0.3, 'E': 0.2, 'F': 0.12, 'F#': 0.07, 'G': 0.07, 'G#': 0.05, 'A': 0.07, 'A#': 0.08, 'B': 0.12}

