# E4 v2 — SLO capacity report — e3v2_proposed_r2

- Source: `e3v2_proposed_r2_raw.csv` — request `/api/v1/transcribe`
- SLO: p95 <= 10 s and error rate <= 5% (first 30 s of each 180 s step excluded)

|   step |   users |   requests |   goodput_rps |   p50_s |   p95_s |   p99_s | error_rate   | meets_slo   |
|-------:|--------:|-----------:|--------------:|--------:|--------:|--------:|:-------------|:------------|
|      0 |      50 |        212 |          0.57 |   15.47 |   19.21 |   19.93 | 59.9%        | no          |
|      1 |     100 |       3148 |          0.51 |   18.93 |   22.85 |   23.26 | 97.6%        | no          |
|      2 |     180 |       6838 |          0.45 |   21.46 |   24.79 |   27.13 | 99.0%        | no          |
|      3 |     280 |      13850 |          0.33 |   28.76 |   34.21 |   34.25 | 99.6%        | no          |
|      4 |     570 |      13914 |          0.35 |   30.78 |   34.09 |   34.93 | 99.6%        | no          |
|      5 |    1067 |      14673 |          0.35 |   31.4  |   37.93 |   40.3  | 99.6%        | no          |

## Failure breakdown per step (steady-state window)

|   step |   connection error |   ok |   rejected (429/503) |
|-------:|-------------------:|-----:|---------------------:|
|      0 |                  0 |   85 |                  127 |
|      1 |                  0 |   76 |                 3072 |
|      2 |                  0 |   67 |                 6771 |
|      3 |                  0 |   49 |                13801 |
|      4 |                  0 |   52 |                13862 |
|      5 |                  7 |   52 |                14614 |

## Capacity

- **SLO capacity: 0 concurrent users** (largest step meeting the SLO)
- Peak goodput X_max: 0.57 successful req/s
- Little's-law ceiling with this service rate: N_max = X_max * (R_slo + Z) = 0.57 * (10 + 2) = **7 users**

Interpretation: if a target (e.g. C2.2 = 1000 users) exceeds N_max, no amount of request routing can meet it at this service rate — it requires more inference throughput (GPU, batching, more workers), or a relaxed SLO / async semantics.