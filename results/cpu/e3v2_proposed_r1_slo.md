# E4 v2 — SLO capacity report — e3v2_proposed_r1

- Source: `e3v2_proposed_r1_raw.csv` — request `/api/v1/transcribe`
- SLO: p95 <= 10 s and error rate <= 5% (first 30 s of each 180 s step excluded)

|   step |   users |   requests |   goodput_rps |   p50_s |   p95_s |   p99_s | error_rate   | meets_slo   |
|-------:|--------:|-----------:|--------------:|--------:|--------:|--------:|:-------------|:------------|
|      0 |      50 |        195 |          0.57 |   15.26 |   18.42 |   19.18 | 55.9%        | no          |
|      1 |     100 |       3105 |          0.57 |   16.82 |   20.92 |   22.01 | 97.3%        | no          |
|      2 |     180 |       6788 |          0.41 |   23.75 |   26.82 |   27.01 | 99.1%        | no          |
|      3 |     270 |      12726 |          0.31 |   32.31 |   34.99 |   35.22 | 99.6%        | no          |
|      4 |     570 |      12439 |          0.31 |   35.31 |   38.4  |   38.63 | 99.6%        | no          |
|      5 |    1000 |      11671 |          0.29 |   39.49 |   42.96 |   45.49 | 99.6%        | no          |

## Failure breakdown per step (steady-state window)

|   step |   connection error |   ok |   rejected (429/503) |
|-------:|-------------------:|-----:|---------------------:|
|      0 |                  0 |   86 |                  109 |
|      1 |                  0 |   85 |                 3020 |
|      2 |                  0 |   62 |                 6726 |
|      3 |                  0 |   46 |                12680 |
|      4 |                  0 |   46 |                12393 |
|      5 |                106 |   44 |                11521 |

## Capacity

- **SLO capacity: 0 concurrent users** (largest step meeting the SLO)
- Peak goodput X_max: 0.57 successful req/s
- Little's-law ceiling with this service rate: N_max = X_max * (R_slo + Z) = 0.57 * (10 + 2) = **7 users**

Interpretation: if a target (e.g. C2.2 = 1000 users) exceeds N_max, no amount of request routing can meet it at this service rate — it requires more inference throughput (GPU, batching, more workers), or a relaxed SLO / async semantics.