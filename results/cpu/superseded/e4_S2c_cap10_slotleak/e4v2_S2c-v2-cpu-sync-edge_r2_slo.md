# E4 v2 — SLO capacity report — e4v2_S2c-v2-cpu-sync-edge_r2

- Source: `e4v2_S2c-v2-cpu-sync-edge_r2_raw.csv` — request `/api/v1/transcribe`
- SLO: p95 <= 10 s and error rate <= 5% (first 30 s of each 180 s step excluded)

|   step |   users |   requests |   goodput_rps |   p50_s |   p95_s |   p99_s | error_rate   | meets_slo   |
|-------:|--------:|-----------:|--------------:|--------:|--------:|--------:|:-------------|:------------|
|      0 |      20 |        294 |          0.84 |    7.51 |   11.05 |   12.63 | 57.1%        | no          |
|      1 |      60 |       3021 |          0.99 |   10    |   10.98 |   11.52 | 95.1%        | no          |
|      2 |     110 |       6661 |          0.95 |   10.43 |   10.79 |   10.88 | 97.9%        | no          |
|      3 |     200 |      14111 |          0.87 |   11.23 |   13.7  |   14.2  | 99.1%        | no          |
|      4 |     510 |      33045 |          0.53 |   18.69 |   20.67 |   21.14 | 99.8%        | no          |
|      5 |    1000 |      29365 |          0.49 |   22.14 |   24.7  |   25.68 | 99.8%        | no          |

## Failure breakdown per step (steady-state window)

|   step |   connection error |   ok |   rejected (429/503) |
|-------:|-------------------:|-----:|---------------------:|
|      0 |                  0 |  126 |                  168 |
|      1 |                  0 |  149 |                 2872 |
|      2 |                  0 |  143 |                 6518 |
|      3 |                  0 |  130 |                13981 |
|      4 |                  0 |   80 |                32965 |
|      5 |                  7 |   73 |                29285 |

## Capacity

- **SLO capacity: 0 concurrent users** (largest step meeting the SLO)
- Peak goodput X_max: 0.99 successful req/s = 23.9 s of audio per second
- Little's-law ceiling with this service rate: N_max = X_max * (R_slo + Z) = 0.99 * (10 + 2) = **12 users**

Interpretation: if a target (e.g. C2.2 = 1000 users) exceeds N_max, no amount of request routing can meet it at this service rate — it requires more inference throughput (GPU, batching, more workers), or a relaxed SLO / async semantics.