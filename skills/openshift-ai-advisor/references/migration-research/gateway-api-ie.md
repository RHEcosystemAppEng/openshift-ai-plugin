# Gateway API Inference Extensions

Kubernetes Gateway API extensions for **inference-aware** routing and load balancing of multi-replica self-hosted GenAI/LLM servers (`InferencePool` + Endpoint Picker over Envoy ext-proc). Peers are DIY sticky/prefix LB, custom EPP wiring, Istio-only L7, and other inference/AI gateways teams run instead of (or before) adopting this catalog path.

## Peers

- DIY sticky / prefix-hash LB — Envoy/Nginx/HAProxy session affinity, cookie sticky, or consistent-/prefix-hash routers across GPU replicas without InferencePool/EPP
- Hand-rolled least-loaded / metric pickers — custom proxies choosing pods from Prometheus/`vllm:gpu_cache_usage_perc`/queue metrics without GAIE CRDs
- Custom Envoy ext_proc EPP — hand-rolled external-processing “scheduler” filter calling a home-grown picker (no `InferencePool` / `EndpointPickerConfig`)
- Istio-only routing — VirtualService / DestinationRule / subset LB (round-robin, least-conn, consistentHash) without InferencePool or KV/queue scorers
- Plain Gateway API HTTPRoute → Service — generic L7 ingress with kube-proxy/Service LB (no inference backend or EPP)
- Envoy AI Gateway — model-based routing, request transforms, and upstream auth without GAIE `InferencePool` scheduling
- LiteLLM / OpenAI-compatible proxy LB — app-layer proxy spreading chat/completions across replica URLs
- Solo / Gloo AI Gateway — higher-level AI gateway in front of self-hosted backends without standardized InferencePool+EPP
- vLLM Production Stack / SGLang router (LB-only) — Helm/engine routers for prefix-/session-aware replica picking outside Gateway API Inference Extensions
- AIBrix gateway — ByteDance/vLLM cloud-native gateway/control plane used for inference LB instead of GAIE on OpenShift
- Apigee / other API management AI frontends — enterprise API gateway routing to model backends without EPP scorers

**Not peers (adjacent catalog jobs):** Distributed Inference with llm-d (full multi-node P/D + productized stack that *uses* GAIE underneath); CMA/HPA (replica *count*, not per-request pick); plain OpenShift Service Mesh for mTLS/authz on non-inference apps; single-replica vLLM/KServe serving with no LB need.

## Detection aliases

- DIY sticky / prefix-hash LB: Envoy/Nginx/HAProxy `hash`/`consistent_hash`/`sticky` cookie; “route by prefix hash”; custom prompt-prefix affinity middleware across GPU Services
- Hand-rolled metric pickers: Prometheus/`vllm:gpu_cache_usage_perc`/queue-depth based pod selection; ADRs “least-loaded GPU”, “KV-aware LB” without `InferencePool`
- Custom Envoy EPP: EnvoyFilter/`ext_proc` calling a non-GAIE scheduler Deployment; home-grown endpoint picker images not `gateway-api-inference-extension` / `llm-d-router-endpoint-picker` / lwepp
- Istio-only: `VirtualService`/`DestinationRule`/`consistentHash`/`leastConn` to model Services; mesh mTLS + ordinary LB with **no** `InferencePool`/`endpointPickerRef`/`EndpointPickerConfig`
- Plain Gateway API: `HTTPRoute` `backendRefs` → `Service` only; no `inference.networking.k8s.io` / `InferencePool`
- Envoy AI Gateway: `envoyproxy/ai-gateway`, Envoy AI Gateway model routes/transforms (not GAIE InferencePool charts)
- LiteLLM / OpenAI proxy LB: `litellm`, LiteLLM proxy/router across multiple self-hosted base URLs; DIY OpenAI-compatible fan-out
- Solo / Gloo AI Gateway: Gloo AI Gateway, Solo AI Gateway in front of LLM replicas without InferencePool
- vLLM Production Stack / SGLang router: `vllm-project/production-stack`/`vllm-stack` prefix router; `sglang_router` / Model Gateway as the LB layer only
- AIBrix gateway: `aibrix`, `vllm-project/aibrix`, AIBrix gateway CRDs used for inference routing
- Apigee / API mgmt AI frontends: Apigee AI/LLM proxy policies routing to self-hosted model backends without EPP

## Row (for table)

| DIY sticky/prefix-hash LB; hand-rolled Prometheus/least-loaded GPU pickers; custom Envoy ext_proc EPP; Istio-only VirtualService/DestinationRule LB; plain Gateway API HTTPRoute→Service; Envoy AI Gateway; LiteLLM/OpenAI-compatible proxy LB; Solo/Gloo AI Gateway; vLLM Production Stack/SGLang router (LB-only); AIBrix gateway; Apigee/API-mgmt AI frontends | Gateway API Inference Extensions | Envoy/Nginx/HAProxy sticky/`consistent_hash`/prefix-hash LB; Prometheus/`vllm:gpu_cache_usage_perc` custom pickers; EnvoyFilter ext_proc home-grown scheduler (no InferencePool); Istio VirtualService/DestinationRule/`consistentHash` without endpointPickerRef; HTTPRoute→Service only; envoyproxy/ai-gateway; litellm proxy fan-out; Gloo/Solo AI Gateway; vllm-stack/sglang_router LB-only; aibrix gateway; Apigee AI/LLM proxy |
