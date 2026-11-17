# E4 v2 — SLO capacity report — e3v2_monolith_r2

- Source: `e3v2_monolith_r2_raw.csv` — request `/api/v1/transcribe`
- SLO: p95 <= 10 s and error rate <= 5% (first 30 s of each 180 s step excluded)

|   step |   users |   requests |   goodput_rps | p50_s   | p95_s   | p99_s   | error_rate   | meets_slo   |
|-------:|--------:|-----------:|--------------:|:--------|:--------|:--------|:-------------|:------------|
|      0 |      10 |         37 |          0.25 | 14.68   | 17.26   | 18.90   | 0.0%         | no          |
|      2 |     100 |          2 |          0    | —       | —       | —       | 100.0%       | no          |
|      3 |     200 |         10 |          0    | —       | —       | —       | 100.0%       | no          |
|      5 |    1000 |         10 |          0    | —       | —       | —       | 100.0%       | no          |

## Failure breakdown per step (steady-state window)

|   step |   connection error |   ok |
|-------:|-------------------:|-----:|
|      0 |                  0 |   37 |
|      2 |                  2 |    0 |
|      3 |                 10 |    0 |
|      5 |                 10 |    0 |

## Capacity

- **SLO capacity: 0 concurrent users** (largest step meeting the SLO)
- Peak goodput X_max: 0.25 successful req/s
- Little's-law ceiling with this service rate: N_max = X_max * (R_slo + Z) = 0.25 * (10 + 2) = **3 users**

Interpretation: if a target (e.g. C2.2 = 1000 users) exceeds N_max, no amount of request routing can meet it at this service rate — it requires more inference throughput (GPU, batching, more workers), or a relaxed SLO / async semantics.