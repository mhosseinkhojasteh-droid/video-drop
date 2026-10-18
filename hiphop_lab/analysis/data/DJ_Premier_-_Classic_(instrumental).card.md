## Measured profile [measured — scripts/analyze_track.py → analysis/data/DJ_Premier_-_Classic_(instrumental).json]

| metric | value |
|---|---|
| duration | 286.56 s, 118 bars of 2.4002 s |
| tempo | **99.993 BPM** (grid residual p90 12.0 ms; comb candidates [[2.883, 100.0], [2.266, 66.7], [1.7, 133.35]]; drift first→last third 0.022 %) |
| first downbeat | 1.705 s (bar-phase margin 1.541; snare backbeat ratio 2.96) |
| key | F# major [estimate, margin 0.022]; alternatives [['F# minor', 0.476], ['B minor', 0.338]] |
| loudness | -8.53 LUFS integrated, short-term p10/p90 [-9.3, -8.0], crest 10.74 dB, sample peak 0.53 dBFS |
| stereo | side−mid -54.5 dB overall, -120.0 dB below 150 Hz |
| spectrum | 68.9 % of energy ≤150 Hz; centroid 2165.0 Hz; HF content to ~10481 Hz |
| swing (hat 16ths) | 39.9 % (50 straight, 66.7 triplet); off-8th hat delay 28.5 ms |
| perc vs harmonic | -0.8 dB |
| harmonic loop similarity (bar lags) | {'1': -0.841, '2': 0.839, '3': -0.844, '4': 0.837, '8': 0.851} |

**16-step onset occupancy** (X strong, x present; whole track):
```
        1 e & a 2 e & a 3 e & a 4 e & a
kick    x x . . x . x . . . X . x . . x
snare   . x . . X . . . . . . . x . . .
hat     x x X . X . . . x . x . x . x .
```
Median micro-timing per step (ms, + = late): kick [29.2, 47.9, 45.9, -52.0, 23.5, 64.7, 14.0, 5.7, -61.4, -55.7, 16.3, -13.2, 27.6, 30.5, 66.4, -24.9], snare [29.4, 45.3, 40.8, None, 14.9, None, 22.0, 41.9, 39.4, 41.5, 21.4, -28.9, 19.0, None, 35.6, -54.3], hat [-5.7, 35.2, 35.2, None, 15.9, None, 25.1, 30.9, 29.0, -58.0, 20.9, -30.3, 20.1, None, 31.8, -68.8]

**Layer timeline** (per bar vs. track median; NO-LOW = sub ≥6 dB down, NO-DRUMS = percussive ≥6 dB down):
b1:NO-LOW,NO-DRUMS,melody-off | b2:NO-LOW,NO-DRUMS,no-hats,melody-off | b3:full | b4:hats+,melody+ | b5:full | b6:hats+,melody+ | b7:full | b8:hats+,melody+ | b9:full | b10:hats+,melody+ | b11:full | b12:hats+,melody+ | b13:full | b14:hats+,melody+ | b15:full | b16:hats+,melody+ | b17:full | b18:hats+ | b19:full | b20:hats+,melody+ | b21:full | b22:hats+,melody+ | b23:full | b24:hats+,melody+ | b25-27:full | b28:hats+,melody+ | b29:full | b30:hats+,melody+ | b31:full | b32:hats+,melody+ | b33:full | b34:hats+,melody+ | b35:full | b36:hats+,melody+ | b37:full | b38:hats+,melody+ | b39:full | b40:hats+,melody+ | b41:full | b42:hats+,melody+ | b43:full | b44:hats+,melody+ | b45:full | b46:hats+,melody+ | b47:full | b48:hats+,melody+ | b49:full | b50:hats+,melody+ | b51:full | b52:hats+,melody+ | b53-55:full | b56:hats+,melody+ | b57:full | b58:hats+,melody+ | b59:full | b60:hats+,melody+ | b61:full | b62:NO-LOW,NO-DRUMS,melody-off | b63:full | b64:hats+,melody+ | b65:full | b66:hats+,melody+ | b67:full | b68:hats+,melody+ | b69:full | b70:hats+,melody+ | b71:full | b72:hats+,melody+ | b73:full | b74:hats+,melody+ | b75:full | b76:hats+,melody+ | b77:full | b78:hats+,melody+ | b79:full | b80:hats+,melody+ | b81:full | b82:hats+,melody+ | b83:full | b84:hats+,melody+ | b85:full | b86:low-thin,hats+,melody+ | b87:full | b88:hats+,melody+ | b89:full | b90:hats+,melody+ | b91:full | b92:hats+,melody+ | b93:full | b94:hats+,melody+ | b95:full | b96:hats+,melody+ | b97:full | b98:hats+,melody+ | b99:full | b100:hats+,melody+ | b101:full | b102:NO-LOW,NO-DRUMS,hats+,melody+ | b103:full | b104:hats+,melody+ | b105:full | b106:hats+,melody+ | b107:full | b108:hats+,melody+ | b109:full | b110:hats+,melody+ | b111:full | b112:hats+,melody+ | b113:full | b114:hats+,melody+ | b115:full | b116:NO-LOW,NO-DRUMS | b117-118:NO-LOW,NO-DRUMS,no-hats,melody-off

**Bars 2–9 harmonic sketch** [estimate: chroma template + bass chroma; not a transcription]: [Dm7/F#maj7 bass D-D-E-G] [F#maj7/F#m7 bass A#-F-E-F#] [Bm7/Bm7 bass B-G-G-A#] [Bmaj7/F#maj7 bass A#-F-F-F#] [Bm7/Bm7 bass B-G#-G-A#] [Bmaj7/F#maj7 bass A#-F-F-F#] [Bm7/Bm7 bass B-G-G-A#] [Bmaj7/Emaj7 bass A#-F-D#-F]

Pitch-class profile: {'C': 0.46, 'C#': 0.54, 'D': 0.47, 'D#': 0.4, 'E': 0.53, 'F': 0.7, 'F#': 1.0, 'G': 0.68, 'G#': 0.74, 'A': 0.78, 'A#': 0.8, 'B': 0.82}
Bass pitch-class profile: {'C': 0.42, 'C#': 0.39, 'D': 0.42, 'D#': 0.42, 'E': 0.57, 'F': 0.8, 'F#': 1.0, 'G': 0.95, 'G#': 0.92, 'A': 0.87, 'A#': 0.91, 'B': 0.82}
