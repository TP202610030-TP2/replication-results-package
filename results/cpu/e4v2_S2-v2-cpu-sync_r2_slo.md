# E4 v2 — SLO capacity report — e4v2_S2-v2-cpu-sync_r2

- Source: `e4v2_S2-v2-cpu-sync_r2_raw.csv` — request `/api/v1/transcribe`
- SLO: p95 <= 10 s and error rate <= 5% (first 30 s of each 180 s step excluded)

|   step |   users |   requests |   goodput_rps |   p50_s |   p95_s |   p99_s | error_rate   | meets_slo   |
|-------:|--------:|-----------:|--------------:|--------:|--------:|--------:|:-------------|:------------|
|      0 |      50 |        135 |          0.87 |    9.2  |   10.83 |   11.59 | 3.0%         | no          |
|      1 |     100 |        195 |          0.84 |   55.05 |   57.06 |   57.89 | 35.4%        | no          |
|      2 |     170 |       2104 |          0.3  |   62.22 |   97.36 |   99.19 | 97.9%        | no          |
|      3 |     270 |       2316 |          0.31 |   75.71 |   87.83 |   91.55 | 98.0%        | no          |
|      4 |     570 |       2292 |          0.39 |   83.04 |  104.09 |  109.05 | 97.5%        | no          |
|      5 |    1000 |       1892 |          0.21 |  110.93 |  125.91 |  126.86 | 98.3%        | no          |

## Failure breakdown per step (steady-state window)

|   step |   HTTP 500 |   ok |   rejected (429/503) |   timeout (504) |
|-------:|-----------:|-----:|---------------------:|----------------:|
|      0 |          0 |  131 |                    4 |               0 |
|      1 |          0 |  126 |                   69 |               0 |
|      2 |          0 |   45 |                 2038 |              21 |
|      3 |          0 |   46 |                 2270 |               0 |
|      4 |        185 |   58 |                 2049 |               0 |
|      5 |       1459 |   32 |                  390 |              11 |

## Capacity

- **SLO capacity: 0 concurrent users** (largest step meeting the SLO)
- Peak goodput X_max: 0.87 successful req/s = 21.0 s of audio per second
- Little's-law ceiling with this service rate: N_max = X_max * (R_slo + Z) = 0.87 * (10 + 2) = **10 users**

Interpretation: if a target (e.g. C2.2 = 1000 users) exceeds N_max, no amount of request routing can meet it at this service rate — it requires more inference throughput (GPU, batching, more workers), or a relaxed SLO / async semantics.