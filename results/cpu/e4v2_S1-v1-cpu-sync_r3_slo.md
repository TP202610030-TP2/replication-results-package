# E4 v2 — SLO capacity report — e4v2_S1-v1-cpu-sync_r3

- Source: `e4v2_S1-v1-cpu-sync_r3_raw.csv` — request `/api/v1/transcribe`
- SLO: p95 <= 10 s and error rate <= 5% (first 30 s of each 180 s step excluded)

|   step |   users |   requests |   goodput_rps |   p50_s |   p95_s |   p99_s | error_rate   | meets_slo   |
|-------:|--------:|-----------:|--------------:|--------:|--------:|--------:|:-------------|:------------|
|      0 |      20 |         59 |          0.39 |   23.39 |   24.18 |   24.32 | 0.0%         | no          |
|      1 |      90 |         71 |          0.39 |   96.15 |  100.03 |  100.18 | 18.3%        | no          |
|      2 |     110 |        119 |          0.05 |  100.1  |  100.26 |  100.27 | 94.1%        | no          |
|      3 |     220 |        228 |          0.13 |   99.9  |  100.32 |  100.35 | 91.2%        | no          |
|      4 |     530 |        584 |          0.07 |   99.88 |  100.28 |  100.34 | 98.3%        | no          |
|      5 |    1000 |       3038 |          0.01 |  100.34 |  100.34 |  100.34 | 100.0%       | no          |

## Failure breakdown per step (steady-state window)

|   step |   HTTP 502 |   ok |   timeout (504) |
|-------:|-----------:|-----:|----------------:|
|      0 |          0 |   59 |               0 |
|      1 |          0 |   58 |              13 |
|      2 |          0 |    7 |             112 |
|      3 |          0 |   20 |             208 |
|      4 |          0 |   10 |             574 |
|      5 |       1878 |    1 |            1159 |

## Capacity

- **SLO capacity: 0 concurrent users** (largest step meeting the SLO)
- Peak goodput X_max: 0.39 successful req/s = 9.5 s of audio per second
- Little's-law ceiling with this service rate: N_max = X_max * (R_slo + Z) = 0.39 * (10 + 2) = **5 users**

Interpretation: if a target (e.g. C2.2 = 1000 users) exceeds N_max, no amount of request routing can meet it at this service rate — it requires more inference throughput (GPU, batching, more workers), or a relaxed SLO / async semantics.