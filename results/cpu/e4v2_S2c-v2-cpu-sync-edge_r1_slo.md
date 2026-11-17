# E4 v2 — SLO capacity report — e4v2_S2c-v2-cpu-sync-edge_r1

- Source: `e4v2_S2c-v2-cpu-sync-edge_r1_raw.csv` — request `/api/v1/transcribe`
- SLO: p95 <= 10 s and error rate <= 5% (first 30 s of each 180 s step excluded)

|   step |   users |   requests |   goodput_rps |   p50_s |   p95_s |   p99_s | error_rate   | meets_slo   |
|-------:|--------:|-----------:|--------------:|--------:|--------:|--------:|:-------------|:------------|
|      0 |      50 |        257 |          0.87 |    9.33 |   11.25 |   12.13 | 49.0%        | no          |
|      1 |     100 |       3127 |          0.84 |   11.83 |   12.86 |   13.05 | 96.0%        | no          |
|      2 |     180 |       6877 |          0.84 |   11.85 |   13.91 |   14.12 | 98.2%        | no          |
|      3 |     280 |      14252 |          0.68 |   14.01 |   17.14 |   19.16 | 99.3%        | no          |
|      4 |     570 |      31730 |          0.48 |   20.83 |   22.25 |   22.88 | 99.8%        | no          |
|      5 |    1000 |      28216 |          0.47 |   22.8  |   25.87 |   27.23 | 99.7%        | no          |

## Failure breakdown per step (steady-state window)

|   step |   connection error |   ok |   rejected (429/503) |
|-------:|-------------------:|-----:|---------------------:|
|      0 |                  0 |  131 |                  126 |
|      1 |                  0 |  126 |                 3001 |
|      2 |                  0 |  126 |                 6751 |
|      3 |                  0 |  102 |                14150 |
|      4 |                  0 |   72 |                31658 |
|      5 |                 14 |   71 |                28131 |

## Capacity

- **SLO capacity: 0 concurrent users** (largest step meeting the SLO)
- Peak goodput X_max: 0.87 successful req/s = 21.0 s of audio per second
- Little's-law ceiling with this service rate: N_max = X_max * (R_slo + Z) = 0.87 * (10 + 2) = **10 users**

Interpretation: if a target (e.g. C2.2 = 1000 users) exceeds N_max, no amount of request routing can meet it at this service rate — it requires more inference throughput (GPU, batching, more workers), or a relaxed SLO / async semantics.