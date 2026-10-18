"""Phase 3: per-track measurement pipeline (machine measurements only, no listening claims).

Usage: python3 -I scripts/analyze_track.py <audio> <out_json> [<out_png>]

Every value written here is a signal measurement. Musical interpretation lives in the track reports.
Known traps handled:
  * beat trackers alias to 4/3, 3/2, 2x of the true tempo on swung hats -> tempo is chosen by a
    comb over onset autocorrelation at 4/8/16 beats, then refined by a least-squares beat grid.
  * peak onset energy in hip-hop sits on the snare (2 & 4) -> bar phase comes from 35-110 Hz kick energy.
"""
import sys, json, warnings
import numpy as np, soundfile as sf, librosa, scipy.signal as ss, pyloudnorm as pyln
warnings.filterwarnings('ignore')

KEYS = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
KK_MAJ = np.array([6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88])
KK_MIN = np.array([6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17])
TP_MAJ = np.array([0.748, 0.060, 0.488, 0.082, 0.670, 0.460, 0.096, 0.715, 0.104, 0.366, 0.057, 0.400])
TP_MIN = np.array([0.712, 0.084, 0.474, 0.618, 0.049, 0.460, 0.105, 0.747, 0.404, 0.067, 0.133, 0.330])
SR = 22050
HOP = 256
FPS = SR / HOP


def bp(y, lo, hi, sr=SR, order=4):
    if lo <= 0:
        sos = ss.butter(order, hi, 'lowpass', fs=sr, output='sos')
    elif hi >= sr / 2:
        sos = ss.butter(order, lo, 'highpass', fs=sr, output='sos')
    else:
        sos = ss.butter(order, [lo, hi], 'bandpass', fs=sr, output='sos')
    return ss.sosfiltfilt(sos, y)


def onset_env(y):
    S = np.abs(librosa.stft(y, n_fft=1024, hop_length=HOP))
    S = np.log1p(100 * S)
    d = np.maximum(0, np.diff(S, axis=1)).sum(0)
    return np.r_[0, d]


def key_scores(prof):
    out = []
    for name, maj, mn in (('kk', KK_MAJ, KK_MIN), ('temperley', TP_MAJ, TP_MIN)):
        for i in range(12):
            out.append((name, KEYS[i] + ' major', np.corrcoef(prof, np.roll(maj, i))[0, 1]))
            out.append((name, KEYS[i] + ' minor', np.corrcoef(prof, np.roll(mn, i))[0, 1]))
    return out


CHORD_T = {}
for i in range(12):
    for q, iv in (('', (0, 4, 7)), ('m', (0, 3, 7)), ('7', (0, 4, 7, 10)), ('m7', (0, 3, 7, 10)), ('maj7', (0, 4, 7, 11)),
                  ('dim', (0, 3, 6)), ('5', (0, 7))):
        v = np.zeros(12); v[[(i + k) % 12 for k in iv]] = 1
        CHORD_T[KEYS[i] + q] = v / np.linalg.norm(v)


def chord_of(c):
    c = c / (np.linalg.norm(c) + 1e-9)
    best = sorted(((float(c @ v), k) for k, v in CHORD_T.items()), reverse=True)
    return best[0][1], round(best[0][0], 2), best[1][1]


def main(path, out_json, out_png=None):
    x, sr0 = sf.read(path, always_2d=True)
    res = {'file': path.split('/')[-1], 'sr_source': sr0, 'dur_s': round(len(x) / sr0, 2)}
    # ---------- loudness / dynamics / stereo (source rate) ----------
    meter = pyln.Meter(sr0)
    res['lufs_integrated'] = round(meter.integrated_loudness(x), 2)
    mono0 = x.mean(1)
    res['sample_peak_dbfs'] = round(20 * np.log10(np.abs(x).max() + 1e-12), 2)
    rms = np.sqrt(np.mean(mono0 ** 2))
    res['crest_db'] = round(20 * np.log10(np.abs(mono0).max() / rms), 2)
    M, S_ = (x[:, 0] + x[:, -1]) / 2, (x[:, 0] - x[:, -1]) / 2
    res['side_minus_mid_db'] = round(10 * np.log10(np.mean(S_ ** 2) / np.mean(M ** 2) + 1e-12), 1)
    lowM = bp(M, 0, 150, sr0); lowS = bp(S_, 0, 150, sr0)
    res['side_minus_mid_below150_db'] = round(10 * np.log10(np.mean(lowS ** 2) / np.mean(lowM ** 2) + 1e-12), 1)
    # short-term loudness spread (3 s windows)
    win = int(3 * sr0); st = []
    for i in range(0, len(x) - win, win):
        l = meter.integrated_loudness(x[i:i + win]) if np.abs(x[i:i + win]).max() > 1e-4 else -70
        if l > -60: st.append(l)
    res['short_term_lufs_p10_p90'] = [round(float(np.percentile(st, 10)), 1), round(float(np.percentile(st, 90)), 1)] if st else None

    y = librosa.resample(mono0, orig_sr=sr0, target_sr=SR)
    # ---------- spectral balance ----------
    spec = np.abs(librosa.stft(y, n_fft=4096, hop_length=2048)) ** 2
    fr = librosa.fft_frequencies(sr=SR, n_fft=4096); tot = spec.sum()
    bands = [(20, 40), (40, 60), (60, 100), (100, 150), (150, 250), (250, 500), (500, 1000), (1000, 2000), (2000, 4000), (4000, 8000), (8000, 11025)]
    res['band_energy_pct'] = {f'{a}-{b}': round(100 * spec[(fr >= a) & (fr < b)].sum() / tot, 2) for a, b in bands}
    cen = librosa.feature.spectral_centroid(S=np.sqrt(spec), sr=SR)[0]
    res['spectral_centroid_hz_median'] = round(float(np.median(cen)), 0)
    # rolloff for lossy-source detection (where content dies)
    spec_db = 10 * np.log10(spec.mean(1) + 1e-20)
    ref = spec_db[(fr > 1000) & (fr < 4000)].mean()
    above = fr[spec_db > ref - 45]
    res['hf_cutoff_hz_est'] = int(above.max()) if len(above) else None

    # ---------- tempo: comb over bar-level autocorrelation ----------
    oe = onset_env(y); oe = oe - ss.medfilt(oe, 31); oe[oe < 0] = 0
    ac = np.correlate(oe, oe, 'full')[len(oe) - 1:]; ac /= ac[0] + 1e-9
    cands = []
    for bpm in np.arange(60, 180.01, 0.05):
        b = 60 / bpm * FPS
        s = sum(ac[int(round(k * b))] for k in (1, 2, 4, 8, 16) if int(round(k * b)) < len(ac))
        cands.append((s, bpm))
    cands.sort(reverse=True)
    top = []
    for s, b in cands:
        if all(abs(b - t[1]) > 1.5 for t in top): top.append((round(float(s), 3), round(float(b), 2)))
        if len(top) == 5: break
    # prefer the hip-hop lane (70-115) among near-equal candidates (within 8 %)
    best = top[0]
    for s, b in top:
        if 70 <= b <= 115 and s >= 0.92 * top[0][0]:
            best = (s, b); break
    bpm0 = best[1]
    res['tempo_candidates_comb'] = top
    # librosa tracker constrained near bpm0, then least-squares linear grid
    _, beats = librosa.beat.beat_track(onset_envelope=oe, sr=SR, hop_length=HOP, start_bpm=bpm0, tightness=400)
    bt = librosa.frames_to_time(beats, sr=SR, hop_length=HOP)
    per0 = 60 / bpm0
    # keep beats consistent with bpm0, fit t = off + k*per
    k = np.round((bt - bt[0]) / per0)
    A = np.vstack([k, np.ones_like(k)]).T
    per, off = np.linalg.lstsq(A, bt, rcond=None)[0]
    resid = bt - (off + k * per)
    # robust refit
    good = np.abs(resid) < 0.04
    per, off = np.linalg.lstsq(A[good], bt[good], rcond=None)[0]
    resid = bt[good] - (off + k[good] * per)
    res['bpm'] = round(60 / per, 3)
    res['bpm_fit_residual_ms_p90'] = round(float(np.percentile(np.abs(resid), 90) * 1000), 1)
    res['bpm_alternatives'] = {'half': round(30 / per, 2), 'double': round(120 / per, 2)}
    # grid drift test: per in first vs last third (tempo constant? drum machine vs live)
    n = len(bt[good]); kk = k[good]; tt = bt[good]
    if n > 30:
        p1 = np.polyfit(kk[:n // 3], tt[:n // 3], 1)[0]; p3 = np.polyfit(kk[-n // 3:], tt[-n // 3:], 1)[0]
        res['tempo_drift_pct_first_vs_last_third'] = round(100 * (p1 - p3) / p1, 3)

    # ---------- bar phase by kick ----------
    lo = np.abs(bp(y, 35, 110)); mid_sn = np.abs(bp(y, 150, 250)); hi_sn = np.abs(bp(y, 1500, 5000)); hat = np.abs(bp(y, 7000, 11000))
    nbeats = int((len(y) / SR - off) / per)
    beat_t = off + np.arange(nbeats) * per
    while beat_t[0] - per > 0: beat_t = np.r_[beat_t[0] - per, beat_t]

    def e_at(sig, t, w=0.07):
        i = int(t * SR); return float(sig[max(0, i - int(0.01 * SR)):i + int(w * SR)].mean()) if 0 <= i < len(sig) - 10 else 0.0

    kick_b = np.array([e_at(lo, t) for t in beat_t]); sn_b = np.array([e_at(hi_sn, t) for t in beat_t])
    phase_score = []
    for p in range(4):
        # beat 1 = strong kick, beats 2 & 4 = strong snare
        s1 = kick_b[p::4].mean(); s24 = sn_b[(p + 1) % 4::2].mean() / (sn_b.mean() + 1e-9)
        phase_score.append(s1 / (kick_b.mean() + 1e-9) + 0.5 * s24)
    ph = int(np.argmax(phase_score))
    srt = sorted(phase_score, reverse=True)
    res['bar_phase_margin'] = round(float(srt[0] - srt[1]), 3)
    bar_starts = beat_t[ph::4]
    res['first_downbeat_s'] = round(float(bar_starts[0]), 3)
    res['snare_backbeat_ratio'] = round(float(sn_b[(ph + 1) % 4::2].mean() / (sn_b[ph::2].mean() + 1e-9)), 2)
    barlen = 4 * per
    bar_starts = bar_starts[bar_starts + barlen <= len(y) / SR]
    res['n_bars'] = int(len(bar_starts)); res['bar_len_s'] = round(float(barlen), 4)

    # ---------- 16-step drum occupancy + microtiming ----------
    def band_onsets(sig_band):
        e = librosa.onset.onset_strength(y=sig_band, sr=SR, hop_length=128)
        pk, pr = ss.find_peaks(e, height=np.percentile(e, 80), distance=int(0.05 * SR / 128))
        return pk * 128 / SR, pr['peak_heights']

    yp = librosa.effects.percussive(y, margin=2.0)
    grids = {}
    micro = {}
    for name, (lo_f, hi_f) in {'kick': (35, 110), 'snare': (1500, 5000), 'hat': (7000, 11000)}.items():
        t_on, h_on = band_onsets(bp(yp, lo_f, hi_f))
        g = np.zeros(16); dev = [[] for _ in range(16)]
        step = barlen / 16
        for t, h in zip(t_on, h_on):
            j = np.searchsorted(bar_starts, t, side='right') - 1
            if j < 0 or j >= len(bar_starts): continue
            pos = (t - bar_starts[j]) / step
            s = int(np.round(pos)) % 16
            g[s] += h; dev[s].append((pos - np.round(pos)) * step * 1000)
        g = g / (g.max() + 1e-9)
        grids[name] = [round(float(v), 2) for v in g]
        micro[name] = [round(float(np.median(d)), 1) if len(d) > 4 else None for d in dev]
    res['drum_grid_16'] = grids
    res['drum_microtiming_ms_16'] = micro
    # swing: offbeat 16ths (steps 1,3,5..) delay vs straight, on hats
    hs = [micro['hat'][i] for i in (2, 6, 10, 14) if micro['hat'][i] is not None]
    h16 = [micro['hat'][i] for i in (1, 3, 5, 7, 9, 11, 13, 15) if micro['hat'][i] is not None]
    res['hat_8th_offbeat_delay_ms'] = round(float(np.median(hs)), 1) if hs else None
    res['hat_16th_offbeat_delay_ms'] = round(float(np.median(h16)), 1) if h16 else None
    sixteenth_ms = barlen / 16 * 1000
    if h16:
        res['swing_pct_16th'] = round(50 + 50 * float(np.median(h16)) / sixteenth_ms, 1)  # 50 = straight, 66.7 = triplet

    # ---------- per-bar features: layers, dropouts, chords ----------
    harm = librosa.effects.harmonic(y, margin=2.0)
    chroma = librosa.feature.chroma_cqt(y=harm, sr=SR, hop_length=512, bins_per_octave=36)
    cfps = SR / 512
    bass_chroma = librosa.feature.chroma_cqt(y=bp(harm, 0, 220), sr=SR, hop_length=512, fmin=librosa.note_to_hz('C1'), n_octaves=3)
    bands_bar = {'sub_35_110': lo, 'lowmid_150_250': mid_sn, 'mid_250_2k': np.abs(bp(y, 250, 2000)), 'presence_2k_5k': hi_sn, 'air_7k_11k': hat}
    harm_mid = np.abs(bp(harm, 250, 4000)); perc_all = np.abs(yp)
    bars = []
    for i, s in enumerate(bar_starts):
        a, b = int(s * SR), int((s + barlen) * SR)
        row = {'bar': i + 1, 't': round(float(s), 2)}
        row['rms_db'] = round(20 * np.log10(np.sqrt(np.mean(y[a:b] ** 2)) + 1e-9), 1)
        for k2, sig in bands_bar.items():
            row[k2] = round(20 * np.log10(np.mean(sig[a:b]) + 1e-9), 1)
        row['harm_mid_db'] = round(20 * np.log10(np.mean(harm_mid[a:b]) + 1e-9), 1)
        row['perc_db'] = round(20 * np.log10(np.mean(perc_all[a:b]) + 1e-9), 1)
        ca, cb = int(s * cfps), int((s + barlen) * cfps)
        cvec = chroma[:, ca:cb].mean(1); bvec = bass_chroma[:, ca:cb].mean(1)
        row['chroma'] = [round(float(v), 3) for v in cvec / (cvec.max() + 1e-9)]
        row['chord'], row['chord_fit'], row['chord_alt'] = chord_of(cvec)
        row['bass_pc'] = KEYS[int(np.argmax(bvec))]
        # half-bar chords
        hm = (ca + cb) // 2
        row['chord_half'] = [chord_of(chroma[:, ca:hm].mean(1))[0], chord_of(chroma[:, hm:cb].mean(1))[0]]
        row['bass_pc_beats'] = [KEYS[int(np.argmax(bass_chroma[:, int((s + q * per) * cfps):int((s + (q + 1) * per) * cfps)].mean(1)))] for q in range(4)]
        bars.append(row)
    res['bars'] = bars
    # dropouts: bars where sub drops >= 6 dB below track median (kick/bass removed)
    sub = np.array([r['sub_35_110'] for r in bars]); med = np.median(sub)
    perc = np.array([r['perc_db'] for r in bars]); pmed = np.median(perc)
    res['dropout_bars_sub'] = [r['bar'] for r in bars if r['sub_35_110'] < med - 6]
    res['dropout_bars_perc'] = [r['bar'] for r in bars if r['perc_db'] < pmed - 6]
    # harmonic loop length: chroma self-similarity at lags 1,2,4,8 bars
    C = np.array([r['chroma'] for r in bars]); C = C - C.mean(0); C = C / (np.linalg.norm(C, axis=1, keepdims=True) + 1e-9)  # mean-centred: similarity of the bar-to-bar deviations
    loop = {}
    for L in (1, 2, 3, 4, 8):
        if len(C) > L + 4: loop[L] = round(float(np.mean(np.sum(C[L:] * C[:-L], axis=1))), 3)
    res['chroma_bar_lag_similarity'] = loop
    # finer: beat-level chroma similarity at lags (beats) to find sub-bar loops
    # key
    prof = chroma.mean(1)
    ks = key_scores(prof)
    agg = {}
    for meth, kname, v in ks: agg.setdefault(kname, []).append(v)
    kr = sorted(((np.mean(v), k2) for k2, v in agg.items()), reverse=True)
    res['key_candidates'] = [(k2, round(float(v), 3)) for v, k2 in kr[:4]]
    res['key_confidence_margin'] = round(float(kr[0][0] - kr[1][0]), 3)
    res['pitch_class_profile'] = {KEYS[i]: round(float(prof[i] / prof.max()), 2) for i in range(12)}
    # bass pitch-class profile
    bp_prof = bass_chroma.mean(1)
    res['bass_pitch_class_profile'] = {KEYS[i]: round(float(bp_prof[i] / bp_prof.max()), 2) for i in range(12)}
    # structure: novelty on per-bar feature vectors
    F = np.array([[r['rms_db'], r['sub_35_110'], r['mid_250_2k'], r['presence_2k_5k'], r['air_7k_11k'], r['harm_mid_db'], r['perc_db']] + list(np.array(r['chroma']) * 3) for r in bars])
    Fz = (F - F.mean(0)) / (F.std(0) + 1e-9)
    nov = np.r_[0, np.linalg.norm(np.diff(Fz, axis=0), axis=1)]
    thr = max(np.percentile(nov, 88), np.median(nov) * 2)
    bounds = [0] + [i for i in range(1, len(nov)) if nov[i] >= thr and (i == 1 or nov[i] >= nov[i - 1])]
    secs = []
    for j, b0 in enumerate(bounds):
        b1 = bounds[j + 1] if j + 1 < len(bounds) else len(bars)
        seg = F[b0:b1]
        secs.append({'start_bar': b0 + 1, 'n_bars': b1 - b0, 't_start': bars[b0]['t'], 'rms_db': round(float(seg[:, 0].mean()), 1),
                     'sub': round(float(seg[:, 1].mean()), 1), 'mid': round(float(seg[:, 2].mean()), 1), 'air': round(float(seg[:, 4].mean()), 1),
                     'harm_mid': round(float(seg[:, 5].mean()), 1), 'perc': round(float(seg[:, 6].mean()), 1)})
    res['sections_auto'] = secs
    # transient sharpness of kick/snare: median attack slope proxy (peak / mean in 30 ms)
    res['perc_to_harm_ratio_db'] = round(float(20 * np.log10(np.sqrt(np.mean(yp ** 2)) / (np.sqrt(np.mean(harm ** 2)) + 1e-9))), 1)

    json.dump(res, open(out_json, 'w'), ensure_ascii=False, indent=1)
    if out_png:
        import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
        fig, ax = plt.subplots(4, 1, figsize=(16, 13), gridspec_kw={'height_ratios': [2, 2, 2, 1.4]})
        tb = [r['t'] for r in bars]
        for k2 in ['sub_35_110', 'mid_250_2k', 'presence_2k_5k', 'air_7k_11k', 'harm_mid_db', 'perc_db']:
            ax[0].plot(range(1, len(bars) + 1), [r[k2] for r in bars], label=k2)
        for s in secs: ax[0].axvline(s['start_bar'], color='k', alpha=.3)
        ax[0].legend(fontsize=7, ncol=6); ax[0].set_title(f"{res['file']}  |  {res['bpm']} BPM  |  key {res['key_candidates'][0][0]}  |  per-bar band energy (dB); lines = auto sections"); ax[0].set_xlabel('bar')
        ax[1].imshow(C.T, aspect='auto', origin='lower', extent=[0.5, len(bars) + .5, -.5, 11.5], cmap='magma'); ax[1].set_yticks(range(12)); ax[1].set_yticklabels(KEYS); ax[1].set_title('chroma per bar')
        S_db = librosa.amplitude_to_db(np.abs(librosa.stft(y[:int(min(len(y), (bar_starts[min(8, len(bar_starts) - 1)] + barlen) * SR))], n_fft=2048, hop_length=256)), ref=np.max)
        ax[2].imshow(S_db[:600], aspect='auto', origin='lower', cmap='magma', vmin=-80); ax[2].set_title('spectrogram, first ~8 bars (0-6.5 kHz)')
        G = np.array([grids['kick'], grids['snare'], grids['hat']])
        ax[3].imshow(G, aspect='auto', cmap='Greys'); ax[3].set_yticks([0, 1, 2]); ax[3].set_yticklabels(['kick', 'snare', 'hat']); ax[3].set_xticks(range(16)); ax[3].set_xticklabels(['1', 'e', '&', 'a', '2', 'e', '&', 'a', '3', 'e', '&', 'a', '4', 'e', '&', 'a']); ax[3].set_title('16-step onset occupancy (whole track)')
        plt.tight_layout(); plt.savefig(out_png, dpi=80); plt.close()


if __name__ == '__main__':
    main(*sys.argv[1:])
