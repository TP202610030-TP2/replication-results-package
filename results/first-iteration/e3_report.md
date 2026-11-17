# E3 — Monolithic vs. Proposed Architecture

| Metric | Proposed (mean) | Monolith (mean) | Test | p-value | Effect size | Significant? |
|---|---|---|---|---|---|---|
| p50 latency (ms) | 16787.4 | 24882.3 | mann-whitney-u | 0.0000 | cliffs_delta=-0.579 | yes |
| p95 latency (ms) | 69787.4 | 54082.9 | mann-whitney-u | 0.9929 | cliffs_delta=-0.000 | no |
| p99 latency (ms) | 82581.9 | 57364.3 | mann-whitney-u | 0.2599 | cliffs_delta=0.028 | no |
| Throughput (req/s) | 2.8 | 4.2 | mann-whitney-u | 0.3933 | cliffs_delta=0.021 | no |

- **Máx. usuarios concurrentes probados**: propuesta=1000, monolito=1000
- **Aislamiento de fallos**: ver el reporte de `e6_fault_injection/` corrido contra ambas arquitecturas.