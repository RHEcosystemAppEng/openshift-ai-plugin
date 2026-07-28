# EvalHub

TrustyAI-managed **multi-provider LLM evaluation hub**: versioned REST + Python SDK (`eval-hub-sdk`) + `evalhub` CLI submit Jobs that fan out to lm-evaluation-harness, Garak, GuideLLM, LightEval (and optional contrib adapters), with reusable collections, weighted pass thresholds, MLflow/OCI export, and multi-tenant scoping. Detection category: **Multi-provider evaluation hub**. Peers are DIY multi-harness glue, custom eval orchestrators, and hand-rolled CI/K8s gates that teams run instead of (or before) adopting EvalHub.

## Peers

- DIY lm-eval + Garak + GuideLLM + LightEval glue — separate CI/Makefile steps for two or more harnesses with hand-merged scores and shared pass/fail
- Custom multi-harness eval gate scripts — Python/shell wrappers that invoke several frameworks against one model URL and invent suite thresholds
- Hand-rolled Kubernetes Jobs / KFP steps per harness — one Job or pipeline stage per provider, shared InferenceService `/v1` endpoint, no hub CR
- Custom REST “eval service” — in-house API posting to multiple backend harnesses (DIY EvalHub API substitute)
- Weighted collection / leaderboard YAML DIY — org suite IDs spanning frameworks (`safety-and-fairness`, domain suites) outside EvalHub `collections`
- Per-harness MLflow glue — each tool logs experiments separately instead of hub `MLFLOW_TRACKING_URI` + job lineage
- BYOF / custom FrameworkAdapter-like wrappers — “bring your own eval container” schedulers without EvalHub adapter registration
- Makefile/CI multi-target chains — `eval` / `benchmark` / `safety-scan` / `perf-bench` chaining different tools into one release gate
- Notebook stitch-together suites — sequential `lm_eval` → `garak` → `guidellm` / `lighteval` cells merging tables by hand
- Upstream eval-hub (standalone) — self-hosted [eval-hub/eval-hub](https://github.com/eval-hub/eval-hub) / SDK outside RHOAI TrustyAI Operator path

**Not peers (adjacent catalog jobs):** **LM Evaluation (LMEval)** (single-framework `LMEvalJob` / lm-eval-only CRD path); **RAGAS** (RAG faithfulness/retrieval, not multi-provider hub); **Automated Risk Assessment** (adversarial TAP/translation safety TP—may *call* EvalHub API but is not the hub); **Guardrails** (runtime rails); **Model Monitoring (TrustyAI)** (tabular/OVMS drift/bias); **Gen AI Playground** (interactive try-out). A lone single-harness notebook/CI with no multi-framework orchestration need stays on that harness or **LMEval**, not this row.

## Detection aliases

- DIY multi-harness glue: CI/Makefile running ≥2 of `lm-eval`/`lm_eval`, `garak`, `guidellm`, `lighteval`; targets `eval`/`benchmark`/`safety-scan`/`perf-bench`; hand-merged score tables / pass criteria
- Custom orchestrators: REST “eval service”, KFP/Tekton steps per harness, shared model URL + fan-out Jobs, weighted suite YAML across frameworks
- MLflow / export DIY: per-harness `MLFLOW_TRACKING_URI` logging; hand-rolled OCI/result export for multi-tool gates
- BYOF smell: custom `FrameworkAdapter`-like wrappers, “bring your own eval container”, org-built adapter images without hub registration
- Upstream / SDK already-on: `pip install eval-hub-sdk`, `from evalhub import SyncEvalHubClient`/`AsyncEvalHubClient`, `JobSubmissionRequest`, `evalhub eval run`/`collections`/`providers`, `FrameworkAdapter` / `run_benchmark_job`
- RHOAI already-on path: `kind: EvalHub`, `apiVersion: trustyai.opendatahub.io/v1alpha1`, `evalhubs.trustyai.opendatahub.io`, spec `providers:` `lm_evaluation_harness`/`garak`/`guidellm`/`lighteval`, `collections:`, `app=eval-hub`, `/api/v1/evaluations/jobs`, header `X-Tenant`
- Design language: “evaluation hub”, “unified eval platform”, “multi-provider eval”, “BYOF adapter”, collections with weighted thresholds

## Row for `EvalHub`

| DIY lm-eval+Garak+GuideLLM+LightEval glue; custom multi-harness eval gate scripts; hand-rolled K8s Jobs/KFP per harness; custom REST eval service; weighted collection/leaderboard YAML DIY; per-harness MLflow glue; BYOF/custom FrameworkAdapter wrappers; Makefile/CI multi-target chains; notebook stitch-together suites; standalone upstream eval-hub | EvalHub | lm-eval+garak+guidellm+lighteval CI glue; multi-harness eval gate / safety-scan+benchmark+perf-bench; KFP/Jobs per harness; custom REST eval service; weighted suite/collection YAML; per-harness MLFLOW_TRACKING_URI; FrameworkAdapter / BYOF eval container; eval-hub-sdk / SyncEvalHubClient / evalhub eval run; kind: EvalHub / trustyai.opendatahub.io / providers lm_evaluation_harness|garak|guidellm|lighteval; “evaluation hub” / multi-provider eval |
