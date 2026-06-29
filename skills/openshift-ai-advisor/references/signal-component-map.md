# Signal-to-Component Map

Use this table to match project findings to OpenShift AI components. Read top-to-bottom; pick the first row that matches.

| What was found | Suggested component |
|---|---|
| PyTorch / TensorFlow / ONNX model files or inference scripts | **KServe** for production serving |
| Custom Flask/FastAPI endpoint serving a model (`model.predict()` behind `/predict`) | **KServe** to replace hand-built serving code |
| LLM weights or LLM inference code | **KServe + vLLM** runtime |
| LLM inference at scale, multi-node GPU references | **llm-d** for distributed inference |
| Custom load balancer / reverse proxy routing to multiple model replicas | **llm-d** for AI-aware routing |
| External LLM API calls (OpenAI, Anthropic, Azure) | **Models-as-a-Service (MaaS)** for governed access |
| Scattered API keys for LLM providers across services or `.env` files | **MaaS** for centralized key management |
| Caikit framework or gRPC/streaming text-generation | **Caikit TGIS** runtime |
| Intel hardware targets, OpenVINO IR format files | **OVMS** runtime |
| NVIDIA TensorRT models, model ensembles, multi-model pipelines | **Triton** runtime |
| scikit-learn / XGBoost / LightGBM model files | **MLServer** runtime |
| RAG pipeline code (chunking, embeddings, vector queries) | **AutoRAG** to optimize, or **RAG Stack** for managed deployment |
| Docker Compose services for vector DBs + custom retrieval API | **RAG Stack** to replace self-managed infrastructure |
| Chunk-size experiments or embedding model comparison scripts | **AutoRAG** for automated optimization |
| Agentic AI patterns (tool-calling, multi-step agents) | **Llama Stack** for unified runtime |
| Custom embedding + retrieval logic in backend | **RAG Stack** for managed infrastructure |
| Distributed training code (DDP, DeepSpeed, Ray Train) | **Distributed Workloads** |
| Fine-tuning scripts (LoRA, QLoRA, PEFT, SFTTrainer) | **Model Customization** |
| Multi-step data/train/eval/deploy scripts | **Data Science Pipelines (KFP)** |
| Airflow DAGs, Prefect flows, Luigi pipelines, Makefile-chained ML steps | **Data Science Pipelines (KFP)** to replace custom orchestration |
| Apache Spark / PySpark code | **Spark Operator (KSO)** |
| Jupyter notebooks in the repo | **Workbenches** for managed environments |
| Custom Dockerfile for notebook/dev environment | **Custom Notebook Images** |
| MLflow usage | **MLflow Integration** (managed) |
| Custom experiment logging (CSV/JSON metrics, TensorBoard, W&B) | **MLflow Integration** to consolidate tracking |
| Ad-hoc model versioning (file naming, metadata JSONs, git-lfs) | **Model Registry** for versioning and governance |
| Model download scripts (`huggingface_hub`, wget/curl for weights) | **Model Catalog** for governed model sourcing |
| LLM evaluation or benchmark code | **LMEval** |
| RAG evaluation code (retrieval quality, answer relevance) | **RAGAS** |
| Content filtering or guardrail logic for LLMs | **NeMo Guardrails** |
| Custom PII detection, topic filtering, or output validators | **NeMo Guardrails** to replace hand-built safety logic |
| Model monitoring code (drift, fairness, bias) | **TrustyAI** |
| Custom Prometheus metrics for model predictions or alerting rules | **TrustyAI** for unified monitoring |
| Hyperparameter search code (Optuna, Ray Tune, GridSearchCV) | **AutoML** |
| HPA configs for inference, scale-to-zero annotations, idle timeouts | **OpenShift Serverless (Knative)** |
| Duplicated feature transforms in training and serving code | **Feature Store** for consistency |
| S3/MinIO/boto3 usage for data or artifacts | **S3-Compatible Object Storage Connections** |
