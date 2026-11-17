# E4 v2 — SLO capacity report — e4v2_S1-v1-cpu-sync_r2

- Source: `e4v2_S1-v1-cpu-sync_r2_raw.csv` — request `/api/v1/transcribe`
- SLO: p95 <= 10 s and error rate <= 5% (first 30 s of each 180 s step excluded)

|   step |   users |   requests |   goodput_rps |   p50_s |   p95_s |   p99_s | error_rate   | meets_slo   |
|-------:|--------:|-----------:|--------------:|--------:|--------:|--------:|:-------------|:------------|
|      0 |      10 |         53 |          0.35 |   25.67 |   26.76 |   26.92 | 0.0%         | no          |
|      1 |      80 |         67 |          0.21 |   78.17 |   99.62 |   99.87 | 52.2%        | no          |
|      2 |     130 |        117 |          0.12 |   99.13 |  100.34 |  100.34 | 84.6%        | no          |
|      3 |     230 |        231 |          0.13 |   99.31 |  100.32 |  100.35 | 91.3%        | no          |
|      4 |     520 |        580 |          0.15 |   99.32 |  100.23 |  100.25 | 96.0%        | no          |
|      5 |    1000 |       2846 |          0.03 |  109.86 |  119.85 |  120.41 | 99.9%        | no          |

## Failure breakdown per step (steady-state window)

|   step |   HTTP 502 |   ok |   timeout (504) |
|-------:|-----------:|-----:|----------------:|
|      0 |          0 |   53 |               0 |
|      1 |          0 |   32 |              35 |
|      2 |          0 |   18 |              99 |
|      3 |          0 |   20 |             211 |
|      4 |          0 |   23 |             557 |
|      5 |       1696 |    4 |            1146 |

## Capacity

- **SLO capacity: 0 concurrent users** (largest step meeting the SLO)
- Peak goodput X_max: 0.35 successful req/s = 8.5 s of audio per second
- Little's-law ceiling with this service rate: N_max = X_max * (R_slo + Z) = 0.35 * (10 + 2) = **4 users**

Interpretation: if a target (e.g. C2.2 = 1000 users) exceeds N_max, no amount of request routing can meet it at this service rate — it requires more inference throughput (GPU, batching, more workers), or a relaxed SLO / async semantics.