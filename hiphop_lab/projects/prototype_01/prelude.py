"""The PRELUDE — Glass Jaw's opening and closing piano, written like a classical pianist would play it (King, 25 Oct 2026:
"if someone puts a hand on the piano it must be Mozart, Beethoven or Bach — no random keys").

Harmony (F minor, 2 chords per bar, Bach's lament bass F-Eb-Db-C, then Ab-Bb, Neapolitan, dominant):
  | Fm      Cm/Eb | Db       C7    | Fm/Ab    Bbm   | Gb/Bb (N6)  C7b9 |  -> half cadence: the riff answers on Fm
Texture: left hand = bass line (octave on the first beat of each bar), middle = Alberti eighths (low-high-mid-high, Mozart),
right hand top = a singing melody in half/quarter notes, voice-led step by step, never doubling the Alberti's top note.
Every note belongs to the chord or is a passing tone between two chord tones. Pedal = legato inside each half bar.
Dynamics: one phrase arch (p -> mf at bar 3 -> diminuendo into the half cadence); melody +18 vel over the accompaniment;
melody lead 12 ms (pianists sound the melody slightly before the accompaniment); timing jitter <= 3 ms.
"""
import random
from render import Note
from theory import n

# (bass, alberti triad low->high, melody [(beat_in_half, dur, note)]) per half bar
HALVES = [
    ('F2',  ['Ab3', 'C4', 'F4'],  [(0, 2.0, 'C5')]),
    ('Eb2', ['G3', 'C4', 'Eb4'],  [(0, 1.0, 'Bb4'), (1, 1.0, 'G4')]),
    ('Db2', ['Ab3', 'Db4', 'F4'], [(0, 2.0, 'Ab4')]),
    ('C2',  ['G3', 'Bb3', 'E4'],  [(0, 1.0, 'G4'), (1, 1.0, 'Bb4')]),
    ('Ab1', ['F3', 'Ab3', 'C4'],  [(0, 1.0, 'Ab4'), (1, 1.0, 'C5')]),
    ('Bb1', ['Bb3', 'Db4', 'F4'], [(0, 2.0, 'Db5')]),
    ('Bb1', ['Bb3', 'Db4', 'Gb4'], [(0, 1.0, 'Db5'), (1, 1.0, 'Bb4')]),
    ('C2',  ['Bb3', 'Db4', 'E4'], [(0, 1.0, 'Db5'), (1, 1.0, 'C5')]),
]
ARCH = [0.80, 0.82, 0.88, 0.90, 1.00, 1.00, 0.92, 0.86]   # phrase dynamics per half bar


def prelude_events(o, spb, halves=8, final=False, seed=3):
    """Notes for the prelude starting at beat o. halves = how many half-bars to play (8 = 4 bars).
    final=True appends the closing F minor (add9) chord, rolled slowly and held."""
    rng = random.Random(seed)
    j = lambda ms=3: rng.uniform(-ms, ms) / 1000 / spb
    lead = -0.012 / spb
    ev = []
    for h in range(halves):
        bass, tri, mel = HALVES[h]; b0 = o + 2 * h; a = ARCH[h]
        # left hand: bass held for the half bar; octave below on the first beat of each bar
        ev.append(Note(b0 + j(), 1.95, n(bass), int(66 * a)))
        if h % 2 == 0: ev.append(Note(b0 + j(), 1.95, n(bass) - 12, int(54 * a)))
        # Alberti: low, high, mid, high — legato under the pedal (each note sustains to the end of the half bar)
        for k, idx in enumerate((0, 2, 1, 2)):
            pos = 0.5 * k
            v = (52 if k == 0 else 44) * a + rng.uniform(-3, 3)
            ev.append(Note(b0 + pos + j(), 2.0 - pos, n(tri[idx]), int(v)))
        # melody
        for bt, d, nm in mel:
            ev.append(Note(b0 + bt + lead + j(2), d * 0.98, n(nm), int(min(110, 80 * a + 6 + rng.uniform(-2, 2)))))
    if final:
        e = o + 2 * halves
        chord = ['F1', 'F2', 'C3', 'Ab3', 'C4', 'G4']   # Fm(add9): the G is the open question that stays
        for k, nm in enumerate(chord):
            ev.append(Note(e + k * 0.03 / spb, 7.0, n(nm), int(70 - 3 * k)))
        ev.append(Note(e + 0.25 + lead, 6.5, n('C5'), 66))
        ev.append(Note(e + 2.0 + lead, 5.0, n('Ab4'), 54))   # the last melody step: C5 -> Ab4, a sigh, not a question
    return ev
