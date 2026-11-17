# E8 — Inference throughput

| label         |   concurrency |   requests |   req_per_s |   audio_s_per_s |   p50_s |   p95_s | error_rate   | device   | compute   |
|:--------------|--------------:|-----------:|------------:|----------------:|--------:|--------:|:-------------|:---------|:----------|
| ct2-fp32-l1t6 |             1 |         20 |        0.43 |            8.32 |    2.01 |    3.93 | 0.0%         | cpu      | fp32      |
| ct2-fp32-l1t6 |             2 |         23 |        0.46 |            8.53 |    4.29 |    7.05 | 0.0%         | cpu      | fp32      |
| ct2-fp32-l1t6 |             4 |         26 |        0.49 |            8.28 |    7.74 |   11.74 | 0.0%         | cpu      | fp32      |
| ct2-fp32-l1t6 |             8 |         29 |        0.46 |            8.26 |   16.1  |   20.31 | 0.0%         | cpu      | fp32      |
| ct2-fp32-l1t6 |            16 |         37 |        0.46 |            8.59 |   33.26 |   37.14 | 0.0%         | cpu      | fp32      |
| ct2-fp32-l3t2 |             1 |         19 |        0.39 |            7.5  |    2.18 |    4.05 | 0.0%         | cpu      | fp32      |
| ct2-fp32-l3t2 |             2 |         25 |        0.52 |            9.84 |    3.37 |    6.16 | 0.0%         | cpu      | fp32      |
| ct2-fp32-l3t2 |             4 |         30 |        0.58 |           10.55 |    6.24 |   10.08 | 0.0%         | cpu      | fp32      |
| ct2-fp32-l3t2 |             8 |         32 |        0.58 |           10.06 |   13.76 |   19.31 | 0.0%         | cpu      | fp32      |
| ct2-fp32-l3t2 |            16 |         40 |        0.57 |           10.64 |   28.18 |   32.95 | 0.0%         | cpu      | fp32      |
| ct2-int8-l1t6 |             1 |         36 |        0.76 |           13.49 |    1.14 |    2.21 | 0.0%         | cpu      | int8      |
| ct2-int8-l1t6 |             2 |         35 |        0.73 |           14.09 |    2.63 |    3.94 | 0.0%         | cpu      | int8      |
| ct2-int8-l1t6 |             4 |         36 |        0.74 |           13.12 |    5.34 |    6.66 | 0.0%         | cpu      | int8      |
| ct2-int8-l1t6 |             8 |         40 |        0.72 |           13.87 |   11.07 |   12.53 | 0.0%         | cpu      | int8      |
| ct2-int8-l1t6 |            16 |         51 |        0.76 |           13.36 |   20.76 |   23.45 | 0.0%         | cpu      | int8      |
| ct2-int8-l2t3 |             1 |         32 |        0.7  |           12.53 |    1.23 |    2.31 | 0.0%         | cpu      | int8      |
| ct2-int8-l2t3 |             2 |         42 |        0.92 |           17.68 |    2.03 |    3.45 | 0.0%         | cpu      | int8      |
| ct2-int8-l2t3 |             4 |         45 |        0.94 |           16.71 |    4.34 |    6.15 | 0.0%         | cpu      | int8      |
| ct2-int8-l2t3 |             8 |         49 |        0.94 |           16.94 |    8.51 |   10.18 | 0.0%         | cpu      | int8      |
| ct2-int8-l2t3 |            16 |         56 |        0.94 |           17.48 |   16.03 |   19.47 | 0.0%         | cpu      | int8      |
| ct2-int8-l2t6 |             1 |         21 |        0.46 |            8.72 |    1.75 |    4.08 | 0.0%         | cpu      | int8      |
| ct2-int8-l2t6 |             2 |         34 |        0.74 |           14.14 |    2.49 |    4.9  | 0.0%         | cpu      | int8      |
| ct2-int8-l2t6 |             4 |         39 |        0.82 |           13.24 |    4.55 |    7.76 | 0.0%         | cpu      | int8      |
| ct2-int8-l2t6 |             8 |         40 |        0.71 |           14.23 |   10.52 |   14.08 | 0.0%         | cpu      | int8      |
| ct2-int8-l2t6 |            16 |         50 |        0.8  |           13.44 |   20.09 |   23.93 | 0.0%         | cpu      | int8      |
| ct2-int8-l3t2 |             1 |         29 |        0.64 |           11.97 |    1.49 |    2.42 | 0.0%         | cpu      | int8      |
| ct2-int8-l3t2 |             2 |         45 |        0.98 |           18.25 |    1.81 |    3.41 | 0.0%         | cpu      | int8      |
| ct2-int8-l3t2 |             4 |         54 |        1.12 |           19.86 |    3.5  |    5.01 | 0.0%         | cpu      | int8      |
| ct2-int8-l3t2 |             8 |         54 |        1.08 |           19.32 |    7.32 |    9.2  | 0.0%         | cpu      | int8      |
| ct2-int8-l3t2 |            16 |         63 |        1.1  |           19.73 |   14.22 |   17.54 | 0.0%         | cpu      | int8      |
| ct2-int8-l3t4 |             1 |         24 |        0.52 |           10.37 |    1.92 |    3.38 | 0.0%         | cpu      | int8      |
| ct2-int8-l3t4 |             2 |         41 |        0.88 |           14.45 |    1.91 |    4.43 | 0.0%         | cpu      | int8      |
| ct2-int8-l3t4 |             4 |         46 |        0.93 |           17.77 |    3.84 |    7.03 | 0.0%         | cpu      | int8      |
| ct2-int8-l3t4 |             8 |         52 |        0.97 |           18.11 |    7.52 |   10.28 | 0.0%         | cpu      | int8      |
| ct2-int8-l3t4 |            16 |         59 |        0.98 |           17.73 |   15.22 |   18.69 | 0.0%         | cpu      | int8      |
| ct2-int8-l4t3 |             1 |         36 |        0.77 |           13.62 |    1.13 |    2.06 | 0.0%         | cpu      | int8      |
| ct2-int8-l4t3 |             2 |         43 |        0.93 |           17.69 |    2.01 |    3.37 | 0.0%         | cpu      | int8      |
| ct2-int8-l4t3 |             4 |         49 |        1.03 |           18.46 |    3.29 |    6.23 | 0.0%         | cpu      | int8      |
| ct2-int8-l4t3 |             8 |         51 |        1.01 |           18.48 |    7.81 |   10.48 | 0.0%         | cpu      | int8      |
| ct2-int8-l4t3 |            16 |         60 |        1.04 |           18.98 |   14.05 |   19.06 | 0.0%         | cpu      | int8      |
| ct2-int8-l6t1 |             1 |         19 |        0.42 |            7.97 |    2.11 |    3.62 | 0.0%         | cpu      | int8      |
| ct2-int8-l6t1 |             2 |         34 |        0.74 |           13.87 |    2.59 |    4.11 | 0.0%         | cpu      | int8      |
| ct2-int8-l6t1 |             4 |         51 |        1.05 |           19.08 |    3.24 |    6.23 | 0.0%         | cpu      | int8      |
| ct2-int8-l6t1 |             8 |         56 |        1.1  |           19.54 |    6.67 |   10.06 | 0.0%         | cpu      | int8      |
| ct2-int8-l6t1 |            16 |         60 |        1.08 |           19.64 |   13.34 |   19.18 | 0.0%         | cpu      | int8      |

## Peak throughput per configuration

- `ct2-fp32-l1t6`: 8.6 s of audio per second
- `ct2-fp32-l3t2`: 10.6 s of audio per second
- `ct2-int8-l1t6`: 14.1 s of audio per second
- `ct2-int8-l2t6`: 14.2 s of audio per second
- `ct2-int8-l2t3`: 17.7 s of audio per second
- `ct2-int8-l3t4`: 18.1 s of audio per second
- `ct2-int8-l4t3`: 19.0 s of audio per second
- `ct2-int8-l6t1`: 19.6 s of audio per second
- `ct2-int8-l3t2`: 19.9 s of audio per second

## Output-preservation control (WER per configuration)

- `ct2-fp32-l1t6`: corpus WER 0.854 over 135 transcriptions
- `ct2-fp32-l3t2`: corpus WER 0.845 over 146 transcriptions
- `ct2-int8-l1t6`: corpus WER 0.847 over 198 transcriptions
- `ct2-int8-l2t3`: corpus WER 0.848 over 224 transcriptions
- `ct2-int8-l2t6`: corpus WER 0.839 over 184 transcriptions
- `ct2-int8-l3t2`: corpus WER 0.839 over 245 transcriptions
- `ct2-int8-l3t4`: corpus WER 0.845 over 222 transcriptions
- `ct2-int8-l4t3`: corpus WER 0.842 over 239 transcriptions
- `ct2-int8-l6t1`: corpus WER 0.847 over 220 transcriptions