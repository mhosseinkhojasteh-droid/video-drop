"""Pitch helpers."""
NAMES = {'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3, 'E': 4, 'F': 5, 'F#': 6, 'Gb': 6, 'G': 7, 'G#': 8, 'Ab': 8, 'A': 9, 'A#': 10, 'Bb': 10, 'B': 11}


def n(s):
    """'C4' -> 60, 'Gb3' -> 54"""
    name = s[:-1] if s[-1].isdigit() and not s[-2].isdigit() else s[:-2]
    octv = int(s[len(name):])
    return NAMES[name] + (octv + 1) * 12


def chord(root, quality):
    iv = {'maj': [0, 4, 7], 'min': [0, 3, 7], 'm7': [0, 3, 7, 10], 'maj7': [0, 4, 7, 11], '7': [0, 4, 7, 10], '9': [0, 4, 7, 10, 14],
          'm9': [0, 3, 7, 10, 14], 'dim7': [0, 3, 6, 9], 'm7b5': [0, 3, 6, 10], '5': [0, 7, 12], 'sus2': [0, 2, 7], 'mmaj7': [0, 3, 7, 11],
          '7b9': [0, 4, 7, 10, 13], 'm11': [0, 3, 7, 10, 14, 17]}[quality]
    r = n(root) if isinstance(root, str) else root
    return [r + i for i in iv]
