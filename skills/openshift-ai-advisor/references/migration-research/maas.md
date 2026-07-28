# Models-as-a-Service (MaaS)

Governed access to **externally hosted** LLMs (cloud provider APIs) via a unified control plane: quotas, RBAC, audit, fewer raw keys in apps. Peers are LLM API gateways/proxies/aggregators and DIY key/rate-limit wrappers that teams use instead of (or before) adopting RHOAI MaaS.

## Peers

- LiteLLM Proxy — self-hosted OpenAI-compatible multi-provider proxy with spend/virtual keys
- Portkey — production LLM gateway (routing, caching, virtual keys, guardrails, observability)
- OpenRouter — managed multi-model aggregator with unified billing API
- Helicone (AI Gateway) — drop-in proxy focused on logging, caching, and light routing
- Cloudflare AI Gateway — edge-managed proxy for caching, rate limits, and provider analytics
- Vercel AI Gateway — managed OpenAI-compatible gateway for Vercel/Next.js apps
- Kong AI Gateway — Kong/Konnect AI Proxy plugins for enterprise API governance of LLM traffic
- Apache APISIX AI Gateway — OSS API gateway with AI proxy / token governance plugins
- Envoy AI Gateway — Kubernetes Gateway-API AI gateway on Envoy for auth/routing/rate limits to GenAI providers
- Bifrost (Maxim) — high-throughput Go OSS AI gateway (virtual keys, budgets, failover)
- BricksLLM — self-hosted gateway emphasizing spend caps, rate limits, and PII masking
- TrueFoundry AI Gateway — enterprise VPC/self-hosted LLM + MCP gateway with budgets/RBAC
- Martian — managed smart router (pick cheapest/best model per request)
- Not Diamond — managed prompt-to-model router
- Unify — managed router/aggregator with quality–cost–latency routing
- Eden AI — managed unified API across many AI/LLM providers
- Merge Gateway — managed production LLM gateway with routing/budget policies
- Databricks AI Gateway — workspace-scoped governed access to external/foundation models
- Custom API-key / OpenAI `base_url` gateway — DIY FastAPI/Nginx/Envoy proxy holding provider keys
- Per-team rate-limit / budget wrappers — shared `llm_client` middleware, TPM/RPM, retry/fallback chains
- Scattered cloud LLM SDK keys — direct OpenAI/Anthropic/Azure/Bedrock/Vertex calls with `.env` key sprawl (no central gateway)

## Detection aliases

- LiteLLM Proxy: `litellm`, `from litellm import completion`, `litellm.completion(`, `litellm --config`, `model_list:`, `LITELLM_MASTER_KEY`, `LITELLM_PROXY_API_BASE`, `ghcr.io/berriai/litellm`, port `:4000`, model prefixes `openai/`/`anthropic/`/`azure/`/`bedrock/`
- Portkey: `portkey-ai`, `PORTKEY_GATEWAY_URL`, `x-portkey-api-key`, `virtual_key`, `@portkey-ai/gateway`
- OpenRouter: `openrouter.ai`, `OPENROUTER_API_KEY`, `https://openrouter.ai/api/v1`
- Helicone: `helicone`, `HELICONE_API_KEY`, `gateway.helicone.ai`, `Helicone-Auth`
- Cloudflare AI Gateway: `gateway.ai.cloudflare.com`, `CLOUDFLARE_ACCOUNT_ID` + AI Gateway route
- Vercel AI Gateway: `ai-gateway.vercel.sh`, Vercel AI SDK `baseURL` to Vercel gateway
- Kong AI Gateway: Kong `ai-proxy` / `ai-prompt-*` plugins, `kong-ai-gateway`, Konnect AI Gateway
- Apache APISIX: `apisix` AI proxy plugins, `apache/apisix`
- Envoy AI Gateway: `envoyproxy/ai-gateway`, Envoy Gateway AIPolicy / GenAI routes
- Bifrost: `maximhq/bifrost`, `getbifrost.ai`, Bifrost gateway binary/Helm
- BricksLLM: `bricksllm`, `BricksLLM`
- TrueFoundry: `truefoundry` AI/LLM gateway, TrueFoundry control plane
- Martian / Not Diamond / Unify / Eden AI / Merge: `withmartian.com`, `notdiamond`, `unify.ai`, `edenai`, `mergegateway` / Merge Gateway
- Databricks AI Gateway: Databricks serving/AI Gateway endpoints, workspace external model routes
- DIY gateway / wrappers: `base_url=` / `baseURL=` / `OPENAI_BASE_URL` / `OPENAI_API_BASE` pointing off `api.openai.com`; custom Deployment+Service “llm-gateway”; per-team TPM/RPM/spend middleware
- Direct cloud SDKs / key sprawl: `openai`/`AzureOpenAI`, `anthropic`, `google-genai`/`vertexai`, `boto3.client("bedrock-runtime")`; LangChain `ChatOpenAI`/`ChatAnthropic`/`ChatBedrock` to cloud; `OPENAI_API_KEY`/`ANTHROPIC_API_KEY`/`AZURE_OPENAI_API_KEY` in `.env`/Secrets across services

## Row (for table)

| LiteLLM Proxy; Portkey; OpenRouter; Helicone; Cloudflare AI Gateway; Vercel AI Gateway; Kong AI Gateway; Apache APISIX AI Gateway; Envoy AI Gateway; Bifrost; BricksLLM; TrueFoundry AI Gateway; Martian; Not Diamond; Unify; Eden AI; Merge Gateway; Databricks AI Gateway; custom API-key / OpenAI base_url gateways; per-team rate-limit/budget wrappers; scattered cloud LLM SDK keys | Models-as-a-Service (MaaS) | litellm / litellm.completion / ghcr.io/berriai/litellm / LITELLM_MASTER_KEY / :4000; portkey-ai / PORTKEY_GATEWAY_URL / virtual_key; openrouter.ai / OPENROUTER_API_KEY; helicone / gateway.helicone.ai; gateway.ai.cloudflare.com; ai-gateway.vercel.sh; Kong ai-proxy plugins; apisix AI proxy; envoyproxy/ai-gateway; maximhq/bifrost; bricksllm; truefoundry AI gateway; Martian/Not Diamond/Unify/Eden AI/Merge; Databricks AI Gateway; OPENAI_BASE_URL/base_url off api.openai.com; OPENAI_API_KEY/ANTHROPIC_API_KEY sprawl; AzureOpenAI/anthropic/google-genai/bedrock-runtime; ChatOpenAI/ChatAnthropic/ChatBedrock to cloud |
