"""Sampler for folders of single-note WAVs named like  spic_A2_v1_RR1.wav / susvib_C#3_v3_1.wav / KSHarp_D4_mf.wav (VSCO-2-CE)."""
import os, re, glob, random
import numpy as np, soundfile as sf
from scipy.signal import resample_poly
from sfz import note_num

DYN = {'pp': 1, 'p': 2, 'mp': 3, 'mf': 4, 'f': 5, 'ff': 6}


class FolderSampler:
    def __init__(self, folder, sr=48000, release=0.25, gain_db=0.0, name_offset=12):
        """name_offset: VSCO-2-CE names most files one octave low (measured with pYIN: +12 st); harp folder is correct (0)."""
        self.sr, self.release, self.gain = sr, release, 10 ** (gain_db / 20)
        self.map = {}  # note -> {layer: [paths]}
        for p in glob.glob(os.path.join(folder, '*.wav')):
            b = os.path.basename(p)
            m = re.search(r'_([A-Ga-g][#b]?-?\d)(?:_|\.)', b)
            if not m: continue
            n = note_num(m.group(1)) + name_offset
            v = re.search(r'_v(\d+)', b); d = re.search(r'_(pp|p|mp|mf|f|ff)(?:_|\.)', b)
            layer = int(v.group(1)) if v else DYN.get(d.group(1), 4) if d else 1
            self.map.setdefault(n, {}).setdefault(layer, []).append(p)
        self.notes = np.array(sorted(self.map)); self.cache = {}
        if not len(self.notes): raise ValueError('no samples in ' + folder)

    def _load(self, p):
        if p not in self.cache:
            x, sr = sf.read(p, always_2d=True, dtype='float32')
            if x.shape[1] == 1: x = np.repeat(x, 2, 1)
            if sr != self.sr: x = resample_poly(x, self.sr, sr, axis=0).astype(np.float32)
            self.cache[p] = x
        return self.cache[p]

    def render_note(self, key, vel, dur, rng=None):
        rng = rng or random
        src = int(self.notes[np.argmin(np.abs(self.notes - key))])
        layers = sorted(self.map[src]); li = layers[min(len(layers) - 1, int(vel / 128 * len(layers)))]
        x = self._load(rng.choice(self.map[src][li]))
        semis = key - src
        if semis:
            r = 2 ** (semis / 12); idx = np.arange(0, len(x) - 1, r)
            x = np.stack([np.interp(idx, np.arange(len(x)), x[:, c]) for c in range(2)], 1).astype(np.float32)
        n_on = int(dur * self.sr); n_rel = int(self.release * self.sr)
        x = x[:n_on + n_rel].copy()
        if len(x) > n_on:
            x[n_on:] *= np.exp(-5 * np.arange(len(x) - n_on) / max(1, n_rel))[:, None]
        return x * self.gain * (0.35 + 0.65 * (vel / 127) ** 1.6)
