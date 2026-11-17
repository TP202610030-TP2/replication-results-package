# E6 v2 — D4-asr-crash-async_r1

```json
{
  "scenario": "D4-asr-crash-async_r1",
  "container": "backend-asr-service-1",
  "mode": "crash",
  "restart_policy": "unless-stopped",
  "load_mode": "async",
  "users": 10,
  "request_scored": "job_e2e",
  "detection_time_s": 2.6,
  "mttr_s": 4.81,
  "outage_reverted_by_script_s": null,
  "neighbour_degraded": {
    "neighbor:http://localhost:8080/health": false,
    "neighbor:http://localhost:8001/health": false,
    "neighbor:http://localhost:8003/health": false,
    "neighbor:http://localhost:8005/health": false
  },
  "before": {
    "requests": 55,
    "success_rate": 1.0
  },
  "during": {
    "requests": 0,
    "success_rate": null
  },
  "after": {
    "requests": 114,
    "success_rate": 1.0
  },
  "overall": {
    "requests": 169,
    "success_rate": 1.0
  },
  "during_failures_by_status": {},
  "jobs_completed_after_fault": 114,
  "jobs_lost": 0
}
```