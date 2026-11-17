# E4 — Scalability Report

| Step | Users | Requests/s | p50 (ms) | p95 (ms) | p99 (ms) | Error rate |
|---|---|---|---|---|---|---|
| 0 | 10 | 1.4 | 5300 | 6800 | 7900 | 0.0% |
| 1 | 50 | 2.2 | 15000 | 24000 | 24000 | 0.0% |
| 2 | 100 | 2.3 | 22000 | 47000 | 47000 | 0.0% |
| 3 | 200 | 2.5 | 23000 | 95000 | 97000 | 0.0% |
| 4 | 500 | 3.3 | 23000 | 135000 | 156000 | 0.0% |
| 5 | 909 | 5.1 | 28000 | 257000 | 284000 | 16.9% |
| 6 | 909 | 5.0 | 28000 | 257000 | 284000 | 0.0% |

## Saturation point (candidate)

Step 1 (~50 concurrent users): p95 latency jumped 3.5x vs previous step. **Review manually before citing in the paper** — this is a heuristic, not a verdict.