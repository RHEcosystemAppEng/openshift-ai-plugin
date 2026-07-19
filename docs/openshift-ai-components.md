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

High-throughput **LLM / generative** inference engine for KServe. Ships as hardware-specific `ServingRuntime` variants (NVIDIA GPU, AMD GPU/ROCm, Intel Gaudi, IBM Spyre, CPU) and exposes OpenAI-compatible completion and chat endpoints for token generation. vLLM is the inference **engine** under KServe — not the full serving platform (autoscaling, canary, multi-model orchestration stay with KServe; multi-node disaggregated scale-out is **Distributed Inference with llm-d**).

**When to use:** When serving large language models and you need optimized token generation throughput. Choose the runtime variant that matches your accelerator hardware (NVIDIA, AMD, Intel Gaudi, IBM Spyre, or CPU).

**Common confusion:**
- Using vLLM for scikit-learn, XGBoost, LightGBM, or other classical ML artifacts (those map to **MLServer**, **OVMS**, or **Triton**).
- Treating vLLM as the whole serving platform rather than the engine under KServe.
- Calling the embeddings endpoint with a generative (non-embedding) model.
- Expecting TrustyAI drift/bias monitoring on vLLM-served LLMs (that path is OVMS + tabular).

**When not to use:** Do not use vLLM for traditional ML framework models — use **MLServer** (or **OVMS** / **Triton** as appropriate). Do not choose vLLM alone when you need multi-node disaggregated LLM serving — evaluate **Distributed Inference with llm-d**. Do not use it as a substitute for evaluation or guardrails.

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

KServe `ServingRuntime` for **traditional ML** frameworks documented in the OpenShift AI deploy path: Scikit-learn, XGBoost, LightGBM, and ONNX, via KFServing V2-style infer endpoints. Marked **Technology Preview** (no production SLAs). Upstream MLServer has a broader plugin list than what the RHOAI deploy wizard documents and auto-configures.

**When to use:** When deploying traditional ML models (classification, regression, etc.) built with frameworks like scikit-learn, XGBoost, or LightGBM in a Kubernetes-native way.

**Common confusion:**
- Choosing MLServer for LLM token generation or OpenAI-style chat APIs (use **vLLM**).
- Assuming full production support despite Technology Preview status.
- Equating upstream MLServer’s plugin catalog with the RHOAI-supported deploy path.

**When not to use:** Do not use MLServer as the primary runtime for generative LLMs — use **vLLM Serving Runtimes**. Prefer a GA runtime (**OVMS**, **Triton**, etc.) when you need production SLAs and MLServer’s Tech Preview status is a blocker. **Model Monitoring (TrustyAI)** still requires OVMS/tabular constraints — serving with MLServer alone does not enable that monitoring path.

**Requirements:**
- KServe must be installed and the model-serving platform enabled.
- Access to S3-compatible object storage for model artifacts.

---

### Red Hat AI Model Optimization Toolkit (LLM Compressor)
**Details:** [About Red Hat AI Model Optimization Toolkit](https://docs.redhat.com/en/documentation/red_hat_ai_inference/3.4/html/red_hat_ai_model_optimization_toolkit/about-llm-compressor_llm-compressor)
**How to use:** [Compressing language models with Red Hat AI Model Optimization Toolkit](https://docs.redhat.com/en/documentation/red_hat_ai_inference/3.4/html/red_hat_ai_model_optimization_toolkit/compressing-language-models-with-model-opt-container_llm-compressor)

Open-source toolkit (based on upstream LLM Compressor) for post-training quantization, sparsity, and compression of large language models—AWQ, GPTQ, FP8, SmoothQuant, SparseGPT, and related schemes—into the `compressed-tensors` format for Hugging Face–compatible deployment with vLLM and Red Hat AI Inference. It is a pre-deployment model-prep step that trades model size and throughput against accuracy; OpenShift AI workbench and pipeline examples that wrap the toolkit are Developer Preview.

**When to use:** When you need to shrink LLMs or speed up inference for vLLM / Red Hat AI Inference serving—for example weight-only schemes for memory-bound, low-QPS latency goals, or INT8/FP8 (and sparsity) for compute-bound, high-throughput deployments—using calibrated compression recipes before you serve the model.

**Common confusion:**
- Expecting it to train or fine-tune models.
- Applying it to traditional ML (sklearn/XGBoost) serving.
- Assuming compression never hurts quality.
- Treating it as a runtime serving feature rather than a pre-deployment model-prep step.

**When not to use:** Do not use LLM Compressor to replace training/fine-tuning — use **Model Customization** / Training Operator paths. Do not compress non-LLM predictive models for MLServer/OVMS/Triton — those runtimes are unrelated. Skip aggressive PTQ when you cannot calibrate on representative data or when post-quant benchmarks regress beyond tolerance; keep full-precision or use milder schemes / QAT-style recovery paths instead. Prefer already-compressed Red Hat–validated model artifacts when you only need a known-good quantized checkpoint and do not need a custom recipe.

**Requirements:**
- Podman or Docker; sudo access; login to `registry.redhat.io`; Hugging Face account and access token (per Red Hat AI Inference 3.4 compression procedure).
- NVIDIA GPU access for the supported CUDA model-opt container workflow (`registry.redhat.io/rhaii/model-opt-cuda-rhel9`); on SELinux hosts, `container_use_devices` must allow device access.
- OpenShift AI workbench/pipeline integration of the toolkit is Developer Preview.

---

### AI Inference Tool Calling
**Details:** [About tool calling](https://docs.redhat.com/en/documentation/red_hat_ai_inference/3.4/html/extending_red_hat_ai_inference_with_tool_calling_capabilities/about-tool-calling_tool-calling)
**How to use:** [Enabling tool calling for OpenAI gpt-oss models](https://docs.redhat.com/en/documentation/red_hat_ai_inference/3.4/html/extending_red_hat_ai_inference_with_tool_calling_capabilities/enabling-gpt-oss-tool-calling_tool-calling)

A Red Hat AI Inference (vLLM) serving feature that lets a deployed LLM emit structured function/tool calls—via chat templates and model-specific `--tool-call-parser` settings—so your application can invoke external APIs, databases, or other tools and feed results back into the conversation. It formats model↔tool messages at the OpenAI-compatible inference API; tool execution itself stays in the client. Documented as Developer Preview in Red Hat AI Inference 3.4.

**When to use:** When a served model must go beyond text generation to request external actions—querying databases, calling APIs, running calculations, or fetching real-time data—and your app should execute those tools and continue the chat with structured `tool_calls` / tool results (`tool_choice` auto, required, or none).

**Common confusion:**
- Treating tool calling as an MCP platform (gateway, catalog, registration).
- Expecting it to provide agent memory or planning loops.
- Assuming every model works without the correct `--tool-call-parser` / chat template.

**When not to use:** Do not use tool calling alone when you need shared, governed enterprise MCP tools across clients — use **MCP Gateway** (+ registration/authorization) or an agent stack. Do not use it for pure text generation with no tools — disable tool flags to avoid unnecessary parser/template complexity. If you need multi-step agent orchestration (memory, planners, multi-agent), pair inference with an agent framework or **Kagenti**-style runtime; tool calling only formats model↔tool messages at the inference layer.

**Requirements:**
- Developer Preview only (not supported for production or business-critical workloads per Red Hat AI Inference 3.4 docs).
- Podman; Linux host with at least one NVIDIA AI accelerator; NVIDIA Container Toolkit with CDI configured.
- Hugging Face account and access token; one or more tools defined for the model to call.
- Enable with `--enable-auto-tool-choice` and a matching `--tool-call-parser` (and `--chat-template` when the model lacks a suitable built-in template); application must execute tools and return results—the server does not run them.

---

### Speculative Decoding (Speculators)
**Details:** [About Speculators](https://docs.redhat.com/en/documentation/red_hat_ai_inference/3.4/html/speculative_decoding/about-speculators_speculative-decoding)
**How to use:** [Deploying speculator models](https://docs.redhat.com/en/documentation/red_hat_ai_inference/3.4/html/speculative_decoding/deploying-speculator-models_speculative-decoding)

Technology Preview library and serving path for **Eagle 3 speculative decoding** with Red Hat AI Inference: a small single-layer draft (speculator) model proposes tokens that the full verifier LLM validates in parallel, raising effective decode throughput and cutting latency while keeping the verifier’s output distribution unchanged. Speculators covers building, training, and storing speculative-decoding algorithms for frameworks such as vLLM; at serve time vLLM loads both draft and verifier from the speculator model configuration.

**When to use:** When LLM decode latency or tokens-per-second is the bottleneck and you can run a trained Eagle 3 speculator alongside the verifier on GPU—especially to cut latency via parallel token validation while preserving verifier-equivalent output quality.

**Common confusion:**
- Expecting free speedups with no tuning of acceptance rate or draft-token count.
- Confusing Speculators (draft model build/serve path) with quantization via **LLM Compressor**.
- Assuming speculative decoding always beats baseline under high concurrency.

**When not to use:** Do not enable speculative decoding without measuring acceptance rate / draft-token count (`k`) on your traffic — poorly tuned speculation can **worsen** cost/perf versus plain decoding. Skip it when GPU memory cannot hold draft + verifier, or when Technology Preview is unacceptable for production SLAs. Prefer plain vLLM serving (or quantization via **LLM Compressor**) when latency is already acceptable or when you need a GA, simpler serving path.

**Requirements:**
- Speculators is Technology Preview only (not supported under Red Hat production SLAs; Red Hat does not recommend production use).
- Red Hat AI Inference container image (`vllm-cuda-rhel9` from `registry.redhat.io`) with Podman or Docker.
- Login to `registry.redhat.io` and a Hugging Face account with an access token (accept model license agreements as needed).
- Linux server with at least one NVIDIA AI accelerator, NVIDIA drivers, and the NVIDIA Container Toolkit.
- GPU capacity to load both the Eagle 3 draft/speculator model and the verifier LLM (vLLM loads both from the speculator configuration).

---

### OCI ModelCar Inference Serving
**Details:** [About OCI-compliant model containers](https://docs.redhat.com/en/documentation/red_hat_ai_inference/3.4/html/inference_serving_language_models_in_oci-compliant_model_containers/about-oci-models_oci-models)
**How to use:** [Creating a modelcar image and pushing it to a container image registry](https://docs.redhat.com/en/documentation/red_hat_ai_inference/3.4/html/inference_serving_language_models_in_oci-compliant_model_containers/rhaiis-creating-modelcar-image_oci-models)

Packages language-model weights as OCI-compliant “modelcar” container images and inference-serves them with Red Hat AI Inference (and KServe on OpenShift AI) so clusters pull models from a container registry instead of repeatedly downloading from S3 or Hugging Face. Modelcars reuse the same versioning, caching, security, and distribution stack you already use for application images, which can cut startup time, reduce local disk churn, and improve performance when images are pre-fetched on nodes. You package the model into an OCI image, push it to a registry, then mount or reference that image from the inference serving path.

**When to use:** Use modelcars when you want language models to travel through your existing container registry workflows—unified tagging, pull caching, and security scanning—rather than a separate object-storage download on every pod start. Prefer this path when registry-cached images and faster cold starts matter more than keeping an S3/URI-centric model ops process.

**Common confusion:**
- Assumed to replace all S3 storage
- Confused with Quay’s artifact-type storage tools (Skopeo/ORAS) rather than inference-serving modelcars
- Very large models (e.g. ~900 GB class) are awkward as container images
- Using `:latest`/untagged images defeats cache benefits (`Always` pull)
- Base images must provide a shell for KServe accessibility checks

**When not to use:** Prefer S3/URI (or PVC) storage when models are enormous or your ops path is already object-storage-centric. Do not use ModelCar merely to store arbitrary OCI artifacts without serving — use Quay + Skopeo/ORAS. For local single-node experiments without registry/GPU serving needs, downloading weights directly is simpler.

**Requirements:**
- Python 3.11 or later, Podman or Docker, and internet access to download models (for example from Hugging Face) when building a modelcar image.
- A configured container image registry you can push to (and are logged in to).
- For OpenShift deployment with Red Hat AI Inference: OpenShift CLI (`oc`), `cluster-admin` privileges, Node Feature Discovery (NFD) and the GPU Operator for your accelerators, plus a modelcar image already pushed to a registry.
- Persistent storage (PVC) for the model cache as shown in the OpenShift modelcar deploy procedure.
- For KServe/OpenShift AI OCI (`oci://`) serving: a base image that provides a shell (not `scratch`), and an image pull secret when the OCI repository is private.

---

### Gateway API Inference Extensions
**Details:** [Distributed Inference with llm-d core components](https://docs.redhat.com/en/documentation/red_hat_ai_inference/3.4/html/distributed_inference_with_llm-d/llmd-core-components_distributed-inference-with-llmd)
**How to use:** [Configuring scheduler settings for LLM inference services](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.4/html/deploy_models_using_distributed_inference_with_llm-d/configuring-llm-scheduler)

Gateway API Inference Extensions build on Kubernetes Gateway API to add inference-aware routing and load balancing for self-hosted generative model servers. An `InferencePool` groups model-serving endpoints while an Endpoint Picker (inference scheduler) integrates with the gateway over ext-proc to choose pods using model-aware, KV-cache, queue-depth, and load signals rather than round-robin Service balancing. OpenShift Service Mesh 3.4 supports Gateway API Inference Extension 1.4.0 for intelligent routing of GPU-accelerated inference workloads; Gateway inference extensions remain Technology Preview.

**When to use:** Use when you run multi-replica self-hosted LLM/GenAI serving and need per-request scheduling that favors warm KV/prefix cache, balanced queue depth, or prefill/decode-aware routing through an Inference Gateway—capabilities described for Distributed Inference with llm-d and OpenShift AI Endpoint Picker configuration.

**Common confusion:**
- Treating it as a generic HTTP API gateway upgrade for ordinary microservices or CRUD APIs.
- Enabling it for a single-replica model deployment where smart endpoint picking adds no value.
- Upstream and Red Hat docs position it for self-hosted GenAI/LLM serving characteristics, not general HTTP traffic.

**When not to use:** Do not use for non-inference HTTP services, external SaaS-only LLM proxies without self-hosted pools, or single-replica demos—standard Gateway API HTTPRoute/Service LB is simpler. For GPU *autoscaling* use CMA/HPA; for mesh mTLS alone, plain Service Mesh is enough. Skip if you cannot operate an endpoint-picker/ext-proc-capable gateway implementation.

**Requirements:**
- OpenShift Service Mesh with Gateway inference extensions (Technology Preview in Service Mesh 3.4 feature support tables); Service Mesh 3.4 documents support for Gateway API Inference Extension 1.4.0 and is supported on OpenShift Container Platform 4.20 and later.
- Kubernetes Gateway API CRDs (generally available on OpenShift Container Platform 4.19 and later; not included on 4.18 and earlier).
- A Gateway API implementation that can integrate the Endpoint Picker via the ext-proc protocol (Red Hat docs describe Gateway API with Red Hat Connectivity Link / Inference Gateway plus Istio/Sail for the inference stack).
- For the OpenShift AI how-to path: OpenShift AI with model serving configured, and privileges to create or update an `LLMInferenceService` (inline or ConfigMap-based `EndpointPickerConfig`).

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

### MCP Gateway
**Details:** [Introduction to the MCP gateway](https://docs.redhat.com/en/documentation/red_hat_connectivity_link/1.4/html/mcp_gateway/mcp-gateway-introduction)
**How to use:** [Installing and configuring MCP gateway](https://docs.redhat.com/en/documentation/red_hat_connectivity_link/1.4/html/installing_the_mcp_gateway/mcp-gateway-install)

Red Hat Connectivity Link’s Model Context Protocol (MCP) gateway aggregates many backend MCP servers behind a single Kubernetes Gateway API endpoint, so agentic clients see one federated MCP surface with unified tool discovery, MCP-aware routing, and session handling. It extends Envoy (Gateway API implementation) with an MCP router (`ext_proc`), broker, and discovery controller that watches `MCPServerRegistration` and related routes; Connectivity Link policies such as `AuthPolicy` secure access. Marked **Technology Preview** in Connectivity Link 1.4 (not production-supported under Red Hat SLAs).

**When to use:** When you need to centralize connectivity for agentic AI applications that call multiple MCP servers—exposing them behind one endpoint, scaling without baking networking into app code, and managing access and security of AI tools the same way you govern REST APIs.

**Common confusion:**
- Using the gateway as a general API gateway for non-MCP HTTP APIs.
- Confusing it with RHOAI MCP Catalog’s upstream “mcp-gateway” dependency name.
- Expecting authentication/authorization without AuthPolicies.
- Using it for a single local MCP server with one client.

**When not to use:** Do not use MCP Gateway for ordinary REST/gRPC north-south traffic — use OpenShift Gateway API / Connectivity Link HTTP policies without MCP extensions. For a single MCP server and a single IDE client, connect the client directly to that server. Do not treat gateway install alone as RBAC — add **MCP Gateway Authorization**. Prefer Connectivity Link MCP Gateway when you need federated multi-server tool lists and session routing at scale; otherwise the operational cost of Gateway + broker + registrations is unjustified.

**Requirements:**
- Technology Preview only — not supported with production SLAs; Red Hat does not recommend production use.
- OpenShift Container Platform with OpenShift CLI (`oc`); install the MCP gateway Operator via OLM (`Subscription` name `mcp-gateway`, channel `preview`, source `redhat-operators`).
- A Gateway API provider and a `Gateway` object with at least one listener; apply an `MCPGatewayExtension` CR targeting that Gateway (one extension per namespace and per Gateway). Create a `ReferenceGrant` if the extension and Gateway are in different namespaces.
- Connectivity Link 1.4.1 or later (1.4.0 is deprecated). Connectivity Link platform prerequisites: OpenShift Container Platform 4.18 or later, Red Hat account with Connectivity Link and OpenShift subscriptions, and cert-manager Operator for Red Hat OpenShift 1.18. On OpenShift 4.18 or older, Red Hat OpenShift Service Mesh is required as the Gateway API provider; if you use Service Mesh, use 3.2.
- Register backends with `MCPServerRegistration` CRs; configure Connectivity Link authentication/authorization (`AuthPolicy` and related MCP gateway authorization) separately from Operator install.

---

### A2A Agent Registry
**Details:** [A2A protocol overview](https://docs.redhat.com/en/documentation/red_hat_build_of_apicurio_registry/3.2/html/apicurio_registry_user_guide/assembly-a2a-features_registry#a2a-overview_registry)
**How to use:** [Registering an agent card](https://docs.redhat.com/en/documentation/red_hat_build_of_apicurio_registry/3.2/html/apicurio_registry_user_guide/agent-registry-quickstart_registry#registering-an-agent-card_registry)

Developer Preview capability in **Red Hat build of Apicurio Registry** that implements the A2A (Agent-to-Agent) protocol for AI agent discovery and lifecycle management. The registry stores Agent Cards as `AGENT_CARD` artifacts and exposes A2A well-known endpoints (`/.well-known/agents`, skill/capability search, and per-artifact retrieval) so agents can find each other; Apicurio can also act as an A2A agent itself with built-in skills such as schema validation, search, and agent discovery.

**When to use:** When you need a central place to publish and discover A2A Agent Cards—searching by name, skill, or capability via well-known endpoints—so orchestrators and other agents can locate peers without hard-coding URLs, including multi-agent pipelines that chain discovered agents.

**Common confusion:**
- Confusing A2A agent discovery with **MCP tool** discovery/execution — A2A finds Agent Cards; MCP exposes tools to LLMs.
- Assuming the registry **runs** agents — it stores and discovers Agent Cards; it does not host agent runtimes.
- Mixing this with **MCP Tool Registry** (`MCP_TOOL` artifacts) — that catalog is for MCP tool definitions, not A2A Agent Cards.

**When not to use:** Do not use A2A Agent Registry when you need LLM tool calling against APIs — use an **MCP server** (and optionally **MCP Tool Registry** for tool definitions). Do not use it as an agent runtime/orchestration engine — use your agent framework / **Agent Sandbox** / platform runtimes. Requires `apicurio.a2a.enabled`; Developer Preview.

**Requirements:**
- Red Hat build of Apicurio Registry with A2A enabled (`apicurio.a2a.enabled=true`; default `false`).
- Developer Preview — not supported for production or business-critical workloads.
- Apicurio Registry running with agent features enabled before registering or discovering Agent Cards.

---

### Red Hat build of Agent Sandbox
**Details:** [Discover Red Hat build of Agent Sandbox](https://docs.redhat.com/en/documentation/openshift_sandboxed_containers/1.12/html/deploying_red_hat_build_of_agent_sandbox/discover-agent-sandbox_agent-sandbox)
**How to use:** [Install Red Hat build of Agent Sandbox](https://docs.redhat.com/en/documentation/openshift_sandboxed_containers/1.12/html/deploying_red_hat_build_of_agent_sandbox/install-agent-sandbox-overview_agent-sandbox)

Technology Preview Kubernetes-native platform on OpenShift Container Platform for isolated, long-lived, stateful singleton workloads such as AI agent runtimes and development environments. It exposes declarative `Sandbox` (and related extension) CRDs—including optional `SandboxWarmPool` for prewarmed pods—so you manage lifecycle, stable identity, persistent state, and hibernation instead of wiring StatefulSets, Services, and PVCs by hand. Optionally pairs with the OpenShift sandboxed containers Operator via `runtimeClassName` for VM-level (Kata) isolation when running untrusted or multitenant agent code.

**When to use:** When you need declarative lifecycle management for long-running isolated agent or interactive environments on OpenShift—fast provisioning via warm pools, persistent state across restarts, and idle hibernation—especially when you also want optional hardware-level isolation through OpenShift sandboxed containers for LLM-generated or otherwise untrusted code.

**Common confusion:**
- Equating Agent Sandbox with **OpenShift sandboxed containers** alone (Kata runtime for any pod).
- Equating it with Agent Cards or MCP registries (agent discovery / tool catalogs).
- Treating it as confidential computing by itself; it is a workload lifecycle API for long-running isolated environments, not agent discovery and not confidential computing on its own.

**When not to use:** Do not use Agent Sandbox when you only need ordinary Deployments/Jobs without singleton stateful agent semantics. Do not use it as an A2A/MCP registry. If you only need Kata isolation for existing pods, evaluate **OpenShift sandboxed containers** runtime classes without the Agent Sandbox CRDs. It is not a substitute for prompt guardrails or MCP authz.

**Requirements:**
- Technology Preview only — not supported with Red Hat production SLAs; not recommended for production (see Technology Preview Features Support Scope).
- Red Hat OpenShift Container Platform 4.19 or later; `cluster-admin` access.
- Install the Red Hat build of Agent Sandbox Operator from OperatorHub (all namespaces; installed namespace `agent-sandbox-system`); the Operator deploys the sandbox controller, sandbox router, and extension CRDs.
- Optional hardware-level isolation: install and configure the OpenShift sandboxed containers Operator and set the appropriate `runtimeClassName` on the `Sandbox` pod template; RHCOS worker nodes required (RHEL workers not supported).

---

### MCP Authorization Server
**Details:** [Integrating with Model Context Protocol (MCP)](https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.6/html/securing_applications_and_services_guide/mcp-authz-server-)
**How to use:** [Setup](https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.6/html/securing_applications_and_services_guide/mcp-authz-server-#mcp-authz-server-setup)

Red Hat build of Keycloak acting as an OAuth 2.0/2.1 authorization server for Model Context Protocol (MCP) clients and servers—issuing tokens, supporting dynamic client registration and (experimental) OAuth Client ID Metadata Documents (CIMD), so MCP hosts can obtain audience-bound access to protected MCP resources. Per Red Hat build of Keycloak 26.6, MCP 2025-03-26 is fully supported (all MUST/SHOULD); MCP 2025-06-18 and 2025-11-25 are partially supported because Resource Indicators for OAuth 2.0 (RFC 8707) are not supported.

**When to use:** When you need an enterprise OAuth/OIDC identity provider to authenticate MCP hosts and issue tokens for protected MCP servers—for example VS Code desktop or other CIMD-capable clients—rather than embedding identity logic in each MCP server. Prefer this when MCP servers should act as OAuth resource servers that validate JWTs from Red Hat build of Keycloak while the AS handles login, consent, and client registration.

**Common confusion:**
- Expecting Keycloak to enforce per-tool RBAC or replace MCP Gateway authorization policies; Keycloak is the IdP/AS—tool-level allow/deny belongs elsewhere (e.g. Connectivity Link MCP Gateway Authorization).
- Assuming full MCP 2025-06-18 / 2025-11-25 MUST compliance without Resource Indicators; RFC 8707 is not supported—documented `scope`/`aud` workarounds are required.

**When not to use:** Do not use it as your only control for which MCP **tools** an agent may call — add **MCP Gateway Authorization** (or equivalent resource-server policy). Do not expect out-of-the-box MCP 2025-06-18 / 2025-11-25 full MUST compliance without the documented `scope`/`aud` workarounds. Do not use it if you only need Lightspeed’s own OpenShift TokenReview auth for `/v1/query`.

**Requirements:**
- Red Hat build of Keycloak deployed as the MCP authorization server (documented for Red Hat build of Keycloak 26.6).
- MCP 2025-03-26: no special Keycloak setup beyond standard OAuth AS usage.
- MCP 2025-06-18 and 2025-11-25: configure optional client scopes with Audience mappers so the access-token `aud` matches the MCP server URL (workaround for unsupported RFC 8707 Resource Indicators / `resource` parameter).
- MCP 2025-11-25 with Client ID Metadata Documents: start Keycloak with `--features=cimd` and configure a client-policy profile (`client-id-metadata-document` executor) plus a policy (`client-id-uri` condition); CIMD support is experimental and may introduce breaking changes.
- MCP servers (not Keycloak) must implement OAuth 2.0 Protected Resource Metadata (RFC 9728) for AS discovery; Keycloak supports OAuth 2.1, Authorization Server Metadata (RFC 8414), and Dynamic Client Registration (RFC 7591) as documented in the compliance table.

---

### MCP Catalog
**Details:** [MCP Catalog for enterprise management of MCP servers](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/release_notes/developer-preview-features_relnotes)
**How to use:** [Configuring Model Context Protocol (MCP) servers](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/experimenting_with_models_in_the_gen_ai_playground/playground-prerequisites_rhoai-user#configuring-model-context-protocol-mcp-servers_rhoai-user)

A Developer Preview OpenShift AI catalog UI where AI operators and platform engineers browse curated MCP servers (Red Hat, partners, and community), view capability/tool metadata, and deploy servers into a namespace without manually sourcing images or configuring transport. After deploy, servers are registered in the gen AI studio configuration so they appear in the playground for interactive experimentation.

**When to use:** Use it when you want a governed discover-to-deploy path for enterprise MCP servers on OpenShift AI—browse validated catalog entries, deploy via the MCP lifecycle operator, then wire them into gen AI studio / playground for agent and tool experimentation rather than hand-rolling containers and registration.

**Common confusion:**
- Thinking the catalog *is* the MCP Gateway or that it implements tool authorization
- Expecting it to author custom MCP server code
- Assuming deploy works without the MCP lifecycle operator

**When not to use:** Do not use MCP Catalog when you only need to register already-running MCP servers with Connectivity Link — use **MCP Server Registration**. Do not use it as production access control — use **MCP Gateway Authorization**. Skip it if you are writing a one-off MCP server for a single client and do not need catalog-mediated deploy/playground wiring. Deploy is gated on **mcp-lifecycle-operator**; without that operator, catalog deploy is unavailable.

**Requirements:**
- Feature is Developer Preview in Red Hat OpenShift AI (documented in 3.5 Developer Preview release notes).
- Install **mcp-lifecycle-operator** on the cluster before deploying from the catalog; the catalog UI deploy action is gated on that operator (and the `MCPServer` CRD it provides).
- Catalog also relies on upstream **mcp-gateway** as a unified runtime endpoint for deployed MCP servers (per release notes).
- Disconnected environments may require mirroring images; some servers need server-specific credentials.
- To expose deployed servers in the gen AI playground, a cluster admin must register them in the `gen-ai-aa-mcp-servers` ConfigMap in `redhat-ods-applications` (or equivalent gen AI studio MCP configuration).

---

### MCP Gateway Authorization
**Details:** [Understanding authorization in MCP gateway](https://docs.redhat.com/en/documentation/red_hat_connectivity_link/1.4/html/registering_mcp_servers_and_creating_policies/mcp-gateway-authorization#con-understanding-mcp-gateway-authorization_mcp-gateway-authorization)
**How to use:** [Configuring MCP gateway authorization with an AuthPolicy](https://docs.redhat.com/en/documentation/red_hat_connectivity_link/1.4/html/registering_mcp_servers_and_creating_policies/mcp-gateway-authorization#proc-mcp-gateway-authorization_mcp-gateway-authorization)

Connectivity Link capability that adds tool- and prompt-level authorization on MCP gateway `tools/call` traffic: after a user authenticates and receives a JWT, a Kuadrant `AuthPolicy` on the gateway’s internal `mcps` listener verifies claims and evaluates CEL (or optional OPA) rules so identities may only invoke permitted MCP capabilities. It complements authentication-only policies on the public `mcp` listener and works with Istio or Gateway API–compatible auth mechanisms on OpenShift; MCP gateway itself is Technology Preview.

**When to use:** When authenticated clients must be limited to specific MCP server tools and prompts behind Connectivity Link MCP Gateway—for example role-based ACLs driven by IdP JWT `resource_access` / role claims and AuthPolicy CEL or OPA rules on the `mcps` listener.

**Common confusion:**
- Conflating with authentication-only AuthPolicies on the public `mcp` listener.
- Confusing with Red Hat build of Keycloak’s separate MCP Authorization Server product.
- Expecting authorization without MCP Gateway or correct listener targeting.

**When not to use:** Do not use MCP Gateway Authorization if you only need to prove identity (authN) — configure authentication AuthPolicy on the `mcp` listener. Do not apply tool RBAC AuthPolicies to the wrong listener (`mcps` is required for tool/call authorization). If you have a single MCP server with trusted in-cluster callers and no multi-tenant tool ACL needs, gateway-level tool RBAC may be overkill — network policies + server-side auth may suffice. This is not a replacement for IdP user management itself (Keycloak/RH-SSO still define roles/claims).

**Requirements:**
- MCP gateway installed (Technology Preview) and Connectivity Link installed.
- `Gateway` with both an `mcp` listener and an `mcps` listener (`mcps` is required for internal `tools/call` routing and authorization).
- Authentication completed, including an authentication-only `AuthPolicy` on the `mcp` listener.
- Identity provider configured to include `group` and `role` claims in JWTs; client IDs must match the namespaced `MCPServerRegistration` name (`{namespace}/{name}`).
- Authorization `AuthPolicy` must target the `mcps` listener (`sectionName: mcps`), not `mcp`.

---

### Prompt Template Registry
**Details:** [Architecture overview (LLM artifact types)](https://docs.redhat.com/en/documentation/red_hat_build_of_apicurio_registry/3.2/html/apicurio_registry_user_guide/assembly-llm-artifact-types-implementation_registry#llm-artifact-types-architecture_registry)
**How to use:** [PROMPT_TEMPLATE implementation details](https://docs.redhat.com/en/documentation/red_hat_build_of_apicurio_registry/3.2/html/apicurio_registry_user_guide/assembly-llm-artifact-types-implementation_registry#llm-artifact-types-prompt-template-implementation_registry)

Built-in `PROMPT_TEMPLATE` artifact type in Red Hat build of Apicurio Registry 3.2 that version-controls LLM prompt templates with typed variables, validation, and backward-compatibility checks (Microsoft Prompty–aligned schema). Optional server-side render (`POST …/render`) substitutes variables with type/required/enum/range validation; optional `mcp` metadata plus the Apicurio Registry MCP server can expose templates as MCP prompts. Release notes list AI/LLM artifact types as Technology Preview; the LLM artifact types implementation guide marks the section Developer Preview—not production-ready.

**When to use:** When you need a governed registry for reusable, versioned prompt templates shared by agents and apps—variable contracts, compatibility rules as templates evolve, optional render APIs, and optional MCP discovery—rather than ad-hoc prompt strings in code or git alone.

**Common confusion:**
- Treating it as a full prompt ops / evaluation platform (A/B analytics, tracing, production LLM gateway).
- Using it as a general document store.
- It is a registry artifact type with validation, compatibility, and render—not an LLM ops suite.

**When not to use:** Do not use it alone when you need prompt evaluation, tracing, or production gateway policy — pair with (or prefer) LLMOps/eval tooling and your inference path. Do not use it to store free-form docs or agent runtime code; use **AGENT_CARD** / **MODEL_SCHEMA** / git as appropriate. Feature is Developer Preview — avoid production-critical sole dependency.

**Requirements:**
- Red Hat build of Apicurio Registry 3.2 with a supported OpenShift deployment and storage backend (PostgreSQL, MySQL, or Red Hat Streams for Apache Kafka).
- Register artifacts as type `PROMPT_TEMPLATE` with required `templateId` and `template` fields; content type `application/json`, `application/x-yaml`, or `text/x-prompt-template` (placeholders in `{{variable}}` form must match `variables` / `inputs` definitions).
- Optional MCP prompt exposure: set `mcp.enabled: true` on the template and run the Apicurio Registry MCP server against a reachable registry (`REGISTRY_URL`; Docker/Podman, or Java 21 and Maven to build from source)—MCP server integration is Developer Preview.
- Treat as Technology Preview / Developer Preview per Apicurio Registry 3.2 docs; not supported for production or business-critical workloads.

---

### Kagenti Operator
**Details:** [Kagenti Operator Repository](https://github.com/kagenti/kagenti-operator)
**How to use:** [Getting Started with Kagenti Operator](https://github.com/kagenti/kagenti-operator/blob/main/kagenti-operator/GETTING_STARTED.md)

Kubernetes operator (Developer Preview in Red Hat OpenShift AI 3.5) for agent and tool workload runtime concerns on OpenShift. An `AgentRuntime` CR that references a Deployment or StatefulSet via `spec.targetRef` triggers injection of AuthBridge (Envoy-based inbound JWT validation and outbound token exchange), SPIFFE workload identity (`spiffe-helper`), and per-agent OpenTelemetry tracing. Deployments labeled `kagenti.io/type: agent` with a protocol label such as `protocol.kagenti.io/a2a` automatically receive an `AgentCard` that advertises capabilities, endpoints, and protocols for machine-readable agent-to-agent (A2A) discovery.

**When to use:** When you deploy agent workloads on OpenShift AI and need platform-managed identity, auth, and observability sidecars plus AgentCard discovery for authenticated, observable multi-agent A2A workflows—rather than wiring those runtime concerns into each agent app yourself.

**Common confusion:**
- Equating Kagenti with **MCP Catalog** (browse/deploy MCP servers).
- Equating it with Connectivity Link **MCP Gateway** (tool aggregation).
- Treating it as the agent application framework you write against.
- Expecting production SLAs on Developer Preview features.

**When not to use:** Do not use Kagenti merely to expose tools to an LLM — start with **AI Inference Tool Calling** and/or **MCP Gateway**. Do not use it as an MCP server marketplace — use **MCP Catalog**. Skip it for single-agent apps that do not need SPIFFE/AuthBridge sidecars or A2A discovery. Avoid production/business-critical reliance while it remains Developer Preview; use plain Deployments + your own auth until the platform path is GA.

**Requirements:**
- Red Hat OpenShift AI 3.5 (or later listing) with AgentCard / AgentRuntime as Developer Preview — not supported by Red Hat and not production-ready (see Developer Preview support scope in the release notes).
- Kagenti platform installed on the cluster; for OpenShift, the operator repository documents `scripts/ocp/setup-kagenti.sh` as the recommended installer.
- AgentCard discovery: deploy the agent as a Kubernetes Deployment or StatefulSet with `kagenti.io/type: agent` and a protocol label such as `protocol.kagenti.io/a2a`.
- AgentRuntime management: create an `AgentRuntime` that references the workload via `spec.targetRef`; labeled agents are injected by default (opt out with `kagenti.io/inject: disabled`).

---

### HITL Tool Approval
**Details:** [About operation approvals](https://docs.redhat.com/en/documentation/red_hat_openshift_lightspeed/1.0/html/configure/ols-configuring-openshift-lightspeed#ols-about-operation-approvals_ols-configuring-openshift-lightspeed)
**How to use:** [Tools approval configuration](https://docs.redhat.com/en/documentation/red_hat_openshift_lightspeed/1.0/html/configure/ols-configuring-openshift-lightspeed#ols-ref-tools-approval-configuration_ols-configuring-openshift-lightspeed)

OpenShift Lightspeed operation approvals provide human-in-the-loop (HITL) validation so selected MCP tool calls pause for confirmation in the web console UI before the service executes them. Policies live in the `OLSConfig` `toolsApprovalConfig` object (`approvalType`: `never`, `always`, or `tool_annotations`; optional `approvalTimeout`, default `600` seconds). With the Observability MCP server, Lightspeed enables HITL for non-read operations by default (`approvalType` defaults to `tool_annotations`), and an administrator must clear the pending UI request before mutating cluster changes proceed.

**When to use:** When OpenShift Lightspeed can invoke write or other non-read MCP tools (Observability MCP or custom MCP servers) and you need human validation in the console before those tools alter the cluster—especially to stop unintended updates or deletes from running unattended.

**Common confusion:**
- Assuming HITL covers all agent platforms cluster-wide, not only OpenShift Lightspeed’s tool-execution UX.
- Treating `approvalType: never` as appropriate when write-capable MCP tools are enabled.
- Marking sensitive custom MCP operations as `read-only`, which can bypass HITL when `tool_annotations` is in effect.
- Confusing Lightspeed HITL with Keycloak or MCP Gateway authorization policy.

**When not to use:** Do not treat HITL as a replacement for RBAC, network policy, or gateway tool filtering. Do not disable approvals (`never`) when write tools are enabled in production. For IDE agents talking to **OCP MCP server**, implement approval in the MCP **client**/gateway — Lightspeed HITL will not protect those paths.

**Requirements:**
- OpenShift Lightspeed Operator installed and an `OLSConfig` custom resource (`cluster`) configured so the Lightspeed Service is deployed.
- Cluster interaction / Observability MCP available for tool-backed cluster changes (`introspectionEnabled` defaults to `true`); cluster interaction is Technology Preview.
- LLM provider with tool calling enabled (required to activate cluster interaction in Lightspeed).
- Configure `toolsApprovalConfig` in the `OLSConfig` CR as needed (`approvalType` default `tool_annotations`; `approvalTimeout` minimum `1`, default `600`).
- For custom MCP servers: enable the `MCPServer` feature gate and MCP server entries in `OLSConfig`; omit `read-only` annotations on sensitive operations if HITL should apply.

---

### MCP Tool Registry
**Details:** [AI/ML artifact types (`MCP_TOOL`)](https://docs.redhat.com/en/documentation/red_hat_build_of_apicurio_registry/3.2/html/apicurio_registry_user_guide/registry-artifact-reference_registry#registry-ai-ml-artifact-types_registry)
**How to use:** [MCP tool discovery (well-known endpoints)](https://docs.redhat.com/en/documentation/red_hat_build_of_apicurio_registry/3.2/html/apicurio_registry_user_guide/agent-discovery-patterns_registry)

Built-in `MCP_TOOL` artifact type in Red Hat build of Apicurio Registry 3.2 for versioning Model Context Protocol tool definitions—name, description, and input/output schemas—as first-class registry content (`application/json`, MCP schema version `2025-11-25`). The registry validates definitions against the MCP specification, tracks evolution with version history and compatibility checking, and (when MCP tools support is enabled) exposes discovery via `/.well-known/mcp-tools` so agent tool catalogs can search by name or input parameter. Release notes list AI/LLM artifact types and MCP tool features as Technology Preview; the agent discovery chapter marks well-known MCP tool discovery as Developer Preview.

**When to use:** When you need a governed, searchable catalog of MCP tool *definitions*—central storage, schema validation, and well-known discovery for shared agent tool catalogs—rather than scattering tool schemas in app config or relying on live MCP servers alone for catalog/governance.

**Common confusion:**
- Mixing this up with **running** MCP servers — this stores and discovers tool *definitions*, not the execution plane.
- Confusing it with **A2A Agent Registry** / `AGENT_CARD` — that is agent capability discovery, not MCP tool schemas.
- Treating it as Lightspeed/RHDH MCP integrations or runtime tool filtering — those are separate runtime paths.

**When not to use:** Do not use MCP Tool Registry when you need tools to execute against a live system — deploy/register an actual **MCP server** (and optionally **MCP Gateway**). Do not use it for agent capability discovery (skills/interfaces) — that is **A2A Agent Registry** / `AGENT_CARD`. Do not use it as Lightspeed’s runtime tool filter — that is **Query-based Tool Filtering**.

**Requirements:**
- Red Hat build of Apicurio Registry 3.2 installed and running.
- Register artifacts as type `MCP_TOOL` with content type `application/json`.
- For well-known discovery (`/.well-known/mcp-tools`, `/.well-known/mcp-tools/{groupId}/{artifactId}`): set `apicurio.mcp-tools.enabled=true` (default `false`; docs label this experimental); endpoints require read-level authorization.
- Treat AI/LLM features including `MCP_TOOL` as Technology Preview per Apicurio Registry 3.2 release notes; well-known MCP tool discovery in the agent discovery guide is Developer Preview — not supported for production or business-critical workloads.

---

### MCP server for OpenShift Container Platform
**Details:** [MCP server overview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/ai_applications/mcp-server#ai-app-mcp-server-mcp-server-overview_mcp-server-overview)
**How to use:** [Install MCP server for Red Hat OpenShift Container Platform](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/ai_applications/mcp-server#ai-mcp-server-install_mcp-server-overview)

Technology Preview Helm-deployed Model Context Protocol (MCP) server that turns OpenShift/Kubernetes inspection and management into MCP tools and resources so AI hosts (Claude Code, Cursor, VS Code, OpenShift Lightspeed, and similar) can diagnose and act on live cluster state. Unlike an MCP gateway—which routes and governs traffic—this server is where tool logic runs (list pods, fetch logs, manage resources, optional toolsets such as metrics or Helm). It respects Kubernetes RBAC, supports `read_only` / tool allowlists, and can sit behind Connectivity Link’s MCP gateway for OAuth and tool-level authorization.

**When to use:** Use it when you want MCP-compatible assistants to troubleshoot or operate an OpenShift cluster in natural language—querying state, events, and logs, and optionally performing controlled actions—with rules you define (RBAC, denied resources, HITL in the client). Prefer it for agentic cluster ops and, where configured, multicluster access patterns described in Red Hat’s Technology Preview guidance, not as a general-purpose chat UI.

**Common confusion:**
- Confusing it with Lightspeed’s **Observability MCP** (operator-installed for OLS chat).
- Confusing the MCP acronym with classic **MachineConfigPool (MCP)** objects.
- Assuming built-in PII redaction or HITL — docs recommend HITL in the client, TrustyAI for redaction, and a gateway for governance; the server itself has no internal PII redaction.

**When not to use:** Do not use it as the OpenShift console chat assistant — that is **OpenShift Lightspeed**. Do not use it when you only need Apicurio or RHDH portal tools. Avoid production without `read_only`/tool allowlists, OAuth/gateway controls, and human approval for writes. Do not confuse CRD name “MCP” with MachineConfigPools.

**Requirements:**
- Technology Preview only — not supported with Red Hat production SLAs; Red Hat does not recommend production use.
- OpenShift Container Platform with admin access to install; deploy via the `redhat-openshift-mcp-server` Helm chart (`openshift-helm-charts`, typically namespace `openshift-mcp-server`) with an Ingress/route hostname.
- An MCP-compatible client (docs cite Claude Code, VS Code, Cursor, or OpenShift Lightspeed).
- For the documented enterprise path: MCP gateway (Connectivity Link), RBAC configuration, optional CR denial (`denied_resources`), and OAuth-based gateway authentication/authorization; docs recommend `read_only` (or carefully scoped toolsets) and human approval for write actions.
- Toolsets such as `core` and `config` are Technology Preview by default; others (for example `kubevirt`, `tekton`) may be Developer Preview per the install docs.

---

### Query-based Tool Filtering
**Details:** [About query-based tool filtering](https://docs.redhat.com/en/documentation/red_hat_openshift_lightspeed/1.0/html/configure/ols-configuring-openshift-lightspeed#ols-about-query-based-tools-filtering_ols-configuring-openshift-lightspeed)
**How to use:** [Enabling query-based tool filtering](https://docs.redhat.com/en/documentation/red_hat_openshift_lightspeed/1.0/html/configure/ols-configuring-openshift-lightspeed#ols-enabling-query-based-tool-filtering_ols-configuring-openshift-lightspeed)

OpenShift Lightspeed capability that uses a hybrid retrieval-augmented generation (RAG) system—balancing semantic search and keyword matching—to select a small, relevant subset of MCP tools for each user request before the LLM sees them. When an application has access to hundreds of tools, sending the full list in one prompt slows performance and raises token costs; this pre-processing step retrieves the best candidates in milliseconds so the model reasons over a lean, high-quality tool set instead of a massive library. Enable it with the `ToolFiltering` feature gate on the cluster `OLSConfig` and tune behavior via `toolFilteringConfig` (`alpha`, `topK`, `threshold`) and optional `maxIterations`.

**When to use:** When OpenShift Lightspeed (or another LLM app on the cluster) exposes a large MCP tool catalog and you need to cut token use, avoid tool-selection interference, and keep execution accuracy high by presenting only the most relevant tools per query—especially once tool counts grow into the hundreds.

**Common confusion:**
- Treating it as a security control (authorization/allowlist) rather than a relevance and performance optimization.
- Mis-tuning `threshold` / `topK` so needed tools are dropped or too many tools still reach the LLM.

**When not to use:** Do not use it as a substitute for RBAC, MCP Gateway authz, or HITL — it does not grant/deny permissions. Skip enabling it when the tool set is already small. For hard deny of tools, use gateway policies / server `enabled_tools` / Lightspeed approval config instead.

**Requirements:**
- OpenShift Lightspeed Operator installed.
- An LLM provider available for use with the OpenShift Lightspeed Service.
- Permission to create or edit the cluster-scoped `OLSConfig` CR (`cluster-admin`, or equivalent).
- `ToolFiltering` listed under `spec.featureGates` on the `OLSConfig` named `cluster` (optionally configure `spec.olsConfig.toolFilteringConfig` with `alpha` 0–1, `topK`, and `threshold` 0.01–0.1; defaults apply if omitted).

---

### Camel Docling
**Details:** [Chapter 35. Docling](https://docs.redhat.com/en/documentation/red_hat_build_of_apache_camel/4.18/html/red_hat_build_of_apache_camel_for_spring_boot_reference/csb-camel-docling-component-starter)
**How to use:** [Basic document conversion to Markdown](https://docs.redhat.com/en/documentation/red_hat_build_of_apache_camel/4.18/html/red_hat_build_of_apache_camel_for_spring_boot_reference/csb-camel-docling-component-starter#basic_document_conversion_to_markdown)

Camel Docling (`camel-docling`) is a producer-only component in Red Hat build of Apache Camel for Spring Boot that converts and processes documents with IBM’s Docling AI document parser inside Camel routes. It turns PDF, Word, PowerPoint, and related formats into Markdown, HTML, JSON, or plain text, and can extract structured data and metadata. It runs either by invoking a local Docling CLI install or by calling a running `docling-serve` API (including async and batch operations in API mode).

**When to use:** Use it when you need document conversion or structured extraction as a step in Camel/Java integration routes—for example preparing PDF/DOCX/PPTX content as Markdown before embedding or RAG with Camel’s vector-store and OpenAI components, as highlighted for Red Hat build of Apache Camel 4.18 AI semantic-processing pipelines.

**Common confusion:**
- Treating it as a complete RAG ingestion platform, embedding service, or drop-in Docling server.
- Overlooking that it is an integration producer that still needs Docling installed or a running `docling-serve`.
- Expecting it to store vectors or call LLMs by itself.

**When not to use:** Skip if you are not building Camel/Java integration routes — call Docling directly from Python/notebooks. For a managed OpenShift AI RAG pipeline (chunk → embed → vector store → retrieve), prefer **RAG Stack** / **Llama Stack** rather than assembling Docling alone. Do not expect consumer/`from("docling:...")` semantics; only producer is supported.

**Requirements:**
- Red Hat build of Apache Camel for Spring Boot with the `camel-docling-starter` Maven dependency (`org.apache.camel.springboot:camel-docling-starter`).
- Only producer is supported (`to("docling:...")`); no consumer endpoint.
- CLI mode (default): Docling installed on the system (`pip install docling`).
- API mode: a running `docling-serve` instance (`pip install docling-serve` and run the server, or Docker image `ghcr.io/docling-project/docling-serve`), with `useDoclingServe=true` and `doclingServeUrl` pointing at the service.

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

Automated search over model algorithms and configurations for **structured prediction** from **CSV** training data — binary/multiclass classification, regression, and time-series forecasting. Produces a leaderboard and notebooks via AutoGluon-backed pipelines. Technology Preview limits include CSV-only input, size caps, no custom algorithm/hyperparameter configuration, and runs that cannot be edited after creation.

**When to use:** When you want to quickly find the best-performing model and hyperparameters for a structured data problem without manually tuning.

**Common confusion:**
- Expecting AutoML to train or fine-tune LLMs / deep generative models (supported tasks are tabular/time-series only).
- Expecting free-form algorithm or hyperparameter control (not available in Tech Preview).
- Ignoring CSV-only and dataset size constraints.
- Confusing AutoML with Optuna/Ray Tune-style search over arbitrary deep-learning training loops.

**When not to use:** Do not use AutoML for LLM training/fine-tuning — use **Distributed Workloads** / training operators and gen-AI workflows instead. Do not use it when you need full control of the search space or non-CSV modalities. For a single already-chosen sklearn model, skip AutoML and train/serve directly (**workbenches** + **MLServer**/**OVMS**).

**Requirements:**
- Distributed Workloads components must be installed (Kueue, Ray and/or Training Operator).
- Workbenches component must be enabled.

---

## Evaluation & Safety

### LM Evaluation (LMEval)
**Details:** [Overview of evaluating AI systems](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/evaluating_ai_systems/overview-evaluating-ai-systems_evaluate)
**How to use:** [Evaluating LLMs with LM-Eval](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/evaluating_ai_systems/evaluating-llms-with-lm-eval_evaluate)

Batch / job-based evaluation of **generative language models** against standardized (and custom) lm-evaluation-harness-style tasks — accuracy, reasoning, toxicity, Q&A, and similar — via `LMEvalJob`, under the TrustyAI operator. Focuses on **output quality** of the language model itself, not retrieval quality of a RAG pipeline.

**When to use:** When you need to evaluate and compare LLM performance before deploying to production — measuring accuracy, reasoning ability, and task-specific metrics across model versions.

**Common confusion:**
- Using LMEval to score RAG pipelines (retrieval quality, faithfulness to context) — that is **RAGAS**.
- Treating LMEval as continuous production drift/bias monitoring — that is **Model Monitoring (TrustyAI)** on tabular/OVMS models.
- Assuming chat-completions APIs support all harness tasks (many multiple-choice tasks need completions/loglikelihood-capable wiring).
- Confusing Technology Preview dashboard UX with a fully supported production control plane.

**When not to use:** Do not use LMEval as your primary tool for RAG retrieval/grounding metrics — use **RAGAS**. Do not use it for tabular fairness/drift on predictive models — use **Model Monitoring (TrustyAI)**. For interactive prompt exploration use the **Gen AI Playground**, then LMEval for systematic scoring.

**Requirements:**
- Set `trustyai` component to `Managed` in the `DataScienceCluster`.
- A deployed LLM model in your project.
- For online evaluations or remote code execution: set `permitOnline` and `permitCodeExecution` to `allow` in the `DataScienceCluster`, and set `allowOnline`/`allowCodeExecution` to `true` in the `LMEvalJob` CR.
- For offline evaluations from S3: access to an S3-compatible storage bucket containing the model and datasets.

### Guardrails (NeMo Guardrails)
**Details:** [Enabling AI safety with NeMo Guardrails](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/enabling_ai_safety_with_guardrails/enabling-ai-safety-with-nemo-guardrails_nemo-guardrails)
**How to use:** [Deploying the NeMo Guardrails service with an LLM](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/enabling_ai_safety_with_guardrails/enabling-ai-safety-with-nemo-guardrails_nemo-guardrails#deploying-the-nemo-guardrails-service-with-an-llm_nemo-guardrails)

Runtime **input/output safety and policy controls** for LLM applications: sensitive-data detection, regex/content filters, topic and custom rails. Exposes guarded check and/or guarded chat endpoints, managed by the TrustyAI operator. No separate NVIDIA subscription is required on OpenShift AI. This is **request-time filtering/orchestration**, not offline model benchmarking.

**When to use:** When LLM responses must comply with safety, regulatory, or content policies — such as blocking sensitive data leakage, enforcing topic boundaries, or filtering toxic content.

**Common confusion:**
- Treating Guardrails as model-quality evaluation (MMLU-style or RAG faithfulness) rather than live request filtering.
- Expecting 100% safety from LLM self-check rails alone (docs recommend layering with other defenses).
- Applying NeMo Guardrails to non-LLM / classical ML inference paths.
- Assuming Guardrails replaces offline **LMEval** or **RAGAS** scoring.

**When not to use:** Do not use Guardrails as a substitute for systematic LLM or RAG evaluation — use **LMEval** / **RAGAS**. Do not use it for tabular predictive-model serving safety. Do not rely on self-check rails alone for compliance-critical guarantees; combine with deterministic detectors and application-level validation. For exploratory prompt testing without a policy plane, use the **Gen AI Playground**.

**Requirements:**
- Set `trustyai` component to `Managed` in the `DataScienceCluster`.
- KServe configured to use RawDeployment mode (`spec.kserve.rawDeploymentServiceConfig` set to `Headed`).
- A deployed LLM model on the model-serving platform.
- No external NVIDIA subscription required — NeMo Guardrails is included with OpenShift AI.

### RAGAS Evaluation Provider
**Docs:** [Overview of evaluating AI systems](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/evaluating_ai_systems/overview-evaluating-ai-systems_evaluate)

Objective metrics for **RAG systems**: retrieval quality (for example context precision/recall), answer relevance, and factual consistency/faithfulness to retrieved context. Integrates via TrustyAI / Llama Stack evaluation provider modes (inline vs remote/pipeline). It **measures** RAG configuration quality to drive iteration (chunking, embeddings, retrieval) — it does not replace the RAG stack or enforce policies at request time.

**When to use:** When you need quantitative assessment of your RAG pipeline's quality — checking whether retrieved documents are relevant, answers are grounded in context, and responses are factually consistent.

**Common confusion:**
- Using RAGAS to benchmark a standalone LLM on general harness tasks (MMLU, GSM8K, etc.) — that is **LMEval**.
- Equating faithfulness/groundedness scores with runtime content policy enforcement (**Guardrails**).
- Expecting RAGAS alone to fix retrieval rather than measure it.
- Ignoring Technology Preview / production-SLA caveats on the Ragas integration.

**When not to use:** Do not use RAGAS for non-RAG LLM capability benchmarks — use **LMEval**. Do not use it as live request filtering — use **Guardrails**. Do not use it for tabular drift/bias — use **Model Monitoring (TrustyAI)**.

**Requirements:**
- Set `trustyai` component to `Managed` in the `DataScienceCluster`.
- A deployed RAG pipeline with accessible inference and retrieval endpoints.

---

### EvalHub
**Details:** [Understanding EvalHub](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/evaluating_ai_systems/evaluating-llms-with-evalhub_evaluate#evalhub-overview_evaluate)
**How to use:** [Submit an evaluation job](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/evaluating_ai_systems/evaluating-llms-with-evalhub_evaluate#evalhub-submit-an-evaluation-job_evaluate)

Evaluation orchestration service for **LLMs** on OpenShift AI (via the TrustyAI Operator): a versioned REST API, Python SDK, and `evalhub` CLI submit jobs that fan out to provider adapters such as lm-evaluation-harness, Garak, GuideLLM, and LightEval. Each benchmark runs as an isolated Kubernetes Job with optional MLflow experiment tracking, reusable collections, and multi-tenant scoping across namespaces.

**When to use:** When you need a single control plane to run and compare multi-framework LLM capability, safety, and performance benchmarks—especially reusable collections, parallel provider jobs, MLflow lineage, and the same API/SDK/CLI path from notebooks through CI—rather than stitching separate harness runs by hand.

**Common confusion:**
- Treating EvalHub as continuous production drift/bias monitoring — that is **Model Monitoring (TrustyAI)**.
- Using it as RAG retrieval/groundedness scoring — that is **RAGAS**.
- Treating it as request-time content/PII/topic filtering — that is **Guardrails**.
- Conflating it with running a single framework (for example LM-Eval via the **LM Evaluation (LMEval)** CRD) without the hub’s multi-provider job API, collections, and SDK/CLI.

**When not to use:** Do not use EvalHub for tabular fairness/drift on predictive models — use **Model Monitoring (TrustyAI)** with OVMS. Do not use it as the primary RAG groundedness/retrieval metric suite — use **RAGAS**. Do not use it as live content/PII/topic controls — use **Guardrails**. For a single LM-Eval-only job path already covered by TrustyAI’s **LM Evaluation (LMEval)** CRD, prefer that simpler path unless you need multi-provider orchestration, collections, or the EvalHub API.

**Requirements:**
- Set the `trustyai` component to `Managed` in the OpenShift AI `DataScienceCluster`.
- Configure KServe to use `RawDeployment` mode.
- Cluster administrator privileges and OpenShift CLI (`oc`) version 4.12 or later to deploy EvalHub.
- A PostgreSQL database and a Secret with a `db-url` connection URI for the EvalHub custom resource.
- A model endpoint accessible from within the cluster (most providers expect an OpenAI-compatible inference URL).
- Optional: set `MLFLOW_TRACKING_URI` (or equivalent MLflow config) to log evaluation results to MLflow.

---

### Automated Risk Assessment
**Details:** [Automated risk assessment overview](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/evaluating_ai_systems/test-model-safety-with-automated-risk-assessment_evaluate#automated-risk-assessment-overview_evaluate)
**How to use:** [Run a risk assessment](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/evaluating_ai_systems/test-model-safety-with-automated-risk-assessment_evaluate#run-a-risk-assessment_evaluate)

Technology Preview feature in Red Hat OpenShift AI for pre-production adversarial safety probing of a model (or model-plus-guardrails) inference endpoint. It generates diverse prompts across harmful-content categories, then applies escalating attack strategies (baseline, system-prompt override variants, translation, TAP) and reports where safety controls can be bypassed—run via the EvalHub evaluations API or directly with Kubeflow Pipelines.

**When to use:** Before promoting a model (or guarded stack) to production when you need to identify safety vulnerabilities and which attack techniques succeed against your endpoint’s controls, including optional custom harm categories for domain policies.

**Common confusion:**
- Using it as continuous production monitoring
- Equating it with capability benchmarks (MMLU-style EvalHub/LMEval)
- Treating it as runtime Guardrails enforcement
- Assuming it only tests the base model and not the guarded stack

**When not to use:** Do not use Automated Risk Assessment as live request filtering — use **Guardrails**. Do not use it for general LLM capability/quality leaderboards — use **EvalHub** / **LMEval**. Skip translation-heavy strategies on disconnected clusters unless translation models are pre-staged (or disable that strategy). Prefer it before production promotion when you must stress-test safety bypasses; it is not a substitute for ongoing monitoring or content rails.

**Requirements:**
- Technology Preview only (not supported under Red Hat production SLAs; not recommended for production use).
- A configured pipeline server (Data Science / AI Pipelines).
- Target and judge model inference endpoints compatible with the OpenAI `/v1` API; a Kubernetes secret containing the model API key.
- S3-compatible storage for pipeline artifacts.
- For EvalHub-triggered runs: an EvalHub authentication token (KFP Python SDK path does not require EvalHub).
- On disconnected clusters: pre-download Helsinki-NLP translation models to S3 (`hf_cache_path`) or disable the translation strategy.

---

## Monitoring & Observability

### Model Monitoring (TrustyAI)
**Details:** [Overview of monitoring your AI systems](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/monitoring_your_ai_systems/overview-of-monitoring-your-ai-systems_monitor)
**How to use:** [Setting up TrustyAI for your project](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/monitoring_your_ai_systems/setting-up-trustyai-for-your-project_monitor)

Production monitoring of **tabular** model predictions for **bias** (fairness metrics over protected attributes and outcomes) and **data drift** (statistical shift between training reference data and live inference inputs), via a per-project TrustyAI service with configurable metrics, thresholds, and dashboards. This catalog entry is the **drift/bias monitoring service** — not the whole TrustyAI operator umbrella (which also hosts LMEval, Guardrails, RAGAS, and related tools). Monitoring only supports models served with **OpenVINO Model Server (OVMS)**; bias/drift metrics cannot be used with non-tabular models including LLMs, and installing `TrustyAIService` in a namespace with non-tabular models can error the service.

**When to use:** When tabular models are in production on OVMS and you need to detect data drift or fairness issues before they impact business outcomes. Critical for regulated industries.

**Common confusion:**
- Equating “TrustyAI” (the operator umbrella) with this drift/bias monitoring service alone.
- Expecting drift/bias metrics on LLMs or other non-tabular deployments.
- Expecting monitoring of models on non-OVMS runtimes (for example vLLM).
- Using it as a substitute for LLM benchmarks, RAG quality scoring, or input/output safety filtering.

**When not to use:** Do not use Model Monitoring (TrustyAI drift/bias) for generative / non-tabular models, or for models not served with OVMS. For LLM capability/toxicity-style checks use **LM Evaluation (LMEval)**; for RAG groundedness/retrieval quality use **RAGAS**; for runtime content/PII/topic controls use **Guardrails (NeMo Guardrails)**. Prefer **OVMS** when you need this monitoring on tabular models.

**Requirements:**
- Set `trustyai` component to `Managed` in the `DataScienceCluster`.
- A TrustyAI service instance must be installed in each project containing models to monitor.
- Model serving platform must be enabled.
- Models to monitor must be served with OpenVINO Model Server (OVMS).
- Optional: for database-backed storage instead of PVC, configure a MySQL or MariaDB 10.5+ database secret before deploying TrustyAI.
- For KServe RawDeployment mode: update the `inferenceservice-config` ConfigMap and create a CA certificate ConfigMap in the model's namespace.

### Gen AI Playground
**Details:** [Playground overview](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/experimenting_with_models_in_the_gen_ai_playground/playground-overview_rhoai-user)
**How to use:** [Configure a playground for your project](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/experimenting_with_models_in_the_gen_ai_playground/configuring-a-playground-for-your-project_rhoai-user)

Interactive **dashboard experimentation** with deployed (and external) generative models **before** application integration: prompt and parameter tuning, optional RAG knowledge sources, MCP tools, side-by-side comparison, and export of a Python starter template. Technology Preview — Red Hat does not recommend production use. Chat history and parameter settings are not preserved across refresh/session end (saved prompts via the Prompt tab → MLflow are the persistence path). Qualitative try-out is not the same as harness/RAGAS metrics.

**When to use:** When you want to quickly test and compare deployed generative models with different prompts and parameters before integrating them into applications — useful for prompt engineering and model selection.

**Common confusion:**
- Treating the playground as a production chat application or multi-user service.
- Expecting durable chat/session state across refresh.
- Using playground clicks as a substitute for reproducible **LMEval** / **RAGAS** jobs or **Guardrails** policy enforcement.
- Confusing playground “evaluate” (qualitative try-out) with harness/RAGAS metrics.

**When not to use:** Do not deploy the playground as the production user-facing LLM UI — build an application against served endpoints (**vLLM**/KServe, optionally **Guardrails**). Do not rely on it for regression gates — use **LMEval** / **RAGAS**. Use it for prompt/model selection experiments, then export and harden elsewhere.

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

Feast-based **centralized feature definitions** with offline (training/batch) and online (low-latency serving) paths so the **same feature logic** is reused across training and inference. Reduces training–serving skew and lets teams share feature tables across projects. Integrated with workbenches. This is for ML feature tables/time-series features — not a vector database or RAG document store. You still own offline/online stores and materialization pipelines; live distributional drift alerts remain **Model Monitoring (TrustyAI)**.

**When to use:** When multiple models or teams share computed features and you need to ensure consistency between training-time and serving-time feature values, or when you want low-latency online feature serving without redundant feature engineering.

**Common confusion:**
- Adopting a feature store for a single-model, single-team, batch-only scoring job where one warehouse query already defines train and score features.
- Treating Feature Store as a vector database / RAG document store.
- Expecting Feature Store to replace drift monitoring.
- Assuming features appear without owning stores and materialization.

**When not to use:** Skip Feature Store when features are request-scoped only, unused across models/teams, and batch scoring already shares one definition — keep transforms in shared libraries or SQL. Do not use it as a substitute for RAG vector storage.

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

Tags describe what kind of solution a component is suited for. A component may carry more than one tag. Each tag must apply to at least two components in this catalog. Tags are not yet assigned to individual components in this document.

| Tag | Meaning |
|-----|---------|
| `predictive-ml` | Classical supervised or unsupervised machine learning — classification, regression, ranking, clustering, and similar structured-data problems. |
| `generative-ai` | Large language models and other generative models for text, code, or multimodal generation. |
| `nlp` | Natural language processing beyond chat alone — understanding, summarization, translation, NER, document conversion, and related language tasks. |
| `rag` | Retrieval-augmented generation: indexing, retrieval, grounding answers in external or private knowledge. |
| `semantic-search` | Embedding documents and retrieving similar content by vector similarity, with or without generative answering. |
| `embeddings` | Generating vector representations of text or other modalities for similarity search, clustering, and retrieval. |
| `agentic-ai` | Multi-step agents that plan, use tools, and orchestrate actions across systems. |
| `tool-integration` | Exposing, federating, authorizing, selecting, and invoking external tools (including MCP and inference-time tool calling) for LLM and agent consumption. |
| `multi-agent` | Discovery, identity, and collaboration among multiple agents (for example A2A Agent Cards and agent-to-agent workflows). |
| `agent-runtime` | Isolated, long-lived platforms for hosting agent workloads—sandboxes, sidecars, identity, and declarative agent lifecycle. |
| `mlops` | Model lifecycle management — versioning, promotion, registries, catalogs, feature stores, and governed handoff between stages. |
| `model-discovery` | Finding, browsing, and selecting pre-validated or cataloged models that are ready to evaluate and deploy. |
| `llm-artifacts` | Governed, versioned registries for prompts, tool definitions, agent cards, and related LLM configuration artifacts. |
| `data-prep` | Data preparation at scale — ETL, document ingestion/extraction, feature engineering, and distributed processing ahead of training or inference. |
| `document-ingestion` | Converting unstructured documents (PDF, Office, and similar) into text or structured forms for indexing, RAG, or downstream AI pipelines. |
| `training` | Model training and fine-tuning, including distributed training, adapter-based customization, and automated model search. |
| `serving` | Production inference — online or batch serving of models with scaling, routing, and operational controls, including governed access to external model APIs. |
| `distributed-compute` | Spreading training, inference, or data processing across multiple nodes when a single machine is not enough. |
| `distributed-inference` | Scaling inference horizontally across nodes when single-server capacity or latency SLOs are insufficient. |
| `model-routing` | Traffic management across model versions or replicas — canary rollouts, A/B testing, and cache-aware or inference-aware request routing. |
| `inference-optimization` | Shrinking models or speeding up serving via quantization, sparsity, speculative decoding, or inference-aware scheduling. |
| `model-packaging` | Packaging and distributing model weights as OCI/container artifacts for registry-based storage, caching, and serving. |
| `evaluation` | Measuring model or pipeline quality, safety, benchmarks, regression, and production drift/bias across versions. |
| `safety` | Runtime filtering, adversarial probing, and policy controls for model inputs/outputs and guarded stacks. |
| `governance` | Quotas, RBAC, audit, human approval gates, tool authorization, approved sources, and controlled access to AI capabilities. |
| `workflow-orchestration` | Automating repeatable multi-step ML or RAG workflows with DAG scheduling, parameterization, and artifact lineage. |
| `experiment-tracking` | Recording and comparing training, tuning, or evaluation runs — parameters, metrics, and artifacts — across experiments and teams. |
| `interactive-development` | Browser-based notebook, IDE, or playground environments for iterative prototyping and hands-on experimentation. |
| `hardware-acceleration` | GPU and specialized accelerator enablement for compute-intensive workloads across supported hardware vendors. |
| `platform` | Shared infrastructure and enablers that support other solution types rather than embodying one solution themselves. |
