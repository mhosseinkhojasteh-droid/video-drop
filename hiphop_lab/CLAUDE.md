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
