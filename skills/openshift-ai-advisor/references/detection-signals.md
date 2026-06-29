# Detection Signals

What to search for when scanning a project. Each category lists concrete file patterns, imports, and infrastructure markers. The component in bold is the likely OpenShift AI replacement.

## Model artifacts

`.pt`, `.pth`, `.onnx`, `.pb`, `.h5`, `.safetensors`, `.pkl`, `.joblib`, `.bst` files.

## Custom model serving endpoints

Flask/FastAPI/Django routes that load a model and return predictions (`model.predict()` behind `/predict`), custom health checks, manual batching logic. Replacement: **KServe**.

## LLM inference code

transformers, `AutoModelForCausalLM`, vllm imports, text-generation scripts, custom tokenizer management, manual GPU memory allocation (`torch.cuda` device management). Replacement: **KServe + vLLM**.

## LLM scaling patterns

Custom load balancers or reverse proxies in front of multiple model replicas, manual model sharding across GPUs/nodes, KV-cache management code. Replacement: **llm-d**.

## External LLM API calls

OpenAI SDK (`openai.ChatCompletion`), Anthropic SDK, Azure OpenAI, LiteLLM, Google GenAI. Also: scattered API key management (keys in env vars, `.env` files, secrets across services), custom retry/fallback logic, per-team rate limiting code. Replacement: **MaaS**.

## RAG patterns

Document loaders, chunking logic, embedding generation, vector store queries (LangChain, LlamaIndex, ChromaDB, pgvector, FAISS, Milvus, Qdrant, Weaviate, Pinecone). Replacement: **RAG Stack** or **AutoRAG**.

## Custom RAG infrastructure

Docker Compose / podman-compose services for vector DBs (pgvector, Milvus, Qdrant, Weaviate), custom embedding endpoints, hand-built retrieval APIs, manual index management code. Replacement: **RAG Stack**.

## RAG tuning patterns

Chunk-size experiments, embedding model comparison scripts, retrieval strategy A/B tests. Replacement: **AutoRAG**.

## Agentic AI patterns

Tool-calling, multi-step agents (LangGraph, CrewAI, AutoGen), custom agent loop implementations, manual context window management, custom tool orchestration code. Replacement: **Llama Stack**.

## Training and fine-tuning

PyTorch DDP, DeepSpeed, Horovod, Ray Train, `torch.distributed`, multi-GPU training scripts, gradient accumulation loops. Replacement: **Distributed Workloads**.

## Fine-tuning specifics

LoRA/QLoRA/PEFT scripts, `SFTTrainer`, custom training loops with adapter layers, dataset preparation for instruction tuning, RLHF reward model training. Replacement: **Model Customization**.

## Hyperparameter search

Optuna, Ray Tune, `sklearn.model_selection.GridSearchCV`, `RandomizedSearchCV`, manual sweep loops, Bayesian optimization code. Replacement: **AutoML**.

## Pipelines and workflow orchestration

Multi-step data-prep/train/evaluate/deploy scripts, Airflow DAGs, Prefect flows, Luigi pipelines, Makefile targets chaining ML steps, shell scripts orchestrating train/evaluate/deploy, cron jobs for retraining. Replacement: **Data Science Pipelines (KFP)**.

## Spark workloads

PySpark, Apache Spark jobs. Replacement: **Spark Operator (KSO)**.

## Notebooks

`.ipynb` files, custom notebook Dockerfiles, `jupyter_notebook_config.py`, JupyterHub/JupyterLab setup configs. Replacement: **Workbenches** / **Custom Notebook Images**.

## Experiment tracking

MLflow usage (`mlflow.log_*`, tracking URIs), custom logging (metrics to CSV/JSON, manual run comparison scripts), TensorBoard logs (`SummaryWriter`, `tf.summary`), Weights & Biases (`wandb.log`, `wandb.init`). Replacement: **MLflow Integration**.

## Model versioning and metadata

Ad-hoc version tracking (file naming: `model_v1.pt`), manual metadata files (JSON/YAML tracking versions, hyperparams, metrics), models in git or git-lfs. Replacement: **Model Registry**.

## Model sourcing

`huggingface_hub.snapshot_download`, `wget`/`curl` for model downloads, model card YAML files, hardcoded model URLs, scripts pulling from external registries. Replacement: **Model Catalog**.

## Evaluation code

lm-eval-harness, custom benchmark scripts, perplexity/accuracy computation code, model comparison notebooks. Replacement: **LMEval**.

## RAG evaluation code

Retrieval quality metrics, answer relevance scoring, faithfulness/groundedness checks, custom RAG quality benchmarks. Replacement: **RAGAS**.

## Safety and guardrail logic

Content filtering, input/output validation for LLMs, PII detection code, topic filtering, profanity filters, custom output validators, regex-based content blockers. Replacement: **NeMo Guardrails**.

## Monitoring

Drift detection, fairness metrics, bias checks, custom Prometheus metrics for model predictions, alerting rules for performance degradation, custom dashboards. Replacement: **TrustyAI**.

## Deployment and scaling patterns

Dockerfiles, Kubernetes manifests, Helm charts, GPU resource requests (`nvidia.com/gpu`, `amd.com/gpu`), HPA configs for inference, scale-to-zero annotations, idle timeouts, custom autoscalers. Replacement: **OpenShift Serverless (Knative)**.

## Service networking

Manual mTLS setup, custom auth middleware, manual traffic splitting (canary/A/B), custom service-to-service auth tokens. Replacement: **Service Mesh (Istio)**.

## Object storage

S3/MinIO connection strings, boto3 usage, `s3fs`, `smart_open` with S3 URIs, MinIO client SDK. Replacement: **S3-Compatible Object Storage Connections**.

## Feature engineering

Shared feature computation between training and serving, duplicated pandas/numpy transforms across scripts and serving code, feature definitions in multiple places. Replacement: **Feature Store**.

## Multi-project structure

Multiple ML sub-projects in the repo, shared resources without namespace isolation, team-specific directories with separate configs. Replacement: **Data Science Projects**.

## Governance and compliance signals

References to EU AI Act, SOC2, HIPAA, or fairness requirements in docs/READMEs/configs. Manual model promotion processes (scripts, Makefiles, or human-driven deploy gates). Model cards or documentation templates for audit purposes. Approval workflows or sign-off steps before deployment. Replacement: **Model Registry** + **TrustyAI** + **Data Science Pipelines**.

## Retraining patterns

Cron jobs or scheduled scripts that retrain models. Drift-triggered retraining logic. Scripts that compare new model performance to a baseline before promoting. Replacement: **Data Science Pipelines (KFP)** + **TrustyAI**.
