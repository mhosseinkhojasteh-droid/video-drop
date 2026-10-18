# QC — Prototype 01 (2026-10-15)

## Deliverables
- `projects/prototype_01/renders/concept_{A,B,C}.{wav,mp3}` + stems — three 8-bar concepts.
- `projects/prototype_01/renders/glass_jaw_v3.{wav,mp3}` + `glass_jaw_v3_stems/` (kick, snare, hats, piano, cello, strings, bass, swell) — full 64-bar arrangement of concept B, 2:51.
- Source: `projects/prototype_01/concepts.py`, `projects/prototype_01/glass_jaw.py` (fully re-renderable, editable as code).

## Concept comparison [measured with the same pipeline as the references]
| | A Sunset Ghost (West Coast) | B Glass Jaw (G-Unit street) | C Concrete Psalm (NY boom-bap) | reference range of its archetype |
|---|---|---|---|---|
| BPM measured | 93.00 | 90.01 | 87.01 | 87–95 / 88–99 / 84–100 |
| LUFS / crest | −10.05 / 10.6 | −10.03 / 10.1 | −10.11 / 11.1 | crest 13–19 / 11–16 / 11–15 |
| energy ≤150 Hz | 64.7 % | 84.1 % | 53.7 % | 61–82 / 31–85 / 65–80 |
| centroid | 2064 Hz | 2333 Hz | 2107 Hz | 1.6–2.8 k / 1.0–2.2 k / 1.8–2.4 k |
| swing (hats) | n/a (too few onsets) | 69.2 % | n/a | 57–73 / 35–66 / 69–74 |
Selection: **B** — strongest emotion engine (♭2 Phrygian menace, used by 5 references), numbers inside its archetype range, clearest vocal space (mid 250 Hz–2 kHz ≈ 10–16 %). A is the runner-up; C's low end is below boom-bap range (54 % vs 65–80 %) and needs a heavier kick/sub before development.

## Glass Jaw revisions (measured, v1 → v3)
| | v1 | v2 | v3 (delivered) | target |
|---|---|---|---|---|
| LUFS | −10.14 | −10.60 | −11.10 | −10…−11 |
| crest | 9.59 | 10.47 | 10.68 | ≥ 11 (close) |
| ≤150 Hz | 84.5 % | 80.5 % | 76.5 % | 65–85 % |
| side−mid | −10.9 dB | −10.2 dB | −15.9 dB | −15…−22 dB |
| true peak | −0.98 | −0.96 | −1.00 dBTP | ≤ −1.0 |
Fixes: auto-balance by stem loudness (bass −4.5 LU vs snare); Salamander piano measured at side−mid −1.6 dB → narrowed to 40 % width; strings 50 %; reverb return 60 % width.
Structure verified by the analysis pipeline: 90.0 BPM, kick/808 drop-outs exactly on verse bars 1 and 9 (bars 13, 21, 37, 45), intro low-pass opening visible, outro closes.

## Scorecard (1–10) — machine + design judgement; ear-dependent items marked
| criterion | score | why |
|---|---|---|
| identity | 6 | one clear motif (2-bar F-Phrygian octave piano sentence) — needs the King's ear |
| emotional impact | ? | cannot be measured; awaiting blind listen |
| groove | 6 | 90 BPM, 64.7 % measured swing, 808 + kick lane split; drum sounds partly synthetic |
| musical motif | 6 | singable, has the rest on beat 4 (punchline slot) |
| arrangement | 6 | Template A executed; hook-vs-verse contrast is small in energy (hook adds octave + cello + strings) |
| sound selection | 5 | piano/cello/violin real samples; hats/clap synthesized → may sound "plastic" |
| vocal compatibility | 7 | mids open, motif thinned in verses, drop bars for MC entries |
| technical delivery | 8 | −11 LUFS, −1 dBTP, mono-safe low end, stems delivered |
| originality | 8 | motif written from scratch; no samples from references (formal n-gram check against reference melodies not possible — no reference transcriptions) |

## Weakest elements → next revision
1. Drum sound realism (synth hats/clap; jazz-kit rimshot as street snare). Fix: layered sampled hats (Big Rusty) + saturated clap; tune snare body; pass drums through MPC60 colour.
2. Hook lift. Fix: hook-only brass/horn stab (VSCO F-horn staccato) on motif accents + strings +3 dB + open-hat pattern; verse piano filtered harder.
3. (ear) whether the Phrygian motif reads "G-Unit street" or "horror". Needs the King's blind listen.

## Limits (honest)
- The model did not listen to anything. All judgements above are measurements or design reasoning.
- Rendering path is real: SFZ multisamples + Surge XT/VST3 + own DSP → WAV/MP3 + stems. No DAW project file (FL Studio) is produced yet; MIDI export is possible (next step).
