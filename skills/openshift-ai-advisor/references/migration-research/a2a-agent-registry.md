# A2A Agent Registry

Developer Preview capability in **Red Hat build of Apicurio Registry** that stores A2A Agent Cards as `AGENT_CARD` artifacts and exposes shared discovery (`/.well-known/agents`, skill/capability search, per-artifact retrieval) so orchestrators locate peers without hard-coding URLs. Peers are DIY/hard-coded agent-card catalogs, scrapers of per-agent well-known cards, and other A2A registries that solve the same shared Agent Card catalog job.

## Peers

- **Hard-coded peer agent URL directories** — orchestrator ConfigMaps/Secrets/env lists of agent base URLs or service DNS; “agent directory” spreadsheets; static peer maps in LangGraph/CrewAI/ADK supervisors
- **Hard-coded Agent Card scrapers** — custom jobs/microservices that `GET` a fixed allowlist of `/.well-known/agent-card.json` (or legacy `/.well-known/agent.json`) and re-index locally for skill search
- **DIY `/.well-known/agents` catalogs** — hand-rolled FastAPI/Nginx/Envoy services mimicking multi-agent search (`GET /.well-known/agents?skill=…`, `POST …/agents/search`) over a homemade card store (Postgres/JSON/Git)
- **Static multi-card catalogs** — monorepo / object-store / GitOps folders of Agent Card JSON served as a flat catalog without Apicurio `AGENT_CARD` lifecycle
- **Upstream / community Apicurio A2A Agent Registry (non-RH)** — `quay.io/apicurio/apicurio-registry` with `APICURIO_A2A_ENABLED` / `apicurio.a2a.enabled` outside Red Hat build (migrate *into* catalog RH path)
- **Other curated A2A registries / marketplaces** — enterprise or public Agent Card catalogs per A2A “curated registries” discovery (publish cards → query by skills/tags); Solo.io–style Agent Registry / Agent Naming Service (ANS) catalogs
- **Direct-config / private discovery** — clients given Agent Card JSON or card URLs at deploy time (A2A “direct configuration”) with no shared search registry
- **Framework-local agent directories** — BeeAI / Google ADK / LangGraph / CrewAI in-process registries of peer agents (name→URL/card) without a central HTTP Agent Card registry

**Not peers (adjacent catalog jobs):** MCP Tool Registry / MCP Gateway / MCP Catalog (LLM↔tool schemas & transport); Agent Sandbox / Kagenti Operator (run/isolate agents or inject cluster AgentCard CRs—not Apicurio `AGENT_CARD` search); single-agent A2A servers that only host one `/.well-known/agent-card.json` with no shared catalog; plain Apicurio schema registry (Avro/Protobuf only, no A2A).

## Detection aliases

- Hard-coded peers: ConfigMap/env lists of agent URLs; “agent directory”; supervisor hard-coded peer DNS/service names; comments “don’t hard-code agent endpoints”
- Scrapers: crawl/fetch loops over `/.well-known/agent-card.json` / `/.well-known/agent.json`; static allowlists of agent domains; homemade “agent card index”
- DIY catalogs: custom `/.well-known/agents`, `/.well-known/agents/search`, `POST …/agents/search`; homemade `AgentSearchResults` / skill query APIs outside Apicurio
- Static catalogs: Git/S3 folders of `*agent-card*.json`; GitOps Agent Card bundles without `artifactType: AGENT_CARD`
- Upstream Apicurio A2A: `quay.io/apicurio/apicurio-registry`, `APICURIO_A2A_ENABLED`, `apicurio.a2a.enabled`, `AGENT_CARD`, `X-Registry-ArtifactType: AGENT_CARD` (non-RH images/docs)
- Other registries: “curated registry”, “agent marketplace”, Solo `agentregistry` / Agent Naming Service (ANS); enterprise Agent Card catalog APIs
- Direct config: baked-in Agent Card JSON / card URL in client config; A2A “private discovery”
- Framework directories: BeeAI/ADK/LangGraph/CrewAI local peer maps; in-memory “available agents” registries
- Protocol markers (need-for-registry): `a2a-sdk`, `@a2a-js/sdk`, `A2ACardResolver`, `message/send` / `message/stream` plus multi-peer resolution by skill

## Row (for table)

| Hard-coded peer agent URL directories / ConfigMaps; hard-coded scrapers of `/.well-known/agent-card.json`; DIY `/.well-known/agents` search catalogs; static Git/S3 Agent Card catalogs; upstream/community Apicurio A2A (non-RH); other curated A2A registries / marketplaces / Solo agentregistry–ANS; direct-config private discovery; framework-local BeeAI/ADK/LangGraph/CrewAI peer directories | A2A Agent Registry | hard-coded agent URLs / agent directory ConfigMap; scrape /.well-known/agent-card.json; DIY /.well-known/agents / agents/search; static agent-card.json catalogs; quay.io/apicurio/apicurio-registry APICURIO_A2A_ENABLED (non-RH); AGENT_CARD outside RH build; curated A2A registry / agent marketplace; Solo agentregistry / ANS; direct Agent Card URL config; BeeAI/ADK/LangGraph/CrewAI local peer maps; a2a-sdk / A2ACardResolver multi-peer skill resolve |
