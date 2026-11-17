# E4 v2 — SLO capacity report — e4v2_S2b-v2-cpu-async_r1

- Source: `e4v2_S2b-v2-cpu-async_r1_raw.csv` — request `job_e2e`
- SLO: p95 <= 10 s and error rate <= 5% (first 30 s of each 180 s step excluded)

|   step |   users |   requests |   goodput_rps |   p50_s |   p95_s |   p99_s | error_rate   | meets_slo   |
|-------:|--------:|-----------:|--------------:|--------:|--------:|--------:|:-------------|:------------|
|      0 |      50 |        160 |          1.07 |    7.47 |    8.53 |    9.46 | 0.0%         | yes         |
|      1 |     100 |        139 |          0.93 |   50.39 |   53.52 |   54.55 | 0.0%         | no          |
|      2 |     150 |        139 |          0.93 |  102.48 |  105.49 |  106.58 | 0.0%         | no          |
|      3 |     250 |        133 |          0.89 |  114.97 |  170.12 |  176.95 | 0.0%         | no          |
|      4 |     560 |        110 |          0.73 |  251.96 |  263.06 |  266.57 | 0.0%         | no          |
|      5 |    1000 |         98 |          0.65 |  317.28 |  355.43 |  360.66 | 0.0%         | no          |
|      6 |     971 |        117 |          0.78 |  459.3  |  522.06 |  526.43 | 0.0%         | no          |
|      7 |     833 |         96 |          0.64 |  625.88 |  688.57 |  693.75 | 0.0%         | no          |
|      8 |     717 |         92 |          0.61 |  740.37 |  755.95 |  756.67 | 0.0%         | no          |
|      9 |     606 |         94 |          0.63 |  827.32 |  888.29 |  893.37 | 0.0%         | no          |
|     10 |     493 |         97 |          0.65 |  995.39 | 1057.35 | 1063.18 | 0.0%         | no          |
|     11 |     377 |        119 |          0.79 | 1157.4  | 1218.12 | 1224.85 | 0.0%         | no          |
|     12 |     239 |        110 |          0.73 | 1329.49 | 1387.02 | 1390.34 | 0.0%         | no          |
|     13 |      99 |         99 |          0.66 | 1417.96 | 1428.54 | 1429.57 | 0.0%         | no          |

## Failure breakdown per step (steady-state window)

|   step |   ok |
|-------:|-----:|
|      0 |  160 |
|      1 |  139 |
|      2 |  139 |
|      3 |  133 |
|      4 |  110 |
|      5 |   98 |
|      6 |  117 |
|      7 |   96 |
|      8 |   92 |
|      9 |   94 |
|     10 |   97 |
|     11 |  119 |
|     12 |  110 |
|     13 |   99 |

## Capacity

- **SLO capacity: 50 concurrent users** (largest step meeting the SLO)
- Peak goodput X_max: 1.07 successful req/s = 25.7 s of audio per second
- Little's-law ceiling with this service rate: N_max = X_max * (R_slo + Z) = 1.07 * (10 + 2) = **13 users**

Interpretation: if a target (e.g. C2.2 = 1000 users) exceeds N_max, no amount of request routing can meet it at this service rate — it requires more inference throughput (GPU, batching, more workers), or a relaxed SLO / async semantics.