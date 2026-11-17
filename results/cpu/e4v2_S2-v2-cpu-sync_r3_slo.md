# E4 v2 — SLO capacity report — e4v2_S2-v2-cpu-sync_r3

- Source: `e4v2_S2-v2-cpu-sync_r3_raw.csv` — request `/api/v1/transcribe`
- SLO: p95 <= 10 s and error rate <= 5% (first 30 s of each 180 s step excluded)

|   step |   users |   requests |   goodput_rps |   p50_s |   p95_s |   p99_s | error_rate   | meets_slo   |
|-------:|--------:|-----------:|--------------:|--------:|--------:|--------:|:-------------|:------------|
|      0 |      50 |        131 |          0.85 |    9.37 |   10.65 |   11.83 | 2.3%         | no          |
|      1 |     100 |        179 |          0.85 |   55.18 |   56.86 |   57.09 | 29.1%        | no          |
|      2 |     170 |       2057 |          0.32 |   63.87 |   98.37 |   99.86 | 97.7%        | no          |
|      3 |     270 |       2180 |          0.31 |   74.88 |   84.61 |   89.99 | 97.8%        | no          |
|      4 |     570 |       2205 |          0.36 |   80.09 |  106.78 |  111.47 | 97.6%        | no          |
|      5 |    1000 |       2258 |          0.41 |   99.88 |  115.2  |  122.37 | 97.3%        | no          |

## Failure breakdown per step (steady-state window)

|   step |   HTTP 500 |   ok |   rejected (429/503) |   timeout (504) |
|-------:|-----------:|-----:|---------------------:|----------------:|
|      0 |          0 |  128 |                    3 |               0 |
|      1 |          0 |  127 |                   52 |               0 |
|      2 |          0 |   48 |                 1991 |              18 |
|      3 |          1 |   47 |                 2132 |               0 |
|      4 |        203 |   54 |                 1948 |               0 |
|      5 |       1718 |   62 |                  477 |               1 |

## Capacity

- **SLO capacity: 0 concurrent users** (largest step meeting the SLO)
- Peak goodput X_max: 0.85 successful req/s = 20.5 s of audio per second
- Little's-law ceiling with this service rate: N_max = X_max * (R_slo + Z) = 0.85 * (10 + 2) = **10 users**

Interpretation: if a target (e.g. C2.2 = 1000 users) exceeds N_max, no amount of request routing can meet it at this service rate — it requires more inference throughput (GPU, batching, more workers), or a relaxed SLO / async semantics.