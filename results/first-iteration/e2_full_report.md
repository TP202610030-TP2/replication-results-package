# E2 — WER / CER / RTF Report

## Overall

| Metric | n | value | interval | basis |
|---|---|---|---|---|
| WER | 2111 | 0.697 | [0.500, 0.852] | median±IQR (non-normal, Shapiro p=0.000) |
| CER | 2111 | 0.172 | [0.089, 0.343] | median±IQR (non-normal, Shapiro p=0.000) |
| RTF | 2111 | 0.149 | [0.120, 0.201] | median±IQR (non-normal, Shapiro p=0.000) |

## RTF por dispositivo

| Device / compute_type | n | value | interval | basis |
|---|---|---|---|---|
| cpu/fp32 | 2111 | 0.149 | [0.120, 0.201] | median±IQR (non-normal, Shapiro p=0.000) |

## WER por duración de clip (bucketed)

| duration_bucket   |   count |     mean |
|:------------------|--------:|---------:|
| 0-5s              |     386 | 0.573694 |
| 5-15s             |     522 | 0.50163  |
| 15-30s            |    1202 | 0.789218 |
| 30-60s            |       1 | 0.59375  |

## WER / CER / RTF por fuente del corpus

| source                                            |    n |   wer_median |   wer_mean |   cer_median |   rtf_median |
|:--------------------------------------------------|-----:|-------------:|-----------:|-------------:|-------------:|
| huqariq (IWSLT2026/que_spa_synthetic_translation) | 1413 |        0.714 |      0.705 |        0.192 |        0.135 |
| siminchik (IWSLT2026/que_spa_unconstrained)       |  698 |        0.638 |      0.625 |        0.121 |        0.183 |

- **Clips con WER > 1.5** (posible alucinación/inserción excesiva): 13 (0.6%)
- **Clips con WER = 0** (transcripción perfecta): 46 (2.2%)
- **Transcripciones vacías** (posible timeout/fallo silencioso): 0