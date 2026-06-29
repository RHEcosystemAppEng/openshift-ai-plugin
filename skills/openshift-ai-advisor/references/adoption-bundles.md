# Adoption Bundles

A bundle is a group of components that solve one problem together. Suggest a bundle when step 2 findings show 2+ of its prerequisites already exist in the project. Zero prerequisites means greenfield; skip it.

---

## RAG bundle

Replace hand-built chunking/embedding/retrieval code with a managed stack, then tune it automatically.

**Components:** RAG Stack, AutoRAG, RAGAS, NeMo Guardrails (optional)

**Prerequisites (2+ to suggest):**
- Chunking + embedding + vector query code (LangChain, LlamaIndex, custom)
- Vector DB running via Docker Compose or podman (pgvector, Milvus, Qdrant, Weaviate)
- Document loaders or ingestion scripts
- LLM calls feeding retrieved context into prompts
- Any retrieval quality scoring code

**What you stop maintaining:** Your Docker Compose vector DB, custom embedding endpoints, chunking parameter experiments, and retrieval pipeline glue code. RAG Stack deploys the infra as a unit. AutoRAG runs the chunk-size/embedding-model sweep you were doing manually. RAGAS gives you retrieval and answer quality scores without writing custom eval scripts.

---

## LLM serving bundle

Stop running inference behind a Flask endpoint or paying for external APIs without quotas.

**Components:** KServe + vLLM, LMEval, NeMo Guardrails, llm-d (at scale), MaaS (for external APIs)

**Prerequisites (2+ to suggest):**
- Model weights on disk or a download script for them
- A custom `/predict` or `/generate` endpoint wrapping a model
- OpenAI/Anthropic/Azure SDK calls scattered across services
- Eval scripts (lm-eval-harness, custom benchmarks)
- Input/output filtering code (PII, toxicity, topic)

**What you stop maintaining:** Your custom serving code (health checks, batching, GPU memory management). vLLM handles token generation with continuous batching. KServe gives you autoscaling, auth, and canary rollouts via `InferenceService` CRD. LMEval runs benchmarks before you promote a model. NeMo Guardrails replaces your regex-based content filters. If you're calling external APIs, MaaS centralizes the keys and adds rate limiting so teams stop managing `.env` files with API keys.

---

## MLOps bundle

Replace your shell scripts that chain train/eval/deploy with actual pipelines and a model registry.

**Components:** Data Science Pipelines (KFP), MLflow Integration, Model Registry, TrustyAI, Model Catalog (optional)

**Prerequisites (2+ to suggest):**
- Multi-step scripts or Makefiles chaining train → evaluate → deploy
- MLflow, TensorBoard, W&B, or CSV-based experiment logging
- Model files versioned by filename (`model_v1.pt`, `model_v2.pt`) or git-lfs
- Drift detection or custom Prometheus metrics for model perf
- `huggingface_hub.snapshot_download` or wget/curl for model weights

**What you stop maintaining:** The Makefile or Airflow DAG that chains your steps. KFP pipelines are versioned, repeatable, and track artifacts in S3 automatically. MLflow replaces your CSV metrics files. Model Registry replaces your `model_v2_final_FINAL.pt` naming scheme with proper versions and stage promotion. TrustyAI replaces your custom Prometheus metrics with built-in drift and bias detection.

---

## Training bundle

Distribute training across multiple GPUs/nodes without writing your own scheduling code.

**Components:** Distributed Workloads, Model Customization, MLflow Integration, Model Registry

**Prerequisites (2+ to suggest):**
- `torch.distributed`, DDP, DeepSpeed, or Ray Train usage
- LoRA/QLoRA/PEFT fine-tuning scripts
- Multi-GPU training scripts with manual `CUDA_VISIBLE_DEVICES` management
- Any experiment tracking
- Optuna or Ray Tune hyperparameter sweeps

**What you stop maintaining:** Your `torchrun` launch scripts and GPU node scheduling. The Training Operator handles multi-node jobs via `PyTorchJob` CRD with Kueue for fair scheduling. Model Customization wraps LoRA/QLoRA workflows. MLflow logs each run. Model Registry stores the output weights with metadata linking back to the training config.

---

## Data science bundle

Replace your custom notebook Dockerfiles and shared-storage hacks with managed workbenches.

**Components:** Workbenches, Data Science Projects, S3-Compatible Object Storage Connections, MLflow Integration, Data Science Pipelines (optional)

**Prerequisites (2+ to suggest):**
- `.ipynb` files in the repo
- Custom Dockerfile for Jupyter/JupyterHub
- `boto3` or `s3fs` code connecting to object storage
- Multiple team directories or sub-projects in one repo
- Experiment tracking code

**What you stop maintaining:** Your Jupyter Dockerfile and the JupyterHub helm chart. Workbenches gives each user a pre-built IDE (Jupyter, VS Code, RStudio) with GPU access and S3 connections already wired. Data Science Projects gives namespace isolation per team. You stop SSHing into shared machines to run notebooks.

---

## Agentic AI bundle

Run your agents on managed inference instead of raw OpenAI API calls.

**Components:** Llama Stack, KServe + vLLM, NeMo Guardrails, RAG Stack (optional)

**Prerequisites (2+ to suggest):**
- LangGraph, CrewAI, AutoGen, or custom agent loop code
- OpenAI/Anthropic SDK calls that agents use for reasoning
- Retrieval logic feeding context to agents
- Planner-executor or supervisor-worker patterns in code
- Manual token counting or context window trimming

**What you stop maintaining:** Your scattered API keys and per-agent rate limiting. Llama Stack exposes OpenAI-compatible endpoints (`/chat/completions`, `/responses`) backed by your own vLLM instance. Your agent code keeps its LangGraph/CrewAI structure but points at the local endpoint instead of `api.openai.com`. NeMo Guardrails validates agent outputs before they reach users. If your agents do retrieval, RAG Stack replaces the vector DB you're running in Docker.

---

## Governance & compliance bundle

Add versioning, audit trails, and bias monitoring so you can pass a compliance review.

**Components:** Model Registry, Model Catalog, TrustyAI, MLflow Integration, Data Science Pipelines (KFP)

**Prerequisites (2+ to suggest):**
- Model files with no real versioning (filename-based, git-lfs, or just overwritten)
- Compliance requirements mentioned anywhere (EU AI Act, SOC2, HIPAA)
- Drift or bias checking code (even rudimentary)
- Manual deploy process (someone runs a script or clicks a button to promote)
- Experiment logs that don't link to what's actually deployed

**What you stop maintaining:** Your ad-hoc model naming and manual promotion scripts. Model Registry gives you versioned artifacts with stage gates (dev → staging → prod) and approval workflows. TrustyAI runs bias and drift checks on every prediction without custom Prometheus exporters. MLflow links each deployed model back to its training run, dataset, and hyperparameters. Pipelines enforce that no model reaches prod without passing eval gates. This is what auditors actually want to see.

---

## Model factory bundle

Automate the retrain/eval/promote cycle so it runs without you.

**Components:** Data Science Pipelines (KFP), Distributed Workloads, LMEval, Model Registry, MLflow Integration, TrustyAI

**Prerequisites (2+ to suggest):**
- Cron jobs or scripts that retrain models periodically
- Eval code that compares new model to a baseline
- Model versioning (even file-naming counts)
- Alerting on model accuracy or latency degradation
- Train → evaluate → deploy steps chained in any form (Makefile, shell, Airflow)

**What you stop maintaining:** Your cron-based retraining and the script that compares metrics before promoting. A KFP pipeline runs on schedule (or on a TrustyAI drift alert), trains with Distributed Workloads, evaluates with LMEval, and if scores pass a threshold, promotes the new version in Model Registry. TrustyAI monitors the deployed model and triggers the next cycle when performance drops. You stop babysitting retraining runs.

---

## Platform engineering bundle

Set up the cluster so data scientists self-serve instead of filing tickets for GPUs and environments.

**Components:** Workbenches, Data Science Projects, Custom Notebook Images, Hardware Profiles, OpenShift Serverless (Knative), Service Mesh (Istio), S3-Compatible Object Storage Connections

**Prerequisites (2+ to suggest):**
- Multiple teams sharing GPU nodes (contention, manual scheduling)
- Per-team namespaces or directory structures with separate configs
- Custom Dockerfiles for dev/notebook environments teams maintain themselves
- `nvidia.com/gpu` resource requests or GPU operator configs in manifests
- HPA or scale-to-zero configs for inference pods
- Manual mTLS setup or auth middleware between services

**What you stop maintaining:** The custom GPU scheduling logic and the tickets queue for "I need a notebook with PyTorch 2.x and 2 A100s." Hardware Profiles define GPU allocations declaratively. Data Science Projects give each team a namespace with quotas. Custom Notebook Images let you publish one blessed image instead of each team maintaining their own Dockerfile. Serverless handles scale-to-zero for inference services. Service Mesh replaces your manual mTLS and traffic-splitting configs.
