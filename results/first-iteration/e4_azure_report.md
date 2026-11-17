# E4 — Scalability Report

| Step | Users | Requests/s | p50 (ms) | p95 (ms) | p99 (ms) | Error rate |
|---|---|---|---|---|---|---|
| 0 | 10 | 1.6 | 4700 | 6000 | 6800 | 0.0% |
| 1 | 41 | 2.2 | 7000 | 20000 | 23000 | 6.8% |
| 2 | 82 | 3.1 | 19000 | 34000 | 43000 | 39.0% |
| 3 | 142 | 3.9 | 20000 | 55000 | 62000 | 55.4% |
| 4 | 197 | 7.2 | 30000 | 53000 | 62000 | 85.4% |
| 5 | 254 | 26.2 | 23000 | 52000 | 68000 | 96.9% |
| 6 | 254 | 29.5 | 22000 | 52000 | 68000 | 100.0% |

## Saturation point (candidate)

Step 1 (~41 concurrent users): error rate > 0%. **Review manually before citing in the paper** — this is a heuristic, not a verdict.