# E4 v2 — SLO capacity report — e4v2_S2c-v2-cpu-sync-edge_r3

- Source: `e4v2_S2c-v2-cpu-sync-edge_r3_raw.csv` — request `/api/v1/transcribe`
- SLO: p95 <= 10 s and error rate <= 5% (first 30 s of each 180 s step excluded)

|   step |   users |   requests |   goodput_rps |   p50_s |   p95_s |   p99_s | error_rate   | meets_slo   |
|-------:|--------:|-----------:|--------------:|--------:|--------:|--------:|:-------------|:------------|
|      0 |      50 |        186 |          0.86 |    9.6  |   11.49 |   11.92 | 30.6%        | no          |
|      1 |     100 |       3060 |          0.73 |   13.45 |   14.7  |   14.92 | 96.4%        | no          |
|      2 |     150 |       6758 |          0.65 |   14.88 |   18.12 |   19.42 | 98.5%        | no          |
|      3 |     250 |      13665 |          0.48 |   20.41 |   24.02 |   24.29 | 99.5%        | no          |
|      4 |     550 |      13504 |          0.47 |   24.43 |   28.19 |   28.82 | 99.5%        | no          |
|      5 |    1000 |      11943 |          0.4  |   29.58 |   37.06 |   38.77 | 99.5%        | no          |

## Failure breakdown per step (steady-state window)

|   step |   HTTP 500 |   connection error |   ok |   rejected (429/503) |
|-------:|-----------:|-------------------:|-----:|---------------------:|
|      0 |          0 |                  0 |  129 |                   57 |
|      1 |          0 |                  0 |  110 |                 2950 |
|      2 |          0 |                  0 |   98 |                 6660 |
|      3 |          0 |                  0 |   72 |                13593 |
|      4 |          1 |                  0 |   70 |                13433 |
|      5 |          0 |                168 |   60 |                11715 |

## Capacity

- **SLO capacity: 0 concurrent users** (largest step meeting the SLO)
- Peak goodput X_max: 0.86 successful req/s = 20.7 s of audio per second
- Little's-law ceiling with this service rate: N_max = X_max * (R_slo + Z) = 0.86 * (10 + 2) = **10 users**

Interpretation: if a target (e.g. C2.2 = 1000 users) exceeds N_max, no amount of request routing can meet it at this service rate — it requires more inference throughput (GPU, batching, more workers), or a relaxed SLO / async semantics.