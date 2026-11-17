# E4 v2 — SLO capacity report — e4v2_S1-v1-cpu-sync_r1

- Source: `e4v2_S1-v1-cpu-sync_r1_raw.csv` — request `/api/v1/transcribe`
- SLO: p95 <= 10 s and error rate <= 5% (first 30 s of each 180 s step excluded)

|   step |   users |   requests |   goodput_rps | p50_s   | p95_s   | p99_s   | error_rate   | meets_slo   |
|-------:|--------:|-----------:|--------------:|:--------|:--------|:--------|:-------------|:------------|
|      0 |      10 |         51 |          0.34 | 26.94   | 28.12   | 28.35   | 0.0%         | no          |
|      1 |      90 |         68 |          0.33 | 96.41   | 99.97   | 100.21  | 27.9%        | no          |
|      2 |     140 |        119 |          0.27 | 99.09   | 100.10  | 100.30  | 66.4%        | no          |
|      3 |     230 |        231 |          0.03 | 99.83   | 99.98   | 99.98   | 98.3%        | no          |
|      4 |     530 |        536 |          0.03 | 99.99   | 100.30  | 100.34  | 99.3%        | no          |
|      5 |    1000 |       2968 |          0    | —       | —       | —       | 100.0%       | no          |

## Failure breakdown per step (steady-state window)

|   step |   HTTP 502 |   ok |   timeout (504) |
|-------:|-----------:|-----:|----------------:|
|      0 |          0 |   51 |               0 |
|      1 |          0 |   49 |              19 |
|      2 |          0 |   40 |              79 |
|      3 |          0 |    4 |             227 |
|      4 |          0 |    4 |             532 |
|      5 |       1841 |    0 |            1127 |

## Capacity

- **SLO capacity: 0 concurrent users** (largest step meeting the SLO)
- Peak goodput X_max: 0.34 successful req/s = 8.2 s of audio per second
- Little's-law ceiling with this service rate: N_max = X_max * (R_slo + Z) = 0.34 * (10 + 2) = **4 users**

Interpretation: if a target (e.g. C2.2 = 1000 users) exceeds N_max, no amount of request routing can meet it at this service rate — it requires more inference throughput (GPU, batching, more workers), or a relaxed SLO / async semantics.