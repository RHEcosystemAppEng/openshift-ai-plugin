# Model Monitoring (TrustyAI)

Production **tabular** bias/fairness (protected attributes → outcomes) and **data drift** (live inference inputs vs training reference) monitoring via per-project `TrustyAIService` on **OVMS**—Prometheus metrics, thresholds, dashboards. Peers are DIY/SaaS drift and fairness stacks that teams run instead of (or before) the RHOAI TrustyAI monitoring service.

## Peers

- Evidently — `evidently` / `evidentlyai` `Report`, `DataDriftPreset`, `TargetDriftPreset`, `ColumnDriftMetric` batch/CI drift dashboards
- alibi-detect — `alibi_detect.cd` `KSDrift`, `MMDDrift`, `ChiSquareDrift`, `ClassifierDrift`, `TabularDrift` on feature batches
- AIF360 — `aif360` / `aif360.sklearn.metrics` `statistical_parity_difference`, `disparate_impact` privileged/unprivileged group fairness
- fairlearn — `MetricFrame`, `demographic_parity_difference`, `equalized_odds_difference` fairness scoring notebooks
- WhyLabs / Fiddler / Arize — SaaS or agent-based production drift/data-quality monitors on tabular predictions
- NannyML — `nannyml` CBPE / estimated performance degradation without ground truth
- DIY KS / PSI / Jensen–Shannon / Chi² — custom scripts comparing training CSV vs live batch distributions
- DIY Prometheus / Grafana model-quality — custom exporters for prediction drift, accuracy drop, SPD/DIR-style gauges + Alertmanager rules
- Offline inference log → batch fairness/drift — log every input/output to CSV/S3, cron Jobs recompute KS/SPD (no live TrustyAI service)

**Not peers (adjacent catalog jobs):** **LMEval** / **EvalHub** (LLM harnesses, not tabular SPD/DIR); **RAGAS** (RAG groundedness/retrieval); **Guardrails (NeMo Guardrails)** (request-time LLM rails); **Automated Risk Assessment** (pre-prod adversarial probing); **Feature Store** (train/serve feature defs—does not replace live drift alerts); **MLflow** (experiment runs, not production inference bias/drift); infra-only Prometheus (node/GPU/HPA without prediction/fairness semantics). TrustyAI operator umbrella CRs for LMEval/Guardrails/RAGAS alone are not this monitoring entry.

## Detection aliases

- Evidently: `evidently`, `evidentlyai`, `from evidently`, `DataDriftPreset`, `TargetDriftPreset`, `ColumnDriftMetric`, `Report`, Evidently UI/presets
- alibi-detect: `alibi-detect`, `alibi_detect`, `alibi_detect.cd`, `KSDrift`, `MMDDrift`, `ChiSquareDrift`, `ClassifierDrift`, `TabularDrift`
- AIF360: `aif360`, `aif360.sklearn.metrics`, `statistical_parity_difference`, `disparate_impact`, privileged/unprivileged group defs
- fairlearn: `fairlearn`, `MetricFrame`, `demographic_parity_difference`, `equalized_odds_difference`
- WhyLabs / Fiddler / Arize: WhyLabs / whylogs / Fiddler / Arize drift or data-quality monitors in deps, config, or SaaS
- NannyML: `nannyml`, CBPE, estimated performance without labels
- DIY stats: KS test, PSI, Jensen–Shannon, Chi² comparing training reference vs live features; “data drift alert”, “protected attribute”, “SPD/DIR”, “fair lending”
- DIY Prometheus: exporters/gauges for prediction drift / fairness; Alertmanager “model performance degradation” / “feature distribution shift” / “bias threshold exceeded”; Grafana model-monitoring/fairness/drift dashboards (not infra-only)
- Offline batch: inference logs → CSV/S3 → scheduled KS/SPD jobs
- RHOAI already-on path: `kind: TrustyAIService`, `trustyai.opendatahub.io`, DSC `trustyai: Managed`, `MM_PAYLOAD_PROCESSORS`, `/metrics/drift/*`, `/metrics/group/fairness/spd|dir/request`, `trustyai_spd` / `trustyai_dir` / `trustyai_meanshift` / `trustyai_kstest` / `trustyai_*`

## Row (for table)

| Evidently drift presets; alibi-detect KS/MMD/ChiSquare/TabularDrift; AIF360 SPD/DIR; fairlearn MetricFrame / demographic parity; WhyLabs / Fiddler / Arize SaaS drift; NannyML CBPE; DIY KS/PSI/JS/Chi² scripts; DIY Prometheus/Grafana model-quality exporters; offline inference-log → batch KS/SPD cron | Model Monitoring (TrustyAI) | evidently / DataDriftPreset / ColumnDriftMetric; alibi_detect.cd / KSDrift / MMDDrift / TabularDrift; aif360 / statistical_parity_difference / disparate_impact; fairlearn / MetricFrame / demographic_parity_difference; WhyLabs / whylogs / Fiddler / Arize; nannyml / CBPE; custom KS/PSI/JS drift vs training reference; Prometheus model-drift/fairness gauges + Grafana; TrustyAIService / /metrics/drift/* / trustyai_spd|dir|meanshift|kstest (already-on) |
