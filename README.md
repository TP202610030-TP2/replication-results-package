# Replication package: resilient and self-adaptive Quechua ASR service

Replication material for the article *Architecting a resilient and self-adaptive speech recognition service for the digital revitalization of Quechua* (submitted to the Journal of Systems and Software).

The package contains:

- the experiment suite used to evaluate the architecture;
- the aggregated results that support the tables of the article.

The platform itself (services, monolithic baseline and deployment manifests) is in separate repositories:

- Backend services, monolithic baseline (`services/monolith-baseline`) and Docker Compose / Azure Container Apps manifests: https://github.com/TP202610030-TP2/Backend
- Web interface: https://github.com/TP202610030-TP2/Frontend

## Contents

```
experiments/   measurement scripts (E1-E9) and the orchestrator run_v2_suite.py
results/first-iteration/   aggregated results of the first iteration (local machine without GPU and Azure Container Apps)
results/cpu/   aggregated results of the final version on the machine without GPU
results/gpu/   aggregated results of the final version on the GPU machine
```

| Folder | Experiment | What it measures |
|---|---|---|
| `experiments/common/` | Shared | HTTP/WebSocket client, statistics (Shapiro-Wilk, Welch, Mann-Whitney, Cliff's delta, Wilcoxon), text normalization for WER/CER, manifest reader |
| `experiments/e1_dataset_characterization/` | E1 | Builds the evaluation manifest from the IWSLT 2026 Quechua corpus and characterizes it |
| `experiments/e2_wer_cer_rtf/` | E2 | WER, CER and RTF over the full corpus |
| `experiments/e4_load_test/` | E4 / E3 | Progressive load (10 to 1000 users), goodput by service objective, synchronous and asynchronous modes, proposal versus monolith |
| `experiments/e5_streaming_codec/` | E5 | Streaming latency and quality, PCM versus Opus |
| `experiments/e6_fault_injection/` | E6 | Fault injection: success before/during/after the crash, detection time, MTTR, propagation, lost jobs |
| `experiments/e7_statistics/` | E7 | Consolidated statistical report |
| `experiments/e8_inference_throughput/` | E8 | Inference throughput by device, precision, batch size and concurrency, and WER control per configuration |
| `experiments/e9_adaptation/` | E9 | Runtime adaptation: decisions, reaction time and reversion under a load burst |
| `experiments/run_v2_suite.py` | All | Switches the stack between configurations (environment variables and `docker compose up --force-recreate`) and runs the phases |

## Mapping between results and the article

### First iteration (`results/first-iteration/`)

| Article | Files in `results/first-iteration/` |
|---|---|
| Evaluation corpus (2111 clips, 10.79 h, 47 identified speakers) | `e1_characterization.md` (speaker names omitted) |
| Criteria C3.1, C4.1 and C4.2 on CPU (median RTF 0.149, no empty transcriptions, 13 clips with WER above 1.5) | `e2_full_report.md` |
| Criterion C4.3 and streaming latency, PCM versus Opus (11.56 versus 5.34 s; 582 785 versus 165 071 bytes) | `e5_report.md` |
| First comparison with the monolith on CPU (median 16.8 versus 24.9 s, Cliff's delta = -0.579) | `e3_report.md`, `e3_{proposed,monolith}_report.md`, `e3_{proposed,monolith}_run_{stats,failures}.csv` |
| Load tests on Azure Container Apps, four scaling configurations (collapse between 244 and 353 users; 2652 and 235 errors with code 401) | `e4_azure_report.md` (no autoscaling), `e4_azure_autoscale_*` (autoscaled `asr-service`), `e4_azure_baked_*` (model packaged in the image), `e4_azure_authscale_*` (autoscaled `asr-service` and `auth-service`); each with `_report.md`, `_run_stats.csv` and `_run_failures.csv` |
| Fault injection of the first iteration with 50 users (`auth-service` crash: 352 failed of 539 requests) | `e6_report.md`, `e6_<service>.summary.json`, `e6_load_during_<service>_outage_{stats,failures}.csv` |

Validity notes for the first iteration, disclosed in the article:

- The 0% failures with `asr-service` down is not valid: `audio-processor` answered 200 without a transcription and the load client did not validate the content of the response. The final protocol validates every response.
- The services were stopped in an orderly way (`docker stop`), which does not trigger the restart policy, so there is no recovery time.
- The Azure load test was run once per configuration, without repetitions.
- In `e6_report.md`, the "Requests lost" column counts the health checks against the stopped container itself; the impact on user traffic is in the second table of that report and in the `e6_load_during_*` files.

### Machine without GPU (`results/cpu/`)

| Article | Files in `results/cpu/` |
|---|---|
| Table 5 (fault injection) and criteria C1.1 to C1.3 | `e6v2_aggregate.md`, `e6v2_<scenario>_r{1,2,3}.{md,summary.json,health.csv}` (scenarios D1 to D7) |
| Table 6, columns "Without GPU" (synchronous goodput and p95 with edge admission control) | `e4v2_S2c-v2-cpu-sync-edge_r{1,2,3}_slo.{csv,md}`, `e4v2_S2c_aggregate.md` |
| Goodput without admission control and first-version replica (0.36 versus 0.82 transcriptions/s) | `e4v2_S2-v2-cpu-sync_r{1,2,3}_slo.*`, `e4v2_S1-v1-cpu-sync_r{1,2,3}_slo.*`, `e4v2_aggregate.md` |
| Criterion C2.2 without GPU, asynchronous mode with 1000 users (5526 of 5527 jobs accepted, all completed) | `e4v2_S2b-v2-cpu-async_r{1,2,3}_jobs.json`, `e4v2_S2b-v2-cpu-async_r{1,3}_slo.*` |
| Table 7, rows "No GPU" (CTranslate2 and transformers) | `e9_B-cpu-adaptive-{ct2,transformers}_r{1,2,3}.{summary.json,decisions.json,timeline.csv}` |
| Inference throughput on the machine without GPU (19.4 versus 7.1 s of audio per second) | `e8_cpu_summary.csv`, `e8_cpu_levels.csv`, `e8_report.{md,csv}`, `e8_*.batches.json` |
| Criterion C3.3 without GPU (proposal versus monolith, Cliff's delta = -0.107) | `e3v2_report.md`, `e3v2_{proposed,monolith}_r{1,2,3}_slo.{csv,md}` |

The second repetition of the asynchronous scenario has no `_slo` report: the suite was stopped during the drain wait, and its job counts were recorded manually in `e4v2_S2b-v2-cpu-async_r2_jobs.json`.

`results/cpu/superseded/` keeps the runs that the article mentions as replaced:

| Folder | Content |
|---|---|
| `e4_S2c_cap6_ablation/` | Initial edge admission limit of 6 in-flight requests, too strict; replaced by the limit of 10 derived with Little's law |
| `e4_S2c_r3_proxy_backlog/`, `e4_S2c_cap10_slotleak/` | Repetitions contaminated by connections that the Docker Desktop network proxy carried over from the previous 1000-user run; discarded and rerun after adding a draining wait |
| `e6_overload_50users/` | Fault injection with 50 users: the platform was already saturated before the crash, so the final protocol uses 10 users |

### GPU machine (`results/gpu/`)

| Article | Files in `results/gpu/` |
|---|---|
| Table 6, columns "With GPU" (synchronous goodput and p95) | `e4v2_S3c-v2-gpu-sync-edge_r{1,2,3}_slo.{csv,md}`, `e4v2_gpu_aggregate.md` |
| Criterion C2.2, asynchronous mode with 1000 users | `e4v2_S4-v2-gpu-async_r{1,2,3}_{jobs.json,slo.csv,slo.md}` |
| Calibration of the edge admission limit (73 in-flight requests) | `e4v2_S3-v2-gpu-sync_r{1,2,3}_slo.*`, `e4v2_S3_aggregate.md` |
| Table 7, rows "GPU" (scenarios A, B and C) | `e9_{A-gpu-adaptive,B-cpu-adaptive,C-cpu-to-gpu}_r{1,2,3}.{summary.json,decisions.json,timeline.csv}` |
| Table 8 (inference throughput) and criterion C3.4 | `e8_report.{md,csv}`, `e8_report_cpuref.{md,csv}`, `e8_*.batches.json` |
| No significant WER change across inference configurations | `e8_wer_control.md` |
| Table 9 (proposal versus monolith on the GPU machine) | `e3v2_gpu_report.md`, `e3v2_{proposed,monolith}_r{1,2,3}_slo.{csv,md}` |
| Table 10 (recognition quality, 2111 clips) | `e2_gpu_report.md` |

In the `_slo.md` files, the `users` column shows the maximum number of active users within the window of each step (for example, 30 or 60 instead of 10 or 50), because users of the next step are already entering at the end of the window. The nominal steps are 10, 50, 100, 200, 500 and 1000 users, and the aggregates use those values.

## Requirements

- Python 3.11 (pinned versions in `experiments/requirements.txt`). With newer Python versions, install the current releases without pins: `pip install locust pandas scipy numpy jiwer httpx tabulate websockets psutil`.
- `ffmpeg` in the PATH (duration probing and Opus encoding).
- Docker and Docker Compose, with the Backend repository running locally. The GPU configurations require an NVIDIA GPU with the NVIDIA Container Toolkit (`docker-compose.gpu.yml` in the Backend repository).
- The evaluation corpus (see below).

```bash
cd experiments
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Evaluation corpus

The corpus is not redistributed. It is the Quechua-Spanish data released for IWSLT 2026 (https://github.com/johneortega/IWSLT2026_Quechua_data):

- 1413 Huqariq clips (`que_spa_synthetic_translation/train`; Zevallos et al., 2022);
- 698 Siminchik clips (`que_spa_unconstrained/train` and `valid`; Cardenas et al., 2018).

```bash
cd experiments/e1_dataset_characterization
python build_manifest_from_iwslt.py --corpus-root /path/to/IWSLT2026_Quechua_data --out manifest.csv
python characterize.py --manifest manifest.csv
# 30-clip stratified sample (20 Huqariq, 10 Siminchik) used by E5 and E8:
python select_sample.py --manifest manifest.csv --ids sample_30_clips.csv --out manifest_e5_sample.csv
```

`sample_30_clips.csv` identifies the sample by the path of each clip inside the corpus repository.

## Running the experiments

1. Start the platform from the Backend repository (`docker compose up --build`, adding `-f docker-compose.gpu.yml` on a GPU machine). For the baseline, start the `monolith-baseline` and `monolith-db` services defined in the Backend `docker-compose.yml` (`docker compose up --build monolith-baseline`, port 8006; set `MONOLITH_DEVICE=cuda` to run it on the GPU).
2. Create test users for the load and fault-injection tests:
   ```bash
   cd experiments/e4_load_test
   python seed_test_users.py --base-url http://127.0.0.1:8000 --count 50 --out users_local_proposed.csv
   ```
3. Run the phases with the orchestrator. `--audio` is the load clip; the article used a single 24.05 s corpus clip close to the median duration.
   ```bash
   cd experiments
   python run_v2_suite.py --phase e8 e9 e6 e4 --audio <clip.wav> --repeats 3            # GPU machine
   python run_v2_suite.py --cpu-only --lanes 3 --threads 2 --phase e8 e9 e6 e4 --audio <clip.wav> --repeats 3   # machine without GPU
   python run_v2_suite.py --phase e3 --audio <clip.wav> --repeats 3                     # proposal versus monolith
   ```
4. Recognition quality and streaming:
   ```bash
   python e2_wer_cer_rtf/run_transcribe_benchmark.py --manifest e1_dataset_characterization/manifest.csv --base-url http://127.0.0.1:8000 --repeats 1 --out results/e2_raw.csv
   python e2_wer_cer_rtf/report.py --raw results/e2_raw.csv --out results/e2_report.md
   python e5_streaming_codec/run_pcm_vs_compressed.py --manifest e1_dataset_characterization/manifest_e5_sample.csv --base-url http://127.0.0.1:8000 --encoding opus --repeats 3 --out results/e5_raw.csv
   python e5_streaming_codec/report.py --raw results/e5_raw.csv --out results/e5_report.md
   ```

Each script writes its raw CSV to `experiments/results/` (ignored by git) and an aggregated Markdown report next to it. Every script documents its options in its header and with `--help`.

The test users created by the scripts use a fixed password (`ExperimentPass123!`) and `example.com` addresses. They exist only in the local stack under test.

Some code comments refer to `docs/` files. Those are internal working notes of the project and are not part of this package; the article and this README describe the protocol.

## Data not included

- Raw per-request and per-clip CSV files and Locust HTML reports: only aggregated reports are included. The raw files contain local paths, the corpus transcriptions and deployment host names.
- Audio and transcriptions of the corpus: they are obtained from the IWSLT 2026 repository, as described above.

## License

- Code (`experiments/`): MIT License (see `LICENSE`).
- Results (`results/`): Creative Commons Attribution 4.0 International (CC BY 4.0).

## How to cite

If you use this material, please cite the article. Citation details will be added after publication.
