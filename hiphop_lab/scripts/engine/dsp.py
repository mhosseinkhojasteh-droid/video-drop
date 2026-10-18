"""DSP building blocks: drum synthesis, vintage sampler emulation, saturation, EQ helpers, loudness."""
import numpy as np, scipy.signal as ss
from scipy.signal import resample_poly

SR = 48000


def _sos(kind, f, sr=SR, order=2):
    return ss.butter(order, f, kind, fs=sr, output='sos')


def hp(x, f, sr=SR, order=2): return ss.sosfilt(_sos('highpass', f, sr, order), x, axis=0)
def lp(x, f, sr=SR, order=2): return ss.sosfilt(_sos('lowpass', f, sr, order), x, axis=0)
def bpf(x, lo, hi, sr=SR, order=2): return ss.sosfilt(ss.butter(order, [lo, hi], 'bandpass', fs=sr, output='sos'), x, axis=0)


def peq(x, f0, gain_db, q=1.0, sr=SR):
    """RBJ peaking EQ."""
    A = 10 ** (gain_db / 40); w = 2 * np.pi * f0 / sr; al = np.sin(w) / (2 * q)
    b = [1 + al * A, -2 * np.cos(w), 1 - al * A]; a = [1 + al / A, -2 * np.cos(w), 1 - al / A]
    return ss.lfilter(np.array(b) / a[0], np.array(a) / a[0], x, axis=0)


def shelf(x, f0, gain_db, kind='low', sr=SR, s=1.0):
    A = 10 ** (gain_db / 40); w = 2 * np.pi * f0 / sr; cw, sw = np.cos(w), np.sin(w)
    al = sw / 2 * np.sqrt((A + 1 / A) * (1 / s - 1) + 2); sa = 2 * np.sqrt(A) * al
    if kind == 'low':
        b = [A * ((A + 1) - (A - 1) * cw + sa), 2 * A * ((A - 1) - (A + 1) * cw), A * ((A + 1) - (A - 1) * cw - sa)]
        a = [(A + 1) + (A - 1) * cw + sa, -2 * ((A - 1) + (A + 1) * cw), (A + 1) + (A - 1) * cw - sa]
    else:
        b = [A * ((A + 1) + (A - 1) * cw + sa), -2 * A * ((A - 1) + (A + 1) * cw), A * ((A + 1) + (A - 1) * cw - sa)]
        a = [(A + 1) - (A - 1) * cw + sa, 2 * ((A - 1) - (A + 1) * cw), (A + 1) - (A - 1) * cw - sa]
    return ss.lfilter(np.array(b) / a[0], np.array(a) / a[0], x, axis=0)


def sat(x, drive_db=6.0, mix=1.0):
    """tanh saturation, level-compensated."""
    g = 10 ** (drive_db / 20); y = np.tanh(x * g) / np.tanh(g)
    return mix * y + (1 - mix) * x


def env_exp(n, tau_s, sr=SR):
    return np.exp(-np.arange(n) / (tau_s * sr))


# ------------------------------------------------------------------ drum synthesis
def kick_808(f0=48.0, decay=0.9, pitch_drop=2.2, drop_tau=0.035, click=0.25, drive_db=4.0, sr=SR):
    """TR-808 style bass drum: sine with exponential pitch sweep + click, gently saturated."""
    n = int((decay * 3 + 0.05) * sr); t = np.arange(n) / sr
    f = f0 * (1 + (pitch_drop - 1) * np.exp(-t / drop_tau))
    ph = 2 * np.pi * np.cumsum(f) / sr
    y = np.sin(ph) * np.exp(-t / decay)
    ck = np.random.default_rng(1).standard_normal(n) * np.exp(-t / 0.0025)
    y += click * bpf(ck, 1000, 6000, sr)
    y = sat(y, drive_db)
    return (y / np.abs(y).max()).astype(np.float32)


def snare_synth(tone=185.0, noise_tau=0.11, tone_tau=0.06, snappy=0.7, sr=SR, seed=2):
    n = int(0.5 * sr); t = np.arange(n) / sr
    body = np.sin(2 * np.pi * tone * t) * np.exp(-t / tone_tau) + 0.5 * np.sin(2 * np.pi * tone * 1.6 * t) * np.exp(-t / (tone_tau * .7))
    nz = np.random.default_rng(seed).standard_normal(n) * np.exp(-t / noise_tau)
    nz = bpf(nz, 1800, 9000, sr)
    y = 0.6 * body + snappy * nz / (np.abs(nz).max() + 1e-9)
    return (y / np.abs(y).max()).astype(np.float32)


def hat_synth(open_=False, sr=SR, seed=3):
    n = int((0.45 if open_ else 0.08) * sr); t = np.arange(n) / sr
    # 808-style: six square oscillators, band-passed
    fr = [205.3, 304.4, 369.6, 522.7, 540.0, 800.0]
    y = sum(np.sign(np.sin(2 * np.pi * f * 2.0 * t + k)) for k, f in enumerate(fr))
    y = bpf(y, 7000, 14000, sr, 4) + 0.3 * hp(np.random.default_rng(seed).standard_normal(n), 8000, sr)
    y *= np.exp(-t / (0.12 if open_ else 0.018))
    return (y / np.abs(y).max()).astype(np.float32)


def clap_synth(sr=SR, seed=4):
    n = int(0.4 * sr); t = np.arange(n) / sr
    nz = bpf(np.random.default_rng(seed).standard_normal(n), 900, 5000, sr)
    env = np.zeros(n)
    for k, d in enumerate((0, 0.011, 0.022, 0.031)):
        i = int(d * sr); env[i:] += np.exp(-(t[:n - i]) / (0.008 if k < 3 else 0.09))
    y = nz * env
    return (y / np.abs(y).max()).astype(np.float32)


# ------------------------------------------------------------------ vintage samplers
def vintage(x, mode='sp1200', sr=SR):
    """Emulate the converter character of classic hip-hop samplers on a mono/stereo array.
    sp1200: 26.04 kHz, 12-bit, weak anti-alias (aliasing grit), output low-pass; the boom-bap crunch.
    mpc60 : 40 kHz, 12-bit companded-ish (16-bit store, 12-bit-like DAC colour), soft top.
    s950  : 39 kHz/31.25 kHz switchable filter, 12-bit, warm low-pass.
    """
    mono = x.ndim == 1
    X = x[:, None] if mono else x
    if mode == 'sp1200':
        fs2, bits, lpf = 26040, 12, 12500
    elif mode == 'mpc60':
        fs2, bits, lpf = 40000, 12, 16000
    elif mode == 's950':
        fs2, bits, lpf = 31250, 12, 10500
    else:
        return x
    # decimate with a weak (1st-order) pre-filter to keep some aliasing
    pre = lp(X, fs2 * 0.48, sr, 1)
    idx = np.arange(0, len(pre), sr / fs2)
    d = np.stack([np.interp(idx, np.arange(len(pre)), pre[:, c]) for c in range(X.shape[1])], 1)
    q = 2 ** (bits - 1)
    peak = np.abs(d).max() + 1e-9
    d = np.round(d / peak * q * 0.98) / q * peak / 0.98
    # zero-order-hold back up (imaging) then output filter
    back = resample_poly(d, sr, fs2, axis=0)
    back = lp(back, lpf, sr, 4)
    back = back[:len(X)]
    if len(back) < len(X): back = np.pad(back, ((0, len(X) - len(back)), (0, 0)))
    return back[:, 0] if mono else back


def pitch_resample(x, semitones):
    """Sampler-style pitch change (speed and pitch together, like an SP-1200/MPC)."""
    if abs(semitones) < 1e-3: return x
    r = 2 ** (semitones / 12)
    idx = np.arange(0, len(x) - 1, r)
    if x.ndim == 1: return np.interp(idx, np.arange(len(x)), x).astype(np.float32)
    return np.stack([np.interp(idx, np.arange(len(x)), x[:, c]) for c in range(x.shape[1])], 1).astype(np.float32)


# ------------------------------------------------------------------ dynamics
def compress(x, thr_db=-18, ratio=4, att_ms=10, rel_ms=120, makeup_db=0, knee_db=6, sidechain=None, sr=SR):
    """Feed-forward RMS-ish compressor (stereo-linked). sidechain: optional key signal."""
    key = x if sidechain is None else sidechain
    k = np.abs(key).max(axis=1) if key.ndim == 2 else np.abs(key)
    a = np.exp(-1 / (att_ms * 1e-3 * sr)); r = np.exp(-1 / (rel_ms * 1e-3 * sr))
    env = ss.lfilter([1 - r], [1, -r], k)  # release-shaped smoothing
    env = np.maximum(env, ss.lfilter([1 - a], [1, -a], k))
    lvl = 20 * np.log10(env + 1e-9)
    over = lvl - thr_db
    gr = np.where(over <= -knee_db / 2, 0, np.where(over >= knee_db / 2, over * (1 - 1 / ratio), (over + knee_db / 2) ** 2 / (2 * knee_db) * (1 - 1 / ratio)))
    g = 10 ** ((-gr + makeup_db) / 20)
    return x * (g[:, None] if x.ndim == 2 else g)


def soft_clip(x, thr=0.89):
    y = np.where(np.abs(x) < thr, x, np.sign(x) * (thr + (1 - thr) * np.tanh((np.abs(x) - thr) / (1 - thr))))
    return y


def true_peak_limit(x, ceiling_db=-1.0, lookahead_ms=1.5, rel_ms=60, sr=SR):
    """4x-oversampled peak detection, lookahead gain computer, delay-compensated."""
    c = 10 ** (ceiling_db / 20)
    up = resample_poly(x, 4, 1, axis=0)
    pk = np.abs(up).max(axis=1).reshape(-1, 4).max(axis=1) if len(up) % 4 == 0 else np.abs(up[:len(up) // 4 * 4]).max(axis=1).reshape(-1, 4).max(axis=1)
    pk = np.pad(pk, (0, len(x) - len(pk)), mode='edge')
    need = np.minimum(1, c / (pk + 1e-12))
    la = int(lookahead_ms * 1e-3 * sr)
    # min over lookahead window
    from scipy.ndimage import minimum_filter1d
    need = minimum_filter1d(need, size=2 * la + 1, origin=0)
    g = _release(need, np.exp(-1 / (rel_ms * 1e-3 * sr)))
    return x * g[:, None]


try:
    from numba import njit
except ImportError:  # pragma: no cover
    njit = lambda f: f


@njit
def _release(need, r):
    g = np.empty_like(need); cur = 1.0
    for i in range(len(need)):
        cur = need[i] if need[i] < cur else need[i] + (cur - need[i]) * r
        g[i] = cur
    return g


def lufs(x, sr=SR):
    import pyloudnorm as pyln
    return pyln.Meter(sr).integrated_loudness(x)


# ------------------------------------------------------------------ texture & synth voices
def vinyl(n, level_db=-38, crackle_per_s=9, sr=SR, seed=11):
    """Vinyl bed: band-limited hiss + sparse crackle impulses + slow rumble, stereo."""
    rng = np.random.default_rng(seed)
    hiss = bpf(rng.standard_normal((n, 2)), 1500, 9000, sr) * 0.25
    ck = np.zeros((n, 2))
    k = rng.poisson(crackle_per_s * n / sr)
    pos = rng.integers(0, n, k)
    ck[pos, rng.integers(0, 2, k)] = rng.uniform(-1, 1, k) * rng.pareto(3, k).clip(0, 6)
    ck = hp(ck, 1200, sr)
    rumble = lp(rng.standard_normal((n, 2)), 40, sr) * 0.6
    y = hiss + ck + rumble
    return (y / (np.abs(y).max() + 1e-9) * 10 ** (level_db / 20)).astype(np.float32)


def glide_lead(notes, spb, total_s, glide_s=0.07, vib_hz=5.2, vib_cents=18, sr=SR, bright=0.18):
    """G-funk whistle lead: one continuous oscillator (sine + a little saw), portamento between notes,
    delayed vibrato. notes = list of (beat, dur_beats, midi, vel)."""
    n = int(total_s * sr); f = np.zeros(n); a = np.zeros(n)
    notes = sorted(notes)
    prev = None
    for beat, dur, m, vel in notes:
        s, e = int(beat * spb * sr), int((beat + dur) * spb * sr)
        e = min(e, n)
        tgt = 440 * 2 ** ((m - 69) / 12)
        if prev is not None and s - prev[1] < int(0.05 * sr):
            g = min(int(glide_s * sr), e - s)
            f[s:s + g] = np.geomspace(prev[0], tgt, g); f[s + g:e] = tgt
        else:
            f[s:e] = tgt
        L = e - s; t = np.arange(L) / sr
        env = np.minimum(1, t / 0.012) * np.minimum(1, (L - np.arange(L)) / (0.06 * sr))
        a[s:e] = np.maximum(a[s:e], env * vel / 127)
        vib = np.clip((t - 0.18) / 0.25, 0, 1) * vib_cents / 1200
        f[s:e] *= 2 ** (vib * np.sin(2 * np.pi * vib_hz * t))
        prev = (tgt, e)
    f[f == 0] = 1
    ph = 2 * np.pi * np.cumsum(f) / sr
    saw = 2 * ((ph / (2 * np.pi)) % 1) - 1
    y = (np.sin(ph) * (1 - bright) + bright * lp(saw, 2500, sr)) * a
    return np.stack([y, y], 1).astype(np.float32)


def bass_808(notes, spb, total_s, decay=0.55, drive_db=7, glide_s=0.0, sr=SR):
    """Tuned 808 bass line: each note = sine with short pitch kick + saturation; notes=(beat,dur,midi,vel)."""
    n = int(total_s * sr); y = np.zeros(n)
    for beat, dur, m, vel in sorted(notes):
        s = int(beat * spb * sr); L = min(int((dur * spb + 0.08) * sr), n - s)
        if L <= 0: continue
        t = np.arange(L) / sr; f0 = 440 * 2 ** ((m - 69) / 12)
        f = f0 * (1 + 1.2 * np.exp(-t / 0.018))
        x = np.sin(2 * np.pi * np.cumsum(f) / sr) * np.exp(-t / decay) * (vel / 127)
        x *= np.minimum(1, (L - np.arange(L)) / (0.02 * sr))
        y[s:s + L] = x + y[s:s + L] * np.exp(-np.arange(L) / (0.004 * sr))  # choke previous note
    y = sat(y, drive_db)
    return np.stack([y, y], 1).astype(np.float32)


def width(x, w):
    """Mid/side width: w=1 unchanged, 0 = mono."""
    m = x.mean(1, keepdims=True); s = (x[:, :1] - x[:, 1:]) / 2
    return np.concatenate([m + w * s, m - w * s], 1)
