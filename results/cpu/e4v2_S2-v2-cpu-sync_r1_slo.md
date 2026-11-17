# E4 v2 — SLO capacity report — e4v2_S2-v2-cpu-sync_r1

- Source: `e4v2_S2-v2-cpu-sync_r1_raw.csv` — request `/api/v1/transcribe`
- SLO: p95 <= 10 s and error rate <= 5% (first 30 s of each 180 s step excluded)

|   step |   users |   requests |   goodput_rps |   p50_s |   p95_s |   p99_s | error_rate   | meets_slo   |
|-------:|--------:|-----------:|--------------:|--------:|--------:|--------:|:-------------|:------------|
|      0 |      50 |        130 |          0.86 |    9.4  |   11.18 |   11.51 | 0.8%         | no          |
|      1 |     100 |        292 |          0.79 |   58.04 |   62.9  |   65.42 | 59.6%        | no          |
|      2 |     170 |       2165 |          0.31 |   65.52 |   95.48 |   99.35 | 97.9%        | no          |
|      3 |     260 |       2299 |          0.31 |   72.75 |   79.89 |   82.84 | 98.0%        | no          |
|      4 |     570 |       2335 |          0.37 |   80.66 |  100.48 |  109.51 | 97.6%        | no          |
|      5 |    1000 |       1905 |          0.2  |  105.88 |  123.85 |  128.84 | 98.4%        | no          |

## Failure breakdown per step (steady-state window)

|   step |   HTTP 500 |   ok |   rejected (429/503) |   timeout (504) |
|-------:|-----------:|-----:|---------------------:|----------------:|
|      0 |          0 |  129 |                    1 |               0 |
|      1 |          0 |  118 |                  174 |               0 |
|      2 |          0 |   46 |                 2100 |              19 |
|      3 |          0 |   47 |                 2252 |               0 |
|      4 |        168 |   56 |                 2110 |               1 |
|      5 |       1491 |   30 |                  372 |              12 |

## Capacity

- **SLO capacity: 0 concurrent users** (largest step meeting the SLO)
- Peak goodput X_max: 0.86 successful req/s = 20.7 s of audio per second
- Little's-law ceiling with this service rate: N_max = X_max * (R_slo + Z) = 0.86 * (10 + 2) = **10 users**

Interpretation: if a target (e.g. C2.2 = 1000 users) exceeds N_max, no amount of request routing can meet it at this service rate — it requires more inference throughput (GPU, batching, more workers), or a relaxed SLO / async semantics.