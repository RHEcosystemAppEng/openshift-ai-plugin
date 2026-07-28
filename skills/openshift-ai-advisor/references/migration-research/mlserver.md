# MLServer ServingRuntime

## Peers
- DIY joblib/pickle FastAPI `/predict` — hand-rolled HTTP wrapper around `joblib.load`/`pickle.load` + `model.predict`/`predict_proba` for sklearn/XGBoost/LightGBM
- DIY Flask/Django/uvicorn sklearn serve — same artifact + ad-hoc JSON feature API behind gunicorn/uvicorn Deployment+Service
- Standalone SeldonIO MLServer — `mlserver start` / `seldonio/mlserver` outside RHOAI; migrate into managed **MLServer ServingRuntime** under KServe
- Seldon Core `SKLEARN_SERVER` / `XGBOOST_SERVER` / `LIGHTGBM_SERVER` — pre-packaged servers (often MLServer + V2/`kfserving` protocol) on non-RHOAI clusters
- Upstream KServe sklearn/xgboost/lightgbm predictors — `spec.predictor.sklearn` / `.xgboost` / `.lightgbm` or `runtime: kserve-sklearnserver` / `kserve-mlserver` outside OpenShift AI
- KFServing V1 sklearn predictor DIY — legacy KFServing manifests serving joblib/bst without RHOAI deploy wizard
- BentoML sklearn/XGBoost service — `@bentoml.service` packaging classical ML into custom containers instead of KServe MLServer runtime
- Ray Serve sklearn wrapper — `serve.deployment` wrapping `.pkl`/`.joblib`/Booster for predictive APIs
- MLflow `models serve` / pyfunc sklearn flavor — local or K8s `mlflow models serve` for sklearn/xgboost artifacts (plain joblib/bst path maps to MLServer on RHOAI)
- Amazon SageMaker scikit-learn / XGBoost inference — built-in SKLearn/XGBoost containers and real-time endpoints
- Google Vertex AI custom prediction (sklearn) — custom container or prebuilt sklearn prediction on Vertex endpoints
- Azure ML sklearn online endpoint — managed online endpoints scoring pickled sklearn/xgboost models
- Cortex (cortexlabs) — open-source K8s/AWS deploy of sklearn/XGBoost as web services
- Tempo (SeldonIO) pipelines — Python inference graphs often backed by MLServer runtimes for classical models
- Custom ONNX Runtime HTTP for classical exports — DIY ORT server for sklearn→ONNX artifacts where RHOAI path would use MLServer’s ONNX/sklearn formats

## Detection aliases
- DIY FastAPI/Flask: `joblib.load`, `pickle.load`, `model.predict(`, `predict_proba(`, `@app.post("/predict")`, `/inference`, `/score`, `model.joblib`, `model.pkl`, `model.pickle`
- XGBoost/LightGBM DIY: `xgboost.Booster`, `XGBClassifier`, `bst.save_model`, `load_model`, `model.bst`, `model.json`, `model.ubj`, `lightgbm.Booster`
- Standalone MLServer: `pip install mlserver`, `mlserver-sklearn`, `mlserver-xgboost`, `mlserver-lightgbm`, `mlserver-onnx`, `mlserver start`, `mlserver build`, `model-settings.json`, `mlserver_sklearn.SKLearnModel`, `mlserver_xgboost.XGBoostModel`, `mlserver_lightgbm.LightGBMModel`, `seldonio/mlserver`, `MLSERVER_MODEL_IMPLEMENTATION`
- Seldon Core: `SKLEARN_SERVER`, `XGBOOST_SERVER`, `LIGHTGBM_SERVER`, `MLFLOW_SERVER`, `kind: SeldonDeployment`, `protocol: kfserving`, `implementation: SKLEARN_SERVER`
- Upstream KServe/KFServing: `runtime: kserve-mlserver`, `runtime: kserve-sklearnserver`, `modelFormat.name: sklearn` / `xgboost` / `lightgbm`, `protocolVersion: v2`, `spec.predictor.sklearn`, `spec.predictor.xgboost`, `spec.predictor.lightgbm`, `POST /v2/models/`
- BentoML: `bentoml`, `@bentoml.service`, `bentoml.sklearn`, `BentoML` + sklearn/xgboost save/load
- Ray Serve: `ray.serve`, `serve.deployment`, sklearn/xgboost inside Ray Serve handlers
- MLflow serve: `mlflow models serve`, `mlflow.pyfunc`, `mlflow.sklearn`, `mlflow.xgboost`, sklearn flavor URI
- Cloud managed: `sagemaker.sklearn`, `SKLearnModel`, `XGBoostModel` (SageMaker), `aiplatform.Model` + sklearn custom prediction (Vertex), Azure ML `sklearn` online endpoint
- Cortex: `cortex deploy`, `cortex.yaml`, cortexlabs sklearn examples
- Tempo: `from tempo import`, `tempo.serve`, Seldon Tempo + MLServer

## Row (for table)
| DIY joblib/pickle FastAPI /predict; DIY Flask/Django/uvicorn sklearn serve; Standalone SeldonIO MLServer; Seldon Core SKLEARN_SERVER/XGBOOST_SERVER/LIGHTGBM_SERVER; Upstream KServe sklearn/xgboost/lightgbm predictors; KFServing V1 sklearn predictor DIY; BentoML sklearn/XGBoost; Ray Serve sklearn wrapper; MLflow models serve / pyfunc sklearn; SageMaker sklearn/XGBoost inference; Vertex AI custom prediction (sklearn); Azure ML sklearn online endpoint; Cortex; Tempo (SeldonIO); Custom ONNX Runtime HTTP for classical exports | MLServer ServingRuntime | DIY FastAPI/Flask: joblib.load, pickle.load, model.predict(, @app.post("/predict"), model.joblib, model.pkl; XGBoost/LightGBM DIY: xgboost.Booster, model.bst, lightgbm.Booster; Standalone MLServer: mlserver-sklearn, mlserver start, model-settings.json, mlserver_sklearn.SKLearnModel, seldonio/mlserver, MLSERVER_MODEL_IMPLEMENTATION; Seldon Core: SKLEARN_SERVER, XGBOOST_SERVER, LIGHTGBM_SERVER, SeldonDeployment, protocol: kfserving; Upstream KServe: runtime: kserve-mlserver, kserve-sklearnserver, modelFormat.name: sklearn/xgboost/lightgbm, protocolVersion: v2, spec.predictor.sklearn; BentoML: bentoml.sklearn, @bentoml.service; Ray Serve: ray.serve + sklearn; MLflow: mlflow models serve, mlflow.sklearn; Cloud: sagemaker.sklearn, Vertex/Azure sklearn endpoints; Cortex: cortex.yaml; Tempo: tempo.serve |
