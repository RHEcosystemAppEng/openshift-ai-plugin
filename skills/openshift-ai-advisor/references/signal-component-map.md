# Signal-to-Component Map

Use this table to match **capability** findings to OpenShift AI components. Read top-to-bottom; pick the first row that matches.

Whether a finding is already on OpenShift AI / OpenShift is signed by the project-scanner (`generic` | `openshift-ai` | `openshift`) from the **RHOAI:** tags in [detection-signals.md](detection-signals.md)—not by this table.

| What was found | Suggested component |
|---|---|
| PyTorch / TensorFlow / ONNX model files or inference scripts | **KServe** for production serving |
| Custom Flask/FastAPI endpoint serving a model (`model.predict()` behind `/predict`) | **KServe** to replace hand-built serving code |
| HPA / Knative scale-to-zero around a loaded model InferenceService | **KServe** (Serverless / RawDeployment modes) |
| LLM weights or generative LLM inference (vLLM, TGI, SGLang, Ollama, DIY CausalLM) | **vLLM Serving Runtimes** (often with **KServe**) |
| Disaggregated / multi-node LLM inference, sticky/prefix-hash LB, llm-d / Dynamo P/D | **llm-d** for distributed inference |
| External LLM API calls (OpenAI, Anthropic, Azure, Bedrock) or LiteLLM/Portkey gateways | **Models-as-a-Service (MaaS)** for governed access |
| Scattered API keys for LLM providers across services or `.env` files | **MaaS** for centralized key management |
| Caikit framework or gRPC/streaming text-generation | **Caikit TGIS** runtime |
| Intel hardware targets, OpenVINO IR format files | **OVMS** runtime |
| NVIDIA Triton / TensorRT models, model ensembles, multi-model pipelines | **Triton** runtime |
| scikit-learn / XGBoost / LightGBM serve (MLServer or DIY joblib `/predict`) | **MLServer** runtime |
| LLM quantization / compression (LLM Compressor, AWQ, GPTQ, FP8, BitsAndBytes PTQ) | **Red Hat AI Model Optimization Toolkit (LLM Compressor)** |
| Inference-time tool / function calling (`--tool-call-parser`, `tool_calls`, chat tool templates) | **AI Inference Tool Calling** |
| Speculative decoding (Eagle3, `--speculative-config`, draft/verifier models) | **Speculative Decoding (Speculators)** |
| OCI ModelCar / `oci://` model images, oras/skopeo model packaging for serving | **OCI ModelCar Inference Serving** |
| InferencePool / Endpoint Picker / KV- or queue-aware LLM gateway routing | **Gateway API Inference Extensions** |
| Ad-hoc model versioning (file naming, metadata JSONs, git-lfs, MLflow register/alias) | **Model Registry** for versioning and governance |
| Model download scripts (`huggingface_hub`, wget/curl for weights, Hub allowlists) | **Model Catalog** for governed model sourcing |
| Agentic AI patterns (LangGraph, CrewAI, AutoGen, multi-step tool loops) | **Llama Stack** for unified runtime |
| RAG pipeline code (chunking, embeddings, vector queries) | **AutoRAG** to optimize, or **RAG Stack** for managed deployment |
| Docker Compose / Helm for vector DBs + custom retrieval API | **RAG Stack** to replace self-managed infrastructure |
| Custom embedding + retrieval logic in backend | **RAG Stack** for managed infrastructure |
| Chunk-size / embedding / top_k sweeps or RAG hyperparameter search | **AutoRAG** for automated optimization |
| MCP federation / multi-server gateway (`MCPServerRegistration`, mcp-proxy fleets) | **MCP Gateway** |
| A2A Agent Cards / `/.well-known/agents` discovery / hard-coded peer agent URLs | **A2A Agent Registry** |
| Isolated agent code-exec sandboxes (Sandbox CR, E2B/Modal/Daytona, per-session pods) | **Red Hat build of Agent Sandbox** |
| MCP OAuth / Protected Resource Metadata / DIY MCP token minting or long-lived API keys | **MCP Authorization Server** |
| MCP server catalogs / `mcp.json` fleets / DIY MCP Deployments without governed catalog | **MCP Catalog** |
| MCP tool/prompt ACL (CEL/OPA on tool names, per-server allowlists, TBAC) | **MCP Gateway Authorization** |
| Shared / versioned prompt templates (`SYSTEM_PROMPT`, `*.prompty`, PromptLayer, git prompts/) | **Prompt Template Registry** |
| Agent workload enrollment / SPIFFE/AuthBridge / `AgentRuntime` / AgentCard labels | **Kagenti Operator** |
| Human-in-the-loop tool approval (LangGraph interrupt, `needs_approval`, MCP destructive hints) | **HITL Tool Approval** |
| Versioned MCP tool *definitions* / scrapers of `tools/list` into static catalogs | **MCP Tool Registry** |
| Cluster ops via MCP (`kubernetes-mcp-server`, DIY `oc`/`kubectl` MCP wrappers) | **MCP server for OpenShift Container Platform** |
| Query-time MCP tool retrieval / semantic tool filtering over large catalogs | **Query-based Tool Filtering** |
| Camel/Java document conversion for RAG (camel-docling, PDFBox/Tika in Camel routes) | **Camel Docling** |
| Jupyter notebooks / JupyterHub / notebook Deployments | **Workbenches** for managed environments |
| Custom Dockerfile for notebook/dev environment (`jupyter/*-notebook` or BYON) | **Custom Notebook Images** |
| Multi-step data/train/eval/deploy scripts | **Data Science Pipelines (KFP)** |
| Airflow DAGs, Prefect flows, Luigi pipelines, Makefile-chained ML steps | **Data Science Pipelines (KFP)** to replace custom orchestration |
| Apache Spark / PySpark / SparkApplication on Kubernetes | **Spark Operator (KSO)** |
| Distributed training code (DDP, DeepSpeed, Ray Train, PyTorchJob) | **Distributed Workloads** |
| Fine-tuning scripts (LoRA, QLoRA, PEFT, SFTTrainer, Unsloth/Axolotl) | **Model Customization** |
| Hyperparameter search / tabular AutoML (Optuna, Ray Tune, GridSearchCV, AutoGluon) | **AutoML** |
| LLM evaluation or benchmark code (lm-eval, Unitxt) | **LMEval** |
| Content filtering or guardrail logic for LLMs (NeMo Guardrails, Presidio middleware) | **NeMo Guardrails** |
| RAG evaluation code (Ragas, TruLens, DeepEval faithfulness) | **RAGAS** |
| Multi-provider LLM eval hub glue (lm-eval + Garak + GuideLLM / EvalHub SDK) | **EvalHub** |
| Adversarial safety / red-team assessment (garak, PyRIT, Promptfoo redteam, HarmBench) | **Automated Risk Assessment** |
| Model monitoring code (Evidently, alibi-detect, AIF360/fairlearn drift/bias) | **TrustyAI** |
| Interactive model playground UIs (Open WebUI, Gradio ChatInterface, Streamlit chat) | **Gen AI Playground** |
| MLflow / W&B / TensorBoard / CSV experiment logging | **MLflow Integration** to consolidate tracking |
| Duplicated feature transforms / Feast / Tecton / Hopsworks / cloud feature stores / DIY online feature cache | **Feature Store** for train–serve consistency |
| Gateway API AuthPolicy / RateLimitPolicy / TLSPolicy DIY, or Kong/nginx north-south auth rate-limit | **Red Hat Connectivity Link (RHCL)** |
| GPU resource requests, GPU Operators, MIG, manual GPU nodeSelector/tolerations | **Hardware Profiles & Accelerator Management** |
