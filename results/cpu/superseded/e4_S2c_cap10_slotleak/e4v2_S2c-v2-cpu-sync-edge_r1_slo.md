# E4 v2 — SLO capacity report — e4v2_S2c-v2-cpu-sync-edge_r1

- Source: `e4v2_S2c-v2-cpu-sync-edge_r1_raw.csv` — request `/api/v1/transcribe`
- SLO: p95 <= 10 s and error rate <= 5% (first 30 s of each 180 s step excluded)

|   step |   users |   requests |   goodput_rps |   p50_s |   p95_s |   p99_s | error_rate   | meets_slo   |
|-------:|--------:|-----------:|--------------:|--------:|--------:|--------:|:-------------|:------------|
|      0 |      30 |        167 |          0.99 |    7.51 |   11.8  |   13.23 | 10.8%        | no          |
|      1 |      70 |       3002 |          1.03 |    9.46 |   10.96 |   11.63 | 94.9%        | no          |
|      2 |     120 |       6745 |          0.99 |    9.97 |   11.45 |   12.15 | 97.8%        | no          |
|      3 |     210 |      14188 |          0.91 |   10.52 |   12.23 |   12.81 | 99.0%        | no          |
|      4 |     520 |      35895 |          0.67 |   14.94 |   16.28 |   16.54 | 99.7%        | no          |
|      5 |    1000 |      38721 |          0.62 |   17.52 |   19.74 |   21.25 | 99.8%        | no          |

## Failure breakdown per step (steady-state window)

|   step |   connection error |   ok |   rejected (429/503) |
|-------:|-------------------:|-----:|---------------------:|
|      0 |                  0 |  149 |                   18 |
|      1 |                  0 |  154 |                 2848 |
|      2 |                  0 |  149 |                 6596 |
|      3 |                  0 |  137 |                14051 |
|      4 |                  0 |  100 |                35795 |
|      5 |                  6 |   93 |                38622 |

## Capacity

- **SLO capacity: 0 concurrent users** (largest step meeting the SLO)
- Peak goodput X_max: 1.03 successful req/s = 24.7 s of audio per second
- Little's-law ceiling with this service rate: N_max = X_max * (R_slo + Z) = 1.03 * (10 + 2) = **12 users**

Interpretation: if a target (e.g. C2.2 = 1000 users) exceeds N_max, no amount of request routing can meet it at this service rate — it requires more inference throughput (GPU, batching, more workers), or a relaxed SLO / async semantics.