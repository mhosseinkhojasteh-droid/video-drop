=== FILE: CLAUDE.md ===
# HIP-HOP PRODUCTION LAB — project rules

Owner: the King (user). Producer persona: THE GOD OF MUSIC (skill `anthropic-skills:the-god-of-music`).
Mission: an evidence-based, reusable system that produces ORIGINAL, vocal-ready hip-hop instrumentals at or above the
level of the 21 reference records in `references/raw/`. Not clones. Not fine-tuning: the "learning" is this repository.

## Read first, every session
1. `PROGRESS.md` (task ledger) → `HANDOFF.md` (exact next steps) → `reports/00_environment_audit.md`.
2. Fresh container? Run `bash scripts/setup_env.sh` (apt + pip + GitHub releases + sample-library clones). Containers are wiped.
3. Reference audio is NOT in git/Drive (copyright, size). Re-supply from the King's RARs (`H:\Youtube Next Claude\Beats for Training Music God`)
   and re-run `scripts/inventory.py` + `scripts/run_all.sh` only if `analysis/data/*.json` are missing.

## Persistence
- Cloud container = scratch. Durable copy of all text knowledge (md/csv/json/py) = Google Drive folder `HIPHOP_PRODUCTION_LAB` (see HANDOFF.md for the folder id).
- Large binaries (sample libraries, plugins) are re-fetched by `scripts/setup_env.sh`; rendered beats are delivered to the King and archived on Drive/H:.

## Evidence standard (every claim carries one tag)
- `[measured]` produced by a script in `scripts/` on the actual audio; cite the json key.
- `[documented]` public, well-known production history (producer, sample source, gear) — recalled knowledge, must be verifiable; never invented.
- `[estimate]` algorithm output with low confidence margin (keys, chords, sections) — needs the King's ear.
- `[hypothesis]` musical interpretation not yet tested.
- `[unknown]`.
The model does NOT listen. It measures. Subjective verdicts belong to the King's ear (blind A/B is the only pass gate).

## Originality rules (hard)
- Never reuse a reference's melody, riff, bassline, sample or full arrangement. Principles transfer; signatures don't.
- Every new motif is checked against the reference pitch/rhythm sequences before rendering (interval-sequence n-gram check).
- Only legally clean sources: CC0 / CC-BY (with attribution) / public domain / own synthesis. No cracked plugins, no warez packs
  (e.g. RLTS / R2R releases, tsvst.ir). No uncleared commercial samples in anything meant for release.

## Technical conventions
- Work at 48 kHz / 32-bit float; encode once at the end (WAV 24-bit master + 320 kbps MP3).
- Render chain: Python sequencer → own SFZ sampler / Surge XT / Dexed (VST3 via pedalboard) → stems → mix bus → master.
- Master targets for a vocal-ready beat: see `producer_bible/mix_preparation.md` (derived from measured references).
- Relative paths only. Never overwrite `references/raw/`.
- After each substantial step: save outputs, update `PROGRESS.md`, write next steps to `HANDOFF.md`, sync text to Drive.

=== FILE: PROGRESS.md ===
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

=== FILE: HANDOFF.md ===
# HANDOFF — exact next steps (updated 2026-10-15)

Drive home folder: HIPHOP_PRODUCTION_LAB  id=1dSnKzEuPE5CcgfK6YK1Ttg5HOYZk9zWc
Text backup on Drive: `LAB_DOCS_*.md` and `LAB_CODE_BUNDLE.txt` (all scripts; split with `=== FILE: path ===` markers).

## State
Phases 0–10 v1 done. Prototype Glass Jaw v3 delivered; waiting for the King's blind listening scores on concept A/B/C and Glass Jaw.

## Next (in order)
1. If container is fresh: restore code from Drive bundle → `bash scripts/setup_env.sh` → restore references → `bash scripts/run_all.sh` (≈40 min) → `python3 -I scripts/make_cards.py && python3 -I scripts/build_reports.py`.
2. Apply the King's verdict. Default plan: Glass Jaw v4 = (a) sampled hats/claps + MPC60 drum colour, (b) hook lift with VSCO F-horn staccato on motif accents and +3 dB strings, (c) MIDI export of all parts (mido) for FL Studio.
3. Develop concept A (West Coast) into a full song; fix concept C low end (heavier kick, sub at −1 LU) and develop.
4. Library gaps: Persian instruments (needs the King's licensed samples or freesound.org allowed in network settings), choir, koto/erhu.
5. Persistence upgrade: the King creates an empty private GitHub repo → attach with push access → push the whole lab (incl. renders via LFS).

=== FILE: reports/00_environment_audit.md ===
# 00 — Environment & asset audit (2026-10-15)

## Execution environment [measured]
- Claude Code cloud container, Linux x86-64, 4 vCPU, 15 GB RAM, Python 3.13, Node 22. Ephemeral: wiped after inactivity.
- Disk: ~30 GB writable allowance at start.
- Desktop Commander MCP is connected but runs **inside this same Linux container** (platform linux, no allowed dirs) —
  it gives NO access to the King's Windows PC (H:\ drive, FL Studio, Chrome).
- Google Drive MCP connected to the King's account (m.hosseinkhojasteh@gmail.com). Text upload works; large binaries via MCP are impractical (base64 through the model).

## Network [measured]
- Allowed: apt (Ubuntu archive), PyPI, GitHub (git clone of public repos, raw.githubusercontent.com, release downloads).
- Blocked by the environment policy: archive.org, freesound.org, 99sounds.org, versilian-studios.com, philharmonia.co.uk,
  musical-artifacts.com, huggingface.co, dl.fbaipublicfiles.com (Demucs weights), tsvst.ir.
  The King can widen this in the cloud environment settings → Network access (Allowed domains).

## Reference dataset [measured — see reports/01_asset_inventory.csv]
21 readable MP3 files, 0 decode errors, 0 duplicates. 19 at 320 kbps; **Shook Ones Pt II and Survival of the Fittest are 128 kbps**
(spectrum above ~16 kHz unusable for those two). Sample rates 44.1/48 kHz, all stereo.
Expected from the King's list but NOT supplied: Gang Starr – Mass Appeal, Common – The Light (with hook).
Extra vs. the ChatGPT list: Mobb Deep – Burn. "50 Cent – In Da Club" filename lacks "instrumental" (vocal presence unverified).

## Tools [measured: installed and tested in this session]
| Need | Tool | Status |
|---|---|---|
| decode / inspect | ffmpeg, ffprobe, sox | OK |
| analysis | librosa 0.11, scipy, pyloudnorm, numpy | OK (librosa `onset_detect`/`peak_pick` segfaults under numba → replaced by scipy `find_peaks`) |
| time-stretch / pitch | rubberband-cli, pedalboard | OK |
| MIDI | mido, pretty_midi | OK |
| synthesis (VST3, headless) | Surge XT 1.3.4, Dexed 1.0.1 (DX7), DPF Kars/Nekobi | OK, render via pedalboard |
| effects (VST3) | CHOWTapeModel 2.11.4, Dragonfly Room/Plate/Hall/ER, MVerb, DPF 3BandEQ, Soul Force | OK |
| GM/drum soundfonts | FluidR3 GM, AVL drumkits (Black Pearl, Red Zeppelin, Blonde Bop, Buskman's) | OK |
| stem separation | — | NOT available (model weights hosts blocked); HPSS used for analysis only |
| DAW | — | none in cloud; FL Studio exists on the King's PC (empty) |
| direct listening | — | the model cannot hear; all "listening" is measurement + the King's ear |

=== FILE: producer_bible/arrangement_principles.md ===
# Arrangement principles [from analysis/structural_maps/*.csv]

## Measured facts
- Bars before drums + low end enter: 1 (8 refs), 2–3 (5), 5 (5: Next Episode, Still D.R.E., Lean Back, Shook Ones, + Ambitionz@3), 7 (Survival), 17 (Blueprint²), 24 (BDKMV, = 12 half-time bars). [measured]
- Long loops: Seen It All 66 bars unchanged, Burn 94, God Body 62, Poppin' 94, Still D.R.E. 99. [measured]
- Single-bar full drop-outs mark sections: Ambitionz 19/55/91 (36-bar period), Nas Is Like 28/82, Ice Cream 47/68–69/83. [measured]
- 8-bar riff blocks: Why We Thugs riff-on at 5–12, 29–36, 53–60, 77–84 (24-bar cycle = 16 verse + 8 hook). [measured; function = hypothesis]
- Every-4th-bar variation: Candy Shop (melody+/hats+ alternating every 4 bars), Next Episode (riff rests on every 4th bar from b38), Lean Back (bass rest every 4 bars). [measured]
- 2-bar call/response inside the loop: Classic, Survival, Still D.R.E. [measured]

## Template A — street/club (G-Unit, West Coast)
`intro 4 (riff, no drums or filtered drums)` → `hook 8` → `verse 16` → `hook 8` → `verse 16` → `hook 8` → `verse 16` → `hook 8` → `outro 4–8`
- Verse = drums + bass + reduced riff (or riff off); Hook = full riff + extra layer.
- Bar 1 of each section: one-bar drop (no kick/bass) or a fill on the bar before.
- Every 4th bar: a fill, a hat roll, a reversed cymbal, or the riff resting.

## Template B — boom-bap / Premier / Wu
`intro 4–8 (sample alone, or drums with filtered sample)` → `verse 16` → `hook 8 (scratch/cut hook or chant)` → × 3 → `outro 4–8`
- One 2-bar loop all song; the hook changes texture (cuts, filtered sample, extra hat density), not the chords.
- One-bar full stop before each hook.

## Template C — soulful / half-time
`intro 8–16 (no drums)` → `verse 16` → `hook 8` → `breakdown 8 (drums out)` → `verse 16` → `hook 8` → `outro`

## Rules
1. Never a bar of nothing between the first and last vocal bar (except deliberate one-bar stops on section boundaries).
2. Section lengths are multiples of 4; verses 16; hooks 8.
3. Change by subtraction first; add at most one element per section.
4. The motif must have a rest or a long note somewhere in its 2–4 bars — the MC's breathing slot.

=== FILE: producer_bible/common_failure_modes.md ===
# Common failure modes (automatic rejection)

1. Motif too busy — no rest for the MC. (Every reference motif has a rest or a held note.)
2. Kick and bass fighting in 40–120 Hz (two subs at once).
3. Mids filled with sustained pads → vocal masking.
4. Wide stereo low end; phase-smeared sub.
5. Over-swing on the snare (swing belongs to hats).
6. Adding layers per section instead of subtracting.
7. Dead bars / silent intro longer than the archetype allows (except soulful archetype).
8. Too clean for boom-bap (no 12-bit/tape colour) or too gritty for Storch club.
9. Loudness by crushing (crest < 10 dB).
10. Accidental copying: a motif whose interval sequence matches a reference riff — run the originality check.
11. Quantised-to-death drums (no micro-timing) — references show +10…+35 ms lazy snares and late hats.
12. Mistaking analysis estimates (keys/chords) for ground truth.

=== FILE: producer_bible/melody_harmony_and_texture.md ===
# Melody, harmony & texture [chroma/bass estimates — need the King's ear for confirmation]

## Emotion engines found in the references
| Engine | Where | Recipe |
|---|---|---|
| ♭2 / Phrygian semitone over a pedal | Ambitionz, Survival, God Body, Candy Shop, Lean Back | tonic pedal in the bass; melody leans on the ♭2 and resolves down; minor 3rd + ♭6 for darkness |
| Jazz dissonance chopped short | N.Y. State of Mind, Shook Ones | dim7 / 7♭9 / m(maj7) voicings as 1/8–1/4-note stabs, high register, sparse |
| Minor i ↔ relative major | Next Episode | 2 chords, 1 bar each, riff rests in bar 4 |
| Extended G-funk chords | G Thang | m7/maj7/9 voicings, funk bass walking roots, portamento lead answering |
| Staccato chord riff | Still D.R.E., Poppin' | 2-bar riff of short chords; rests between hits create the groove |
| Chromatic descending bass under minor i–iv | Poppin' Them Thangs | bass F#–F–E / F#–E♭–B style chromatic walk |
| Dominant-7 chain without resolution | Burn, Ice Cream | V7 of V7 colours, never landing |
| Open fifths + pedal | Triumph | no 3rds = martial/ancient; strings/horns in octaves |
| Maj7 I–IV dream | BDKMV, Blueprint² | maj7 voicings, suspended, long sustains |

## Motif rules
- Length 1–2 bars, repeated; at most 5–7 distinct notes; one rhythmic hook (syncopation on the "a" of 2 or the "&" of 4 is common).
- Range kept above 400 Hz or below 200 Hz during verses so it doesn't sit on the vocal formants (300 Hz–3 kHz) — or make it staccato.
- The motif contains a rest or a held note ≥ 1 beat.

## Texture / sound families
- West Coast: Rhodes/FM e-piano (Dexed), piano (Salamander), Moog-style lead (Surge), funk bass (Growlybass/Surge), strings (VSCO2).
- Storch club: piano/keys stabs, exotic lead (Surge plucks/strings, later Persian instruments), 808 sub (own synth).
- Boom-bap: "sampled record" chain = keys/strings/horns → tape (CHOWTape) → 12-bit (SP-1200) → filter; upright bass (Meatbass).
- Wu/mafioso: VSCO2 strings/brass/timpani in octaves, mono, gritty.

## Our edge (not in any reference)
Persian modal colour (Shur / Homayoun / Segah's quarter-tones) maps naturally onto the ♭2 engine above. Needs licensed Persian instrument samples (santur, tar, kamancheh, ney) — currently missing from the library (see sound_library/requirements.md).

=== FILE: producer_bible/mix_preparation.md ===
# Mix & master preparation [measured targets]

| Metric | References (min / median / max) | Our beat delivery target |
|---|---|---|
| Integrated LUFS | −19.8 / −11.4 / −8.0 | −10.0 ± 0.5 (beat-only, leaves room for the vocal mix) |
| Crest (peak/RMS, mono) | 10.7 / 13.5 / 19.3 dB | ≥ 11 dB |
| True peak | rips clip at 0 dBFS | ≤ −1.0 dBTP (4× oversampled limiter) |
| Energy ≤150 Hz | 31 / 74 / 87 % | 65–80 % (archetype dependent) |
| Side−mid | −72 / −19 / −6 dB | −15…−22 dB overall, < −30 dB below 150 Hz |
| Spectral centroid | 1.0–3.8 kHz (median ~2.1 kHz) | 1.6–2.4 kHz |

## Chain (scripts/engine)
1. Stems at 48 kHz float. Per-stem: HPF everything except kick/bass at 100–150 Hz; drums through vintage() emulation where the archetype needs grit.
2. One shared room/plate (Dragonfly or pedalboard Reverb) on a send, HPF 250 Hz on the return.
3. Bus: gentle glue (2:1, 30 ms attack), optional CHOWTape for "record" colour.
4. Master: soft clip (tanh, thr 0.89) → 4× true-peak limiter −1 dBTP → loudness iterate to target.
5. QC: LUFS, crest, true peak, mono compatibility (L+R correlation), spectrum vs. archetype table.

=== FILE: producer_bible/producer_bible.md ===
# THE PRODUCER'S BIBLE — v1 (2026-10-15)

Built from 21 measured reference instrumentals (`analysis/track_reports/`, `reports/02_audio_technical_analysis.csv`,
`producer_bible/archetype_stats.json`). Tags: [measured] · [documented] · [estimate] · [hypothesis]. The model measures; the King's ear judges.

## 0. The seven laws that every reference obeys [measured across 21/21 unless stated]

1. **Tempo lane 81–100 BPM** (median 93.4); the one exception (Kendrick, 134) is a 67 BPM half-time feel. Our default lane: 84–98.
2. **The low end owns the record.** Median 74 % of energy ≤150 Hz (range 31–87 %). The mids (250 Hz–2 kHz) are kept thin — that is where the rapper lives.
   The only mid-forward record (Poppin' Them Thangs, 31 %) compensates with very short, percussive piano hits.
3. **One loop, many bars.** Median harmonic loop = 2 bars; most records run one loop for 60–120 bars. Arrangement is done by **subtraction**
   (drop the bass, drop the drums, mute the riff) rather than by adding new parts.
4. **Section markers are single-bar drop-outs** (Ambitionz b19/55/91, Nas Is Like b28/82, Ice Cream b47/68/83): the beat stops, the MC enters alone, the drums return on bar 2.
5. **Swing lives in the hats, not the kick.** Median 16th swing 62.5 % (straight = 50, triplet = 66.7); boom-bap/Premier sits at 69–74 %, West Coast ~57–61 %, G-Unit/Storch often straight-to-light or triplet bounce (In Da Club 66 %).
6. **Narrow image.** Median side−mid −19 dB; 90s NY/Wu records are effectively mono (Triumph −72 dB, Ice Cream −40 dB). Width is never the source of impact.
7. **Loud but breathing.** Modern masters −8 to −10 LUFS with 10.5–13 dB crest; 90s records −11 to −16 LUFS. Our delivery target for a vocal-ready beat: **−10 ± 0.5 LUFS, crest ≥ 11 dB, ≤ −1 dBTP** (leaves headroom for the vocal mix; final song master goes to −8…−9).

## 1. Archetypes (measured ranges: min / median / max)

| Archetype | refs | BPM | swing16 % | ≤150 Hz % | LUFS | identity engine |
|---|---|---|---|---|---|---|
| West Coast / G-funk / 2001 | G Thang, Next Episode, Still D.R.E., Ambitionz | 87–94–95 | 57–61–73 | 61–66–82 | −20…−9 | extended chords or a 2-bar staccato riff; funk bass; portamento lead used sparingly; 4-bar intro before drums |
| G-Unit / Storch street-club | In Da Club, Candy Shop, Poppin', Lean Back, Why We Thugs | 88–95–99 | 35–45–66 | 31–74–85 | −15…−8 | one hook riff (often ♭2/Phrygian colour), huge sub, sparse kick, 8-bar riff blocks, every-4th-bar ear candy |
| DJ Premier NY boom-bap | NY State of Mind, Nas Is Like, Classic, Seen It All | 84–93–100 | 40–71–74 | 65–72–80 | −15…−8.5 | 2-bar chop as call/response; jazz dissonance; heavy late hats; one-bar stops; near-mono |
| Gritty underground (Mobb) | Shook Ones II, Survival, Burn | 94–95–96 | ~59 | 78–81–87 | −12…−9 | tiny dissonant high loop or ♭II-over-root sample, busy kick, cold sub, 5–7-bar teasing intro |
| Wu-Tang / martial-cinematic | Triumph, Ice Cream, God Body | 81–90–91 | 60–64–66 | 69–71–79 | −16…−8.6 | mono, drums louder than sample (+9 dB on Ice Cream), open fifths / ♭2 dissonance, marching kicks, orchestral intro statement |
| Soulful / laid-back | BDKMV, Blueprint² | 67(½)–90 | 47–72 | 50–84 | −16…−13 | maj7 harmony, long drumless intros (16–22 bars), half-time space, dynamic masters (crest 16–17 dB) |
| Dark mafioso (cross-cuts) | Seen It All, Ice Cream, Burn, Survival | 90–96 | 59–72 | 70–87 | −13…−9 | minor i–♭VII or dominant-7 chains without resolution, no brightness, heavy swing |

Detail: `archetype_matrix.csv`, `rhythm_and_groove.md`, `melody_harmony_and_texture.md`, `arrangement_principles.md`, `vocal_space_and_arrangement.md`, `mix_preparation.md`, `common_failure_modes.md`.

## 2. What creates the emotion (the "soul") — hypotheses grounded in measurements
- **Menace / dread** = a semitone (♭2) rubbing against a pedal tone (Ambitionz F#-G-G#, Survival F over E, God Body D/E♭, Candy Shop G over F#, Lean Back A over G#). Five of 21 records use it. [measured chroma; emotion = hypothesis]
- **Noir / tension** = jazz dissonance (dim, 7♭9) chopped into short stabs + heavy late hats (NY State of Mind).
- **Swagger / cool** = minor i ↔ relative major alternation (Next Episode) or a static riff with a built-in rest (the punchline slot).
- **Triumph / ceremony** = open fifths and marching quarter-note kicks (Triumph), or a bright 2-bar call/response chop (Classic).
- **Calm confidence / vibe** = maj7 I–IV harmony, half-time, long drumless intros (BDKMV, Blueprint²).
- **Bounce** = straight kick + near-triplet hats (In Da Club 66 %).

## 3. Our production doctrine (how the factory works)
1. **Motif first.** No drums until a 1–2-bar motif exists that is singable after one hearing and has a rest (a hole for the MC).
2. **Pick the emotion engine** from §2 before choosing sounds.
3. **Drums second, swing set per archetype** (rhythm_and_groove.md), kick/bass lane ownership decided (one owns 40–60 Hz, the other 60–120 Hz).
4. **Arrange by subtraction** on the measured templates (arrangement_principles.md): 4–8-bar intro, 16-bar verses, 8-bar hooks, single-bar drop-outs at section starts, a change every 4th bar.
5. **Mix for the absent vocal** (vocal_space_and_arrangement.md): carve 250 Hz–4 kHz under verses, keep the image narrow, master to −10 LUFS.
6. **Originality gate** before render: motif interval/rhythm n-grams must not match the reference motifs; no reference samples.
7. **The King's blind A/B is the only pass.**

=== FILE: producer_bible/rhythm_and_groove.md ===
# Rhythm & groove [measured: drum_grid_16, drum_microtiming_ms_16, swing_pct_16th]

## Tempo
- 21 refs: 81–100 BPM, median 93.4 (Kendrick 134 = 67 half-time). Exact grids (Classic 99.993, Blueprint² 89.996) = drum machine; others 0.01–0.6 % off integer = sampled/live loops at non-round tempos.
- Default: West Coast 92–95, G-Unit 88–98, Premier 84–96, Mobb 94–96, Wu 81–91, soulful 67–90.

## Swing (16th off-beat delay, 50 = straight, 66.7 = triplet)
- Premier/NY: 69–74 % (very late hats; MPC-60/SP-1200 swing 66–75 settings).
- West Coast: 57–61 % (light); Still D.R.E. 73 % (late hats on straight 8ths).
- Wu: 60–66 %. In Da Club 66 % (bounce). Storch records often near-straight.
- Implementation: `Song(swing=...)` delays odd 16ths; per-track override (keys straight, hats swung) via `Track(swing=...)`.

## Kick / snare / hat archetypes (whole-track occupancy; X strong x present)
```
West Coast (Still D.R.E.)   K x....X..X...X...  S x.x.X.x.X.x.X.x.   (snare/clap 2&4 + ghosts)
Storch club (Lean Back)     K X.........X.....  S ..X.X..x.x..X...   (two kicks a bar is enough)
Premier (NYSOM)             K X.xxx....xX.x..X  S X.x.X...xX..X.x.   (chopped break)
Mobb (Shook Ones)           K x.x.xXX.x.X.xxX.  S x.X.x...X.X.x.x.   (busy kick)
Wu (Triumph)                K X.X.X.X.X...x...  S x.x.X.x.x.x.X.x.   (marching)
```
(occupancy blends all sections; use as tendency, not as a pattern to copy)

## Micro-timing (median per step, ms; + = late vs. kick grid)
- Snare on 2/4 typically +10…+35 ms behind the kick-derived grid on sampled records (Ambitionz +15…+30) → snares are lazy.
- Hats +17…+30 ms on off-8ths in swung records.
- Our engine defaults: kick 0 ms, snare +12 ms, hats swing per archetype ± 4 ms humanize, velocity jitter ±6.

## Rules
1. Kick and bass never fight: either the kick owns 40–60 Hz and the bass sits 60–120 Hz, or the 808 *is* the bass (kick = short click + 808 tail).
2. The snare is the loudest transient after the kick; claps layered for West Coast/Storch.
3. Ghost notes only in boom-bap/West Coast, never in sparse Storch-club patterns.
4. Swing the hats, not the snare.

=== FILE: producer_bible/vocal_space_and_arrangement.md ===
# Vocal space [measured spectra + hypotheses]

- References keep 250 Hz–2 kHz at only ~4–16 % of total energy [measured]; the vocal's fundamental (100–250 Hz male) and formants (300 Hz–3 kHz) are left mostly free.
- Verse vs. hook: the melodic layer is reduced or removed under verses (In Da Club, Why We Thugs, Next Episode) [measured timelines].
- Width: narrow beds (median side−mid −19 dB) keep the centre for the vocal; ambience lives in the sides above 250 Hz.
- The motif's rests are the MC's punchline slots (Next Episode bar 4).

## Engine rules for a vocal-ready beat
1. Under verses: −2…−4 dB dynamic dip 800 Hz–3 kHz on melodic stems (or a verse arrangement without the lead).
2. No sustained instrument with a fundamental between 150 and 400 Hz during verses unless staccato.
3. Keep the sub/kick mono below 150 Hz.
4. Provide a "verse" and a "hook" version of the riff in every beat (stems delivered separately).
5. Deliver stems: drums, bass, keys/melody, extras, FX — so the King's vocal chain (God of Vocals) can duck what it needs.

=== FILE: sound_library/requirements.md ===
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

=== FILE: quality_control/prototype_01_qc.md ===
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

=== FILE: projects/beat_briefs/TEMPLATE.md ===
# Beat brief — <title>
- Archetype (producer_bible/archetype_matrix.csv):
- Emotion engine (producer_bible.md §2):
- One-sentence soul:
- BPM / swing (hats) / key-mode:
- Motif (1–2 bars, notes + rhythm, where is the rest?):
- Drum architecture (kick/snare/hat 16-step + micro-timing):
- Bass strategy (808 vs bass guitar vs upright; who owns 40–60 Hz):
- Sound palette (library assets by manifest name):
- Form (arrangement_principles.md template) + where the drop-outs are:
- Vocal space plan (what thins under verses):
- Targets: LUFS −10…−11, crest ≥ 11, ≤150 Hz %, side−mid, centroid (archetype row of archetype_stats.json)
- Originality: what reference signature is this closest to, and why it is not a copy:
- Render: script path; QC: analyze_track.py on the export, compare with the archetype range.

