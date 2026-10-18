"""Builds the measured part of every track report + structural maps + the technical CSV from analysis/data/*.json.

Usage: python3 -I scripts/make_cards.py
Outputs: analysis/structural_maps/<track>.csv, analysis/data/<track>.card.md (measured section only),
         reports/02_audio_technical_analysis.csv
"""
import json, glob, os, csv
import numpy as np

STEPS = ['1', 'e', '&', 'a', '2', 'e', '&', 'a', '3', 'e', '&', 'a', '4', 'e', '&', 'a']


def grid_str(g, thr=0.45):
    return ''.join('X' if v >= 0.75 else 'x' if v >= thr else '.' for v in g)


def phrase_view(d):
    """Group consecutive bars with similar energy/layer profile; report sub/perc dropouts and layer adds."""
    bars = d['bars']
    sub = np.array([b['sub_35_110'] for b in bars]); perc = np.array([b['perc_db'] for b in bars])
    air = np.array([b['air_7k_11k'] for b in bars]); hm = np.array([b['harm_mid_db'] for b in bars])
    med = {k: float(np.median(v)) for k, v in (('sub', sub), ('perc', perc), ('air', air), ('hm', hm))}
    tags = []
    for i, b in enumerate(bars):
        t = []
        if sub[i] < med['sub'] - 6: t.append('NO-LOW')
        elif sub[i] < med['sub'] - 3: t.append('low-thin')
        if perc[i] < med['perc'] - 6: t.append('NO-DRUMS')
        if air[i] < med['air'] - 6: t.append('no-hats')
        elif air[i] > med['air'] + 3: t.append('hats+')
        if hm[i] > med['hm'] + 3: t.append('melody+')
        elif hm[i] < med['hm'] - 6: t.append('melody-off')
        tags.append(','.join(t) if t else 'full')
    return tags


def main():
    rows = []
    for jp in sorted(glob.glob('analysis/data/*.json')):
        d = json.load(open(jp)); name = os.path.basename(jp)[:-5]
        tags = phrase_view(d)
        with open(f'analysis/structural_maps/{name}.csv', 'w', newline='') as fh:
            w = csv.writer(fh); w.writerow(['bar', 't_s', 'state', 'rms_db', 'sub', 'perc', 'air', 'harm_mid', 'chord_est', 'chord_half_est', 'bass_pc_beats'])
            for b, tg in zip(d['bars'], tags):
                w.writerow([b['bar'], b['t'], tg, b['rms_db'], b['sub_35_110'], b['perc_db'], b['air_7k_11k'], b['harm_mid_db'], b['chord'], '|'.join(b['chord_half']), '-'.join(b['bass_pc_beats'])])
        # compressed state timeline
        segs = []; cur = tags[0]; st = 1
        for i, tg in enumerate(tags[1:], 2):
            if tg != cur: segs.append((st, i - 1, cur)); cur, st = tg, i
        segs.append((st, len(tags), cur))
        timeline = ' | '.join(f"b{a}-{b}:{s}" if a != b else f"b{a}:{s}" for a, b, s in segs)
        # first 8 bars chord/bass sequence (loop identity, estimate)
        seq = ' '.join(f"[{'/'.join(b['chord_half'])} bass {'-'.join(b['bass_pc_beats'])}]" for b in d['bars'][1:9])
        g = d['drum_grid_16']; mt = d['drum_microtiming_ms_16']
        be = d['band_energy_pct']
        low = sum(v for k, v in be.items() if int(k.split('-')[1]) <= 150)
        card = f"""## Measured profile [measured — scripts/analyze_track.py → analysis/data/{name}.json]

| metric | value |
|---|---|
| duration | {d['dur_s']} s, {d['n_bars']} bars of {d['bar_len_s']} s |
| tempo | **{d['bpm']} BPM** (grid residual p90 {d['bpm_fit_residual_ms_p90']} ms; comb candidates {d['tempo_candidates_comb'][:3]}; drift first→last third {d.get('tempo_drift_pct_first_vs_last_third')} %) |
| first downbeat | {d['first_downbeat_s']} s (bar-phase margin {d['bar_phase_margin']}; snare backbeat ratio {d['snare_backbeat_ratio']}) |
| key | {d['key_candidates'][0][0]} [estimate, margin {d['key_confidence_margin']}]; alternatives {d['key_candidates'][1:3]} |
| loudness | {d['lufs_integrated']} LUFS integrated, short-term p10/p90 {d['short_term_lufs_p10_p90']}, crest {d['crest_db']} dB, sample peak {d['sample_peak_dbfs']} dBFS |
| stereo | side−mid {d['side_minus_mid_db']} dB overall, {d['side_minus_mid_below150_db']} dB below 150 Hz |
| spectrum | {round(low,1)} % of energy ≤150 Hz; centroid {d['spectral_centroid_hz_median']} Hz; HF content to ~{d['hf_cutoff_hz_est']} Hz |
| swing (hat 16ths) | {d.get('swing_pct_16th')} % (50 straight, 66.7 triplet); off-8th hat delay {d['hat_8th_offbeat_delay_ms']} ms |
| perc vs harmonic | {d['perc_to_harm_ratio_db']} dB |
| harmonic loop similarity (bar lags) | {d['chroma_bar_lag_similarity']} |

**16-step onset occupancy** (X strong, x present; whole track):
```
        {' '.join(STEPS)}
kick    {' '.join(grid_str(g['kick']))}
snare   {' '.join(grid_str(g['snare']))}
hat     {' '.join(grid_str(g['hat']))}
```
Median micro-timing per step (ms, + = late): kick {mt['kick']}, snare {mt['snare']}, hat {mt['hat']}

**Layer timeline** (per bar vs. track median; NO-LOW = sub ≥6 dB down, NO-DRUMS = percussive ≥6 dB down):
{timeline}

**Bars 2–9 harmonic sketch** [estimate: chroma template + bass chroma; not a transcription]: {seq}

Pitch-class profile: {d['pitch_class_profile']}
Bass pitch-class profile: {d['bass_pitch_class_profile']}
"""
        open(f'analysis/data/{name}.card.md', 'w').write(card)
        rows.append(dict(track=name, dur_s=d['dur_s'], bpm=d['bpm'], key_est=d['key_candidates'][0][0], key_margin=d['key_confidence_margin'],
                         lufs=d['lufs_integrated'], crest_db=d['crest_db'], side_mid_db=d['side_minus_mid_db'], low_le150_pct=round(low, 1),
                         centroid_hz=d['spectral_centroid_hz_median'], swing16=d.get('swing_pct_16th'), hat8_delay_ms=d['hat_8th_offbeat_delay_ms'],
                         perc_vs_harm_db=d['perc_to_harm_ratio_db'], bars=d['n_bars'], kick=grid_str(g['kick']), snare=grid_str(g['snare']), hat=grid_str(g['hat']),
                         dropouts_low=' '.join(map(str, d['dropout_bars_sub'])), dropouts_drums=' '.join(map(str, d['dropout_bars_perc'])), hf_cutoff=d['hf_cutoff_hz_est']))
    with open('reports/02_audio_technical_analysis.csv', 'w', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    print(len(rows), 'cards')


if __name__ == '__main__':
    main()
