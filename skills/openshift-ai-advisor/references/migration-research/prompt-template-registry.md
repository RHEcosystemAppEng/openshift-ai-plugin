# Prompt Template Registry

Built-in `PROMPT_TEMPLATE` artifact type in **Red Hat build of Apicurio Registry** 3.2 that version-controls LLM prompt templates (Microsoft Prompty–aligned schema) with typed variables, validation, backward-compatibility checks, optional server-side `POST …/render`, and optional MCP prompt exposure. Peers are SaaS/self-hosted prompt registries, cloud prompt management APIs, git/Prompty stores, and hardcoded `SYSTEM_PROMPT` patterns that teams use instead of (or before) adopting RH Apicurio `PROMPT_TEMPLATE`.

## Peers

- **Hardcoded / in-code prompt strings** — `SYSTEM_PROMPT` / `system_prompt` / `PROMPT_V1` / `prompt_v2_final` constants; multi-line f-strings / Jinja; inlined `messages=[{"role":"system","content":"You are…"}]` duplicated across services
- **Git `prompts/` / YAML / Prompty stores** — `prompts/`, `prompt_templates/`, `*.prompty`, LangChain `load_prompt` / `prompt.save`; DIY `prompt-registry` / `grompt` / `promptfile` / `prompts/<id>/prompt.yaml` without a shared registry API
- **Langfuse Prompt Management** — `langfuse.create_prompt` / `get_prompt` / `update_prompt`; labels `production`/`staging`/`latest`/`canary`; self-hosted or cloud Prompt Management UI
- **LangSmith / LangChain Hub** — `client.push_prompt` / `pull_prompt`; legacy `hub.pull` / `hub.push` / `lc://` paths; `owner/prompt-name:commit_hash`
- **MLflow Prompt Registry** — `mlflow.genai.register_prompt` / `load_prompt`; MLflow UI **Prompts** tab with aliases/tags for staging/production
- **PromptLayer prompt registry** — `PromptLayer` / `pl_client.run(prompt_name=…, prompt_release_label="prod")`; release labels for deploy-without-code
- **Braintrust / LangWatch prompt registries** — SaaS prompt-as-infrastructure registries with immutable versions and env promotion
- **Amazon Bedrock Prompt Management** — `create_prompt` / `get_prompt` / `create_prompt_version`; ARNs `arn:aws:bedrock:…:prompt/…`; Flows/Agents referencing managed prompt IDs
- **ConfigMap / Secret prompt blobs** — K8s ConfigMaps/Secrets (or feature-flag env vars) holding full prompt bodies for many microservices without Apicurio lifecycle
- **Upstream / community Apicurio `PROMPT_TEMPLATE` (non-RH)** — `quay.io/apicurio/apicurio-registry` LLM artifact types outside Red Hat build (migrate *into* catalog RH path)

**Not peers (adjacent catalog jobs):** full Langfuse/LangSmith **tracing/evals** alone (LLMOps suite—pair, don’t replace); MCP Tool Registry (`MCP_TOOL`); A2A Agent Registry (`AGENT_CARD`); Model Registry / `MODEL_SCHEMA` (models, not prompts); NeMo Guardrails / safety rails; production LLM gateways; classical Avro/Protobuf schema registry only.

## Detection aliases

- Hardcoded: `SYSTEM_PROMPT`, `system_prompt`, `PROMPT_TEMPLATE` string constants; `PROMPT_V1` / `prompt_v2` / `prompt_v2_really_final`; inlined system `messages=[{"role": "system"`; comments “update prompt in three places”
- Git/Prompty: `prompts/`, `prompt_templates/`, `templates/prompts/`; `*.prompty`; LangChain `load_prompt` / `prompt.save` / `lc://prompts/`; `PromptRegistry.from_dir`, `grompt.load`, `*.prompt.yaml`, `.grompt/`; smolagents `prompts.yaml`
- Langfuse: `langfuse`, `@langfuse/client`, `LANGFUSE_PUBLIC_KEY` / `LANGFUSE_SECRET_KEY`; `create_prompt` / `get_prompt` / `update_prompt`; `get_prompt(…, label="production")`; Prompt Management UI
- LangSmith/Hub: `langsmith` `push_prompt` / `pull_prompt`; `LANGCHAIN_API_KEY` / `LANGSMITH_API_KEY`; `langchainhub` / `hub.pull` / `hub.push`; `owner/prompt-name`; smith.langchain.com
- MLflow prompts: `mlflow.genai.register_prompt` / `load_prompt`; MLflow **Prompts** tab; `{{ var }}` registered templates used as control plane
- PromptLayer: `promptlayer`, `PromptLayer`, `prompt_release_label` / `promptReleaseLabel`, `get_prompt_template`, `pl_client.run(prompt_name=`
- Braintrust/LangWatch: Braintrust / LangWatch prompt registry SDKs; “prompts as infrastructure”; immutable prompt version IDs
- Bedrock: `bedrock-agent` `create_prompt` / `get_prompt` / `create_prompt_version` / `list_prompts`; `arn:aws:bedrock:…:prompt/`
- ConfigMap DIY: ConfigMaps/Secrets with full prompt bodies; env/feature flags selecting prompt string blobs
- Upstream Apicurio: `quay.io/apicurio/apicurio-registry` + `PROMPT_TEMPLATE` / `X-Registry-ArtifactType: PROMPT_TEMPLATE` outside RH build; `POST …/render`; `mcp.enabled` + `list_mcp_prompts` / `render_prompt_template`

## Row (for table)

| Hardcoded SYSTEM_PROMPT / prompt_v*_final strings; git prompts/ / *.prompty / LangChain load_prompt; Langfuse Prompt Management; LangSmith/LangChain Hub; MLflow Prompt Registry; PromptLayer release labels; Braintrust/LangWatch prompt registries; Amazon Bedrock Prompt Management; ConfigMap/Secret prompt blobs; upstream/community Apicurio PROMPT_TEMPLATE (non-RH) | Prompt Template Registry | SYSTEM_PROMPT / system_prompt / PROMPT_V1 / prompt_v2_final; prompts/ / prompt_templates/ / *.prompty; load_prompt / prompt.save / lc://prompts/; langfuse create_prompt/get_prompt label=production; langsmith push_prompt/pull_prompt / hub.pull; mlflow.genai.register_prompt/load_prompt; promptlayer prompt_release_label; Braintrust/LangWatch prompt registry; bedrock create_prompt/get_prompt/create_prompt_version / arn:aws:bedrock:…:prompt/; ConfigMap prompt bodies; X-Registry-ArtifactType: PROMPT_TEMPLATE (non-RH quay.io/apicurio) |
