# E4 v2 — SLO capacity report — e4v2_S2c-v2-cpu-sync-edge_r3

- Source: `e4v2_S2c-v2-cpu-sync-edge_r3_raw.csv` — request `/api/v1/transcribe`
- SLO: p95 <= 10 s and error rate <= 5% (first 30 s of each 180 s step excluded)

|   step |   users |   requests |   goodput_rps |   p50_s |   p95_s |   p99_s | error_rate   | meets_slo   |
|-------:|--------:|-----------:|--------------:|--------:|--------:|--------:|:-------------|:------------|
|      0 |      10 |        376 |          0.43 |    9.83 |   17.01 |   18.61 | 82.7%        | no          |
|      1 |      50 |       2977 |          0.75 |   12.84 |   14.91 |   16.05 | 96.2%        | no          |
|      2 |     100 |       6688 |          0.67 |   14.78 |   16.31 |   16.59 | 98.5%        | no          |
|      3 |     200 |      14063 |          0.71 |   14.18 |   14.99 |   17.89 | 99.2%        | no          |
|      4 |     510 |      13499 |          0.48 |   23.03 |   27.79 |   28.28 | 99.5%        | no          |
|      5 |    1000 |      11990 |          0.36 |   30.93 |   39.76 |   41.13 | 99.5%        | no          |

## Failure breakdown per step (steady-state window)

|   step |   HTTP 500 |   connection error |   ok |   rejected (429/503) |
|-------:|-----------:|-------------------:|-----:|---------------------:|
|      0 |          0 |                  0 |   65 |                  311 |
|      1 |          0 |                  0 |  113 |                 2864 |
|      2 |          0 |                  0 |  101 |                 6587 |
|      3 |          0 |                  0 |  106 |                13957 |
|      4 |          1 |                  0 |   72 |                13426 |
|      5 |          0 |                 34 |   54 |                11902 |

## Capacity

- **SLO capacity: 0 concurrent users** (largest step meeting the SLO)
- Peak goodput X_max: 0.75 successful req/s = 18.1 s of audio per second
- Little's-law ceiling with this service rate: N_max = X_max * (R_slo + Z) = 0.75 * (10 + 2) = **9 users**

Interpretation: if a target (e.g. C2.2 = 1000 users) exceeds N_max, no amount of request routing can meet it at this service rate — it requires more inference throughput (GPU, batching, more workers), or a relaxed SLO / async semantics.