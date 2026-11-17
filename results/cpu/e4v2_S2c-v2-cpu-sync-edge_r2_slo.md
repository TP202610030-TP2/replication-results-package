# E4 v2 — SLO capacity report — e4v2_S2c-v2-cpu-sync-edge_r2

- Source: `e4v2_S2c-v2-cpu-sync-edge_r2_raw.csv` — request `/api/v1/transcribe`
- SLO: p95 <= 10 s and error rate <= 5% (first 30 s of each 180 s step excluded)

|   step |   users |   requests |   goodput_rps |   p50_s |   p95_s |   p99_s | error_rate   | meets_slo   |
|-------:|--------:|-----------:|--------------:|--------:|--------:|--------:|:-------------|:------------|
|      0 |      50 |        253 |          0.86 |    9.4  |   10.97 |   11.24 | 49.0%        | no          |
|      1 |     100 |       3074 |          0.75 |   13.25 |   14.46 |   14.79 | 96.4%        | no          |
|      2 |     180 |       6826 |          0.67 |   14.16 |   17.26 |   17.68 | 98.5%        | no          |
|      3 |     270 |      13420 |          0.47 |   21.25 |   22.91 |   23.36 | 99.5%        | no          |
|      4 |     580 |      13411 |          0.48 |   23.34 |   27.47 |   27.74 | 99.5%        | no          |
|      5 |    1000 |      12069 |          0.41 |   27.4  |   33.8  |   35.56 | 99.5%        | no          |

## Failure breakdown per step (steady-state window)

|   step |   connection error |   ok |   rejected (429/503) |
|-------:|-------------------:|-----:|---------------------:|
|      0 |                  0 |  129 |                  124 |
|      1 |                  0 |  112 |                 2962 |
|      2 |                  0 |  101 |                 6725 |
|      3 |                  0 |   70 |                13350 |
|      4 |                  0 |   72 |                13339 |
|      5 |                 30 |   62 |                11977 |

## Capacity

- **SLO capacity: 0 concurrent users** (largest step meeting the SLO)
- Peak goodput X_max: 0.86 successful req/s = 20.7 s of audio per second
- Little's-law ceiling with this service rate: N_max = X_max * (R_slo + Z) = 0.86 * (10 + 2) = **10 users**

Interpretation: if a target (e.g. C2.2 = 1000 users) exceeds N_max, no amount of request routing can meet it at this service rate — it requires more inference throughput (GPU, batching, more workers), or a relaxed SLO / async semantics.