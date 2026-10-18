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
