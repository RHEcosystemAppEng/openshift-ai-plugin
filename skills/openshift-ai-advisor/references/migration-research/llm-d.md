# Distributed Inference with llm-d

Kubernetes-native multi-node LLM serving with AI-aware routing, disaggregated prefill/decode, and KV-cache-aware scheduling (`LLMInferenceService`). Peers are other distributed / P/D orchestration stacks and DIY multi-replica LB patterns teams run instead of (or before) adopting this catalog path.

## Peers

- NVIDIA Dynamo — open-source datacenter-scale orchestrator (KV-aware router, planner, NIXL P/D) over vLLM / SGLang / TensorRT-LLM
- AIBrix — ByteDance/vLLM cloud-native GenAI inference control plane (gateway, autoscaler, distributed KV, P/D)
- Llumnix — full-stack distributed LLM serving with dynamic scheduling, live KV migration, adaptive P/D
- Mooncake — Moonshot KV-cache-centric P/D platform (Transfer Engine + Store; often paired with SGLang/vLLM)
- SGLang PD + Model Gateway — engine-native `--disaggregation-mode` prefill/decode workers + `sglang_router` / Model Gateway
- vLLM Production Stack — K8s Helm reference stack for multi-replica vLLM with prefix-/session-aware router + LMCache
- OME — Oracle/SGLang Kubernetes-native distributed LLM inference operator/stack
- Ray Serve LLM — Ray Serve multi-replica LLM apps with prefix-aware / power-of-two routing
- ATOMesh — AMD ROCm distributed inference gateway (multi-node disagg + KV-aware routing for Instinct)
- MoLink — heterogeneous/geo-distributed vLLM scale-out with cross-node pipeline partitioning
- DistServe / Splitwise-style research P/D stacks — academic goodput-oriented prefill/decode pool designs (often forked/adapted in-house)
- DIY disaggregated prefill/decode Deployments — separate prefill vs decode GPU pools + hand-rolled KV handoff (NIXL/Mooncake/RDMA scripts)
- DIY sticky / prefix-hash LB — Envoy/Nginx/HAProxy session affinity or custom prefix-hash routers across GPU replicas without a productized scheduler
- DIY KV-cache affinity proxies — custom reverse proxies / ZMQ KV-event subscribers / block-hash indexes in front of multi-node vLLM

## Detection aliases

- NVIDIA Dynamo: `ai-dynamo/dynamo`, `nvidia-dynamo`, `dynamo-run`, Dynamo `Frontend`/`Worker`/`Planner`, Dynamo disaggregated serving docs, NIXL under Dynamo (not llm-d charts)
- AIBrix: `aibrix`, `vllm-project/aibrix`, `AIBrix`, AIBrix gateway/autoscaler CRDs, `aibrix-controller-manager`
- Llumnix: `llumnix`, `llumnix-project/llumnix`, `LlumSched`, `Llumlet`, `llumnix.ai`, PD-KVS mode
- Mooncake: `kvcache-ai/Mooncake`, `mooncake`, `Mooncake Transfer Engine`, `Mooncake Store`, `MOONCAKE_`, `--disaggregation-transfer-backend mooncake`
- SGLang PD / router: `sglang.launch_server --disaggregation-mode`, `--disaggregation-mode prefill|decode`, `sglang_router.launch_router --pd-disaggregation`, `SGLANG_DISAGGREGATION_`, `SGLANG_MOONCAKE_`
- vLLM Production Stack: `vllm-project/production-stack`, `vllm-stack` Helm, `servingEngineSpec`, Production Stack prefix-aware router, LMCache `--kv-offloading-backend lmcache`
- OME: `ome`, Oracle Model Engine / SGLang OME operator, OME InferenceService-style CRDs for distributed SGLang
- Ray Serve LLM: `ray.serve`, `@serve.deployment`, Ray Serve LLM prefix-aware router, `RayService` multi-replica LLM
- ATOMesh: `atomesh`, ATOMesh AMD ROCm inference gateway, Instinct P/D disagg
- MoLink: `molink`, MoLink distributed vLLM / cross-node pipeline parallel serving
- DistServe / Splitwise: `DistServe`, `Splitwise`, papers/code forks implementing separate prefill/decode machine pools
- DIY P/D Deployments: separate `prefill`/`decode` Deployments or StatefulSets; `NixlConnector` / NIXL / RDMA KV transfer scripts outside llm-d Helm; role labels `prefill`/`decode`
- DIY sticky / prefix-hash LB: Envoy/Nginx/HAProxy `hash`/`consistent_hash`/`sticky` cookie or `prefix` routing across GPU Services; custom “route by prefix hash” middleware
- DIY KV affinity proxies: hand-rolled KV-cache indexes, ZMQ subscribers to vLLM `--kv-events-config` without GAIE/EPP product stack, custom InferencePool-like pickers

## Row (for table)
| NVIDIA Dynamo; AIBrix; Llumnix; Mooncake; SGLang PD + Model Gateway; vLLM Production Stack; OME; Ray Serve LLM; ATOMesh; MoLink; DistServe/Splitwise-style P/D; DIY prefill/decode Deployments + KV handoff; DIY sticky/prefix-hash LB; DIY KV-cache affinity proxies | Distributed Inference with llm-d | `ai-dynamo/dynamo`/`nvidia-dynamo`/`dynamo-run`; `aibrix`/`vllm-project/aibrix`; `llumnix`/`LlumSched`/`Llumlet`; `kvcache-ai/Mooncake`/`mooncake`/`MOONCAKE_`; `sglang --disaggregation-mode`/`sglang_router --pd-disaggregation`; `vllm-project/production-stack`/`vllm-stack` Helm/`servingEngineSpec`; OME (Oracle/SGLang); `ray.serve` LLM prefix router/`RayService`; `atomesh`; `molink`; `DistServe`/`Splitwise`; DIY prefill+decode Deployments + NIXL/RDMA KV transfer; Envoy/Nginx/HAProxy sticky/`consistent_hash`/prefix-hash LB; DIY ZMQ/`--kv-events-config` KV affinity proxies |
