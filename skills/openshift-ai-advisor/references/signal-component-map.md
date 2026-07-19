# Signal-to-Component Map

Use this table to match **capability** findings to OpenShift AI components. Read top-to-bottom; pick the first row that matches.

Whether a finding is already on OpenShift AI / OpenShift is signed by the project-scanner (`generic` | `openshift-ai` | `openshift`) from the **RHOAI:** tags in [detection-signals.md](detection-signals.md)—not by this table.

| What was found | Suggested component |
|---|---|
| PyTorch / TensorFlow / ONNX model files or inference scripts | **KServe** for production serving |
| Custom Flask/FastAPI endpoint serving a model (`model.predict()` behind `/predict`) | **KServe** to replace hand-built serving code |
| LLM weights or generative LLM inference (vLLM, TGI, SGLang, Ollama, DIY CausalLM) | **vLLM Serving Runtimes** (often with **KServe**) |
| Disaggregated / multi-node LLM inference, sticky/prefix-hash LB, llm-d / Dynamo P/D | **llm-d** for distributed inference |
| External LLM API calls (OpenAI, Anthropic, Azure, Bedrock) or LiteLLM/Portkey gateways | **Models-as-a-Service (MaaS)** for governed access |
| Scattered API keys for LLM providers across services or `.env` files | **MaaS** for centralized key management |
| Caikit framework or gRPC/streaming text-generation | **Caikit TGIS** runtime |
| Intel hardware targets, OpenVINO IR format files | **OVMS** runtime |
| NVIDIA Triton / TensorRT models, model ensembles, multi-model pipelines | **Triton** runtime |
| scikit-learn / XGBoost / LightGBM serve (MLServer or DIY joblib `/predict`) | **MLServer** runtime |
| RAG pipeline code (chunking, embeddings, vector queries) | **AutoRAG** to optimize, or **RAG Stack** for managed deployment |
| Docker Compose / Helm for vector DBs + custom retrieval API | **RAG Stack** to replace self-managed infrastructure |
| Chunk-size / embedding / top_k sweeps or RAG hyperparameter search | **AutoRAG** for automated optimization |
| Agentic AI patterns (LangGraph, CrewAI, AutoGen, multi-step tool loops) | **Llama Stack** for unified runtime |
| Custom embedding + retrieval logic in backend | **RAG Stack** for managed infrastructure |
| Distributed training code (DDP, DeepSpeed, Ray Train, PyTorchJob) | **Distributed Workloads** |
| Fine-tuning scripts (LoRA, QLoRA, PEFT, SFTTrainer, Unsloth/Axolotl) | **Model Customization** |
| Multi-step data/train/eval/deploy scripts | **Data Science Pipelines (KFP)** |
| Airflow DAGs, Prefect flows, Luigi pipelines, Makefile-chained ML steps | **Data Science Pipelines (KFP)** to replace custom orchestration |
| Apache Spark / PySpark / SparkApplication on Kubernetes | **Spark Operator (KSO)** |
| Jupyter notebooks / JupyterHub / notebook Deployments | **Workbenches** for managed environments |
| Custom Dockerfile for notebook/dev environment (`jupyter/*-notebook` or BYON) | **Custom Notebook Images** |
| MLflow / W&B / TensorBoard / CSV experiment logging | **MLflow Integration** to consolidate tracking |
| Ad-hoc model versioning (file naming, metadata JSONs, git-lfs, MLflow register/alias) | **Model Registry** for versioning and governance |
| Model download scripts (`huggingface_hub`, wget/curl for weights, Hub allowlists) | **Model Catalog** for governed model sourcing |
| LLM evaluation or benchmark code (lm-eval, Unitxt) | **LMEval** |
| RAG evaluation code (Ragas, TruLens, DeepEval faithfulness) | **RAGAS** |
| Content filtering or guardrail logic for LLMs (NeMo Guardrails, Presidio middleware) | **NeMo Guardrails** |
| Model monitoring code (Evidently, alibi-detect, AIF360/fairlearn drift/bias) | **TrustyAI** |
| Hyperparameter search / tabular AutoML (Optuna, Ray Tune, GridSearchCV, AutoGluon) | **AutoML** |
| HPA / Knative scale-to-zero around a loaded model InferenceService | **KServe** (Serverless / RawDeployment modes) |
| Duplicated feature transforms / Feast / Tecton / Hopsworks / cloud feature stores / DIY online feature cache | **Feature Store** for train–serve consistency |
| GPU resource requests, GPU Operators, MIG, manual GPU nodeSelector/tolerations | **Hardware Profiles & Accelerator Management** |
| MCP federation/gateway, MCP catalogs, HITL tool approval, prompt registries, A2A cards | Matching **MCP / agent** catalog component from detection-signals |
