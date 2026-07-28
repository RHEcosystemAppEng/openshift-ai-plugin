# KServe (Single-Model Serving Platform)

Kubernetes-native **single-model serving control plane**: per-model servers, storage pull, networking, autoscaling (Knative or RawDeployment), and auth via `ServingRuntime` / `InferenceService` CRDs. Peers are other serving platforms, managed cloud endpoints, standalone model servers run as DIY Deployments, and hand-rolled `/predict` stacks that teams use instead of (or before) adopting this platform.

## Peers

- Seldon Core — Kubernetes-native serving with `SeldonDeployment` / v2 `Model`+`Pipeline` CRDs, canary/A-B graphs
- BentoML / Yatai / BentoCloud — Python-first packaging (`bentofile`) plus K8s or managed deploy of Bento services
- Ray Serve — Python-native distributed serving graphs; often on KubeRay instead of InferenceService
- TensorFlow Serving — framework-native TF/SavedModel HTTP/gRPC server as the production endpoint
- TorchServe — PyTorch/TorchScript model server (`.mar` archives, management + inference APIs)
- NVIDIA Triton Inference Server (standalone) — multi-framework inference server Deployed without a KServe control plane
- OpenVINO Model Server (standalone) — OVMS image/gRPC/REST serving outside ServingRuntime/InferenceService
- MLServer (standalone) — Seldon MLServer V2 protocol server without KServe runtime wiring
- Amazon SageMaker Endpoints — managed real-time / serverless inference hosting
- Google Vertex AI Prediction — managed Vertex endpoints / prediction services
- Azure Machine Learning Online Endpoints — managed online (and batch) scoring endpoints
- Hugging Face Inference Endpoints — managed Hub-model dedicated/autoscaled inference APIs
- MLflow Model Serving — `mlflow models serve` / Databricks Model Serving for logged pyfunc flavors
- ClearML Serving — ClearML-orchestrated inference services on K8s/containers (often Triton/TorchServe engines)
- Anyscale — managed Ray Serve production hosting
- Knative Serving DIY — Knative `Service`/`Revision` wrapping a model container for scale-to-zero without KServe CRDs
- custom FastAPI / Flask / Django `/predict` + Deployment+Service+HPA — hand-rolled model HTTP API and K8s scaling
- standalone TGI / vLLM Deployment+Service — generative HTTP API as a plain workload (no InferenceService lifecycle)

## Detection aliases

- Seldon Core: `SeldonDeployment`, `kind: Model` + `kind: Pipeline` (Seldon v2), `machinelearning.seldon.io`, `seldon-core`, `SeldonDeployment`, `predictor_type`, `seldonio/seldon-core-operator`
- BentoML / Yatai / BentoCloud: `bentoml`, `import bentoml`, `@bentoml.service`, `bentofile.yaml`, `bentoml build`, `bentoml containerize`, `yatai`, `BentoRequest`, `BentoDeployment`, `api.bentoml.com`
- Ray Serve: `ray.serve`, `from ray import serve`, `@serve.deployment`, `serve.run(`, `ServeDeployment`, `KubeRay`, `RayService`, `rayproject/ray`
- TensorFlow Serving: `tensorflow/serving`, `tensorflow_model_server`, `--model_base_path=`, `/v1/models/`, `saved_model_cli`, `TFServing`
- TorchServe: `torchserve`, `torch-model-archiver`, `.mar`, `config.properties`, `pytorch/torchserve`, `/predictions/`, `management_api`
- Triton (standalone): `nvcr.io/nvidia/tritonserver`, `tritonserver`, `--model-repository=`, `config.pbtxt`, `tritonclient`, `platform: "onnxruntime_onnx"`
- OVMS (standalone): `openvino/model_server`, `ovms`, `ovms --model_path`, gRPC `:9000`, `optimum-cli export openvino`
- MLServer (standalone): `pip install mlserver`, `mlserver start`, `model-settings.json`, `mlserver_sklearn.SKLearnModel`, `mlserver-xgboost`
- SageMaker Endpoints: `sagemaker.CreateEndpoint`, `SagemakerRuntime.InvokeEndpoint`, `aws sagemaker create-endpoint`, `SageMaker` RealTimeEndpoint, `HuggingFaceModel.deploy`
- Vertex AI Prediction: `aiplatform.Endpoint`, `vertexai` predict, `gcloud ai endpoints`, `Vertex AI` Online Prediction
- Azure ML Online Endpoints: `azure.ai.ml`, `ManagedOnlineEndpoint`, `az ml online-endpoint`, `azureml-inference`
- Hugging Face Inference Endpoints: `create_inference_endpoint`, `InferenceEndpoint`, `hf.co/api/endpoint`, `huggingface_hub` endpoints, `HF_INFERENCE_ENDPOINT`
- MLflow / Databricks Serving: `mlflow models serve`, `mlflow.pyfunc`, `/invocations`, `databricks` model serving, `served_models`
- ClearML Serving: `clearml-serving`, `clearml_serving`, `clearml serving`, ClearML Serving Service Task
- Anyscale: `anyscale`, `anyscale serve`, Anyscale Cloud Ray Serve apps
- Knative Serving DIY: `serving.knative.dev/v1` `kind: Service`, `autoscaling.knative.dev/min-scale`, `kn service create`, scale-to-zero model container (no `serving.kserve.io`)
- custom FastAPI/Flask `/predict` + Deployment+Service+HPA: `@app.post("/predict")`, `Flask` `/predict`, `model.predict(`, `/health`/`/ready`, DIY `Deployment`+`Service`+`HorizontalPodAutoscaler` around loaded weights
- standalone TGI / vLLM Deployment: `ghcr.io/huggingface/text-generation-inference`, `text-generation-launcher`, `vllm/vllm-openai`, `vllm serve`, `python -m vllm.entrypoints.openai.api_server` as Deployment (no InferenceService)

## Row (for table)

| Seldon Core; BentoML / Yatai / BentoCloud; Ray Serve; TensorFlow Serving; TorchServe; NVIDIA Triton Inference Server (standalone); OpenVINO Model Server (standalone); MLServer (standalone); Amazon SageMaker Endpoints; Google Vertex AI Prediction; Azure ML Online Endpoints; Hugging Face Inference Endpoints; MLflow Model Serving; ClearML Serving; Anyscale; Knative Serving DIY; custom FastAPI/Flask/Django /predict + Deployment+Service+HPA; standalone TGI/vLLM Deployment+Service | KServe (Single-Model Serving Platform) | Seldon Core: SeldonDeployment, machinelearning.seldon.io, seldonio/seldon-core-operator; BentoML/Yatai: bentoml, @bentoml.service, bentofile.yaml, BentoDeployment, yatai; Ray Serve: ray.serve, @serve.deployment, RayService, KubeRay; TensorFlow Serving: tensorflow/serving, tensorflow_model_server, --model_base_path; TorchServe: torchserve, torch-model-archiver, .mar, pytorch/torchserve; Triton standalone: nvcr.io/nvidia/tritonserver, config.pbtxt, --model-repository; OVMS standalone: openvino/model_server, ovms; MLServer standalone: mlserver start, model-settings.json, mlserver_sklearn; SageMaker: CreateEndpoint, InvokeEndpoint, sagemaker; Vertex AI: aiplatform.Endpoint, gcloud ai endpoints; Azure ML: ManagedOnlineEndpoint, az ml online-endpoint; HF Endpoints: create_inference_endpoint, InferenceEndpoint; MLflow/Databricks: mlflow models serve, /invocations; ClearML Serving: clearml-serving; Anyscale: anyscale serve; Knative DIY: serving.knative.dev/v1 Service, autoscaling.knative.dev (no serving.kserve.io); DIY /predict: FastAPI/Flask @app.post("/predict"), model.predict(, Deployment+Service+HPA; TGI/vLLM DIY: text-generation-inference, vllm/vllm-openai, vllm serve as Deployment |
