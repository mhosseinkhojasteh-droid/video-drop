# Mix & master preparation [measured targets]

| Metric | References (min / median / max) | Our beat delivery target |
|---|---|---|
| Integrated LUFS | −19.8 / −11.4 / −8.0 | −10.0 ± 0.5 (beat-only, leaves room for the vocal mix) |
| Crest (peak/RMS, mono) | 10.7 / 13.5 / 19.3 dB | ≥ 11 dB |
| True peak | rips clip at 0 dBFS | ≤ −1.0 dBTP (4× oversampled limiter) |
| Energy ≤150 Hz | 31 / 74 / 87 % | 65–80 % (archetype dependent) |
| Side−mid | −72 / −19 / −6 dB | −15…−22 dB overall, < −30 dB below 150 Hz |
| Spectral centroid | 1.0–3.8 kHz (median ~2.1 kHz) | 1.6–2.4 kHz |

## Chain (scripts/engine)
1. Stems at 48 kHz float. Per-stem: HPF everything except kick/bass at 100–150 Hz; drums through vintage() emulation where the archetype needs grit.
2. One shared room/plate (Dragonfly or pedalboard Reverb) on a send, HPF 250 Hz on the return.
3. Bus: gentle glue (2:1, 30 ms attack), optional CHOWTape for "record" colour.
4. Master: soft clip (tanh, thr 0.89) → 4× true-peak limiter −1 dBTP → loudness iterate to target.
5. QC: LUFS, crest, true peak, mono compatibility (L+R correlation), spectrum vs. archetype table.
