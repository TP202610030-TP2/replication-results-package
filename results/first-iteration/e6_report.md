# E6 — Fault Injection Results

| Container | Detection (s) | Recovery (s) | Requests lost | % lost | Propagated? |
|---|---|---|---|---|---|
| backend-asr-service-1 | 3.4 | NOT recovered | 26/26 | 100.0% | no |
| backend-auth-service-1 | 3.5 | NOT recovered | 23/25 | 92.0% | no |
| backend-transcription-manager-1 | 3.5 | NOT recovered | 22/24 | 91.7% | no |
| backend-monolith-baseline-1 | 3.7 | NOT recovered | 24/26 | 92.3% | no |

**Nota de interpretación**: la columna "Requests lost/% lost" de arriba mide los health-checks de `inject.py` contra el propio contenedor detenido (trivialmente ~100%, confirma que la caída ocurrió, no mide impacto real). "Propagated?" se calcula sobre los `/health` de los servicios vecinos — no es afectado por este detalle.

## Impacto real sobre tráfico de usuario (carga concurrente real durante cada apagón)

Con ~50 usuarios concurrentes reales ejecutando login+transcribe durante cada corte (no solo health-checks), el failure rate observado en `/api/v1/transcribe` fue:

| Servicio caído | Requests totales | Fallas | % fallas | Comportamiento |
|---|---|---|---|---|
| `asr-service` | 437 | 0 | **0.0%** | las requests en curso se encolan (hasta 81s de latencia) y se completan cuando el contenedor vuelve — sin pérdida |
| `auth-service` | 539 | 352 | **65.3%** | cada request pasa por `validate-token` contra `auth-service`; sin él, casi todo falla — incluye login y transcribe ya autenticados |
| `transcription-manager` | 238 | 0 | **0.0%** | diseño "non-fatal on failure" (`services/asr-service/app/services/whisper_service.py`): el cliente recibe su transcripción igual, solo se pierde la persistencia |
| `monolith-baseline` | 1160 | 1082 | **93.3%** | un solo proceso — la caída de cualquier componente interno tumba absolutamente todo, incluido login |

Esta es la evidencia empírica para la fila "Separación de responsabilidades" de la Tabla III: la arquitectura propuesta aísla el impacto real de una caída según qué servicio falle (0% a 65%, nunca todo el sistema), mientras que el monolito lo propaga al 93%+ del tráfico sin excepción — confirmando cuantitativamente la afirmación cualitativa de aislamiento de fallos.