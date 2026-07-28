# Data Science Pipelines (Kubeflow Pipelines)

KFP-based **ML workflow orchestration** on OpenShift AI: define, version, schedule, and track multi-step DAGs (data prep → train → evaluate → deploy) with S3 artifact lineage, parameterized runs, and recurring executions (`aipipelines: Managed`). Peers are other ML/dataflow orchestrators, standalone Kubeflow Pipelines, notebook/DVC graduation stacks, and Makefile/cron DIY retrain chains that teams use instead of (or before) adopting RHOAI Data Science Pipelines.

## Peers

- Apache Airflow — DAGs / TaskFlow chaining prep→train→eval→deploy (`PythonOperator` / `KubernetesPodOperator`, Astronomer/MWAA/Composer)
- Prefect — `@flow` / `@task` retrain and promote flows with cron/deployments and work pools
- Luigi — Spotify-style `luigi.Task` graphs (`requires` / `output` / `run`) for Clean→Train→Score
- Flyte — Kubernetes-native typed workflows (`@workflow` / `@task`, FlytePropeller) as the ML DAG engine
- ZenML — pipeline/step abstractions that compile to Airflow/Kubeflow/other orchestrators
- Metaflow — Netflix-style `@step` DAGs (`metaflow.FlowSpec`) often on AWS Batch/K8s
- Dagster — software-defined assets / jobs / schedules for ML and data pipelines
- Kedro — project pipeline nodes/pipelines (`Pipeline`, `node`) often run via Airflow/Kubeflow backends
- standalone Kubeflow Pipelines — off-cluster `kfp` SDK / `pipeline.yaml` / `kfp.Client` without RHOAI pipeline server
- Argo Workflows DIY — raw `Workflow` / `CronWorkflow` for ML steps outside DSP (`aipipelines`)
- Makefile / shell DIY — `make train|evaluate|deploy|pipeline` or `train.sh` / `retrain.sh` / `run_pipeline.sh` chains
- CronJob / cron DIY — host crontab or `kind: CronJob` scheduled `python train.py` / `retrain.py` without a pipeline engine
- DVC stages — `dvc.yaml` / `dvc repro` as the only multi-step orchestrator (graduation candidate)
- papermill / notebook chains — multi-notebook cell-order or `papermill` parameter sweeps without a scheduler

## Detection aliases

- Apache Airflow: `from airflow import DAG`, `@dag` / `@task`, `PythonOperator`, `BashOperator`, `KubernetesPodOperator`, `task1 >> task2`, `schedule_interval` / `schedule`, `apache-airflow`, Astronomer/MWAA/Composer, DAGs under `dags/`
- Prefect: `from prefect import flow, task`, `@flow`, `@task`, `flow.serve(..., cron=...)`, `prefect deploy`, `prefect.yaml`, `prefect worker start`, `prefect-aws`
- Luigi: `import luigi`, `luigi.Task`, `requires` / `output` / `run`, `luigi.LocalTarget`, `luigi.build`, `python -m luigi`
- Flyte: `flytekit`, `@workflow`, `@task`, `FlyteFile` / `FlyteDirectory`, `pyflyte`, FlytePropeller, `flytectl`
- ZenML: `zenml`, `@pipeline`, `@step`, `zenml pipeline run`, ZenML stack / orchestrator config
- Metaflow: `from metaflow import FlowSpec, step`, `@step`, `metaflow`, `argo-workflows` Metaflow scheduler
- Dagster: `dagster`, `@asset`, `@job`, `@op`, `Definitions`, `dagster-webserver`, `schedule` / `Sensor`
- Kedro: `kedro`, `Pipeline(`, `node(`, `kedro run`, `catalog.yml`, `pipeline_registry.py`
- standalone KFP: `from kfp import dsl`, `@dsl.pipeline`, `@dsl.component`, `compiler.Compiler().compile`, `pipeline.yaml` / `PipelineSpec`, `kfp.Client()`, `kfp dsl compile`, `kfp-kubernetes` (no RHOAI Pipelines tab / DSC `aipipelines`)
- Argo Workflows DIY: `kind: Workflow`, `kind: CronWorkflow`, `argoproj.io`, `argo submit` for train/eval/deploy (no DSP pipeline server)
- Makefile / shell DIY: Makefile targets `train` / `evaluate` / `eval` / `deploy` / `pipeline` / `all`, `make train`, `train.sh`, `retrain.sh`, `run_pipeline.sh`
- CronJob / cron DIY: `kind: CronJob`, `schedule: "0 2 * * *"`, crontab/`systemd` timer + `python train.py` / `retrain.py`, names `model-retraining` / `nightly-retrain`
- DVC: `dvc.yaml`, `dvc repro`, `dvc stage`, stages `prepare` → `train` → `evaluate`
- papermill / notebooks: `papermill`, multi-`.ipynb` “pipeline” cell order, notebook parameter sweeps without KFP/Airflow schedule
- RHOAI already-on (confirm): DSC `aipipelines: Managed`, Elyra `.pipeline`, OpenShift AI Pipelines tab / pipeline server

## Row (for table)

| Apache Airflow; Prefect; Luigi; Flyte; ZenML; Metaflow; Dagster; Kedro; standalone Kubeflow Pipelines; Argo Workflows DIY; Makefile/shell DIY; CronJob/cron DIY; DVC stages; papermill/notebook chains | Data Science Pipelines (Kubeflow Pipelines) | Airflow: from airflow import DAG, @dag/@task, PythonOperator/KubernetesPodOperator, task1 >> task2, apache-airflow; Prefect: @flow/@task, flow.serve cron, prefect.yaml, prefect deploy; Luigi: luigi.Task, requires/output/run, luigi.build; Flyte: flytekit, @workflow/@task, pyflyte, FlytePropeller; ZenML: zenml @pipeline/@step, zenml pipeline run; Metaflow: FlowSpec/@step; Dagster: @asset/@job, Definitions; Kedro: Pipeline(, node(, kedro run; standalone KFP: from kfp import dsl, @dsl.pipeline, compiler.Compiler, pipeline.yaml, kfp.Client (no aipipelines); Argo DIY: kind Workflow/CronWorkflow, argoproj.io; Makefile/shell: make train|evaluate|deploy|pipeline, train.sh/retrain.sh; CronJob/cron: kind CronJob schedule + python train.py/retrain.py; DVC: dvc.yaml, dvc repro; papermill: papermill, multi-ipynb cell-order pipelines |
