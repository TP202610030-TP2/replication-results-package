# E6 v2 — D2-auth-crash-local_r3

```json
{
  "scenario": "D2-auth-crash-local_r3",
  "container": "backend-auth-service-1",
  "mode": "crash",
  "restart_policy": "unless-stopped",
  "load_mode": "sync",
  "users": 10,
  "request_scored": "/api/v1/transcribe",
  "detection_time_s": 1.56,
  "mttr_s": 4.21,
  "outage_reverted_by_script_s": null,
  "neighbour_degraded": {
    "neighbor:http://localhost:8080/health": false,
    "neighbor:http://localhost:8003/health": false,
    "neighbor:http://localhost:8005/health": false
  },
  "before": {
    "requests": 50,
    "success_rate": 1.0
  },
  "during": {
    "requests": 4,
    "success_rate": 1.0
  },
  "after": {
    "requests": 176,
    "success_rate": 1.0
  },
  "overall": {
    "requests": 230,
    "success_rate": 1.0
  },
  "during_failures_by_status": {}
}
```