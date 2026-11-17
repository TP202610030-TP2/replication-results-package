# E6 v2 — D1-asr-crash_r2

```json
{
  "scenario": "D1-asr-crash_r2",
  "container": "backend-asr-service-1",
  "mode": "crash",
  "restart_policy": "unless-stopped",
  "load_mode": "sync",
  "users": 10,
  "request_scored": "/api/v1/transcribe",
  "detection_time_s": 2.2,
  "mttr_s": 4.6,
  "outage_reverted_by_script_s": null,
  "neighbour_degraded": {
    "neighbor:http://localhost:8080/health": false,
    "neighbor:http://localhost:8001/health": false,
    "neighbor:http://localhost:8003/health": false,
    "neighbor:http://localhost:8005/health": false
  },
  "before": {
    "requests": 50,
    "success_rate": 1.0
  },
  "during": {
    "requests": 15,
    "success_rate": 0.0
  },
  "after": {
    "requests": 172,
    "success_rate": 1.0
  },
  "overall": {
    "requests": 237,
    "success_rate": 0.9367
  },
  "during_failures_by_status": {
    "503": 15
  }
}
```