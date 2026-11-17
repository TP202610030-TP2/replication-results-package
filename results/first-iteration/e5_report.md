# E5 — Raw PCM vs. Compressed Streaming Report

| Condition | n | WER (mean±CI95) | CER (mean±CI95) | Latency s (mean±CI95) | Bytes sent (mean) |
|---|---|---|---|---|---|
| pcm | 90 | 0.735±[0.668,0.801] | 0.261±[0.206,0.316] | 11.56±[10.20,12.91] | 582785 |
| opus | 90 | 0.736±[0.660,0.812] | 0.271±[0.206,0.335] | 5.34±[4.73,5.95] | 165071 |

## Hypothesis test (PCM vs. comprimido)

| Metric | Test | p-value | Effect size | Significant at 0.05? |
|---|---|---|---|---|
| WER | mann-whitney-u | 0.6716 | cliffs_delta=0.037 | no |
| CER | mann-whitney-u | 0.9703 | cliffs_delta=0.003 | no |
| Latency | mann-whitney-u | 0.0000 | cliffs_delta=0.523 | yes |

**Interpretación**: si WER/CER del canal comprimido son significativamente mayores (p<0.05, effect size no despreciable), la afirmación de alucinación por compresión queda soportada empíricamente. Si no, hay que corregir esa afirmación en el paper.