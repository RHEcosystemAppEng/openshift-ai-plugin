# Feature Store

Feast-based **centralized ML feature definitions** with shared offline (training/batch) and online (low-latency serving) paths so the same feature logic is reused across train and serve, reducing training–serving skew and enabling multi-model/team feature sharing. Peers are standalone Feast, commercial/cloud feature platforms, and DIY duplicated transforms / Redis caches / hand-rolled point-in-time joins that teams use instead of (or before) adopting RHOAI Feature Store (`feastoperator: Managed`, `kind: FeatureStore`).

## Peers

- Feast standalone — self-hosted Feast (`feature_store.yaml`, `Entity`/`FeatureView`, `feast apply`/`materialize`) outside RHOAI DSC / Feast Operator
- Tecton — managed feature platform (Feature Services, materialization, online/offline retrieval) as the system of record
- Hopsworks Feature Store — Hopsworks FS / Feature View / training datasets and online serving
- Databricks Feature Store / Unity Catalog features — Databricks FS / UC feature tables as the governed feature catalog
- Google Vertex AI Feature Store — Vertex Feature Store / Feature Online Store / Feature Registry SDKs
- Amazon SageMaker Feature Store — SageMaker FeatureGroup / offline+online store APIs
- Azure Machine Learning Feature Store — Azure ML feature store / feature sets as the shared definitions
- DIY Redis / DynamoDB feature cache — entity-keyed KV “features” populated by cron/Airflow without a Feast registry
- Duplicated pandas / Spark / SQL transforms — train path Spark/SQL/dbt vs serve path pandas/numpy/FastAPI reimplementation (train–serve skew)
- Hand-rolled point-in-time joins — `merge_asof` / custom ASOF SQL / notebook spines without a shared feature registry
- Shared transform library only — pip package of `engineer_features` imported by train+serve with no offline/online stores or materialization
- Spreadsheet / Markdown feature specs — DS→MLE handoff docs reimplemented independently per repo

## Detection aliases

- Feast standalone: `pip install feast`, `from feast import Entity, FeatureView, Field, FeatureStore, FeatureService`, `@on_demand_feature_view`, `feature_store.yaml` (`project`/`registry`/`online_store`/`offline_store`/`provider`), `get_historical_features` / `get_online_features`, `feast init`/`apply`/`plan`/`materialize`/`materialize-incremental`, `feature_repo/`, `POST …/get-online-features` (often `:6566`) — without DSC `feastoperator` / `kind: FeatureStore`
- Tecton: `tecton`, `FeatureService`, `BatchFeatureView` / `StreamFeatureView` / `RealtimeFeatureView`, `tecton.apply`, Tecton materialization / online store
- Hopsworks: `hsfs`, `hopsworks`, Feature Store / Feature View / Training Dataset APIs, Hopsworks online FG serving
- Databricks Feature Store / UC features: `databricks.feature_store`, `FeatureStoreClient`, `create_table` / `write_table` / `create_training_set`, Unity Catalog feature tables
- Vertex AI Feature Store: `aiplatform.Featurestore`, `FeatureOnlineStore`, `gcloud ai featurestore`, Vertex Feature Registry
- SageMaker Feature Store: `sagemaker.FeatureGroup`, `create_feature_group`, `PutRecord` / `GetRecord`, SageMaker Feature Store offline+online
- Azure ML Feature Store: `azure.ai.ml` feature store / feature set, `az ml feature-set`
- DIY Redis/Dynamo feature cache: Redis/DynamoDB hash keyed by `user_id`/`entity_id`, cron/`kind: CronJob`/Airflow materialize into cache, no Feast registry
- Duplicated pandas/Spark/SQL: Spark/SQL/dbt features in `train/` + pandas/`def engineer_features` in `serve/`; skew parity tests (`test_feature_parity`); “training-serving skew” / NULL-fill offline≠online comments
- Hand-rolled PIT joins: `merge_asof`, custom ASOF SQL, “as-of” training spines without FeatureView registry
- Shared library only: shared `feature_engineering.py` / `preprocess.py` / `transforms.py` package, no online store / materialize
- Feature-spec docs: feature column spreadsheets/Markdown, “which notebook defines production features?”, “copy winning feature logic to prod”
- RHOAI already-on (confirm): DSC `feastoperator: Managed`, `apiVersion: feast.dev/v1alpha1`/`feast.dev/v1` `kind: FeatureStore`, `oc get feast`/`featurestores`, label `feature-store-ui: enabled`

## Row (for table)

| Feast standalone; Tecton; Hopsworks Feature Store; Databricks Feature Store / UC features; Vertex AI Feature Store; SageMaker Feature Store; Azure ML Feature Store; DIY Redis/Dynamo feature cache; duplicated pandas/Spark/SQL transforms; hand-rolled point-in-time joins; shared transform library only; spreadsheet/Markdown feature specs | Feature Store | feast Entity/FeatureView/FeatureStore/FeatureService, feature_store.yaml, get_historical_features/get_online_features, feast apply/materialize (non-DSC); tecton FeatureService/BatchFeatureView; hsfs/hopsworks Feature View; databricks.feature_store FeatureStoreClient; aiplatform.Featurestore / FeatureOnlineStore; sagemaker.FeatureGroup; azure.ai.ml feature-set; Redis/Dynamo entity KV + cron materialize; train Spark/SQL vs serve pandas skew / test_feature_parity; merge_asof / ASOF DIY; shared engineer_features package without online store; feature-spec spreadsheets |
