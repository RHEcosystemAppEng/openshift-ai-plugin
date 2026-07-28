# Model Registry

Centralized **model versioning, metadata, and promotion** control plane: register artifacts, track versions/lineage, RBAC-share across projects, and gate staging→production with OCI/ModelCar-backed storage. Peers are cloud/SaaS model registries, standalone MLflow/W&B registries, Unity Catalog models, and DIY git-lfs/DVC/filename “registries” that teams use instead of (or before) adopting RHOAI Model Registry.

## Peers

- MLflow Model Registry (standalone) — self-hosted or Databricks MLflow `register_model` / stages / aliases (`champion`/`challenger`) as the lifecycle store
- Weights & Biases Artifacts / Model Registry — W&B artifact versions + registered models with aliases and lineage
- Amazon SageMaker Model Registry — managed model packages, approval statuses, and deploy-from-registry
- Databricks Unity Catalog models — UC `CREATE MODEL` / model versions as the governed artifact catalog
- Google Vertex AI Model Registry — Vertex registered models / model versions for promotion and deploy
- Azure Machine Learning Model Registry — Azure ML registered models + versioning + stage tags
- ClearML Models — ClearML model repository / versioning as the system of record
- Neptune model registry — Neptune project model versions and stage metadata
- Comet ML Model Registry — Comet registered models / model assets
- Domino Model Registry — Domino Data Lab model registry / governance gate
- Kubeflow Model Registry (upstream DIY) — self-managed `kubeflow/model-registry` outside RHOAI DSC
- DVC + git-lfs DIY versioning — `dvc.yaml` / `.dvc` remotes and Git LFS for `*.pt`/`*.onnx` as the release store
- Ad-hoc filename / folder versioning — `model_v1.pt`, `best_model.pth`, `models/v1/`, timestamp/metric checkpoints
- Sidecar metadata manifests — hand-maintained `model_metadata.json` / `versions.yaml` / `registry.json` next to weights
- Promote-script + S3 URI DIY — `promote.sh` / CI copy to prod bucket; versioned S3 prefixes as the only gate

## Detection aliases

- MLflow Model Registry: `mlflow.register_model`, `MlflowClient()`, `create_registered_model`, `create_model_version`, `transition_model_version_stage`, `set_registered_model_alias`, stages `Staging`/`Production`/`Archived`, aliases `champion`/`challenger`/`candidate`/`shadow`, `mlflow models`
- W&B Artifacts / Registry: `wandb`, `wandb.Artifact`, `use_artifact`, `link_model`, `wandb.Api().artifact`, W&B Model Registry / aliases in UI or API
- SageMaker Model Registry: `sagemaker.ModelPackage`, `create_model_package`, `ModelPackageGroup`, `aws sagemaker create-model-package`, approval statuses PendingManualApproval/Approved
- Unity Catalog models: `databricks` Unity Catalog `CREATE MODEL`, `mlflow` + UC registry URI (`databricks-uc`), `models:/` UC paths, `RegisteredModel` in UC
- Vertex AI Model Registry: `aiplatform.Model`, `gcloud ai models upload`, Vertex Model Registry / model versions
- Azure ML Model Registry: `azure.ai.ml`, `ml_client.models`, `az ml model create`, Azure ML registered model versions / stage tags
- ClearML Models: `clearml`, `OutputModel`, `InputModel`, ClearML model repository / Model ID
- Neptune: `neptune`, `neptune.init_model`, `ModelVersion`, Neptune model registry
- Comet: `comet_ml`, Comet Model Registry / `log_model` registered assets
- Domino: Domino Model Registry UI/API, Domino model versions / governance
- Kubeflow Model Registry (upstream): `kubeflow/model-registry`, `pip install model-registry`, `from model_registry import ModelRegistry` without RHOAI DSC/`kind: ModelRegistry`
- DVC + git-lfs: `dvc.yaml`, `*.dvc`, `.dvc/config`, `dvc push`/`dvc pull`, `.gitattributes` `filter=lfs` for `*.pt`/`*.pth`/`*.onnx`/`*.safetensors`
- Ad-hoc filenames: `model_v1.pt`, `model_v2.pth`, `best_model.pth`, `latest_model.pth`, `model_final.pt`, `models/v1/`, `model_YYYYMMDD*.pth`, `*_val_0.*.pth`
- Sidecar manifests: `model_metadata.json`, `versions.yaml`, `model_versions.csv`, `registry.json` version→path/metrics tables
- Promote + S3 DIY: `promote_model.py`, `promote.sh`, copy checkpoint to prod bucket, `s3://…/models/vN/`, “which pickle is in prod?” runbooks

## Row (for table)

| MLflow Model Registry (standalone); W&B Artifacts/Registry; SageMaker Model Registry; Databricks Unity Catalog models; Vertex AI Model Registry; Azure ML Model Registry; ClearML Models; Neptune model registry; Comet ML Model Registry; Domino Model Registry; Kubeflow Model Registry (upstream DIY); DVC+git-lfs DIY versioning; ad-hoc filename/folder versioning; sidecar metadata manifests; promote-script + S3 URI DIY | Model Registry | mlflow.register_model / MlflowClient / transition_model_version_stage / set_registered_model_alias / champion|challenger; wandb.Artifact / link_model / W&B Model Registry; sagemaker.ModelPackage / ModelPackageGroup / create-model-package; databricks-uc / CREATE MODEL / models:/ UC; aiplatform.Model / gcloud ai models; azure.ai.ml models / az ml model create; clearml OutputModel/InputModel; neptune.init_model; comet_ml model registry; Domino Model Registry; kubeflow/model-registry / model_registry.ModelRegistry (non-DSC); dvc.yaml / *.dvc / git-lfs *.pt; model_v1.pt / best_model.pth / models/v1/; model_metadata.json / versions.yaml / registry.json; promote.sh / s3://…/models/vN/ |
