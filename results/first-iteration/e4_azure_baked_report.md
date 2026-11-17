# E4 — Scalability Report

| Step | Users | Requests/s | p50 (ms) | p95 (ms) | p99 (ms) | Error rate |
|---|---|---|---|---|---|---|
| 0 | 10 | 1.4 | 4900 | 6000 | 6400 | 0.0% |
| 1 | 40 | 1.6 | 6100 | 28000 | 32000 | 7.0% |
| 2 | 78 | 3.1 | 19000 | 37000 | 42000 | 19.9% |
| 3 | 141 | 4.0 | 25000 | 57000 | 69000 | 63.4% |
| 4 | 199 | 7.6 | 30000 | 51000 | 66000 | 86.8% |
| 5 | 244 | 26.2 | 27000 | 50000 | 67000 | 97.1% |
| 6 | 244 | 0.1 | 26000 | 50000 | 67000 | 100.0% |

## Saturation point (candidate)

Step 1 (~40 concurrent users): error rate > 0%. **Review manually before citing in the paper** — this is a heuristic, not a verdict.