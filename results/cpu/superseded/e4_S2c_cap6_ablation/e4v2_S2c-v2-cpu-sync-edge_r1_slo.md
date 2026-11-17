# E4 v2 — SLO capacity report — e4v2_S2c-v2-cpu-sync-edge_r1

- Source: `e4v2_S2c-v2-cpu-sync-edge_r1_raw.csv` — request `/api/v1/transcribe`
- SLO: p95 <= 10 s and error rate <= 5% (first 30 s of each 180 s step excluded)

|   step |   users |   requests |   goodput_rps |   p50_s |   p95_s |   p99_s | error_rate   | meets_slo   |
|-------:|--------:|-----------:|--------------:|--------:|--------:|--------:|:-------------|:------------|
|      0 |      20 |        329 |          0.54 |   10.71 |   12.4  |   12.84 | 75.4%        | no          |
|      1 |      60 |       3293 |          0.54 |   11.65 |   12.1  |   12.16 | 97.5%        | no          |
|      2 |     110 |       7007 |          0.61 |    9.93 |   10.21 |   10.25 | 98.7%        | no          |
|      3 |     210 |      14358 |          0.53 |   11.15 |   12.06 |   12.27 | 99.4%        | no          |
|      4 |     510 |      35113 |          0.4  |   15.14 |   15.44 |   15.53 | 99.8%        | no          |
|      5 |    1000 |      36242 |          0.38 |   17.26 |   18.49 |   18.67 | 99.8%        | no          |

## Failure breakdown per step (steady-state window)

|   step |   connection error |   ok |   rejected (429/503) |
|-------:|-------------------:|-----:|---------------------:|
|      0 |                  0 |   81 |                  248 |
|      1 |                  0 |   81 |                 3212 |
|      2 |                  0 |   91 |                 6916 |
|      3 |                  0 |   80 |                14278 |
|      4 |                  0 |   60 |                35053 |
|      5 |                  3 |   57 |                36182 |

## Capacity

- **SLO capacity: 0 concurrent users** (largest step meeting the SLO)
- Peak goodput X_max: 0.61 successful req/s = 14.6 s of audio per second
- Little's-law ceiling with this service rate: N_max = X_max * (R_slo + Z) = 0.61 * (10 + 2) = **7 users**

Interpretation: if a target (e.g. C2.2 = 1000 users) exceeds N_max, no amount of request routing can meet it at this service rate — it requires more inference throughput (GPU, batching, more workers), or a relaxed SLO / async semantics.