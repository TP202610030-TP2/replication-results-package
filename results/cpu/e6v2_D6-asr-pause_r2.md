# E6 v2 — D6-asr-pause_r2

```json
{
  "scenario": "D6-asr-pause_r2",
  "container": "backend-asr-service-1",
  "mode": "pause",
  "restart_policy": "unless-stopped",
  "load_mode": "sync",
  "users": 10,
  "request_scored": "/api/v1/transcribe",
  "detection_time_s": 1.06,
  "mttr_s": 60.03,
  "outage_reverted_by_script_s": 60.1,
  "neighbour_degraded": {
    "neighbor:http://localhost:8080/health": false,
    "neighbor:http://localhost:8001/health": false,
    "neighbor:http://localhost:8003/health": false,
    "neighbor:http://localhost:8005/health": false
  },
  "before": {
    "requests": 49,
    "success_rate": 1.0
  },
  "during": {
    "requests": 0,
    "success_rate": null
  },
  "after": {
    "requests": 125,
    "success_rate": 0.96
  },
  "overall": {
    "requests": 174,
    "success_rate": 0.9713
  },
  "during_failures_by_status": {}
}
```