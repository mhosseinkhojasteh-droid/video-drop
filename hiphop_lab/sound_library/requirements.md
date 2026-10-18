# Sound-library requirements & gap analysis (2026-10-15)

Legend: ESSENTIAL · HIGH · OPTIONAL · COVERED · SYNTH (replaceable by own sound design) · UNNEEDED

| Need (role) | Archetypes | Status | Covered by / gap |
|---|---|---|---|
| Acoustic kick/snare/hat multisamples (to be "sampled" through SP-1200/MPC emulation) | boom-bap, Mobb, Wu, West Coast | COVERED | Virtuosity Drums (CC0), Big Rusty Drums (CC0), AVL kits |
| 808/909 machine drums | Storch club, West Coast | SYNTH | dsp.kick_808 / snare_synth / hat_synth / clap_synth |
| Classic break-beat character (Funky Drummer-type) | boom-bap | SYNTH+COVERED | program breaks with acoustic kits + vintage(); real breaks are copyrighted → not used |
| Grand / upright piano | West Coast, Storch, Mobb | COVERED | Salamander (CC-BY 3.0, credit Alexander Holm), Splendid (PD) |
| Rhodes / FM e-piano | West Coast, soulful | COVERED (synth) | Dexed DX7 (GPL); jRhodes3d rejected (NC licence) |
| Funk/electric bass | West Coast | COVERED | Growlybass (CC0) + Surge bass patches |
| Upright bass | boom-bap, Wu | COVERED | Meatbass pizz (CC0) |
| Sub / 808 bass | all | SYNTH | Surge "Sub" patches + own 808 |
| Strings (sustain, staccato, pizz), brass, timpani, bells, harp, organ | mafioso, Wu, West Coast | COVERED | VSCO-2-CE (CC0) |
| G-funk portamento lead | West Coast | COVERED (synth) | Surge XT leads |
| Guitar (wah/funk licks, clean stabs) | West Coast, soul | COVERED | Black & Green Guitars (CC0) |
| Saxophone / horns for soul phrases | soulful, boom-bap | COVERED | Bear Sax (CC0), VSCO2 brass |
| Vinyl crackle, tape hiss, dust | boom-bap | SYNTH | to implement in dsp.py (filtered noise + crackle impulses) |
| Risers, impacts, reverse cymbals | transitions | SYNTH | dsp/Surge FX patches |
| Real reverb spaces | all | COVERED | Dragonfly Room/Plate/Hall, pedalboard Reverb |
| Tape saturation | boom-bap, soul | COVERED | CHOWTapeModel (GPL) |
| **Persian instruments (santur, tar/setar, kamancheh, ney, tombak, daf)** | our signature edge | **HIGH — GAP** | no CC0/CC-BY multisample found on allowed hosts yet; options: the King records/sources licensed samples; widen network to freesound.org (many CC0 one-shots) |
| **Soul/jazz "record" source material for chopping** | boom-bap, soulful | **HIGH — GAP (legal)** | own compositions rendered as fake records (piano/strings/sax → tape → vinyl) — legal and original; public-domain recordings need archive.org (blocked) |
| East-Asian instruments (koto, erhu, shamisen, gongs) for martial-arts textures | Wu | OPTIONAL — GAP | VSCO2 has gongs/bells; koto/erhu missing |
| Vocal chops / choir "aah" | soulful, cinematic | OPTIONAL — GAP | Surge vocal-ish patches; real choir missing |
| Scratch samples | Premier hooks | OPTIONAL | can be generated from our own renders with the God-of-Music scratch DSP |
| Warez plugins/packs (tsvst.ir etc.) | — | UNNEEDED / REJECTED | illegal for release + Windows binaries don't run here |
