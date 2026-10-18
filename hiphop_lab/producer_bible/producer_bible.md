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
