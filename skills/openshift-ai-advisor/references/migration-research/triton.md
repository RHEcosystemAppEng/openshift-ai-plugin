# NVIDIA Triton Inference Server

RHOAI wraps NVIDIA Triton as a tested/verified KServe `ServingRuntime` for multi-framework GPU inference (TensorRT, ONNX, PyTorch, TensorFlow), dynamic batching, concurrent model execution, and model ensembles/pipelines. Left-column peers are **non-Triton** framework servers and DIY multi-model stacks teams use instead of that path, plus **standalone Triton** (raw `nvcr.io/nvidia/tritonserver` Deployments/Helm outside RHOAI) as a migrate-from into the catalog runtime.

## Peers

- TorchServe — PyTorch-native production server (`.mar` archives, custom handlers); common single-framework alternative to Triton’s multi-backend GPU path
- TensorFlow Serving — TF SavedModel / gRPC-REST serving with version policies; TF-centric alternative to Triton’s TensorFlow backend
- DeepSparse Server — Neural Magic CPU ONNX inference HTTP server (`deepsparse.server`); sparse/quantized CPU alternative to Triton GPU multi-model serving
- ONNX Runtime Server / ORT HTTP DIY — Microsoft `onnxruntime_server` or FastAPI wrapping `onnxruntime` / TensorRT EP; ONNX-only peer without Triton model repo
- Custom multi-model ensemble DIY — FastAPI/Flask `/predict` loading and chaining multiple ONNX/TensorRT/Torch/TF models in app code
- Hand-rolled dynamic batching queues — custom request coalescing in front of TensorRT/ORT/PyTorch without a model server
- NVIDIA TensorRT standalone + thin HTTP — `trtexec` / `.plan`/`.engine` engines behind a homemade REST/gRPC wrapper (no Triton ensembles)
- Standalone NVIDIA Triton (`nvcr.io/nvidia/tritonserver`) — DIY Deployment/Helm/Compose with `tritonserver --model-repository=`; migrate into RHOAI `triton-kserve-rest` ServingRuntime
- BentoML multi-model runners — Bento packaging with multiple runners / Triton-as-runner optional; Python-first multi-artifact serve without RHOAI Triton
- Ray Serve multi-deployment — Ray actors/deployments chaining models with batching APIs as a DIY ensemble plane
- Seldon Core custom / prepackaged servers — Seldon graphs or custom servers for multi-step inference pipelines on Kubernetes (non-RHOAI)
- Amazon SageMaker multi-model / Triton container mode — SageMaker MMEs or “Triton mode” packaging (`config.pbtxt` + version dirs) outside OpenShift AI
- KFServing/KServe upstream `predictor.triton` DIY — InferenceService pointing at Triton image/config on vanilla Kubernetes (not OpenShift AI managed runtime)
- PyTorch eager + FastAPI multi-worker — `torch.load` / TorchScript in Uvicorn workers with manual concurrency (no TorchServe/Triton)

## Detection aliases

- TorchServe: `torchserve`, `torch-model-archiver`, `.mar`, `MAR_CONFIG`, `config.properties` (`inference_address`, `management_address`), `Handler` / `BaseHandler`, image `pytorch/torchserve`, ports `:8080`/`:8081`
- TensorFlow Serving: `tensorflow_model_server`, `tensorflow/serving`, `model_config_list`, `SavedModel`, `--model_base_path=`, gRPC `:8500` / REST `:8501`, `PredictRequest`
- DeepSparse Server: `deepsparse`, `deepsparse.server`, `pip install deepsparse[server]`, `server-config.yaml` endpoints, SparseZoo `zoo:` stubs
- ONNX Runtime Server / ORT DIY: `onnxruntime_server`, `InferenceSession`, `onnxruntime-gpu`, `TensorrtExecutionProvider` / `CUDAExecutionProvider`, FastAPI + `ort.InferenceSession`
- Custom multi-model ensemble DIY: multiple `onnxruntime`/`tensorrt`/`torch.jit.load` loads in one service; app-level “pipeline” / “cascade” / “ensemble” comments; chained `/predict` stages
- Hand-rolled dynamic batching: custom `asyncio.Queue` / batch-window loops before `execute_async_v3` / ORT `run`; DIY `preferred_batch_size`-like constants without `config.pbtxt`
- TensorRT standalone: `trtexec`, `tensorrt`, `nvinfer`, `.engine` / `.plan` (no `config.pbtxt`), `cuda.Device` + custom Flask/FastAPI
- Standalone Triton: `nvcr.io/nvidia/tritonserver`, `tritonserver`, `--model-repository=` / `--model-store=`, `config.pbtxt`, `platform: "tensorrt_plan"|"onnxruntime_onnx"|"pytorch_libtorch"|"ensemble"`, `ensemble_scheduling`, `tritonclient`, `import triton_python_backend_utils`, ports `8000`/`8001`/`8002`, `perf_analyzer` / `model-analyzer`
- BentoML: `bentoml`, `@bentoml.service`, `bentoml.Runner`, `bentoml build`, `BentoML` Triton runner extras
- Ray Serve: `ray.serve`, `@serve.deployment`, `serve.run(`, `rayproject/ray` Serve apps chaining models
- Seldon Core: `SeldonDeployment`, `PredictorSpec`, Seldon V2 `InferenceGraph` / pipeline steps, `seldonio/` images
- SageMaker MME / Triton mode: `MultiModelConfig`, SageMaker Triton inference container, `config.pbtxt` under SageMaker model dir, `sagemaker-tritonserver`
- Upstream KServe Triton predictor: `spec.predictor.triton`, `modelFormat.name: triton`, InferenceService + Triton image without RHOAI `triton-kserve-rest` / `openshift.io/display-name` Triton
- PyTorch FastAPI DIY: `torch.load` / `torch.jit.load` + FastAPI `/predict` / Uvicorn multi-worker GPU serve

## Row (for table)

| TorchServe; TensorFlow Serving; DeepSparse Server; ONNX Runtime Server / ORT HTTP DIY; custom multi-model ensemble DIY; hand-rolled dynamic batching queues; NVIDIA TensorRT standalone + thin HTTP; standalone nvcr.io/nvidia/tritonserver Deployments; BentoML multi-model runners; Ray Serve multi-deployment; Seldon Core custom/prepackaged servers; SageMaker multi-model / Triton container mode; upstream KServe predictor.triton DIY; PyTorch eager + FastAPI multi-worker | NVIDIA Triton Inference Server | torchserve / torch-model-archiver / .mar / pytorch/torchserve; tensorflow_model_server / tensorflow/serving / SavedModel / :8500/:8501; deepsparse.server / zoo: stubs; onnxruntime_server / InferenceSession / TensorrtExecutionProvider; DIY multi-model FastAPI chains / batch queues; trtexec / .engine/.plan thin HTTP; nvcr.io/nvidia/tritonserver / tritonserver --model-repository= / config.pbtxt / ensemble_scheduling / tritonclient / triton_python_backend_utils / :8000/:8001/:8002; bentoml Runner; ray.serve @serve.deployment; SeldonDeployment / InferenceGraph; SageMaker MultiModelConfig / sagemaker-tritonserver; spec.predictor.triton / modelFormat.name: triton; torch.load + FastAPI /predict |
