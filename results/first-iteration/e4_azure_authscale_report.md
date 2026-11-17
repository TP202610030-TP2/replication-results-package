# E4 — Scalability Report

| Step | Users | Requests/s | p50 (ms) | p95 (ms) | p99 (ms) | Error rate |
|---|---|---|---|---|---|---|
| 0 | 10 | 1.5 | 4800 | 6200 | 10000 | 0.0% |
| 1 | 41 | 2.9 | 8500 | 20000 | 24000 | 4.5% |
| 2 | 79 | 3.3 | 13000 | 32000 | 39000 | 38.5% |
| 3 | 141 | 4.9 | 17000 | 35000 | 88000 | 39.1% |
| 4 | 223 | 6.9 | 20000 | 43000 | 144000 | 63.2% |
| 5 | 353 | 13.0 | 30000 | 56000 | 149000 | 85.9% |
| 6 | 353 | 0.0 | 30000 | 56000 | 149000 | 100.0% |

## Saturation point (candidate)

Step 1 (~41 concurrent users): error rate > 0%. **Review manually before citing in the paper** — this is a heuristic, not a verdict.