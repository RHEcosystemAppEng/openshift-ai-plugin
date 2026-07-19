# Detection Signals

What to search for when scanning a project. Each category lists **capability** markers (cross-product / DIY patterns) plus a few **RHOAI:** markers that indicate the OpenShift AI / ODH product is already present. Sign Implementation as `openshift-ai` (or `openshift` when only platform CRs without ODH) when RHOAI markers match; otherwise `generic`. Map categories to OpenShift AI components later via `signal-component-map.md`.

## Model artifacts

`.pt`, `.pth`, `.onnx`, `.pb`, `.h5`, `.safetensors`, `.pkl`, `.joblib`, `.bst`, `model.onnx`, `saved_model/`, `config.json` + `tokenizer.json` next to weights. Supporting: `s3://` / `pvc://` / `hf://` / `oci://` / `https://` storage URIs, boto3/`s3fs`/`snapshot_download` model pulls. RHOAI: `model-registry://` storageUri; `/opt/app-root` workbench model mounts.

---

## Custom model serving endpoints

Flask/FastAPI/Django `/predict` + `model.predict(`, custom `/health`/`/ready`, manual batching; DIY `Deployment`+`Service`+`HPA` around a loaded model. Manifests: `InferenceService`, `ServingRuntime`, `ClusterServingRuntime`, `serving.kserve.io/v1beta1`; `from kserve import Model, ModelServer`; `/v1/models/<name>:predict`, `/v2/models/<name>/infer`; `storageUri`, `modelFormat.name`. Scale-to-zero / Knative `autoscaling.knative.dev/*` / `minReplicas`/`maxReplicas` on InferenceService fold here (Serverless mode). RHOAI: DSC `kserve: Managed`; `serving.knative.openshift.io/enablePassthrough`.

## vLLM / generative LLM serving

`import vllm`, `from vllm import LLM`, `SamplingParams`, `AsyncLLMEngine`; `vllm serve`, `python -m vllm.entrypoints.openai.api_server`; images `vllm/vllm-openai`; flags `--gpu-memory-utilization`, `--tensor-parallel-size`, `--max-model-len`, `--enable-prefix-caching`; metrics `vllm:gpu_cache_usage_perc`. DIY: `AutoModelForCausalLM`, `pipeline("text-generation")`, manual `torch.cuda` / `device_map="auto"`; TGI/SGLang/Ollama as generative HTTP APIs. OpenAI `/v1/chat/completions` against self-hosted host. RHOAI: `quay.io/modh/vllm`; ServingRuntime display `vLLM … ServingRuntime for KServe`; `modelFormat.name: vLLM`.

## Distributed / disaggregated LLM inference

`kind: LLMInferenceService` (`serving.kserve.io`); `oc get llmisvc`; `spec.router.{route,gateway,scheduler}`; charts/images `llm-d-router-*`, `llm-d-kv-cache*`, `NixlConnector`/NIXL, `--kv-events-config`, separate prefill/decode Deployments; `LeaderWorkerSet`; custom sticky/prefix-hash LB across GPU replicas; NVIDIA Dynamo P/D as same-need signal. Labels `llm-d.ai/inferenceServing=true`. RHOAI: Gateway `openshift-ai-inference`; Connectivity Link + Leader Worker Set on OCP.

## External LLM API gateways

`openai` / `AzureOpenAI` / `anthropic` / `google-genai` / `boto3.client("bedrock-runtime")`; LiteLLM Proxy / Portkey / OpenRouter; LangChain `ChatOpenAI`/`ChatAnthropic`/`ChatBedrock` aimed at **cloud** hosts; scattered `OPENAI_API_KEY` / `.env` keys; per-team rate-limit/retry/`base_url` wrappers. RHOAI: `MaaSSubscription`/`ExternalModel` (`maas.opendatahub.io`); ns `models-as-a-service`.

## Caikit + TGIS text generation

Packages `caikit`, `caikit-nlp`, `caikit-tgis-backend`; `import caikit_nlp`; `python -m caikit.runtime`; `/api/v1/task/text-generation` (+streaming); ServingRuntime `caikit-tgis-runtime`, `supportedModelFormats: caikit`; `text-generation-launcher`; dirs `*-caikit` with `module_id`. RHOAI: `quay.io/opendatahub/caikit-tgis-serving`; display **Caikit TGIS ServingRuntime for KServe**.

## OpenVINO Model Server

`openvino` / `optimum-intel` / `OVModelFor*`; IR `*.xml`+`*.bin`; `ovms` / OpenVINO Model Server images (`openvino/model_server`); gRPC `:9000` / REST predict; `mo.py`/`ovc` / `optimum-cli export openvino`; DIY FastAPI wrapping OpenVINO Runtime. RHOAI: `runtime: kserve-ovms`; `quay.io/modh/openvino_model_server`.

## NVIDIA Triton

`config.pbtxt`, `--model-repository=`, `platform: "tensorrt_plan"|"onnxruntime_onnx"|"pytorch_libtorch"|"ensemble"`; `nvcr.io/nvidia/tritonserver`; `import triton_python_backend_utils`; `tritonclient`; KServe `spec.predictor.triton` / `modelFormat.name: triton`; DIY multi-model TensorRT/ONNX chains. RHOAI: ServingRuntime `triton-kserve-rest` / display-name Triton.

## MLServer / sklearn–XGBoost serve

`pip install mlserver` / `mlserver-sklearn` / `mlserver-xgboost`; `model-settings.json` with `mlserver_sklearn.SKLearnModel`; `mlserver start`; artifacts `model.joblib`/`model.pkl`/`model.bst`; `protocolVersion: v2`; `spec.predictor.sklearn`/`.xgboost`/`.lightgbm`; DIY `joblib`/`pickle` + `/predict`. RHOAI: `runtime: kserve-mlserver` / display **MLServer ServingRuntime for KServe**.

## LLM quantization / compression

`llmcompressor` / `from llmcompressor import oneshot`; modifiers `GPTQModifier`, `AWQModifier`, `SmoothQuantModifier`, `SparseGPTModifier`; schemes `W4A16`/`W8A8`/`FP8_DYNAMIC`; `compressed_tensors` / `quant_method: "compressed-tensors"`; DIY `auto-gptq`, `autoawq`, `BitsAndBytesConfig`. RHOAI: `registry.redhat.io/rhaii/model-opt-cuda-rhel9`.

## Inference-time tool / function calling

vLLM `--enable-auto-tool-choice`, `--tool-call-parser` (`llama3_json`/`hermes`/`mistral`/`granite`/`openai`/…), `--chat-template` + `tool_chat_template_*.jinja`; client `tools=[{type:function…}]`, `tool_choice="auto"`, `message.tool_calls`, `role:"tool"` against **local** OpenAI base URL. RHOAI: ServingRuntime additional tool-calling args / RHAIIS `tool_chat_template_*.jinja`.

## Speculative decoding

Package `speculators`; `Eagle3Speculator` / `Eagle3DraftModel`; vLLM `speculative_config` / `--speculative-config` / `--speculative-model` / `--num-speculative-tokens`; methods `eagle3`/`eagle`/`ngram`/`mtp`/`medusa`; HF `*-speculator.eagle3` / `speculators_config` in `config.json`. RHOAI: HF `RedHatAI/*-speculator.eagle3`; `registry.redhat.io/rhaii/vllm-cuda-rhel9`.

## OCI ModelCar serving

`storageUri: oci://registry…/model:tag`; KServe ModelCar sidecar mounting `/models` (or `/mnt/models`); Containerfile `ubi-micro`/`shell-capable` base + `COPY` weights + `config.json`/`tokenizer*`; `oras push` / `skopeo copy` of model artifacts; `enableModelcar` / `oci+native://`; DIY “weights as OCI image” for InferenceService. RHOAI: `quay.io/redhat-ai-services/modelcar-catalog`; `registry.redhat.io/rhelai1/modelcar-*`.

## Inference-aware gateway routing

`kind: InferencePool` (`inference.networking.k8s.io`); `endpointPickerRef`; `HTTPRoute` → InferencePool (not plain Service); `InferenceObjective`; `EndpointPickerConfig`; scorers `prefix-cache-scorer`/`kv-cache-utilization`/`queue-scorer`; Envoy ext_proc EPP; headers `x-gateway-destination-endpoint`, `x-gateway-inference-objective`. Mesh mTLS/VirtualService alone is insufficient—escalate here for KV/queue-aware picking. RHOAI: Gateway `openshift-ai-inference` / Connectivity Link Inference Gateway.

---

## Model versioning and metadata

Ad-hoc `model_v1.pt`/`best_model.pth`/`models/v1/` naming and timestamp/metric checkpoints; sidecar `model_metadata.json`/`versions.yaml`/`registry.json`; git-lfs / `dvc.yaml` as the release store; MLflow `register_model` / stage APIs / aliases `champion`/`challenger`; `ModelRegistry` client or REST `registered_models`; SageMaker / Unity Catalog / W&B model registries; promote scripts + S3 artifact URIs for versioned weights. RHOAI: DSC `modelregistry: Managed`; `kind: ModelRegistry`.

## Model sourcing / discovery

`huggingface_hub.snapshot_download` / `hf_hub_download` / `hf download`; `hf://` paths; `HF_TOKEN` / Hub cache env; hardcoded `huggingface.co/…/resolve/…` wget/curl or `git lfs clone`; model-card YAML (`pipeline_tag`, `library_name`, `base_model`); ModelScope `snapshot_download`; Hub `from_pretrained("org/name")` bootstrap; hand allowlists / “paste a repo id” onboarding; fetch scripts into cluster storage. RHOAI: Model catalog UI / “Red Hat AI models”; DSC `modelregistry: Managed`.

## Agentic runtime / multi-agent stacks

LangGraph (`StateGraph`, `create_react_agent`, `ToolNode`); CrewAI `Agent`/`Crew`/`Process`; AutoGen/AG2 `AssistantAgent`/`GroupChat`; OpenAI Agents SDK `Agent`/`Runner`; Semantic Kernel / LlamaIndex agents; DIY `while tool_calls` + `max_iterations` / custom tool maps; `responses.create` or `ChatOpenAI(base_url=…)`+`bind_tools` against self-hosted multi-turn stack; `llama-stack` / `LlamaStackClient`. RHOAI: DSC `llamastackoperator: Managed`; `kind: LlamaStackDistribution` (`llamastack.io`).

## RAG application patterns

LangChain/LlamaIndex loaders + chunkers (`RecursiveCharacterTextSplitter`); embeddings + retrievers; vector stores Chroma/FAISS/pgvector/Milvus/Qdrant/Weaviate/Pinecone; `RetrievalQA` / `create_retrieval_chain` / `VectorStoreIndex` / `as_query_engine`; Compose/Helm vector DB + embed + LLM + `/ask`|`/retrieve`|`/ingest` APIs; `SentenceTransformer` / `/v1/embeddings`; hybrid/rerank; S3/MinIO corpus staging + `ingest.py`. RHOAI: `LlamaStackDistribution` RAG providers; `rh-ai-quickstart` / `ai-architecture-charts` RAG.

## RAG hyperparameter tuning

Nested `chunk_size`/`chunk_overlap`/`top_k` sweeps; embedding-model bake-offs; dense vs hybrid A/B; Optuna/Ray Tune / LlamaIndex `ParamTuner` over RAG params; upstream `autorag` / `rag-opt`; RAGAS (or recall@k) scoring a golden QA set; `leaderboard.csv` / `compare_results.py` ranking patterns. RHOAI: pipeline `documents-rag-optimization-pipeline`; Gen AI studio AutoRAG.

---

## MCP federation / gateway

Multi-server MCP federation: `MCPGatewayExtension` / `MCPServerRegistration` / `MCPVirtualServer` (`mcp.kuadrant.io`); Envoy ext_proc router + broker; headers `X-Mcp-Virtualserver`, `x-mcp-toolname`, `mcp-session-id`; listeners `mcp`/`mcps`; DIY `mcp-proxy` fleet aggregators, `docker mcp gateway`, ContextForge, agentgateway/`MCPRoute`, or N separate MCP URLs with hand-rolled tool prefixes. RHOAI: OLM `Subscription` `mcp-gateway` (`redhat-operators`).

## A2A agent card registry

Shared A2A Agent Card catalogs: `AGENT_CARD` artifacts; Agent Card JSON `skills[]`/`capabilities`/`url`; discovery `GET /.well-known/agents` (skill/capability search) or `POST …/agents/search`; SDKs `a2a-sdk` / `@a2a-js/sdk`; JSON-RPC `message/send`/`message/stream`; hard-coded peer agent URL directories or scrapers of `/.well-known/agent-card.json`. RHOAI: `apicurio.a2a.enabled=true` / RH Apicurio A2A.

## Isolated agent code execution

Isolated agent code-exec environments: `Sandbox` / `SandboxClaim` / `SandboxWarmPool` (`agents.x-k8s.io`); `k8s-agent-sandbox` / `SandboxClient`; warm pools + hibernation/TTL; optional `runtimeClassName: gvisor|kata`; DIY StatefulSet×1+PVC, per-session `/execute` pods, or E2B/Modal/Daytona sandboxes targeted for on-cluster. RHOAI: OperatorHub “Red Hat build of Agent Sandbox”; ns `agent-sandbox-system`.

## MCP OAuth authorization server

Enterprise MCP OAuth: Protected Resource Metadata `/.well-known/oauth-protected-resource`; AS discovery + PKCE; CIMD/DCR client registration; scopes `mcp:tools`/`mcp:prompts`/`mcp:resources`; Audience/`resource` binding; MCP servers validating JWTs; DIY embedded login/token minting or long-lived API keys in IDE `mcpServers` instead of an IdP. RHOAI: OLM `rhbk-operator`; `KC_FEATURES=cimd` / `--features=cimd`.

## MCP server catalog / lifecycle

MCP server discover→deploy governance: official/Smithery/Docker catalogs + scrapers; client `mcpServers` / `mcp.json` with many hardcoded URLs; Compose/`npx`/`docker run` install paths; DIY K8s MCP Deployments; `MCPServer` (`mcp.x-k8s.io`) ContainerImage lifecycle; hand-maintained allowlists instead of a curated on-cluster catalog. RHOAI: ConfigMap `gen-ai-aa-mcp-servers` in `redhat-ods-applications`; mcp-lifecycle-operator.

## MCP tool/prompt authz policies

Tool/prompt ACL (not identity alone): CEL/OPA checks on `x-mcp-toolname`/`x-mcp-promptname`; JWT `tool:`/`prompt:` roles in `resource_access`; wristband `x-mcp-authorized` filtered `tools/list`; DIY per-server allowlists / agentgateway `mcpAuthorization` / Traefik TBAC / custom ext_proc tool RBAC. RHOAI: AuthPolicy `sectionName: mcps`; Authorino in `kuadrant-system`.

## Shared prompt templates

Shared prompt template stores: hardcoded `SYSTEM_PROMPT` / `prompt_v*_final`; git `prompts/` / `*.prompty` / LangChain `load_prompt`; Langfuse/LangSmith/MLflow/PromptLayer/Bedrock versioned prompts + release labels; Apicurio `PROMPT_TEMPLATE` with `{{variables}}` and optional render—multi-app reuse without a shared registry API. RHOAI: RH Apicurio `PROMPT_TEMPLATE` / `X-Registry-ArtifactType: PROMPT_TEMPLATE`.

## Agent workload enrollment / identity

Platform agent/tool enrollment: `AgentRuntime`/`AgentCard` (`agent.kagenti.dev`); labels `kagenti.io/type: agent|tool` + `protocol.kagenti.io/a2a|mcp`; AuthBridge/SPIFFE sidecars; DIY Envoy/oauth2-proxy/SPIRE + Keycloak client registration per Deployment; custom scrapers of `/.well-known/agent-card.json` for discovery/isolation. RHOAI: ns `kagenti-system`; `opendatahub-io`/`red-hat-data-services` agents-operator forks.

## Human-in-the-loop tool approval

Human-in-the-loop tool execution gates: LangGraph `interrupt`/`HumanInTheLoopMiddleware`; OpenAI Agents `needs_approval`/`require_approval`; CrewAI `@before_tool_call`; AutoGen/Claude/LlamaIndex/Mastra approval hooks; MCP `readOnlyHint`/`destructiveHint` client confirmations; DIY pending-action approval UIs before mutating `tools/call`. RHOAI: `OLSConfig` + `toolsApprovalConfig` / `approvalType: never|always|tool_annotations`.

## MCP tool artifact registry

Versioned MCP tool *definitions*: `MCP_TOOL` artifacts with `name`/`inputSchema`/`outputSchema`; discovery `GET /.well-known/mcp-tools`; `mcp_tool:parameter:…` labels; duplicated schemas in ConfigMaps/YAML/prompts; scrapers of live `tools/list` into static catalogs—definition governance, not live execution. RHOAI: `apicurio.mcp-tools.enabled=true`.

## OpenShift / Kubernetes MCP server

Cluster ops via MCP: `kubernetes-mcp-server` / Helm openshift charts; `--read-only`/`--toolsets`/`--disable-destructive`; `/mcp` or `/sse`; toolsets `core,config,helm,openshift`; tools `pods_list`/`pods_log`/`resources_*`/`helm_*`; DIY `kubectl_*` MCP wrappers or agents shelling `oc`/`kubectl`/`helm` instead of a native API MCP server. RHOAI: chart `redhat-openshift-mcp-server`; ns `openshift-mcp-server`.

## Query-based MCP tool filtering

Query-time MCP tool retrieval (relevance, not authZ): embed/BM25 hybrid over tool catalogs → `top_k` + threshold; LiteLLM `mcp_semantic_tool_filter`; Portkey tool-filter; dmcp/mcpfind/ToolPicker; LangChain `LLMToolSelectorMiddleware`; meta `search_tools` then load schemas—large catalogs causing token burn or wrong-tool selection. RHOAI: `OLSConfig` `featureGates: ToolFiltering` / `toolFilteringConfig`.

## Camel document conversion for RAG

Camel document conversion for RAG ingestion: Maven `camel-docling`/`camel-docling-starter`; URI `docling:CONVERT_TO_MARKDOWN`/`EXTRACT_STRUCTURED_DATA`/`BATCH_*`/`CHUNK_*`; `useDoclingServe` + docling-serve `:5001`; DIY PDFBox/Tika/poi-ooxml in Camel before embed/vector routes. RHOAI: RH Camel AI features listing `camel-docling` / CSB Docling docs.

---

## Interactive notebooks / workbenches

`*.ipynb`; JupyterLab/server configs (`.jupyter/`, `NOTEBOOK_ARGS`/`ServerApp.*`); JupyterHub/`KubeSpawner`/Z2JH `singleuser`; Docker Jupyter stacks on `:8888` (`start-notebook.py`, `JUPYTER_ENABLE_LAB`); custom notebook Deployment+Route/Ingress+PVC; IDE home mounts (`/opt/app-root/src`, `/home/jovyan`); GPU on Jupyter/code-server pods; code-server/RStudio ML workflows. RHOAI: `kind: Notebook` + `notebooks.opendatahub.io/inject-oauth`; DSC `workbenches: Managed`.

## Custom notebook / BYON images

Notebook/workbench `Dockerfile`/`Containerfile` (`FROM jupyter/*-notebook` + extras); `USER 0`→pkgs→`USER 1001`; `COPY requirements.txt`/`Pipfile.lock`; `fix-permissions /opt/app-root`; `WORKDIR /opt/app-root/src`; `start-notebook.sh|py`/`start-singleuser.sh`; baked `jupyter_*_config.py`; Hub `singleuser.image`/`KubeSpawner.image`; CI build/push of notebook tags; session `pip install` setup cells; `NB_PREFIX`/`/api` probe contract for custom IDEs. RHOAI: `FROM quay.io/modh/odh-*-notebook`; ImageStream `opendatahub.io/notebook-image: 'true'`.

## ML pipelines / workflow orchestration

Airflow DAGs / Prefect `@flow` / Luigi tasks chaining train→evaluate→deploy; Makefile/`*.sh` pipeline targets; CronJob/`retrain.sh` scheduled retrain; `from kfp import dsl`/`@dsl.pipeline`/`pipeline.yaml`/`kfp.Client`; Elyra `.pipeline`; DVC/`papermill` multi-step graduation candidates. RHOAI: DSC `aipipelines: Managed`; OpenShift AI Pipelines tab / pipeline server.

## Spark on Kubernetes

`kind: SparkApplication`/`ScheduledSparkApplication` (`sparkoperator.k8s.io`); Helm `spark-operator`; `spark-submit --master k8s://` + `spark.kubernetes.container.image`; PySpark/`SparkSession`/`spark.sql` cluster ETL/feature jobs; Airflow `SparkSubmitOperator` to k8s; cron Spark without operator schedule CR. RHOAI: DSC `kubeflowsparkoperator: Managed`.

## Multi-node / multi-GPU training infra

`torch.distributed`/DDP/FSDP; DeepSpeed ZeRO/`ds_config.json`; Horovod/`horovodrun`; `torchrun`/`WORLD_SIZE`/`NCCL_*`; Ray `TorchTrainer`/`RayCluster`/`RayJob`; Accelerate/Lightning multi-device strategies; `kind: PyTorchJob` (`kubeflow.org/v1`); Kueue `LocalQueue`/`kueue.x-k8s.io/queue-name`; SSH/Slurm/MPI/`torchrun --nnodes` DIY without CRs. RHOAI: DSC `ray`/`trainingoperator: Managed`; CodeFlare SDK.

## Fine-tuning / adapters

`peft`/`LoraConfig`/`get_peft_model`; QLoRA `load_in_4bit`/`BitsAndBytesConfig`; `adapter_config.json`/`adapter_model.safetensors`; TRL `SFTTrainer`/DPO/PPO/ORPO/GRPO + preference pairs; Unsloth `FastLanguageModel`; Axolotl/LLaMA-Factory/torchtune SFT loops; Alpaca/ShareGPT/`*-lora|sft|dpo` artifacts. RHOAI: `training_hub` / pipelines `sft_pipeline`/`osft_pipeline`.

## Tabular AutoML / HPO

`GridSearchCV`/`RandomizedSearchCV`/`Halving*SearchCV`; Optuna/`ray.tune`/`Hyperopt`/`keras_tuner`/`wandb.sweep`; AutoGluon `TabularPredictor`/`TimeSeriesPredictor`/leaderboard; FLAML/TPOT/auto-sklearn/H2O/PyCaret tabular AutoML; CSV+target multi-model bake-offs; `leaderboard.csv`/`cv_results_`. RHOAI: `autogluon-tabular-training-pipeline` / AutoML dashboard run.

---

## LLM capability benchmarks

`lm-eval`/`lm_eval`/Eleuther harness; tasks `mmlu`/`hellaswag`/`gsm8k`/`arc_*`/`leaderboard*`; `simple_evaluate`; `loglikelihood_rolling`/perplexity metrics; Unitxt `taskRecipes`/`cards.*`; CI/notebook capability bake-offs vs completions endpoints. RHOAI: `kind: LMEvalJob` (`trustyai.opendatahub.io`).

## Runtime LLM guardrails

`nemoguardrails`/`RailsConfig`/`LLMRails`; Colang rails + PII/topic/jailbreak/content-safety/regex flows; Presidio sensitive-data detect/mask; Guardrails AI validators; request-time middleware/moderation sidecars on the live inference path (not offline red-team). RHOAI: `kind: NemoGuardrails` (`trustyai.opendatahub.io`); DSC `trustyai: Managed`.

## RAG quality metrics

`from ragas import evaluate`; metrics `faithfulness`/`answer_relevancy`/`context_precision`/`context_recall`; eval rows `question`/`contexts`/`ground_truth`; TruLens/DeepEval/LangSmith RAG groundedness analogues; CI faithfulness/retrieval regression gates. RHOAI: `ENABLE_RAGAS` / `trustyai_ragas*` providers.

## Multi-provider evaluation hub

DIY glue merging lm-evaluation-harness + Garak + GuideLLM + LightEval into one gate; `eval-hub-sdk`/`evalhub` CLI; collections/weighted thresholds; `FrameworkAdapter`/BYOF; parallel multi-provider Jobs + shared model URL. RHOAI: `kind: EvalHub` (`trustyai.opendatahub.io`).

## Adversarial safety / red-team assessment

`garak` probes (`dan`/`promptinject`/…); PyRIT / Promptfoo `redteam` / DeepTeam / HarmBench / TAP/PAIR; jailbreak datasets; ASR/harm-category policy CSVs; pre-prod attacker+judge+target campaigns (not runtime rails). RHOAI: EvalHub `"provider_id":"garak-kfp"` / `"id":"intents"`.

## Tabular drift / fairness monitoring

Evidently / alibi-detect drift; AIF360/fairlearn SPD/DIR bias; custom KS/PSI exporters + Prometheus/Grafana model-quality alerts; tabular protected-attribute monitoring vs training reference (not LLM harness/rails). RHOAI: `kind: TrustyAIService`; DSC `trustyai: Managed`; `/metrics/drift/*`.

## Interactive model playground UIs

Open WebUI / LibreChat / Gradio `ChatInterface` / Streamlit `st.chat_*` / Chainlit against OpenAI-compatible/vLLM endpoints; curl-only “try the model”; side-by-side prompt/parameter sandboxes (not production chat or harness eval). RHOAI: Gen AI studio → Playground; ConfigMap `gen-ai-aa-mcp-servers`.

## Experiment tracking

`mlflow.log_*`/`mlflow.start_run`/`MLFLOW_TRACKING_URI`; TensorBoard `SummaryWriter`/`tfevents`; W&B `wandb.log`/`wandb.init`; Neptune/Comet/Aim/ClearML; CSV/JSON/`CSVLogger` manual run tables; DIY `mlflow server`+Postgres+MinIO. RHOAI: DSC `mlflowoperator: Managed`; `kind: MLflow` (`mlflow.opendatahub.io`).

## Feature store / train–serve skew

Duplicated pandas/Spark/SQL transforms across train vs serve (skew parity tests); Feast `Entity`/`FeatureView`/`feature_store.yaml`/`feast materialize`/`get_historical_features`/`get_online_features`; Tecton/Hopsworks/Databricks/Vertex/SageMaker Feature Store SDKs; DIY Redis/Dynamo feature cache + cron materialize; hand-rolled point-in-time joins without a shared registry. RHOAI: DSC `feastoperator: Managed`; `kind: FeatureStore` (`feast.dev`).

## GPU / accelerator scheduling

`nvidia.com/gpu`/`amd.com/gpu`/`habana.ai/gaudi`/`ibm.com/spyre_*` requests; manual GPU `nodeSelector`/`tolerations`/taint matrices; NFD + NVIDIA/AMD/Gaudi/Spyre GPU Operators; MIG/GFD device names; Compose/`--gpus` local GPU DIY mapped to cluster allocation (not Knative scale-to-zero alone). RHOAI: `kind: HardwareProfile` (`infrastructure.opendatahub.io`); `opendatahub.io/recommended-accelerators`.
