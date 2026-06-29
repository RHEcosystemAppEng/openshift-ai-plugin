# Red Hat OpenShift AI Self-Managed 3.4 — Components Reference

Reference: [OpenShift AI Self-Managed 3.4 Documentation](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.4)

---

## Model Serving & Inference

### KServe (Single-Model Serving Platform)

A Kubernetes-native model serving platform that deploys each model from its own dedicated model server. KServe manages the full lifecycle of model deployments including storage access, networking, scaling, and authorization via `ServingRuntime` and `InferenceService` CRDs.

**When to use:** When you need to deploy and serve individual ML/LLM models in production with autoscaling, authentication, and monitoring. Supports both Knative (serverless) and RawDeployment modes.

**Requirements:**
- Install the cert-manager Operator.
- Access to S3-compatible object storage, a URI-based repository, an OCI-compliant registry, or a PVC for model artifacts.
- For GPU-accelerated serving: enable GPU support and install the relevant GPU operator (NVIDIA GPU Operator, AMD GPU Operator, or Intel Gaudi Base Operator) plus the Node Feature Discovery Operator.
- For Knative (serverless) mode: install OpenShift Serverless (Knative Serving) and OpenShift Service Mesh.

### vLLM Serving Runtimes

High-performance LLM inference engine available as multiple pre-configured `ServingRuntime` variants for KServe. Supports hardware-specific runtimes for NVIDIA GPU, AMD GPU (ROCm), Intel Gaudi, IBM Spyre, and CPU-only inference.

**When to use:** When serving large language models and you need optimized token generation throughput. Choose the runtime variant that matches your accelerator hardware (NVIDIA, AMD, Intel Gaudi, IBM Spyre, or CPU).

**Requirements:**
- KServe must be installed and the model-serving platform enabled.
- For the NVIDIA GPU runtime: enable GPU support, install the Node Feature Discovery Operator and the NVIDIA GPU Operator.
- For the AMD GPU runtime: install the AMD GPU Operator and configure a hardware profile.
- For the Intel Gaudi runtime: install the Intel Gaudi Base Operator.
- For CPU-only inference: no accelerator operators needed.

### Distributed Inference with llm-d

A Kubernetes-native framework (led by Red Hat with Google, NVIDIA, AMD, Hugging Face) for serving LLMs at scale across multiple nodes. Uses intelligent AI-aware network routing, disaggregated prefill/decode phases, and KV-cache-aware scheduling via the `LLMInferenceService` CRD.

**When to use:** When a single model server is not enough — you need to scale LLM inference horizontally across multiple nodes with production-grade SLOs, or when you need advanced scheduling strategies like prefix-cache-aware routing.

**Requirements:**
- OpenShift Container Platform 4.20 or later.
- Install the cert-manager Operator.
- Install the Red Hat Connectivity Link Operator.
- Install the Red Hat Leader Worker Set Operator.
- KServe must be installed and enabled.

### Models-as-a-Service (MaaS)

Provides governed access to externally hosted LLMs (e.g. cloud provider APIs) through a unified control plane. Administrators can set quotas, RBAC, and audit policies on top of third-party model endpoints.

**When to use:** When you want to give teams access to cloud-hosted LLMs (e.g. GPT, Claude) while maintaining centralized governance, usage limits, and audit trails — without hosting the models yourself.

**Requirements:**
- KServe must be installed and the model-serving platform enabled.
- Network access to the external model provider APIs.

### Caikit TGIS ServingRuntime

A model serving runtime that uses the Caikit framework with the Text Generation Inference Server (TGIS) backend. Provides gRPC and REST inference endpoints.

**When to use:** When deploying text-generation models that benefit from the Caikit model management framework, particularly for NLP workloads requiring streaming responses.

**Requirements:**
- KServe must be installed and the model-serving platform enabled.
- Access to S3-compatible object storage for model artifacts.

### OpenVINO Model Server (OVMS)

Intel's high-performance inference runtime optimized for Intel hardware. Supports a wide range of model formats and provides both REST and gRPC interfaces.

**When to use:** When serving predictive AI models (classification, object detection, NLP) on Intel CPUs/GPUs and you need high-throughput, low-latency inference with broad model format support.

**Requirements:**
- KServe must be installed and the model-serving platform enabled.
- Access to S3-compatible object storage for model artifacts.

### NVIDIA Triton Inference Server

NVIDIA's multi-framework inference server supporting TensorRT, ONNX, PyTorch, TensorFlow, and more. Provides dynamic batching, model ensembles, and concurrent model execution.

**When to use:** When you need to serve multiple model types (including ensembles) on NVIDIA GPUs with advanced features like dynamic batching and model pipelines.

**Requirements:**
- KServe must be installed and the model-serving platform enabled.
- NVIDIA GPU Operator and Node Feature Discovery Operator installed.
- For IBM Z or IBM Power variants: access to the IBM Cloud Container Registry or Triton Inference Server Quay repository.

### MLServer ServingRuntime

A model serving runtime for KServe that supports multiple ML frameworks (scikit-learn, XGBoost, LightGBM, MLflow) through a plugin architecture.

**When to use:** When deploying traditional ML models (classification, regression, etc.) built with frameworks like scikit-learn, XGBoost, or LightGBM in a Kubernetes-native way.

**Requirements:**
- KServe must be installed and the model-serving platform enabled.
- Access to S3-compatible object storage for model artifacts.

---

## Model Management

### Model Registry

A centralized service for storing, versioning, and promoting ML models with metadata. Supports OCI-compliant storage (ModelCar format), RBAC-based access control, and PostgreSQL-backed metadata. Models can be registered from S3-compatible storage or URIs and automatically converted to OCI images.

**When to use:** When teams need to share, version, and promote models across projects with traceability and governance. Essential for MLOps workflows where models move through dev/staging/production stages.

**Requirements:**
- Set `modelregistry` component to `Managed` in the `DataScienceCluster`.
- For production: access to an external PostgreSQL 16.x database or MySQL 5.x+ (MySQL 9.x recommended).
- Access to S3-compatible object storage for OCI-compliant model storage.

### Model Catalog

A curated, searchable catalog of validated third-party models that are ready for deployment. Administrators can govern which model sources are available to teams.

**When to use:** When data scientists need to discover, evaluate, and quickly deploy pre-validated models without manually sourcing and configuring them. Useful for rapid prototyping and standardizing on approved models.

**Requirements:**
- The `modelregistry` component must be enabled (`Managed`) in the `DataScienceCluster`.
- At least one model registry must be created in your deployment.

---

## Agentic AI & RAG

### Llama Stack (Operator)

A unified AI runtime managed by the Llama Stack Operator that integrates model inference, embedding generation, vector storage, and retrieval services into a single stack. Provides OpenAI-compatible APIs (Chat Completions, Responses API) for RAG and agentic workflows. Managed via the `LlamaStackDistribution` CRD.

**When to use:** When building retrieval-augmented generation (RAG) applications or agentic AI workflows and you want a turnkey stack that bundles inference + embeddings + vector DB + retrieval behind OpenAI-compatible endpoints.

**Requirements:**
- Install the Llama Stack Operator.
- Install the Red Hat OpenShift Service Mesh Operator 3.x.
- Install the cert-manager Operator.
- GPU-enabled nodes available on the cluster.
- Install the Node Feature Discovery Operator.
- Install the NVIDIA GPU Operator.
- Access to S3-compatible object storage for model artifacts.

### RAG Stack Deployment

An administrator-driven deployment pattern that provisions the full RAG infrastructure: LLM inference (vLLM), vector storage (PostgreSQL with pgvector), embedding service, and retrieval endpoints — all managed as a single unit.

**When to use:** When you need to deploy a complete RAG pipeline for a project team — including data ingestion, chunking, embedding, vector storage, and retrieval — without requiring each team to assemble the stack themselves.

**Requirements:**
- Llama Stack Operator and its prerequisites (see Llama Stack above).
- PostgreSQL with pgvector extension for vector storage.
- Access to S3-compatible object storage for data and model artifacts.
- GPU-enabled nodes for the LLM inference and embedding services.

### AutoRAG

An automated pipeline for building and optimizing RAG systems. Evaluates different retrieval strategies, chunking approaches, and embedding models to find the best configuration for your data and use case.

**When to use:** When you have a RAG use case but aren't sure which retrieval strategy, chunk size, or embedding model will perform best. AutoRAG automates the search for the optimal configuration.

**Requirements:**
- Llama Stack Operator and its prerequisites (see Llama Stack above).
- A deployed RAG stack (LLM inference, vector storage, embedding service).

---

## Development Environment

### Workbenches

Browser-based development environments (Jupyter, VS Code, RStudio) pre-configured with data science libraries, GPU access, and secure connections to cluster resources. Provisioned via CRDs or the dashboard with resource quotas and hardware profiles.

**When to use:** When data scientists and AI engineers need an interactive development environment with direct access to cluster GPUs, data sources, and model serving endpoints for prototyping, training, and experimentation.

**Requirements:**
- Set `workbenches` component to `Managed` in the `DataScienceCluster`.
- To use a custom workbench namespace, create the namespace before installing the OpenShift AI Operator.

### Custom Notebook Images

Administrator-published container images that extend the default workbench environments with additional libraries, tools, or configurations specific to your organization.

**When to use:** When the default IDE images lack specific libraries or tools your team requires, or when you need to standardize the development environment across teams.

**Requirements:**
- Workbenches component must be enabled.
- Custom images must be published to a container registry accessible from the cluster.
- If the cluster is running in FIPS mode, custom images must be based on UBI 9 or RHEL 9.

### Data Science Projects

Namespace-scoped organizational units that group workbenches, pipelines, model servers, data connections, and storage into a single manageable entity with RBAC.

**When to use:** When organizing work into isolated, governed projects where teams can collaborate on models, pipelines, and deployments while maintaining resource boundaries.

**Requirements:**
- OpenShift AI dashboard component must be enabled.

### S3-Compatible Object Storage Connections

First-class integration for connecting workbenches and pipelines to S3-compatible storage (AWS S3, MinIO, Ceph) for storing datasets, model artifacts, and pipeline outputs.

**When to use:** When your data or model artifacts live in S3-compatible storage and you need seamless access from notebooks, training jobs, and model serving runtimes.

**Requirements:**
- Access to an S3-compatible object storage service (AWS S3, MinIO, Ceph, etc.) with valid credentials.
- Workbenches or pipelines component must be enabled.

---

## Pipelines & Automation

### Data Science Pipelines (Kubeflow Pipelines)

KFP-based pipeline engine for defining, versioning, scheduling, and tracking multi-step ML workflows. Supports DAG-based task orchestration, artifact tracking in S3, parameterized runs, and scheduled recurring executions.

**When to use:** When you need to automate multi-step ML workflows (data prep, training, evaluation, deployment) with versioning, scheduling, and reproducibility. Essential for moving from notebooks to production ML.

**Requirements:**
- Set `aipipelines` component to `Managed` in the `DataScienceCluster`.
- Write access to an S3-compatible object storage bucket for pipeline artifacts.
- If the cluster is running in FIPS mode, custom container images must be based on UBI 9 or RHEL 9.
- To use your own Argo Workflows instance, set `argoWorkflowsControllers.managementState` to `Removed` in the `DataScienceCluster`.

### Kubeflow Spark Operator (KSO)

Enables running Apache Spark applications as Kubernetes-native workloads for distributed data processing. Integrates with OpenShift AI for large-scale ETL and feature engineering.

**When to use:** When your ML pipeline requires large-scale data processing, ETL, or feature engineering that exceeds single-node capacity and needs distributed compute via Spark.

**Requirements:**
- Install the Kubeflow Spark Operator from OperatorHub.
- Data Science Pipelines component should be enabled if integrating Spark into ML pipelines.

---

## Training & Fine-Tuning

### Distributed Workloads (KubeRay, Training Operator)

Infrastructure for distributing ML training and data processing jobs across multiple nodes with GPU-aware scheduling, auto-scaling, and monitoring. Supports frameworks like PyTorch, TensorFlow, and Ray.

**When to use:** When training large models or processing large datasets that exceed single-node GPU memory or compute capacity. Enables data-parallel and model-parallel training strategies.

**Requirements:**
- Install the Red Hat build of Kueue Operator.
- Install the cert-manager Operator.
- Set `kueue` to `Unmanaged` (to let the external Kueue Operator manage it), and set `ray` and/or `trainingoperator` to `Managed` in the `DataScienceCluster`.
- At least 1.6 vCPU and 2 GiB memory available for the distributed workloads infrastructure (in addition to base OpenShift AI requirements).
- For GPU workloads: enable GPU support and install the relevant GPU operator.

### Model Customization (Fine-Tuning)

Tools and workflows for customizing pre-trained models (LoRA, QLoRA, full fine-tuning) for domain-specific tasks. Integrates with the training operator and distributed workloads infrastructure.

**When to use:** When a pre-trained model needs to be adapted to your specific domain, vocabulary, or task — such as fine-tuning a general LLM on financial services terminology and workflows.

**Requirements:**
- Distributed Workloads components must be installed (Kueue, Ray and/or Training Operator).
- GPU-enabled nodes with sufficient VRAM for the model being fine-tuned.
- Access to S3-compatible object storage for datasets and model checkpoints.

### AutoML

Automated machine learning that searches for optimal model architectures, hyperparameters, and preprocessing steps for a given dataset and objective.

**When to use:** When you want to quickly find the best-performing model and hyperparameters for a structured data problem without manually tuning.

**Requirements:**
- Distributed Workloads components must be installed (Kueue, Ray and/or Training Operator).
- Workbenches component must be enabled.

---

## Evaluation & Safety

### LM Evaluation (LMEval)

A framework for systematically evaluating LLM performance. Configure `LMEvalJob` resources to run standardized benchmarks, compare model versions, and track metrics over time.

**When to use:** When you need to evaluate and compare LLM performance before deploying to production — measuring accuracy, reasoning ability, and task-specific metrics across model versions.

**Requirements:**
- Set `trustyai` component to `Managed` in the `DataScienceCluster`.
- A deployed LLM model in your project.
- For online evaluations or remote code execution: set `permitOnline` and `permitCodeExecution` to `allow` in the `DataScienceCluster`, and set `allowOnline`/`allowCodeExecution` to `true` in the `LMEvalJob` CR.
- For offline evaluations from S3: access to an S3-compatible storage bucket containing the model and datasets.

### Guardrails (NeMo Guardrails)

A safety framework that orchestrates detectors to filter and validate LLM inputs and outputs. Supports content filtering, sensitive data detection, topic control, and custom validation rules. Exposes guarded inference endpoints.

**When to use:** When LLM responses must comply with safety, regulatory, or content policies — such as preventing hallucinations, blocking sensitive data leakage, enforcing topic boundaries, or filtering toxic content.

**Requirements:**
- Set `trustyai` component to `Managed` in the `DataScienceCluster`.
- KServe configured to use RawDeployment mode (`spec.kserve.rawDeploymentServiceConfig` set to `Headed`).
- A deployed LLM model on the model-serving platform.
- No external NVIDIA subscription required — NeMo Guardrails is included with OpenShift AI.

### RAGAS Evaluation Provider

Metrics framework for evaluating RAG system quality. Measures retrieval quality, answer relevance, and factual consistency to identify issues in RAG pipeline configurations.

**When to use:** When you need quantitative assessment of your RAG pipeline's quality — checking whether retrieved documents are relevant, answers are grounded in context, and responses are factually consistent.

**Requirements:**
- Set `trustyai` component to `Managed` in the `DataScienceCluster`.
- A deployed RAG pipeline with accessible inference and retrieval endpoints.

---

## Monitoring & Observability

### Model Monitoring (TrustyAI)

Monitoring service that tracks model bias, data drift, and performance degradation over time. Provides configurable metrics, thresholds, and dashboard visualizations.

**When to use:** When models are in production and you need to detect performance degradation, data drift, or fairness issues before they impact business outcomes. Critical for regulated industries.

**Requirements:**
- Set `trustyai` component to `Managed` in the `DataScienceCluster`.
- A TrustyAI service instance must be installed in each project containing models to monitor.
- Model serving platform must be enabled.
- Optional: for database-backed storage instead of PVC, configure a MySQL or MariaDB 10.5+ database secret before deploying TrustyAI.
- For KServe RawDeployment mode: update the `inferenceservice-config` ConfigMap and create a CA certificate ConfigMap in the model's namespace.

### Gen AI Playground

An interactive browser-based environment for experimenting with deployed models. Supports prompt engineering, parameter tuning, and side-by-side model comparison.

**When to use:** When you want to quickly test and compare deployed models with different prompts and parameters before integrating them into applications — useful for prompt engineering and model selection.

**Requirements:**
- OpenShift AI dashboard component must be enabled.
- At least one model deployed on the model-serving platform.

---

## Experiment Tracking

### MLflow Integration

Integration with MLflow for experiment tracking, model logging, metric recording, and artifact management. Provides a centralized view of training runs across teams.

**When to use:** When you need to track experiments, compare training runs, log model artifacts, and manage the ML experiment lifecycle across multiple data scientists.

**Requirements:**
- Workbenches component must be enabled.
- Access to S3-compatible object storage for artifact storage (optional but recommended).

---

## Feature Management

### Feature Store

A centralized service for defining, storing, and serving reusable machine learning features. Ensures consistent feature computation between training and serving (avoiding training-serving skew). Integrated with workbenches.

**When to use:** When multiple models or teams share computed features and you need to ensure consistency between training-time and serving-time feature values, or when you want to avoid redundant feature engineering.

**Requirements:**
- Set `feastoperator` component to `Managed` in the `DataScienceCluster`.
- Workbenches component must be enabled.

---

## Platform & Infrastructure

### Hardware Profiles & Accelerator Management

Administrator-configured hardware profiles that define GPU/accelerator resource allocations. Supports NVIDIA, AMD, Intel Gaudi, and IBM Spyre accelerators with the Node Feature Discovery Operator.

**When to use:** When you need to manage and allocate GPU/accelerator resources across teams and projects, ensuring workloads run on the correct hardware with appropriate resource limits.

**Requirements:**
- Install the Node Feature Discovery Operator.
- Install the GPU operator for your hardware: NVIDIA GPU Operator, AMD GPU Operator, Intel Gaudi Base Operator, or IBM Spyre Operator.

### OpenShift Serverless (Knative Serving)

Serverless autoscaling for model serving and agent workloads. Scales pods to zero when idle and automatically spins up when requests arrive, reducing compute costs.

**When to use:** When workloads are bursty or infrequent and you want to minimize compute costs by scaling to zero during idle periods — ideal for agents or models that aren't called continuously.

**Requirements:**
- Install the OpenShift Serverless Operator from OperatorHub.
- OpenShift Service Mesh must be installed if using KServe with Knative mode.

### OpenShift Service Mesh (Istio)

Service mesh layer providing mTLS, traffic management, observability, and authorization policies for inter-service communication. Required by KServe when using Knative-based serving.

**When to use:** When you need encrypted service-to-service communication, fine-grained traffic routing (canary deployments, A/B testing), or when deploying KServe with Knative mode.

**Requirements:**
- Install the Red Hat OpenShift Service Mesh Operator from OperatorHub.

### Usage Telemetry

Configurable telemetry collection for tracking platform usage, resource consumption, and adoption metrics. Administrators can enable, disable, or customize what data is collected.

**When to use:** When administrators need visibility into platform adoption and resource utilization, or when compliance requirements dictate controlling what telemetry data leaves the cluster.

**Requirements:**
- No additional operators required — configured via the OpenShift AI Operator settings.

### Stable API Tiers

Each OpenShift AI API endpoint is mapped to a support tier (stable, beta, alpha) that defines stability guarantees, deprecation timelines, and migration paths.

**When to use:** When building integrations or automation against OpenShift AI APIs and you need to understand which endpoints are stable for production use versus experimental.

**Requirements:**
- No additional requirements — API tier metadata is available in the OpenShift AI documentation.
