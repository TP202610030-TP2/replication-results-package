# E3 v2 — propuesta (n=3) frente a monolito (n=3)

| Usuarios | Arquitectura | Solicitudes | Éxito | Goodput (mediana) | p50 | p95 | p99 | Fallos |
|---|---|---|---|---|---|---|---|---|
| 10 | Propuesta | 298 | 100.0 % | 0.56 | 14.9 | 19.8 | 21.5 | — |
| 10 | Monolito | 232 | 100.0 % | 0.48 | 15.6 | 24.5 | 27.3 | — |
| 50 | Propuesta | 10688 | 2.8 % | 0.56 | 17.7 | 21.7 | 23.1 | 503×10387 |
| 50 | Monolito | 2 | 100.0 % | 0.00 | 22.3 | 23.0 | 23.1 | — |
| 100 | Propuesta | 23895 | 1.1 % | 0.45 | 21.0 | 26.5 | 26.9 | 503×23640 |
| 100 | Monolito | 50 | 0.0 % | 0.00 | nan | nan | nan | 0×50 |
| 200 | Propuesta | 48292 | 0.4 % | 0.33 | 27.9 | 34.5 | 35.0 | 503×48099 |
| 200 | Monolito | 10 | 0.0 % | 0.00 | nan | nan | nan | 0×10 |
| 500 | Propuesta | 50897 | 0.4 % | 0.35 | 30.4 | 37.1 | 38.5 | 503×50706 |
| 500 | Monolito | 40 | 0.0 % | 0.00 | nan | nan | nan | 0×40 |
| 1000 | Propuesta | 51781 | 0.4 % | 0.37 | 32.1 | 41.2 | 43.1 | 503×51455, 0×133 |
| 1000 | Monolito | 25 | 0.0 % | 0.00 | nan | nan | nan | 0×25 |

| Usuarios | Prueba | Valor p | Tamaño de efecto | Magnitud | Mediana propuesta (s) | Mediana monolito (s) | Significativo |
|---|---|---|---|---|---|---|---|
| 10 | mann-whitney-u | 0.03389 | cliffs_delta = -0.107 | despreciable | 14.9 | 15.6 | Sí |
