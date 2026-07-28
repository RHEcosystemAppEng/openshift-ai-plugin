# MLflow Integration

On-cluster **experiment tracking**—parameters, metrics, artifacts, and run comparison across data scientists—via the OpenShift AI MLflow operator (`mlflowoperator: Managed`, `kind: MLflow`). Peers are SaaS/self-hosted trackers, TensorBoard event dirs, DIY CSV/JSON/spreadsheet run tables, and standalone `mlflow server` stacks that teams use instead of (or before) adopting RHOAI MLflow Integration.

## Peers

- Weights & Biases (W&B) — SaaS/offline `wandb.init` / `wandb.log` dashboards as the team experiment control plane
- Neptune — `neptune.init_run` / Neptune AI SaaS run and metadata tracking
- Comet ML — `comet_ml.Experiment` / Comet dashboards for metrics and artifacts
- Aim — `aim.init` / Aim UI self-hosted or hosted run comparison
- ClearML — ClearML Server + agents (Compose Redis/Mongo/ES) for experiments and artifacts
- TensorBoard — `SummaryWriter` / `tf.summary` / `tfevents` under `runs/` or `lightning_logs/` (local or cloud TensorBoard without a multi-team param store)
- DIY CSV / JSON run tables — hand-rolled `metrics.csv` / `results.json` / Lightning `CSVLogger` / pandas concat of run folders
- Spreadsheet / Google Sheet run logs — shared sheets or README tables of run_id → metrics as the comparison store
- Standalone MLflow server — Docker Compose / Helm / VM `mlflow server` + PostgreSQL + MinIO/S3 (`./mlruns`, `--backend-store-uri`, `--default-artifact-root`) outside RHOAI
- Sacred / lightweight JSON trackers — Sacred observers, blackboxml, similar file-based experiment libs
- Cloud experiment services — SageMaker Experiments, Azure ML run history, Vertex AI Experiments as off-cluster trackers
- Polyaxon / Katib metric UIs — Polyaxon or Kubeflow Katib used primarily for metric history (not HPO search alone)
- DVC experiments — `dvc exp` metric tables without a shared tracking UI (graduation candidate)

## Detection aliases

- Weights & Biases: `import wandb`, `wandb.init`, `wandb.log`, `wandb.finish`, `wandb.config`, `WANDB_API_KEY`, `wandb login`, `WandbLogger`, Accelerate `log_with="wandb"`, `mode="offline"`, `.wandb/`, `wandb sync`, `wandb.sweep`
- Neptune: `neptune.init_run`, `neptune`, `NEPTUNE_API_TOKEN`, Neptune run/project URLs
- Comet: `comet_ml.Experiment`, `comet_ml`, `COMET_API_KEY`, Accelerate `log_with="comet"`
- Aim: `aim.init`, `aim.Run`, Aim UI, Accelerate `log_with="aim"`
- ClearML: `clearml`, `Task.init`, ClearML Server Compose (Redis/Mongo/ES), ClearML agents, Accelerate `log_with="clearml"`
- TensorBoard: `SummaryWriter`, `writer.add_scalar`, `tf.summary.create_file_writer`, `tf.summary.scalar`, `tensorboard --logdir`, `runs/`, `lightning_logs/`, `.*tfevents.*`, `TensorBoardLogger`, Keras `TensorBoard` callback, Accelerate `log_with="tensorboard"`
- DIY CSV / JSON: `metrics.csv`, `results.json`, `experiments.csv`, `run_history.json`, `hparams.yaml`, Lightning `CSVLogger`, `pandas.DataFrame(...).to_csv("metrics.csv")`, scripts that `pd.concat` run CSVs
- Spreadsheets: Google Sheet / Excel of runs; README tables “run_id → accuracy”
- Standalone MLflow: `mlflow server`, `mlflow ui`, `--backend-store-uri postgresql://`, `--default-artifact-root s3://`, `MLFLOW_TRACKING_URI` → local/`file:`/`./mlruns`, Docker Compose MLflow+Postgres+MinIO, `MLFLOW_S3_ENDPOINT_URL` (no DSC `mlflowoperator` / `kind: MLflow` opendatahub)
- MLflow client already in code (migrate URI): `import mlflow`, `mlflow.start_run`, `mlflow.log_param` / `log_metric` / `log_artifact`, `mlflow.autolog`, `mlflow.set_tracking_uri`, `MLFLOW_TRACKING_URI`, Lightning `MLFlowLogger`, Accelerate `log_with="mlflow"`
- Sacred / light trackers: `sacred`, `Experiment(`, blackboxml, mlt-experiments CSV export
- Cloud experiments: SageMaker Experiments, Azure ML run history, Vertex AI Experiments / TensorBoard
- Polyaxon / Katib (metrics-only): Polyaxon experiment UI; Katib used for metric history not search
- DVC experiments: `dvc exp`, `dvc exp show` as primary metric table
- RHOAI already-on (confirm): DSC `mlflowoperator: Managed`, `kind: MLflow` (`mlflow.opendatahub.io`), `kind: MLflowConfig`, `MLFLOW_TRACKING_AUTH=kubernetes-namespaced`, gateway `/mlflow`

## Row (for table)

| Weights & Biases (W&B); Neptune; Comet ML; Aim; ClearML; TensorBoard; DIY CSV/JSON run tables; spreadsheet/Google Sheet run logs; standalone MLflow server (Compose/Helm/VM + Postgres + MinIO); Sacred / lightweight JSON trackers; SageMaker/Azure ML/Vertex Experiments; Polyaxon/Katib metric UIs; DVC experiments | MLflow Integration | wandb.init / wandb.log / WANDB_API_KEY / WandbLogger; neptune.init_run; comet_ml.Experiment; aim.init / Aim UI; clearml Task.init / ClearML Server; SummaryWriter / tf.summary / tfevents / tensorboard --logdir / TensorBoardLogger; metrics.csv / results.json / CSVLogger / hparams.yaml; Google Sheet run tables; mlflow server / mlflow ui / --backend-store-uri postgresql / --default-artifact-root s3 / ./mlruns / Compose MLflow+Postgres+MinIO (no mlflowoperator); mlflow.start_run / log_param|log_metric|log_artifact / MLFLOW_TRACKING_URI / MLFlowLogger; sacred Experiment; SageMaker/Azure/Vertex Experiments; Polyaxon / Katib metric UI; dvc exp |
