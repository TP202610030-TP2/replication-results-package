# E4 — Scalability Report

| Step | Users | Requests/s | p50 (ms) | p95 (ms) | p99 (ms) | Error rate |
|---|---|---|---|---|---|---|
| 0 | 10 | 0.7 | 13000 | 16000 | 21000 | 0.0% |
| 1 | 48 | 1.4 | 27000 | 51000 | 59000 | 2.5% |
| 2 | 97 | 1.8 | 31000 | 66000 | 69000 | 18.4% |
| 3 | 145 | 3.1 | 31000 | 70000 | 71000 | 64.0% |
| 4 | 190 | 5.8 | 31000 | 70000 | 71000 | 84.2% |
| 5 | 245 | 12.8 | 31000 | 70000 | 71000 | 94.0% |
| 6 | 245 | 0.0 | 31000 | 70000 | 71000 | 100.0% |

## Saturation point (candidate)

Step 1 (~48 concurrent users): error rate > 0%. **Review manually before citing in the paper** — this is a heuristic, not a verdict.