# E4 v2 — SLO capacity report — e3v2_proposed_r3

- Source: `e3v2_proposed_r3_raw.csv` — request `/api/v1/transcribe`
- SLO: p95 <= 10 s and error rate <= 5% (first 30 s of each 180 s step excluded)

|   step |   users |   requests |   goodput_rps |   p50_s |   p95_s |   p99_s | error_rate   | meets_slo   |
|-------:|--------:|-----------:|--------------:|--------:|--------:|--------:|:-------------|:------------|
|      0 |      50 |        190 |          0.59 |   14.14 |   19.69 |   20.28 | 53.2%        | no          |
|      1 |     100 |       3121 |          0.59 |   16.84 |   18.3  |   18.76 | 97.1%        | no          |
|      2 |     170 |       6786 |          0.53 |   18.54 |   19.45 |   19.98 | 98.8%        | no          |
|      3 |     270 |      14207 |          0.44 |   21.99 |   25.01 |   25.12 | 99.5%        | no          |
|      4 |     570 |      16652 |          0.4  |   26.93 |   30.38 |   30.92 | 99.6%        | no          |
|      5 |    1013 |      15222 |          0.37 |   29.76 |   35.82 |   36.66 | 99.6%        | no          |

## Failure breakdown per step (steady-state window)

|   step |   connection error |   ok |   rejected (429/503) |
|-------:|-------------------:|-----:|---------------------:|
|      0 |                  0 |   89 |                  101 |
|      1 |                  0 |   89 |                 3032 |
|      2 |                  0 |   80 |                 6706 |
|      3 |                  0 |   66 |                14141 |
|      4 |                  0 |   60 |                16592 |
|      5 |                 22 |   56 |                15144 |

## Capacity

- **SLO capacity: 0 concurrent users** (largest step meeting the SLO)
- Peak goodput X_max: 0.59 successful req/s
- Little's-law ceiling with this service rate: N_max = X_max * (R_slo + Z) = 0.59 * (10 + 2) = **7 users**

Interpretation: if a target (e.g. C2.2 = 1000 users) exceeds N_max, no amount of request routing can meet it at this service rate — it requires more inference throughput (GPU, batching, more workers), or a relaxed SLO / async semantics.