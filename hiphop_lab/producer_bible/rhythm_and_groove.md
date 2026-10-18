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
