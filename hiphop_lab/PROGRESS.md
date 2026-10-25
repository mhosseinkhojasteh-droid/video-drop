# PROGRESS — task ledger (update after every substantial step)

| Phase | Task | Status | Evidence |
|---|---|---|---|
| 0 | Environment audit | DONE 2026-10-15 | reports/00_environment_audit.md |
| 1 | Project structure, CLAUDE.md, setup script | DONE | CLAUDE.md, scripts/setup_env.sh |
| 2 | Inventory 21 references (hash, format, decode) | DONE | reports/01_asset_inventory.csv, scripts/inventory.py |
| 3 | Analysis pipeline v2 (tempo comb + LS grid, kick-phase downbeat, 16-step drum occupancy + microtiming, swing, per-bar layers, chords/bass estimates, key w/ margin, sections, loudness, stereo) | DONE, run on 21/21 | scripts/analyze_track.py, scripts/run_all.sh, analysis/data/*.json, analysis/plots/*.png |
| 3b | Measured cards + structural maps + technical CSV | DONE | scripts/make_cards.py, analysis/structural_maps/*.csv, reports/02_audio_technical_analysis.csv |
| 4 | Track reports (21) | DONE | analysis/track_reports/*.md (scripts/build_reports.py) |
| 5 | Producer's Bible v1 (8 chapters + archetype stats) | DONE | producer_bible/ |
| 6 | Sound-library requirements / gap analysis | DONE | sound_library/requirements.md, asset_manifest.csv |
| 7 | Acquisition (free, licensed) | PARTLY DONE: 9 CC0/CC-BY/PD libraries + Surge XT, Dexed, ChowTape, Dragonfly, DPF | sound_library/asset_manifest.csv |
| 8 | Production workflow + brief template | DONE (v1) | projects/beat_briefs/TEMPLATE.md |
| 9 | Prototype: 3 concepts + Glass Jaw full arrangement v3 | DONE, awaiting the King's ear | projects/prototype_01/, quality_control/prototype_01_qc.md |
| 10 | QA + handoff | DONE (v1) | quality_control/prototype_01_qc.md, HANDOFF.md |

## Tests / failures log
- librosa onset_detect/peak_pick segfaults (numba gufunc) → replaced with scipy.signal.find_peaks. Parallel runs OK after that.
- librosa beat_track aliased Ambitionz to 118.6 BPM (4/3 of 87.3) → tempo now from comb over onset autocorrelation at 1/2/4/8/16 beats, verified.
- SFZ parser: inline `#include` inside `<group>` lines (Salamander) → includes now resolved anywhere; `*silence` pseudo-samples skipped.
- Surge XT patch loading: state applies one audio block late → warm-up render of 0.5 s after loading a patch (scripts/engine/jucestate.py).
- Engine smoke test: 4 bars, Virtuosity kit via SP-1200 emulation + Salamander piano + Surge "Sub 1" bass → -10.06 LUFS, -1.01 dBTP, 10.8 s render.
- Growlybass SFZ sounds one octave below the written key (pYIN measured) → SFZ(key_offset=12).
- VSCO-2-CE file names are one octave low for strings/brass (pYIN: +12.0 st), harp correct → FolderSampler(name_offset=12).
- Concepts v0 had 91–98 % energy below 150 Hz → loudness-based auto_balance (render.auto_balance) fixed it (65–84 %).
- Salamander piano side−mid −1.6 dB (very wide) → dsp.width(0.4).

## 2026-10-16 — the King's verdict & v4
- Scores: A 7/20, B 10/20 (only pass), C 0 (no soul), Glass Jaw v3: soul but weak, low end muffled.
- Glass Jaw v4 built from a written story (projects/prototype_01/glass_jaw_v4.py, quality_control/glass_jaw_v4_qc.md).
- New bible chapter: producer_bible/worlds_of_the_references.md (the world each reference builds + THE LAW OF THE STORY).
- Engine lesson: never balance sub-bass stems by LUFS; use peak/band-RMS rules (kick peak = snare +1.5 dB; 808 low-band RMS = kick +1 dB).

## 2026-10-25 — v4 12/20, v5 13/20 → v6
- v5: two-hand humanised piano, natural drums, musical fills, new intro, pianist coda + tape stop. King: intro weak, some hits off-beat, outro tape-stop bad, the final piano was the best part.
- v6: one swing grid for all parts (root cause of "off-beat": 808 unswung vs swung kick), intro = the pianist theme + riff behind glass + crime teaser + GOLDEN V tag + 1/16 breath + boom; outro = one-beat stop, impact, theme returns. 68 bars, 3:03, -10.3 LUFS, -1 dBTP.
- New: scripts/engine/signature.py (GOLDEN V tag), scripts/engine/paths.py (Windows-portable plugin paths).
