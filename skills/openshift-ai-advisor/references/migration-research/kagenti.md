# Kagenti Operator

Kubernetes operator (Developer Preview in Red Hat OpenShift AI) that enrolls agent/tool Deployments via `AgentRuntime`, injects AuthBridge (Envoy JWT in / token exchange out), SPIFFE (`spiffe-helper`), and per-agent OTel, and auto-syncs cluster `AgentCard` CRs for A2A discovery from labeled workloads (`kagenti.io/type`, `protocol.kagenti.io/a2a|mcp`). Peers are DIY enrollment, identity, and discovery/isolation stacks teams build instead of (or before) adopting **Kagenti Operator**.

## Peers

- **DIY SPIFFE/SPIRE + Keycloak per agent** — hand-rolled SPIRE agents/`spiffe-helper` sidecars, trust-domain SVIDs, and Keycloak (or other IdP) OAuth2 client registration per Deployment; secrets like per-agent client credentials without `AgentRuntime`
- **Envoy / oauth2-proxy enrollment sidecars** — manually injected Envoy, oauth2-proxy, or similar inbound JWT validation + outbound token exchange on every agent Pod (AuthBridge stand-in)
- **Custom agent-card scrapers for discovery/isolation** — controllers/jobs that `GET /.well-known/agent-card.json` (or legacy `agent.json`) from labeled pods and drive NetworkPolicies, allowlists, or local indexes from card/signature status
- **Hand-rolled AgentCard / enrollment Controllers** — homemade CRDs or operators that label Deployments, mutate sidecars, and maintain a cluster agent inventory without `agent.kagenti.dev`
- **Per-agent Istio/Linkerd + mTLS identity** — mesh sidecars and identity for agents instead of Kagenti AuthBridge/SPIFFE injection
- **App-embedded auth & identity** — JWT validation, token exchange, and SPIFFE/mTLS wired into each LangGraph/CrewAI/ADK/AG2 agent process (no platform webhook injection)
- **DIY per-agent OTel / MLflow wiring** — custom sidecars or SDK bootstrap for agent tracing/observability without `AgentRuntime` OTEL fields
- **Upstream / community Kagenti outside RHOAI** — `kagenti/kagenti-operator` Helm (`ghcr.io/kagenti/...`), `scripts/kind/setup-kagenti.sh`, or non-RH `agents-operator` installs (migrate *into* catalog RHOAI DP path)
- **ODH / RHDS agents-operator forks (non-catalog path)** — `opendatahub-io/agents-operator` / `red-hat-data-services/agents-operator` clones used as DIY platform outside listed OpenShift AI Developer Preview

**Not peers (adjacent catalog jobs):** A2A Agent Registry (Apicurio `AGENT_CARD` shared search—not workload `AgentCard` CRs); MCP Catalog / MCP Gateway / MCP Tool Registry (tool marketplace & federation); AI Inference Tool Calling (model-server tools); Agent Sandbox (`Sandbox`/`SandboxClaim` isolated execution); agent app frameworks alone (LangGraph/CrewAI/ADK code without enrollment/identity); Connectivity Link / plain Gateway API HTTP without agent runtime injection.

## Detection aliases

- SPIFFE/SPIRE DIY: `spire-agent`, `spiffe-helper`, `SPIRE_ENABLED`, trust-domain SVIDs on agent Deployments; Keycloak client registration per agent; `keycloak-admin-secret` / per-agent client-credential Secrets without Kagenti CRs
- Envoy/oauth2-proxy: hand-injected `envoy` / `oauth2-proxy` sidecars; “AuthBridge-like” JWT validate + token exchange; comments “enroll agent”, “platform-managed agent identity”
- Scrapers/isolation: crawl `/.well-known/agent-card.json` / `agent.json` from pods; custom NetworkPolicy-from-card controllers; JWS/signature gates on A2A peers
- Homemade enrollment: custom AgentRuntime-like CRDs; webhook mutating agent Deployments; DIY `AgentCard` indexes outside `agent.kagenti.dev`
- Mesh identity: Istio/Linkerd mTLS PeerAuthentication/AuthorizationPolicy as agent zero-trust stand-in
- App-embedded: in-process JWT/mTLS/SPIFFE in agent containers; no sidecar inject labels
- Observability DIY: per-agent OTel Collector sidecars / MLflow hooks without Operator
- Upstream Kagenti: `ghcr.io/kagenti/kagenti-operator`, `kagenti-operator-chart`, `setup-kagenti.sh`, `kagenti-system` on non-RHOAI clusters; `opendatahub-io/agents-operator`, `red-hat-data-services/agents-operator`
- Protocol/workload markers (need-for-operator): multi-agent Deployments + desire for A2A discovery and zero-trust sidecars; labels mimicking `kagenti.io/type` / `protocol.kagenti.io/*` without the operator

## Row (for table)

| DIY SPIFFE/SPIRE + Keycloak client registration per agent; Envoy/oauth2-proxy enrollment sidecars; custom /.well-known/agent-card.json scrapers for discovery/isolation; hand-rolled AgentCard/enrollment controllers; Istio/Linkerd mTLS agent identity; app-embedded JWT/SPIFFE/auth; DIY per-agent OTel/MLflow; upstream/community Kagenti or ODH/RHDS agents-operator outside RHOAI DP | Kagenti Operator | spire-agent / spiffe-helper / SPIRE_ENABLED; Keycloak per-agent clients; envoy / oauth2-proxy sidecars; AuthBridge-like JWT+token exchange; scrape /.well-known/agent-card.json; NetworkPolicy-from-card; DIY AgentRuntime/AgentCard CRDs; Istio/Linkerd agent mTLS; in-process agent JWT/SPIFFE; ghcr.io/kagenti/kagenti-operator / setup-kagenti.sh / kagenti-system (non-RHOAI); opendatahub-io/agents-operator; red-hat-data-services/agents-operator; enroll agent / platform-managed agent identity |
