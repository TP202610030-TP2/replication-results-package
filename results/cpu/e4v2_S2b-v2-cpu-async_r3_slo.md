# E4 v2 — SLO capacity report — e4v2_S2b-v2-cpu-async_r3

- Source: `e4v2_S2b-v2-cpu-async_r3_raw.csv` — request `job_e2e`
- SLO: p95 <= 10 s and error rate <= 5% (first 30 s of each 180 s step excluded)

|   step |   users |   requests |   goodput_rps |   p50_s |   p95_s |   p99_s | error_rate   | meets_slo   |
|-------:|--------:|-----------:|--------------:|--------:|--------:|--------:|:-------------|:------------|
|      0 |      50 |        134 |          0.89 |    8.51 |   14.66 |   17.77 | 0.0%         | no          |
|      1 |     100 |        144 |          0.96 |   48.84 |   51.32 |   52.31 | 0.0%         | no          |
|      2 |     170 |        139 |          0.93 |  101.67 |  103.86 |  104.77 | 0.0%         | no          |
|      3 |     280 |        126 |          0.84 |  114.35 |  170.98 |  179.15 | 0.0%         | no          |
|      4 |     560 |        108 |          0.72 |  259.31 |  273.67 |  276.8  | 0.0%         | no          |
|      5 |    1000 |         99 |          0.66 |  329.31 |  359.47 |  362.96 | 0.0%         | no          |
|      6 |     972 |        111 |          0.74 |  462.48 |  524.91 |  530.38 | 0.0%         | no          |
|      7 |     840 |        107 |          0.71 |  625.86 |  689.59 |  695.09 | 0.0%         | no          |
|      8 |     714 |        107 |          0.71 |  738.01 |  741.51 |  742.19 | 0.0%         | no          |
|      9 |     589 |        106 |          0.71 |  828.02 |  884.93 |  891.16 | 0.0%         | no          |
|     10 |     460 |        112 |          0.75 |  997.82 | 1053.24 | 1058.65 | 0.0%         | no          |
|     11 |     329 |        119 |          0.79 | 1161.61 | 1213.28 | 1220.54 | 0.0%         | no          |
|     12 |     186 |        127 |          0.85 | 1320.52 | 1353.9  | 1354.45 | 0.0%         | no          |
|     13 |      34 |         34 |          0.23 | 1340.32 | 1344.69 | 1345.56 | 0.0%         | no          |

## Failure breakdown per step (steady-state window)

|   step |   ok |
|-------:|-----:|
|      0 |  134 |
|      1 |  144 |
|      2 |  139 |
|      3 |  126 |
|      4 |  108 |
|      5 |   99 |
|      6 |  111 |
|      7 |  107 |
|      8 |  107 |
|      9 |  106 |
|     10 |  112 |
|     11 |  119 |
|     12 |  127 |
|     13 |   34 |

## Capacity

- **SLO capacity: 0 concurrent users** (largest step meeting the SLO)
- Peak goodput X_max: 0.96 successful req/s = 23.1 s of audio per second
- Little's-law ceiling with this service rate: N_max = X_max * (R_slo + Z) = 0.96 * (10 + 2) = **12 users**

Interpretation: if a target (e.g. C2.2 = 1000 users) exceeds N_max, no amount of request routing can meet it at this service rate — it requires more inference throughput (GPU, batching, more workers), or a relaxed SLO / async semantics.