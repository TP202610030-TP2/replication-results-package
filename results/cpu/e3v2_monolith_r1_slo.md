# E4 v2 — SLO capacity report — e3v2_monolith_r1

- Source: `e3v2_monolith_r1_raw.csv` — request `/api/v1/transcribe`
- SLO: p95 <= 10 s and error rate <= 5% (first 30 s of each 180 s step excluded)

|   step |   users |   requests |   goodput_rps | p50_s   | p95_s   | p99_s   | error_rate   | meets_slo   |
|-------:|--------:|-----------:|--------------:|:--------|:--------|:--------|:-------------|:------------|
|      0 |      10 |         70 |          0.47 | 13.69   | 14.91   | 15.25   | 0.0%         | no          |
|      2 |     100 |         10 |          0    | —       | —       | —       | 100.0%       | no          |
|      5 |    1000 |         10 |          0    | —       | —       | —       | 100.0%       | no          |

## Failure breakdown per step (steady-state window)

|   step |   connection error |   ok |
|-------:|-------------------:|-----:|
|      0 |                  0 |   70 |
|      2 |                 10 |    0 |
|      5 |                 10 |    0 |

## Capacity

- **SLO capacity: 0 concurrent users** (largest step meeting the SLO)
- Peak goodput X_max: 0.47 successful req/s
- Little's-law ceiling with this service rate: N_max = X_max * (R_slo + Z) = 0.47 * (10 + 2) = **6 users**

Interpretation: if a target (e.g. C2.2 = 1000 users) exceeds N_max, no amount of request routing can meet it at this service rate — it requires more inference throughput (GPU, batching, more workers), or a relaxed SLO / async semantics.