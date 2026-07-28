# OpenVINO Model Server (OVMS)

Intel high-performance **predictive** inference server (REST/gRPC; TF Serving + KServe APIs) optimized for Intel CPU/GPU/NPU, with broad formats (OpenVINO IR, ONNX, TF, Paddle, TFLite). Peers are other Intel/CPU inference servers, DIY OpenVINO Runtime HTTP wrappers, and ONNX/CPU serving stacks that overlap the same job—plus standalone upstream OVMS outside RHOAI’s `kserve-ovms` path.

## Peers

- Upstream OpenVINO Model Server (standalone) — `openvino/model_server` / `intel/openvino-model-server` Docker/K8s outside RHOAI ServingRuntime
- DIY OpenVINO Runtime FastAPI/Flask — custom `/predict` or `/infer` wrapping `openvino` / `Core().compile_model` on IR/ONNX
- OpenVINO GenAI in-process app — `openvino_genai` `LLMPipeline`/`VLMPipeline` embedded in a local service (not managed OVMS)
- openvino_openai_model_serve / DIY OpenAI-compat OpenVINO FastAPI — community FastAPI bridges for OpenVINO models via OpenAI-shaped endpoints
- optimum-intel OVModelFor* HTTP service — `OVModelFor*` / `optimum-cli export openvino` loaded inside a custom ASGI/WSGI server
- Microsoft ONNX Runtime Server (deprecated) — historic `onnxruntime_server` HTTP/gRPC for ONNX on CPU overlapping predictive serve
- Community onnxruntime-server (kibae) — TCP/HTTP REST server for ONNX sessions (CPU/CUDA)
- DIY ONNX Runtime + FastAPI — `onnxruntime.InferenceSession` behind Flask/FastAPI `/predict`
- TensorFlow Serving — production TF SavedModel gRPC/REST server; OVMS reuses TF Serving–style Predict APIs and versioned model repos
- TorchServe — PyTorch predictive model server (landscape peer for classic DL serving on CPU/GPU)
- DeepSparse Server (Neural Magic) — CPU sparsity-aware ONNX inference server (FastAPI; EOL community, still seen in repos)
- BentoML OpenVINO/ONNX runners — Bento service packaging OpenVINO or ONNX runners as REST APIs
- Seldon Core OpenVINO/ONNX servers — Seldon/MLServer-style predictors wrapping OpenVINO or ONNX on K8s outside RHOAI
- Triton + OpenVINO backend (standalone) — `backend: "openvino"` / OpenVINO EP on Triton outside RHOAI when the goal is Intel IR/ONNX serve
- ONNX Runtime OpenVINO Execution Provider DIY — `CUDAExecutionProvider`/`OpenVINOExecutionProvider` session in a custom microservice
- In-process OpenVINO notebooks/apps — IR `.xml`+`.bin` + `ovc`/`mo` conversion with no dedicated model server (migration *candidate* to OVMS)

## Detection aliases

- Upstream OVMS: `openvino/model_server`, `openvino/model_server:*-gpu`, `intel/openvino-model-server`, binary/`ovms`, `--model_path`, `--model_name`, `--config_path`, `--rest_port`, `--port`, `--target_device`, `--model_repository_path`, `model_config_list`, `ovmsclient`, gRPC `:9000`
- DIY OpenVINO Runtime HTTP: `import openvino`, `openvino.runtime`, `Core().compile_model`, `read_model`, FastAPI/Flask `/predict`/`/infer` loading `*.xml`/`*.bin`
- OpenVINO GenAI in-process: `import openvino_genai`, `LLMPipeline`, `VLMPipeline` as local app (not OVMS image)
- OpenAI-compat OpenVINO FastAPI: `openvino_openai_model_serve`, DIY uvicorn OpenVINO + `/v1/chat/completions`
- optimum-intel: `optimum-intel`, `from optimum.intel import OVModelFor*`, `optimum-cli export openvino`, `OVModelForCausalLM.from_pretrained`
- IR / conversion: paired `*.xml`+`*.bin`, `ovc`, `mo.py`/`mo`, `openvino.convert_model`, `nncf`, Open Model Zoo / `omz_downloader`
- Microsoft ORT Server: `onnxruntime_server`, `--model_path` + `--http_port`/`--grpc_port` (deprecated docs)
- Community ORT server: `kibae/onnxruntime-server`, `kibaes/onnxruntime-server`, `onnxruntime_server --model-dir`
- DIY ORT HTTP: `onnxruntime`, `InferenceSession`, FastAPI/`/predict` over `.onnx`
- TensorFlow Serving: `tensorflow/serving`, `tensorflow_model_server`, `tensorflow_serving.apis`/`PredictRequest`, versioned `model_name/<int>/`
- TorchServe: `torchserve`, `torch-model-archiver`, `MAR` handlers, `pytorch/torchserve`
- DeepSparse: `deepsparse`, `deepsparse.server`, `neuralmagic/deepsparse`, DeepSparse FastAPI server CLI
- BentoML: `bentoml`, OpenVINO/ONNX runner in `service.py`, `bentoml serve`
- Seldon: `SeldonDeployment`, Seldon OpenVINO/ONNX server images, non-RHOAI MLServer OpenVINO plugin
- Triton OpenVINO backend: `backend: "openvino"`, Triton `config.pbtxt` + IR/ONNX, standalone `nvcr.io/nvidia/tritonserver` (Intel path)
- ORT OpenVINO EP: `OpenVINOExecutionProvider`, `onnxruntime-openvino`
- Device / HW: `--target_device CPU|GPU|NPU|AUTO`, `/dev/dri`, `/dev/accel`, OpenVINO GPU/NPU tags
- RHOAI adoption markers (already on path): `runtime: kserve-ovms`, `quay.io/modh/openvino_model_server`, ServingRuntime display **OpenVINO Model Server**

## Row (for table)

| Upstream OVMS standalone; DIY OpenVINO Runtime FastAPI/Flask; OpenVINO GenAI in-process; openvino_openai_model_serve / DIY OpenAI-compat OpenVINO FastAPI; optimum-intel OVModelFor* HTTP; Microsoft ONNX Runtime Server; kibae onnxruntime-server; DIY ONNX Runtime + FastAPI; TensorFlow Serving; TorchServe; DeepSparse Server; BentoML OpenVINO/ONNX; Seldon Core OpenVINO/ONNX; Triton OpenVINO backend standalone; ORT OpenVINO EP DIY; in-process OpenVINO notebooks/apps | OpenVINO Model Server (OVMS) | openvino/model_server / intel/openvino-model-server / ovms / --model_path / model_config_list / ovmsclient / :9000; import openvino / Core().compile_model / FastAPI /predict on *.xml+*.bin; openvino_genai LLMPipeline/VLMPipeline; openvino_openai_model_serve; optimum-intel / OVModelFor* / optimum-cli export openvino; ovc / mo.py / paired .xml+.bin; onnxruntime_server; kibaes/onnxruntime-server; onnxruntime InferenceSession + FastAPI; tensorflow/serving / PredictRequest; torchserve; deepsparse.server; bentoml OpenVINO/ONNX; SeldonDeployment OpenVINO/ONNX; Triton backend openvino; OpenVINOExecutionProvider; --target_device CPU\|GPU\|NPU; kserve-ovms / quay.io/modh/openvino_model_server |
