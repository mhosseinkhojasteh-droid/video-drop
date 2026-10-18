"""Phase 4: assemble analysis/track_reports/<track>.md = interpretation (below) + measured card (make_cards.py).

Tags: [measured] script output · [documented] public production history (recalled, verifiable) ·
[estimate] low-confidence algorithm output · [hypothesis] musical interpretation not yet confirmed by ear · [unknown].
The model has not listened to these records; every "sounds like" statement is a hypothesis for the King's ear.
"""
import os, glob

R = {}

R['Ice_Cube_Why_We_Thugs_Instrumental'] = dict(
    title="Ice Cube — Why We Thugs (2006)", archetype="G-Unit/Storch-era street-club · West Coast attitude",
    documented="Produced by Scott Storch [documented]. Laugh Now, Cry Later era.",
    identity="Hard, bright, loop-driven street anthem. Constant energy (LUFS spread tiny), dense low end (77 % ≤150 Hz) [measured]. Emotion: defiance, swagger [hypothesis].",
    groove="99.0 BPM, very stable grid; kick on 1 and around beat 3 region with snare on 2 & 4 [measured]. Hats sparse in occupancy → the rhythmic drive is carried by the melodic synth riff, not by a busy hat [hypothesis from occupancy + melody+ bars].",
    harmony="Two-chord pendulum in the A–B–C area (chroma alternates A-minor-ish / B-ish every half bar) [estimate]. Storch signature: a single repeated synth/keys hook carrying the whole tension.",
    structure="Arrangement by 8-bar 'melody+' blocks: bars 5–12, 29–36, 53–60, 77–84 add a melodic layer (hook sections) on a 24-bar cycle (16 verse + 8 hook) [measured timeline; section function = hypothesis].",
    vocal="Mids are left open in verses (melody layer drops out), which is where the rapper sits; hooks add the lead synth [hypothesis].",
    principles=["One unforgettable riff + constant drums; arrangement = adding/removing that riff in 8-bar blocks.", "Keep a 24-bar verse+hook cycle with no dead bars.", "Loud but not crushed: −9.4 LUFS with 11 dB crest."],
    dont=["The riff's exact interval/rhythm sequence", "Its specific synth timbre combination"],
    unknown=["Exact instrument identities", "Whether the hook layer is strings, synth brass or keys"])

R['2pac_-_Ambitionz_Az_a_Ridah_Instrumental_HD_Quality'] = dict(
    title="2Pac — Ambitionz Az a Ridah (1996)", archetype="West Coast · dark G-funk-adjacent, ominous",
    documented="Produced by Daz Dillinger [documented]. All Eyez on Me.",
    identity="Ominous, menacing West Coast. Chromatic pitch cluster (F#–G–G# all near max in the pitch-class profile and the bass profile) [measured] → a semitone-rubbing motif that creates dread [hypothesis].",
    groove="87.3 BPM (tracker aliased to 118.6 = 4/3; corrected by comb) [measured]. Moderate swing 56.9 % with hats ~18–24 ms late on off-beats [measured] — laid-back West Coast pocket.",
    harmony="Static tonal centre around G with chromatic neighbour tones (G–G#–F#) rather than chord changes [estimate]. Tension from half-steps, not from progressions.",
    structure="Intro 2 bars without drums/low end; then the loop runs with single-bar full drop-outs (drums+hats removed) at bars 19, 55, 91 — a 36-bar period [measured] that marks section starts.",
    vocal="Very low mid energy (250 Hz–2 kHz ≈ 4 %) [measured] → huge vocal space; the beat lives in sub-bass and top.",
    principles=["Dread from semitone motion over a pedal tone.", "Single-bar total drop-out as the section marker (the MC enters alone).", "87 BPM + light swing = menace without rush."],
    dont=["The specific chromatic synth line and its rhythm"],
    unknown=["Synth source", "Exact bar/section functions (no vocal reference)"])

R['50_Cent_-_Candy_Shop_instrumental'] = dict(
    title="50 Cent — Candy Shop (2005)", archetype="G-Unit/Storch club · exotic-minor seduction",
    documented="Produced by Scott Storch [documented]. The Massacre; features Olivia.",
    identity="Seductive, exotic, minimal club record. 85 % of energy ≤150 Hz [measured] — the sub owns it; the melodic hook is sparse and modal.",
    groove="98.0 BPM [measured]. Hat occupancy concentrated on beat 2 and 3-and (sparse) [measured]; a call-and-response between hook stabs and sub hits [hypothesis].",
    harmony="F#-minor centre with the G (flat-2) prominent: bars alternate G-ish / F#-ish (Gmaj7/F#5 sketches) [estimate] → Phrygian colour (♭2 over the tonic) = the 'Middle-Eastern' flavour [hypothesis consistent with chroma].",
    structure="4-bar cycle of variation: 'melody+' and 'hats+' bars recur every 4 bars (b9, 13, 33, 37, 41…; hats+ b6, 10, 14…) [measured] → ear-candy every 4th bar keeps a static loop alive.",
    vocal="Mid band nearly empty [measured] → vocals and the female hook sit on top.",
    principles=["Phrygian ♭2 against the tonic = instant exotic tension (and a Persian-friendly scale).", "Change something every 4th bar (fill, extra hat, hook stab) without changing the loop.", "Let the sub carry the groove; the melody only punctuates."],
    dont=["The Candy Shop hook motif and its rhythmic placement"],
    unknown=["Exact instrument (synth vs. sampled ethnic instrument)"])

R['50_Cent_-_In_Da_Club'] = dict(
    title="50 Cent — In Da Club (2003)", archetype="G-Unit/Dre club anthem",
    documented="Produced by Dr. Dre with Mike Elizondo [documented]. Filename has no 'instrumental' → vocal presence NOT verified [unknown].",
    identity="Sparse, bouncy, confident. Dynamic for a club record (−14.7 LUFS, crest 15.6 dB) [measured] — this rip is quieter than the others; don't copy its loudness.",
    groove="89.9 BPM, hat swing ≈ 66 % (near triplet) [measured] → the famous bounce. Kick pattern dense around beat 1 and 2-and/3 [measured].",
    harmony="C#-minor-ish centre, chroma moves D#–E–D around C# (bass E-D-C# walk) [estimate]; strings/keys stab figure.",
    structure="Melody layer absent bars 1–5 and 15–21, 43–45, 51–53 [measured] → the hook instrumentation is switched off under verses — classic Dre subtraction arrangement.",
    vocal="Vocal space created by removing the melodic stab in verses [hypothesis from timeline].",
    principles=["Near-triplet hat swing (≈66 %) over straight kicks = bounce.", "Dre subtraction: same drums all song, melodic layer on/off defines verse vs hook.", "Few elements, each with its own frequency lane."],
    dont=["The In Da Club string/synth stab figure and kick pattern combination"],
    unknown=["Whether vocals are present in this file", "Section labels"])

R['DJ_Premier_-_Classic_(instrumental)'] = dict(
    title="DJ Premier — Classic (2007, Nike Air Force 1 anniversary)", archetype="NY boom-bap (Premier)",
    documented="Produced by DJ Premier for Rakim, Nas, KRS-One and Kanye West [documented].",
    identity="Triumphant, ceremonial boom-bap. Loudest reference (−8.5 LUFS, crest 10.7) [measured] — a modern Premier master.",
    groove="99.99 BPM — drum-machine exact [measured]. Hats and melody alternate in a strict 2-bar call/response (bars even: hats+ melody+) [measured] → the classic Premier 2-bar chop.",
    harmony="Minor-7 colour around B/F# (Bm7 ↔ F#maj7 alternation) [estimate] — chopped sample phrase.",
    structure="Strict 2-bar alternation all the way (b3 full, b4 hats+melody+, …) [measured] — the arrangement is the chop itself.",
    vocal="Mid band relatively busy (centroid higher) but the 2-bar call/response leaves 'answer' gaps for the rapper [hypothesis].",
    principles=["The 2-bar chop: bar A states, bar B answers — the loop is a conversation.", "Machine-tight tempo, swing lives in the chop placement.", "Modern Premier masters are loud (−8.5 LUFS) yet keep ~10.7 dB crest."],
    dont=["The specific sample phrase / chop points"],
    unknown=["Original sample source"])

R['DJ_Premier_-_Seen_it_All_(instrumental)'] = dict(
    title="'Seen It All' (instrumental, attributed to DJ Premier in the filename)", archetype="Dark mafioso / NY boom-bap",
    documented="[unknown] — record identity/credits not verified; the filename says DJ Premier.",
    identity="Dark, mafioso, steady (no drop-outs in 66 bars) [measured]. C#-minor centre with m7 colour; 80 % ≤150 Hz [measured].",
    groove="91.96 BPM, strong swing (72 % — beyond triplet, i.e. very late off-beat 16ths/hats) [measured; estimate of feel] → heavy laid-back walk.",
    harmony="C#m7 ↔ E / C#5 alternation; bass C#–B–B–B then C#–C#–G#–C# [estimate] → minor 2-bar loop with a descending whole-step in the bass (C#→B).",
    structure="One continuous loop, no measured drop-outs until the end [measured] → arrangement presumably done by the vocal and subtle filtering [hypothesis].",
    vocal="Dark low-mid weighted bed; rapper sits above [hypothesis].",
    principles=["Mafioso darkness = minor i–♭VII bass motion + heavy swing + no brightness.", "A loop can run 60+ bars if its internal 2-bar phrase has tension and release."],
    dont=["The specific chop/sample"],
    unknown=["Producer, sample, year"])

R['Dr._Dre_-_Nuthin_But_A_G_Thang_(INSTRUMENTAL)'] = dict(
    title="Dr. Dre — Nuthin' but a 'G' Thang (1992)", archetype="West Coast G-funk (canonical)",
    documented="Produced by Dr. Dre; built on Leon Haywood 'I Want'a Do Something Freaky to You' (interpolated/sampled) [documented]. The Chronic.",
    identity="Relaxed, sunny, funky. Very dynamic (crest 19.3 dB, −19.8 LUFS) [measured] — 1992 mastering, quieter era.",
    groove="94.7 BPM, swing ≈ 60.6 % [measured] → loose funk pocket. Snare on 2 & 4 clean; hats on 8ths [measured].",
    harmony="Major-7/minor-7 movement around B/F#/C (Bm7–Fmaj7 style alternation) [estimate] — soulful extended chords typical of G-funk.",
    structure="Bars 51–54 and 63–70 alternate NO-LOW / low-thin [measured] → bass removed on alternating bars = a breakdown device. 'melody+' blocks at 27–30, 43–50, 59–62, 79–94 [measured] (G-funk lead / keys entries) [hypothesis].",
    vocal="Mid-heavy for G-funk (64 % low) — keys and lead share the vocal range, so the lead plays only between/after lines [hypothesis].",
    principles=["G-funk = extended chords (m7/maj7/9) + funk bass + whiny portamento lead used sparingly.", "Breakdown by removing the bass on alternate bars.", "Swing ~60 %: loose but not triplet."],
    dont=["The Leon Haywood-derived progression + bass line", "The lead melody"],
    unknown=["Exact chord qualities (needs transcription)"])

R['Dr._Dre_-_The_Next_Episode_(Instrumental)'] = dict(
    title="Dr. Dre — The Next Episode (1999)", archetype="West Coast 2001-era (cinematic G-funk)",
    documented="Produced by Dr. Dre with Mel-Man; based on David McCallum's 'The Edge' [documented].",
    identity="Cinematic, cocky, iconic guitar/bass figure. Intro bars 1–4 without drums (melody only) [measured].",
    groove="95.4 BPM; kick on 1 with a dense 8th-ish kick pattern later in the bar [measured]; swing value not computed (insufficient off-beat hat onsets) [measured].",
    harmony="D#/B power-chord bars then D#m7 ↔ F#maj7 alternation [estimate] — minor i ↔ relative major motion.",
    structure="Intro 4 bars (no drums) → drums at bar 5; bars 29–32 drop drums again (break) [measured]; then every 4th bar 'melody-off' (b38, 42, 46…) [measured] → the riff rests on bar 4 of every 4-bar phrase, leaving a hole for the rapper's punchline.",
    vocal="The 4-bar riff with a built-in rest bar = a punchline slot [hypothesis].",
    principles=["Build the riff with a rest in bar 4 — the beat 'breathes' for the punchline.", "Drums-out break mid-song (4 bars) resets attention.", "Minor i ↔ relative major alternation = cool tension."],
    dont=["The McCallum-derived riff", "The exact bass/guitar figure"],
    unknown=["Instrumentation split (guitar vs. bass vs. keys)"])

R['Dr_Dre-_Still_Dre_instrumental'] = dict(
    title="Dr. Dre — Still D.R.E. (1999)", archetype="West Coast 2001-era (piano-led)",
    documented="Produced by Dr. Dre and Mel-Man; the piano riff played by Scott Storch [documented].",
    identity="Iconic, regal, minimal. Piano-only intro bars 1–3 (hats −42 dB → −29 dB at bar 5) [measured]. 105 bars with essentially no arrangement changes [measured] — the riff carries the whole record.",
    groove="93.43 BPM; snare 2 & 4; strong late off-beats (swing ≈ 72.9 % on 16ths) [measured; estimate of feel].",
    harmony="Strict 1-bar alternation of two pitch-sets (chroma flips A#/F ↔ E/A every bar) [measured on chroma plot] → a 2-bar riff of staccato piano chords.",
    structure="Intro 4 bars piano (+strings) → full from bar 5 → no changes until outro [measured].",
    vocal="Piano occupies 500 Hz–2 kHz (15.9 % — highest mid share of batch 1) but in short staccato hits, leaving gaps [measured + hypothesis].",
    principles=["A staccato chord riff with rests can fill the mids without masking vocals.", "No arrangement needed if the 2-bar riff is strong enough — minimalism as confidence.", "Piano intro before drums: 4 bars."],
    dont=["The Still D.R.E. piano riff (chord voicings + rhythm)", "Its string line"],
    unknown=["Exact voicings (needs transcription)"])

R['Fat_Joe_-_Lean_Back_(Instrumental)'] = dict(
    title="Terror Squad (Fat Joe) — Lean Back (2004)", archetype="Storch-era club · Latin/East Coast",
    documented="Produced by Scott Storch [documented].",
    identity="Swaggering, half-time-feel club groove. Intro 4 bars without drums [measured]. Bass/keys stab pattern with recurring 'low-thin' bars every 4 bars (b6, 14, 18, 22, 30…) [measured] → planned bass rests.",
    groove="95.1 BPM; kick only on 1 and 3 (X.........X.....) [measured] — extremely sparse kick; snare/claps carry the rhythm.",
    harmony="G#/D# centre with A natural colour (Amaj7 vs G# bars) [estimate] → semitone shift (♭2 colour again, Storch habit).",
    structure="4-bar intro; then a 4-bar cell where bar 2 drops the low end — the 'lean back' space [measured + hypothesis].",
    vocal="Sparse kick + bass rests = room for call-and-response chant hooks [hypothesis].",
    principles=["Two kicks per bar can be enough if the snare/clap and bass hits are syncopated.", "Planned bass rests every 4 bars create a dance 'move' moment.", "Storch ♭2 semitone colour reappears (Candy Shop, Lean Back)."],
    dont=["The Lean Back stab rhythm and melodic figure"],
    unknown=["Instrument identities"])

R['G_Unit_-_Poppin__Them_Thangs'] = dict(
    title="G-Unit — Poppin' Them Thangs (2003)", archetype="G-Unit street anthem (piano-led, aggressive)",
    documented="Produced by Scott Storch [documented, moderate confidence — verify].",
    identity="Aggressive, militant, piano-driven. Lowest low-end share of all (30.6 % ≤150 Hz) [measured] → mid-forward record: the piano/keys hit hard in the mids. Loud (−8.0 LUFS) [measured].",
    groove="88.0 BPM, swing 66 % (triplet feel) [measured]. 8th hats straight-through [measured].",
    harmony="F#-minor, bars alternate F#m ↔ Bm7 with bass F#–F–E / F#–D#–B descent [estimate] → chromatic descending bass under a minor i–iv = menace.",
    structure="Almost no layer changes (b1–94 full) [measured] → the drama is in the riff, not the arrangement.",
    vocal="Mid-forward beat → vocals must be EQ'd to cut through, or the piano must leave rhythmic gaps [hypothesis].",
    principles=["Chromatic descending bass line under i–iv minor = street menace.", "Aggression can come from mid-range piano hits instead of sub.", "Triplet-swung hats at 88 BPM."],
    dont=["The piano riff"],
    unknown=["Producer verification", "Exact piano voicings"])

R['Jay-Z_-_Blueprint_2_(Instrumental)'] = dict(
    title="Jay-Z — Blueprint² (title track, 2002)", archetype="Soulful/cinematic East Coast",
    documented="[unknown] producer not verified here.",
    identity="Reflective, grand. Long intro: bars 1–16 have no drums and no low end [measured] (sample breathing alone). Dynamic master (−15.7 LUFS, crest 17.4) [measured].",
    groove="90.0 BPM, swing ≈ 72 % [measured]. Kick pattern X...x..X..X.x..x [measured].",
    harmony="Static C-major-7 / E-bass colour for the first bars (Cmaj7 over E) [estimate] → a suspended, unresolved soul sample.",
    structure="16-bar drumless intro; then melody+ blocks of 2–4 bars alternating with full bars (b17–18, 21–26, 29–32, 49–50, 53–56, 73–74, 77–80) [measured].",
    vocal="Low-end only half the energy (50 % ≤150 Hz) → mids carry the sample; vocal competes, so the sample must duck or thin under verses [hypothesis].",
    principles=["A long drumless intro (16 bars) is legitimate when the sample has narrative weight.", "Maj7-over-3rd voicing = unresolved, reflective."],
    dont=["The sample/chop"],
    unknown=["Producer and sample source"])

R['Kendrick_Lamar_-_Bitch,_Don_t_Kill_My_Vibe_[Instrumental]'] = dict(
    title="Kendrick Lamar — Bitch, Don't Kill My Vibe (2012)", archetype="Soulful / laid-back modern West Coast",
    documented="Produced by Sounwave; sample: Boom Clap Bachelors 'Tiden Flyver' [documented, moderate confidence — verify].",
    identity="Dreamy, hazy, floating. 134.0 BPM in double-time = 67 BPM half-time feel [measured + interpretation]. Intro bars 1–22 have no drums/low end [measured].",
    groove="Kick on quarter notes in the double-time grid (X...X.x.X.x.X.x.) [measured] — reads as a half-time 67 BPM with 8th-note pulse.",
    harmony="C# major-7 centre with F#maj7 (IV) colour [estimate] → major-7 dream harmony (no minor darkness).",
    structure="Long intro (22 bars in 134-grid = 11 bars half-time); repeated big drop-outs b57–70 (14 bars, no drums/low) [measured] — breakdowns around the hook.",
    vocal="84 % ≤150 Hz but hazy top; lots of space [measured + hypothesis].",
    principles=["Half-time at ~67 BPM gives 'vibe' — space for melodic flows.", "Maj7 (I–IV) harmony = calm confidence instead of menace.", "Long drumless passages as emotional reset."],
    dont=["The Tiden Flyver sample/vocal chop"],
    unknown=["Sample treatment details"])

R['Mathematics,_Method_Man,_AZ,_Wu_Tang_Clan_God_Body_INSTRUMENTA'] = dict(
    title="Mathematics feat. Method Man & AZ — God Body (Wu-Tang family)", archetype="Wu-Tang / gritty NY",
    documented="Producer Mathematics [documented as artist; production credit not verified here].",
    identity="Gritty, dense, loud (−8.6 LUFS, crest 10.8) [measured]. Runs bars 2–63 without any layer change [measured].",
    groove="81.0 BPM — slowest of the set [measured]. Swing 59.5 % [measured]. Kick syncopated off the 1 (..x.X..X..X.x.xx) [measured; downbeat phase margin should be checked].",
    harmony="D minor area with Eb (♭2) colour (D#maj7/Em7 alternation) [estimate] → semitone-shifted sample = Wu dissonance.",
    structure="Continuous loop [measured].",
    vocal="Dense bed; the vocal must be bright and forward [hypothesis].",
    principles=["81 BPM + ♭2 dissonance + grit = Wu weight.", "One loop for 60+ bars with three MCs carrying the variation."],
    dont=["The sample"],
    unknown=["Sample source", "Exact bar phase (syncopated kick)"])

R['Mobb_Deep_-_Burn_(Instrumentals)'] = dict(
    title="Mobb Deep — Burn (Infamy era, 2001)", archetype="Dark NY / mafioso",
    documented="Mobb Deep record; production credit not verified here (likely Havoc) [unknown].",
    identity="Dark, steady, heavy low end (86.7 % ≤150 Hz — highest) [measured]. No layer changes bars 1–94 [measured].",
    groove="95.6 BPM; kick X...x..xX.X.x... [measured].",
    harmony="Dominant-7 colours (G7, A7, E7) with chromatic bass A–G–D–C / F–F–D–A [estimate] → bluesy, unresolved dominant chain.",
    structure="Continuous loop, outro drop at b96 [measured].",
    vocal="Huge sub, quiet mids → vocals sit easily [hypothesis].",
    principles=["Dominant-7 chains without resolution = unease.", "When the sub carries 87 % of the energy, every other element must be thin and dark."],
    dont=["The loop"],
    unknown=["Producer, sample"])

R['Mobb_Deep_Shook_Ones,_Pt_II_Instrumental'] = dict(
    title="Mobb Deep — Shook Ones, Pt. II (1995)", archetype="Gritty underground NY (canonical)",
    documented="Produced by Havoc; contains a sped/pitched Herbie Hancock 'Jessica' piano fragment and other jazz samples [documented, moderate confidence — verify]. 128 kbps source [measured].",
    identity="Paranoid, cold, claustrophobic. G-minor, pitch profile spread (dissonant cluster) [measured/estimate].",
    groove="93.97 BPM; busy kick (x.x.xXX.x.X.xxX.) [measured] — the famous dense, stumbling kick pattern feel.",
    harmony="G-minor with a dissonant high piano figure [estimate]; Gm7/Cm7 sketches.",
    structure="Intro 6 bars: drums/low enter and leave (b1–3 none, b4–5 partial, b6 none) [measured] → teasing intro; melody-off block b37–40 [measured].",
    vocal="Mid band quiet, the high piano stab sits above the vocal range [hypothesis].",
    principles=["Dissonant, tiny, high-register loop + heavy sub = paranoia.", "Intro that teases the drums before committing.", "Kick density as aggression (busy kick, plain snare)."],
    dont=["The piano fragment / sample", "The exact kick pattern"],
    unknown=["Sample sources (verify)"])

R['Mobb_Deep_Survival_Of_The_Fittest_Instrumental'] = dict(
    title="Mobb Deep — Survival of the Fittest (1995)", archetype="Gritty underground NY",
    documented="Produced by Mobb Deep (Havoc) [documented]; jazz piano sample (reportedly Barry Harris 'Skylark') [documented, moderate confidence — verify]. 128 kbps source.",
    identity="Bleak, haunting. Intro bars 1–6 with no drums [measured]; then a strict 2-bar alternation (odd bars full, even bars melody+) [measured] — a 2-bar sample phrase where bar 2 carries the melodic tail.",
    groove="95.15 BPM; kick X.X....xX.x....x, snare on 2 & 4 [measured].",
    harmony="E/F semitone (Fmaj7 chroma over E bass) [estimate] → ♭2 over the bass = haunted.",
    structure="6-bar drumless intro, then the 2-bar call/response loop for the whole song [measured].",
    vocal="Bass pedal on E keeps the floor fixed while the sample moves above [hypothesis].",
    principles=["♭II over the root (F over E) = haunting.", "2-bar sample phrase where bar 2 'answers' — loop as a sentence.", "6-bar drumless intro for mood."],
    dont=["The piano sample"],
    unknown=["Sample verification"])

R['Nas_-_N_Y._State_Of_Mind_Instrumental'] = dict(
    title="Nas — N.Y. State of Mind (1994)", archetype="DJ Premier NY boom-bap (canonical)",
    documented="Produced by DJ Premier; samples Joe Chambers 'Mind Rain' (piano) and Donald Byrd 'Flight Time' [documented].",
    identity="Tense, nocturnal, cinematic street noir. 84.5 BPM [measured].",
    groove="84.48 BPM; swing 69 % [measured]. Kick X.xxx....xX.x..X (chopped, irregular) [measured] → Premier's syncopated, chopped-break feel.",
    harmony="F#/C# area with diminished colour (Ddim/C#7 sketches) [estimate] → dark jazz piano dissonance.",
    structure="Intro alternating low-thin/full bars (b1–5) [measured]; hats+ blocks b49–52 and b89–99 [measured] → hat density raised in later sections.",
    vocal="Mid 65 % low share; the jazz piano sits in short stabs [hypothesis].",
    principles=["Jazz dissonance (dim/7♭9) chopped into short stabs = noir.", "84 BPM + 69 % swing = heavy walking pocket.", "Raise hat density for later verses instead of adding instruments."],
    dont=["The Mind Rain piano chop", "Flight Time bass"],
    unknown=["Exact chop points"])

R['Nas_-_Nas_Is_Like_(Instrumental)_-_HQ'] = dict(
    title="Nas — Nas Is Like (1999)", archetype="DJ Premier NY boom-bap",
    documented="Produced by DJ Premier [documented]. I Am… era.",
    identity="Ceremonial, stately. Intro bars 1–8 low-thin/melody-off [measured] → 8-bar intro with the cut/scratch or thin sample before full drums.",
    groove="94.5 BPM; swing 74 % (very late hats) [measured; estimate of feel].",
    harmony="Semitone neighbour A ↔ A# / G# ↔ A alternation (Amaj7/A#7) [estimate] → Premier's chromatic chop shift.",
    structure="Full drop-outs at b28 and b82 (single bars) [measured] → classic one-bar break before a new section; melody-off b91–93 into the outro [measured].",
    vocal="Premier leaves space for scratched hooks (cuts) [documented habit; hypothesis here].",
    principles=["One-bar full stop before the hook/verse = punctuation.", "Chromatic semitone chop shift (A ↔ A#) as the 'turn' of the loop.", "8-bar intro."],
    dont=["The sample chop"],
    unknown=["Sample source"])

R['Raekwon_-_Ice_Cream_(Instrumental)_[Track_13]'] = dict(
    title="Raekwon — Ice Cream (1995)", archetype="Wu-Tang mafioso / soulful-dark",
    documented="Produced by RZA [documented]. Only Built 4 Cuban Linx… Sample attributions not verified here.",
    identity="Smooth-menacing, mafioso cool. Essentially MONO (side−mid −40 dB) [measured] — 90s Wu mixes are mono-centred; percussion 9.3 dB above harmonic content [measured] → drums dominate.",
    groove="89.6 BPM, swing 66 % (triplet) [measured]; hats 26 ms late on off-8ths [measured].",
    harmony="C#-minor area with dominant-7 colours (D#7, F#7, A7) [estimate] → soul-sample chords.",
    structure="Single/two-bar full drop-outs at b47, b68–69, b83 [measured] (section markers); many single 'melody+' bars every 4 bars [measured] → sample phrase accent on bar 4.",
    vocal="Mono, mid-quiet bed; vocals centre [hypothesis].",
    principles=["Mono-centred mix = old-school weight; width is not required for impact.", "Drums louder than the sample (+9 dB perc vs harmonic) = RZA grit.", "Drop-out bars as section markers."],
    dont=["The sample and its chop"],
    unknown=["Sample sources"])

R['Wu_Tang_Clan_-_Triumph_Instrumental'] = dict(
    title="Wu-Tang Clan — Triumph (1997)", archetype="Wu-Tang / martial-arts cinematic",
    documented="Produced by RZA [documented]. Wu-Tang Forever.",
    identity="Epic, militant, cinematic. MONO file (side−mid −72 dB) [measured]. Very dynamic (−16 LUFS, crest 14.9) [measured]. 127 bars, longest reference.",
    groove="91.0 BPM, swing 64 % [measured]. Kick on every quarter in the first half (X.X.X.X.X...) [measured] — marching.",
    harmony="Power-fifth sketches D5/G5 with a D bass pedal [estimate] → modal (no 3rds) = martial/medieval.",
    structure="Intro bars 1–8 melody+ (string/horn statement) [measured]; then long continuous verse sections with melody-off pockets (b85, 88–91, 103, 105) [measured] — 9 MCs, the arrangement is the verse order.",
    vocal="Modal, open fifths leave all harmonic room for vocals [hypothesis].",
    principles=["Open fifths + pedal bass = martial/cinematic (no major/minor commitment).", "Marching quarter-note kick for militancy.", "8-bar orchestral intro statement."],
    dont=["The sample/horn line"],
    unknown=["Sample source; exact instrumentation"])


def main():
    os.makedirs('analysis/track_reports', exist_ok=True)
    n = 0
    for name, d in R.items():
        card = open(f'analysis/data/{name}.card.md').read()
        md = f"""# {d['title']}

**Archetype:** {d['archetype']}  ·  **Source file:** `references/raw/` ({name})
**Evidence status:** measured by script; NOT listened to by the model. Every [hypothesis] needs the King's ear.

## 1. Identity & emotional character
{d['identity']}

**Production history:** {d['documented']}

## 2–3. Tempo, groove, timing
{d['groove']}

## 4–6. Drums, bass, harmony & texture
{d['harmony']}

## 7–9. Structure, sections, layer changes
{d['structure']}
Full per-bar map: `analysis/structural_maps/{name}.csv` · plot: `analysis/plots/{name}.png`

## 11. Vocal compatibility
{d['vocal']}

## 12. Transferable principles
""" + '\n'.join(f'- {p}' for p in d['principles']) + """

## 13. Signature elements that must NOT be reproduced
""" + '\n'.join(f'- {p}' for p in d['dont']) + """

## 14. Open questions / needed evidence
""" + '\n'.join(f'- {p}' for p in d['unknown']) + "\n\n" + card
        open(f'analysis/track_reports/{name}.md', 'w').write(md); n += 1
    missing = [os.path.basename(p)[:-8] for p in glob.glob('analysis/data/*.card.md') if os.path.basename(p)[:-8] not in R]
    print(n, 'reports written; missing interpretations:', missing)


if __name__ == '__main__':
    main()
