# E4 — Scalability Report

| Step | Users | Requests/s | p50 (ms) | p95 (ms) | p99 (ms) | Error rate |
|---|---|---|---|---|---|---|
| 0 | 10 | 1.6 | 4500 | 5900 | 6600 | 0.0% |
| 1 | 42 | 2.7 | 8300 | 20000 | 25000 | 4.2% |
| 2 | 85 | 3.4 | 15000 | 35000 | 43000 | 42.3% |
| 3 | 143 | 4.2 | 19000 | 56000 | 73000 | 59.8% |
| 4 | 208 | 7.6 | 28000 | 51000 | 70000 | 86.1% |
| 5 | 307 | 13.0 | 30000 | 56000 | 81000 | 85.6% |

## Saturation point (candidate)

Step 1 (~42 concurrent users): error rate > 0%. **Review manually before citing in the paper** — this is a heuristic, not a verdict.