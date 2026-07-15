# Red Hat OpenShift AI Self-Managed 3.5 — Components Reference

Reference: [OpenShift AI Self-Managed 3.5 Documentation](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5)

---

## Model Serving & Inference

### KServe (Single-Model Serving Platform)
**Details:** [Model serving platform](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/configuring_your_model-serving_platform/configuring-your-model-serving-platform_rhoai-admin#model_serving_platform)
**How to use:** [Deploying models on the model serving platform](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/deploying_models/deploying_models#deploying-models-on-the-model-serving-platform_rhoai-user)

A Kubernetes-native model serving platform that deploys each model from its own dedicated model server. KServe manages the full lifecycle of model deployments including storage access, networking, scaling, and authorization via `ServingRuntime` and `InferenceService` CRDs.

**When to use:** When you need to deploy and serve individual ML/LLM models in production with autoscaling, authentication, and monitoring. Supports both Knative (serverless) and RawDeployment modes.

**Requirements:**
- Install the cert-manager Operator.
- Access to S3-compatible object storage, a URI-based repository, an OCI-compliant registry, or a PVC for model artifacts.
- For GPU-accelerated serving: enable GPU support and install the relevant GPU operator (NVIDIA GPU Operator, AMD GPU Operator, or Intel Gaudi Base Operator) plus the Node Feature Discovery Operator.
- For Knative (serverless) mode: install OpenShift Serverless (Knative Serving) and OpenShift Service Mesh.

### vLLM Serving Runtimes
**Details:** [vLLM NVIDIA GPU ServingRuntime for KServe](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/deploying_models/making_inference_requests_to_deployed_models#vllm_nvidia_gpu_servingruntime_for_kserve)
**How to use:** [Customizing the vLLM model-serving runtime](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/configuring_your_model-serving_platform/customizing_model_deployments#Customizing-the-vllm-runtime_rhoai-admin)

High-performance LLM inference engine available as multiple pre-configured `ServingRuntime` variants for KServe. Supports hardware-specific runtimes for NVIDIA GPU, AMD GPU (ROCm), Intel Gaudi, IBM Spyre, and CPU-only inference.

**When to use:** When serving large language models and you need optimized token generation throughput. Choose the runtime variant that matches your accelerator hardware (NVIDIA, AMD, Intel Gaudi, IBM Spyre, or CPU).

**Requirements:**
- KServe must be installed and the model-serving platform enabled.
- For the NVIDIA GPU runtime: enable GPU support, install the Node Feature Discovery Operator and the NVIDIA GPU Operator.
- For the AMD GPU runtime: install the AMD GPU Operator and configure a hardware profile.
- For the Intel Gaudi runtime: install the Intel Gaudi Base Operator.
- For CPU-only inference: no accelerator operators needed.

### Distributed Inference with llm-d
**Details:** [Deploying models by using Distributed Inference with llm-d](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/deploy_models_using_distributed_inference_with_llm-d/deploying-models-using-distributed-inference_distributed-inference)
**How to use:** [Enabling Distributed Inference with llm-d](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/deploy_models_using_distributed_inference_with_llm-d/deploying-models-using-distributed-inference_distributed-inference#enabling-distributed-inference_distributed-inference)

A Kubernetes-native framework (led by Red Hat with Google, NVIDIA, AMD, Hugging Face) for serving LLMs at scale across multiple nodes. Uses intelligent AI-aware network routing, disaggregated prefill/decode phases, and KV-cache-aware scheduling via the `LLMInferenceService` CRD.

**When to use:** When a single model server is not enough — you need to scale LLM inference horizontally across multiple nodes with production-grade SLOs, or when you need advanced scheduling strategies like prefix-cache-aware routing.

**Requirements:**
- OpenShift Container Platform 4.20 or later.
- Install the cert-manager Operator.
- Install the Red Hat Connectivity Link Operator.
- Install the Red Hat Leader Worker Set Operator.
- KServe must be installed and enabled.

### Models-as-a-Service (MaaS)
**Details:** [Models-as-a-Service overview](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/govern_llm_access_with_models-as-a-service/deploy-and-manage-models-as-a-service_maas#maas-overview_maas-deploy)
**How to use:** [Access models through Models-as-a-Service](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/govern_llm_access_with_models-as-a-service/use-models-as-a-service_maas-deploy#access-models-with-maas_maas-user)

Provides governed access to externally hosted LLMs (e.g. cloud provider APIs) through a unified control plane. Administrators can set quotas, RBAC, and audit policies on top of third-party model endpoints.

**When to use:** When you want to give teams access to cloud-hosted LLMs (e.g. GPT, Claude) while maintaining centralized governance, usage limits, and audit trails — without hosting the models yourself.

**Requirements:**
- KServe must be installed and the model-serving platform enabled.
- Network access to the external model provider APIs.

### Caikit TGIS ServingRuntime
**Details:** [Caikit TGIS ServingRuntime for KServe](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/deploying_models/making_inference_requests_to_deployed_models#caikit_tgis_servingruntime_for_kserve)
**How to use:** [Deploying models on the model serving platform](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/deploying_models/deploying_models#deploying-models-on-the-model-serving-platform_rhoai-user)

A model serving runtime that uses the Caikit framework with the Text Generation Inference Server (TGIS) backend. Provides gRPC and REST inference endpoints.

**When to use:** When deploying text-generation models that benefit from the Caikit model management framework, particularly for NLP workloads requiring streaming responses.

**Requirements:**
- KServe must be installed and the model-serving platform enabled.
- Access to S3-compatible object storage for model artifacts.

### OpenVINO Model Server (OVMS)
**Details:** [OpenVINO Model Server](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/deploying_models/making_inference_requests_to_deployed_models#openvino_model_server)
**How to use:** [Deploying a model stored in an OCI image by using the CLI](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/deploying_models/deploying_models#deploying-model-stored-in-oci-image_rhoai-user)

Intel's high-performance inference runtime optimized for Intel hardware. Supports a wide range of model formats and provides both REST and gRPC interfaces.

**When to use:** When serving predictive AI models (classification, object detection, NLP) on Intel CPUs/GPUs and you need high-throughput, low-latency inference with broad model format support.

**Requirements:**
- KServe must be installed and the model-serving platform enabled.
- Access to S3-compatible object storage for model artifacts.

### NVIDIA Triton Inference Server
**Details:** [NVIDIA Triton Inference Server](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/deploying_models/making_inference_requests_to_deployed_models#nvidia_triton_inference_server)
**How to use:** [Adding a tested and verified runtime](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/configuring_your_model-serving_platform/configuring_model_servers#adding-a-tested-and-verified-runtime_rhoai-admin)

NVIDIA's multi-framework inference server supporting TensorRT, ONNX, PyTorch, TensorFlow, and more. Provides dynamic batching, model ensembles, and concurrent model execution.

**When to use:** When you need to serve multiple model types (including ensembles) on NVIDIA GPUs with advanced features like dynamic batching and model pipelines.

**Requirements:**
- KServe must be installed and the model-serving platform enabled.
- NVIDIA GPU Operator and Node Feature Discovery Operator installed.
- For IBM Z or IBM Power variants: access to the IBM Cloud Container Registry or Triton Inference Server Quay repository.

### MLServer ServingRuntime
**Details:** [MLServer ServingRuntime for KServe](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/deploying_models/making_inference_requests_to_deployed_models#mlserver_servingruntime_for_kserve)
**How to use:** [Deploying models by using the MLServer runtime](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/deploying_models/deploying_models#deploying-models-using-mlserver-runtime_rhoai-user)

A model serving runtime for KServe that supports multiple ML frameworks (scikit-learn, XGBoost, LightGBM, MLflow) through a plugin architecture.

**When to use:** When deploying traditional ML models (classification, regression, etc.) built with frameworks like scikit-learn, XGBoost, or LightGBM in a Kubernetes-native way.

**Requirements:**
- KServe must be installed and the model-serving platform enabled.
- Access to S3-compatible object storage for model artifacts.

---

## Model Management

### Model Registry
**Details:** [Overview of the model catalog and model registries](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/working_with_model_registries/overview-of-model-registries_working-model-registry#model_registry)
**How to use:** [Working with model registries](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/working_with_model_registries/working-with-model-registries_model-registry)

A centralized service for storing, versioning, and promoting ML models with metadata. Supports OCI-compliant storage (ModelCar format), RBAC-based access control, and PostgreSQL-backed metadata. Models can be registered from S3-compatible storage or URIs and automatically converted to OCI images.

**When to use:** When teams need to share, version, and promote models across projects with traceability and governance. Essential for MLOps workflows where models move through dev/staging/production stages.

**Requirements:**
- Set `modelregistry` component to `Managed` in the `DataScienceCluster`.
- For production: access to an external PostgreSQL 16.x database or MySQL 5.x+ (MySQL 9.x recommended).
- Access to S3-compatible object storage for OCI-compliant model storage.

### Model Catalog
**Details:** [Overview of the model catalog and model registries](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/working_with_the_model_catalog/overview-of-model-registries_working-model-catalog)
**How to use:** [Discovering and evaluating models in the model catalog](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/working_with_the_model_catalog/viewing-models-in-the-catalog_working-model-catalog)

A curated, searchable catalog of validated third-party models that are ready for deployment. Administrators can govern which model sources are available to teams.

**When to use:** When data scientists need to discover, evaluate, and quickly deploy pre-validated models without manually sourcing and configuring them. Useful for rapid prototyping and standardizing on approved models.

**Requirements:**
- The `modelregistry` component must be enabled (`Managed`) in the `DataScienceCluster`.
- At least one model registry must be created in your deployment.

---

## Agentic AI & RAG

### Llama Stack (Operator)
**Details:** [Overview of OGX](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/working_with_ogx/overview-of-ogx_rag)
**How to use:** [Activating the OGX Operator](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/working_with_ogx/activating-the-ogx-operator_rag)

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
**Details:** [Overview of OGX](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/working_with_ogx/overview-of-ogx_rag)
**How to use:** [OGX application examples (RAG stack)](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/working_with_ogx/ogx-adv-examples_rag)

An administrator-driven deployment pattern that provisions the full RAG infrastructure: LLM inference (vLLM), vector storage (PostgreSQL with pgvector), embedding service, and retrieval endpoints — all managed as a single unit.

**When to use:** When you need to deploy a complete RAG pipeline for a project team — including data ingestion, chunking, embedding, vector storage, and retrieval — without requiring each team to assemble the stack themselves.

**Requirements:**
- Llama Stack Operator and its prerequisites (see Llama Stack above).
- PostgreSQL with pgvector extension for vector storage.
- Access to S3-compatible object storage for data and model artifacts.
- GPU-enabled nodes for the LLM inference and embedding services.

### AutoRAG
**Details:** [AutoRAG overview](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/working_with_autorag/autorag-overview_autorag)
**How to use:** [Create an AutoRAG optimization run](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/working_with_autorag/creating-autorag-optimization-run_autorag)

An automated pipeline for building and optimizing RAG systems. Evaluates different retrieval strategies, chunking approaches, and embedding models to find the best configuration for your data and use case.

**When to use:** When you have a RAG use case but aren't sure which retrieval strategy, chunk size, or embedding model will perform best. AutoRAG automates the search for the optimal configuration.

**Requirements:**
- Llama Stack Operator and its prerequisites (see Llama Stack above).
- A deployed RAG stack (LLM inference, vector storage, embedding service).

---

## Development Environment

### Workbenches
**Details:** [Overview (workbench CRDs)](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/creating_a_workbench/api-workbench-overview_api-workbench)
**How to use:** [Using project workbenches](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/working_on_projects/using-project-workbenches_projects)

Browser-based development environments (Jupyter, VS Code, RStudio) pre-configured with data science libraries, GPU access, and secure connections to cluster resources. Provisioned via CRDs or the dashboard with resource quotas and hardware profiles.

**When to use:** When data scientists and AI engineers need an interactive development environment with direct access to cluster GPUs, data sources, and model serving endpoints for prototyping, training, and experimentation.

**Requirements:**
- Set `workbenches` component to `Managed` in the `DataScienceCluster`.
- To use a custom workbench namespace, create the namespace before installing the OpenShift AI Operator.

### Custom Notebook Images
**Details:** [Creating custom workbench images](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/managing_openshift_ai/creating-custom-workbench-images)
**How to use:** [Creating a custom image by using the ImageStream CRD](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/creating_a_workbench/api-custom-image-creating_api-workbench)

Administrator-published container images that extend the default workbench environments with additional libraries, tools, or configurations specific to your organization.

**When to use:** When the default IDE images lack specific libraries or tools your team requires, or when you need to standardize the development environment across teams.

**Requirements:**
- Workbenches component must be enabled.
- Custom images must be published to a container registry accessible from the cluster.
- If the cluster is running in FIPS mode, custom images must be based on UBI 9 or RHEL 9.

---

## Pipelines & Automation

### Data Science Pipelines (Kubeflow Pipelines)
**Details:** [Managing AI pipelines](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/working_with_ai_pipelines/managing-ai-pipelines_ai-pipelines)
**How to use:** [Managing pipeline runs](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/working_with_ai_pipelines/managing-pipeline-runs_ai-pipelines)

KFP-based pipeline engine for defining, versioning, scheduling, and tracking multi-step ML workflows. Supports DAG-based task orchestration, artifact tracking in S3, parameterized runs, and scheduled recurring executions.

**When to use:** When you need to automate multi-step ML workflows (data prep, training, evaluation, deployment) with versioning, scheduling, and reproducibility. Essential for moving from notebooks to production ML.

**Requirements:**
- Set `aipipelines` component to `Managed` in the `DataScienceCluster`.
- Write access to an S3-compatible object storage bucket for pipeline artifacts.
- If the cluster is running in FIPS mode, custom container images must be based on UBI 9 or RHEL 9.
- To use your own Argo Workflows instance, set `argoWorkflowsControllers.managementState` to `Removed` in the `DataScienceCluster`.

### Kubeflow Spark Operator (KSO)
**Details:** [Overview of the Kubeflow Spark Operator (KSO)](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/creating_distributed_data_processing_applications_with_the_kubeflow_spark_operator/overview-of-kubeflow-operator_data-processing)
**How to use:** [Using the Kubeflow Spark Operator](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/creating_distributed_data_processing_applications_with_the_kubeflow_spark_operator/using-the-ks-operator_data-processing)

Enables running Apache Spark applications as Kubernetes-native workloads for distributed data processing. Integrates with OpenShift AI for large-scale ETL and feature engineering.

**When to use:** When your ML pipeline requires large-scale data processing, ETL, or feature engineering that exceeds single-node capacity and needs distributed compute via Spark.

**Requirements:**
- Install the Kubeflow Spark Operator from OperatorHub.
- Data Science Pipelines component should be enabled if integrating Spark into ML pipelines.

---

## Training & Fine-Tuning

### Distributed Workloads (KubeRay, Training Operator)
**Details:** [Overview of distributed workloads](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/working_with_distributed_workloads/overview-of-distributed-workloads_distributed-workloads)
**How to use:** [Running Ray-based distributed workloads](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/working_with_distributed_workloads/running-ray-based-distributed-workloads_distributed-workloads)

Infrastructure for distributing ML training and data processing jobs across multiple nodes with GPU-aware scheduling, auto-scaling, and monitoring. Supports frameworks like PyTorch, TensorFlow, and Ray.

**When to use:** When training large models or processing large datasets that exceed single-node GPU memory or compute capacity. Enables data-parallel and model-parallel training strategies.

**Requirements:**
- Install the Red Hat build of Kueue Operator.
- Install the cert-manager Operator.
- Set `kueue` to `Unmanaged` (to let the external Kueue Operator manage it), and set `ray` and/or `trainingoperator` to `Managed` in the `DataScienceCluster`.
- At least 1.6 vCPU and 2 GiB memory available for the distributed workloads infrastructure (in addition to base OpenShift AI requirements).
- For GPU workloads: enable GPU support and install the relevant GPU operator.

### Model Customization (Fine-Tuning)
**Details:** [Overview of the model customization workflow](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/customize_models_for_gen_ai_and_agentic_ai_applications/overview-of-the-model-customization-workflow_custom-models)
**How to use:** [Train the model by using your prepared data](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/customize_models_for_gen_ai_and_agentic_ai_applications/train-the-model-by-using-your-prepared-data_custom-models)

Tools and workflows for customizing pre-trained models (LoRA, QLoRA, full fine-tuning) for domain-specific tasks. Integrates with the training operator and distributed workloads infrastructure.

**When to use:** When a pre-trained model needs to be adapted to your specific domain, vocabulary, or task — such as fine-tuning a general LLM on financial services terminology and workflows.

**Requirements:**
- Distributed Workloads components must be installed (Kueue, Ray and/or Training Operator).
- GPU-enabled nodes with sufficient VRAM for the model being fine-tuned.
- Access to S3-compatible object storage for datasets and model checkpoints.

### AutoML
**Details:** [AutoML overview](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/working_with_automl/automl-overview_automl)
**How to use:** [Create an AutoML optimization run](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/working_with_automl/creating-automl-optimization-run_automl)

Automated machine learning that searches for optimal model architectures, hyperparameters, and preprocessing steps for a given dataset and objective.

**When to use:** When you want to quickly find the best-performing model and hyperparameters for a structured data problem without manually tuning.

**Requirements:**
- Distributed Workloads components must be installed (Kueue, Ray and/or Training Operator).
- Workbenches component must be enabled.

---

## Evaluation & Safety

### LM Evaluation (LMEval)
**Details:** [Overview of evaluating AI systems](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/evaluating_ai_systems/overview-evaluating-ai-systems_evaluate)
**How to use:** [Evaluating LLMs with LM-Eval](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/evaluating_ai_systems/evaluating-llms-with-lm-eval_evaluate)

A framework for systematically evaluating LLM performance. Configure `LMEvalJob` resources to run standardized benchmarks, compare model versions, and track metrics over time.

**When to use:** When you need to evaluate and compare LLM performance before deploying to production — measuring accuracy, reasoning ability, and task-specific metrics across model versions.

**Requirements:**
- Set `trustyai` component to `Managed` in the `DataScienceCluster`.
- A deployed LLM model in your project.
- For online evaluations or remote code execution: set `permitOnline` and `permitCodeExecution` to `allow` in the `DataScienceCluster`, and set `allowOnline`/`allowCodeExecution` to `true` in the `LMEvalJob` CR.
- For offline evaluations from S3: access to an S3-compatible storage bucket containing the model and datasets.

### Guardrails (NeMo Guardrails)
**Details:** [Enabling AI safety with NeMo Guardrails](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/enabling_ai_safety_with_guardrails/enabling-ai-safety-with-nemo-guardrails_nemo-guardrails)
**How to use:** [Deploying the NeMo Guardrails service with an LLM](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/enabling_ai_safety_with_guardrails/enabling-ai-safety-with-nemo-guardrails_nemo-guardrails#deploying-the-nemo-guardrails-service-with-an-llm_nemo-guardrails)

A safety framework that orchestrates detectors to filter and validate LLM inputs and outputs. Supports content filtering, sensitive data detection, topic control, and custom validation rules. Exposes guarded inference endpoints.

**When to use:** When LLM responses must comply with safety, regulatory, or content policies — such as preventing hallucinations, blocking sensitive data leakage, enforcing topic boundaries, or filtering toxic content.

**Requirements:**
- Set `trustyai` component to `Managed` in the `DataScienceCluster`.
- KServe configured to use RawDeployment mode (`spec.kserve.rawDeploymentServiceConfig` set to `Headed`).
- A deployed LLM model on the model-serving platform.
- No external NVIDIA subscription required — NeMo Guardrails is included with OpenShift AI.

### RAGAS Evaluation Provider
**Docs:** [Overview of evaluating AI systems](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/evaluating_ai_systems/overview-evaluating-ai-systems_evaluate)

Metrics framework for evaluating RAG system quality. Measures retrieval quality, answer relevance, and factual consistency to identify issues in RAG pipeline configurations.

**When to use:** When you need quantitative assessment of your RAG pipeline's quality — checking whether retrieved documents are relevant, answers are grounded in context, and responses are factually consistent.

**Requirements:**
- Set `trustyai` component to `Managed` in the `DataScienceCluster`.
- A deployed RAG pipeline with accessible inference and retrieval endpoints.

---

## Monitoring & Observability

### Model Monitoring (TrustyAI)
**Details:** [Overview of monitoring your AI systems](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/monitoring_your_ai_systems/overview-of-monitoring-your-ai-systems_monitor)
**How to use:** [Setting up TrustyAI for your project](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/monitoring_your_ai_systems/setting-up-trustyai-for-your-project_monitor)

Monitoring service that tracks model bias, data drift, and performance degradation over time. Provides configurable metrics, thresholds, and dashboard visualizations.

**When to use:** When models are in production and you need to detect performance degradation, data drift, or fairness issues before they impact business outcomes. Critical for regulated industries.

**Requirements:**
- Set `trustyai` component to `Managed` in the `DataScienceCluster`.
- A TrustyAI service instance must be installed in each project containing models to monitor.
- Model serving platform must be enabled.
- Optional: for database-backed storage instead of PVC, configure a MySQL or MariaDB 10.5+ database secret before deploying TrustyAI.
- For KServe RawDeployment mode: update the `inferenceservice-config` ConfigMap and create a CA certificate ConfigMap in the model's namespace.

### Gen AI Playground
**Details:** [Playground overview](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/experimenting_with_models_in_the_gen_ai_playground/playground-overview_rhoai-user)
**How to use:** [Configure a playground for your project](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/experimenting_with_models_in_the_gen_ai_playground/configuring-a-playground-for-your-project_rhoai-user)

An interactive browser-based environment for experimenting with deployed models. Supports prompt engineering, parameter tuning, and side-by-side model comparison.

**When to use:** When you want to quickly test and compare deployed models with different prompts and parameters before integrating them into applications — useful for prompt engineering and model selection.

**Requirements:**
- OpenShift AI dashboard component must be enabled.
- At least one model deployed on the model-serving platform.

---

## Experiment Tracking

### MLflow Integration
**Details:** [About MLflow](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/working_with_mlflow/about-mlflow_mlflow)
**How to use:** [Install and configure MLflow](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/working_with_mlflow/installing-mlflow_mlflow)

Integration with MLflow for experiment tracking, model logging, metric recording, and artifact management. Provides a centralized view of training runs across teams.

**When to use:** When you need to track experiments, compare training runs, log model artifacts, and manage the ML experiment lifecycle across multiple data scientists.

**Requirements:**
- Workbenches component must be enabled.
- Access to S3-compatible object storage for artifact storage (optional but recommended).

---

## Feature Management

### Feature Store
**Details:** [Overview of machine learning features and Feature Store](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/working_with_machine_learning_features/overview-of-ml-features-and-feature-store.adoc_featurestore)
**How to use:** [Configuring Feature Store](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/working_with_machine_learning_features/configuring_feature_store)

A centralized service for defining, storing, and serving reusable machine learning features. Ensures consistent feature computation between training and serving (avoiding training-serving skew). Integrated with workbenches.

**When to use:** When multiple models or teams share computed features and you need to ensure consistency between training-time and serving-time feature values, or when you want to avoid redundant feature engineering.

**Requirements:**
- Set `feastoperator` component to `Managed` in the `DataScienceCluster`.
- Workbenches component must be enabled.

---

## Platform & Infrastructure

### Hardware Profiles & Accelerator Management
**Details:** [Overview of accelerators](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/working_with_accelerators/overview-of-accelerators_accelerators)
**How to use:** [Working with hardware profiles](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/working_with_accelerators/working-with-hardware-profiles_accelerators)

Administrator-configured hardware profiles that define GPU/accelerator resource allocations. Supports NVIDIA, AMD, Intel Gaudi, and IBM Spyre accelerators with the Node Feature Discovery Operator.

**When to use:** When you need to manage and allocate GPU/accelerator resources across teams and projects, ensuring workloads run on the correct hardware with appropriate resource limits.

**Requirements:**
- Install the Node Feature Discovery Operator.
- Install the GPU operator for your hardware: NVIDIA GPU Operator, AMD GPU Operator, Intel Gaudi Base Operator, or IBM Spyre Operator.

---

## Solution Tags

Tags describe what kind of solution a component is suited for. A component may carry more than one tag. Tags are not yet assigned to individual components in this document.

| Tag | Meaning |
|-----|---------|
| `predictive-ml` | Classical supervised or unsupervised machine learning — classification, regression, ranking, clustering, and similar structured-data problems. |
| `generative-ai` | Large language models and other generative models for text, code, or multimodal generation. |
| `computer-vision` | Image and video perception workloads such as detection, segmentation, and visual classification. |
| `nlp` | Natural language processing beyond chat alone — understanding, summarization, translation, NER, and related language tasks. |
| `multimodal` | Models and pipelines that combine multiple input or output modalities — text, image, audio, or video — in a single workload. |
| `rag` | Retrieval-augmented generation: indexing, retrieval, grounding answers in external or private knowledge. |
| `semantic-search` | Embedding documents and retrieving similar content by vector similarity, with or without generative answering. |
| `embeddings` | Generating vector representations of text or other modalities for similarity search, clustering, and retrieval. |
| `agentic-ai` | Multi-step agents that plan, use tools, and orchestrate actions across systems. |
| `mlops` | Model lifecycle management — versioning, promotion, registries, catalogs, and governed handoff between stages. |
| `model-discovery` | Finding, browsing, and selecting pre-validated or cataloged models that are ready to evaluate and deploy. |
| `data-prep` | Data preparation at scale — ETL, feature engineering, and distributed data processing ahead of training or inference. |
| `feature-management` | Centralized definition, storage, and serving of reusable features with consistency between training and inference. |
| `training` | Model training and fine-tuning, including distributed training and adapter-based customization. |
| `automl` | Automated search over model architectures, hyperparameters, and preprocessing for a given dataset and objective. |
| `serving` | Production inference — online or batch serving of models with scaling, routing, and operational controls. |
| `batch-inference` | Offline or scheduled scoring of large datasets rather than (or in addition to) real-time online serving. |
| `distributed-compute` | Spreading training, inference, or data processing across multiple nodes when a single machine is not enough. |
| `distributed-inference` | Scaling inference horizontally across nodes when single-server capacity or latency SLOs are insufficient. |
| `external-models` | Governed access to third-party or cloud-hosted model APIs without self-hosting the weights. |
| `model-routing` | Traffic management across model versions or replicas — canary rollouts, A/B testing, and cache-aware request routing. |
| `serverless` | Autoscaling inference and agent workloads to zero during idle periods and spinning up on demand for bursty traffic. |
| `evaluation` | Measuring model or pipeline quality, safety, benchmarks, and regression across versions. |
| `safety` | Runtime filtering and validation of model inputs and outputs for content policy, sensitive data, topic control, and related risk controls. |
| `monitoring` | Continuous production observability of deployed models — drift detection, bias tracking, and performance degradation. |
| `governance` | Quotas, RBAC, audit, policy enforcement, approved model sources, and controlled access to AI capabilities. |
| `workflow-orchestration` | Automating repeatable multi-step ML workflows with DAG scheduling, parameterization, and artifact lineage. |
| `experiment-tracking` | Recording and comparing training or tuning runs — parameters, metrics, and artifacts — across experiments and teams. |
| `interactive-development` | Browser-based notebook, IDE, or playground environments for iterative prototyping and hands-on experimentation. |
| `hardware-acceleration` | GPU and specialized accelerator enablement for compute-intensive workloads across supported hardware vendors. |
| `platform` | Shared infrastructure and enablers that support other solution types rather than embodying one solution themselves. |
