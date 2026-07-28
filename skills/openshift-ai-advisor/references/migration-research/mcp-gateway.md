# MCP Gateway

Red Hat Connectivity Link’s MCP gateway federates many backend MCP servers behind one Kubernetes Gateway API endpoint (Envoy + `ext_proc` router + broker + `MCPServerRegistration` discovery), with unified `tools/list`, MCP-aware routing, and session handling. Peers are other multi-server MCP aggregators/gateways and DIY federation patterns teams use instead of (or before) adopting Connectivity Link **MCP Gateway**.

## Peers

- Docker MCP Gateway — `docker mcp gateway run` / `docker/mcp-gateway` CLI toolkit; container-lifecycle MCP aggregator (Desktop or Linux plugin)
- IBM ContextForge — `mcp-contextforge-gateway` / Helm chart often named `mcp-gateway`; federates MCP (+ A2A/REST) with registry/governance
- sparfenyuk/mcp-proxy (fleet mode) — multi-backend MCP aggregator (vs transport-only stdio↔SSE bridge for one server)
- Solo agentgateway MCP federation — `AgentgatewayBackend` / `appProtocol: agentgateway.dev/mcp`
- Envoy AI Gateway MCP aggregation — `MCPRoute` / aggregating MCP mode on Envoy AI Gateway
- Custom Envoy MCP filter / ext_proc wiring — hand-rolled Envoy MCP JSON-RPC fan-out without Kuadrant CRs
- Nginx / reverse-proxy / sidecar MCP fan-out — DIY proxy that merges `tools/list` / `tools/call` across HTTP/SSE backends
- Hand-rolled tool-name prefixing — collision handling across many MCP servers in app or proxy code
- DIY multi-MCP URL federation — N separate MCP server URLs in Cursor/Claude/VS Code with duplicated auth and no central gateway
- TrueFoundry AI/MCP Gateway — enterprise VPC/self-hosted LLM + MCP gateway with budgets/RBAC (when used as MCP control plane)

**Not peers (adjacent catalog jobs):** MCP Catalog / MCP Lifecycle Operator (browse/deploy servers); MCP Gateway Authorization / MCP Authorization Server (tool RBAC / OAuth AS); MCP Tool Registry (definition catalog); transport-only single-server mcp-proxy; plain Gateway API HTTP without MCP federation.

## Detection aliases

- Docker MCP Gateway: `docker mcp gateway`, `docker mcp gateway run`, `docker/mcp-gateway`, `docker-mcp` CLI plugin, MCP Toolkit profiles/catalogs
- ContextForge: `IBM/mcp-context-forge`, `mcp-contextforge-gateway`, Helm release/chart `mcp-gateway` (non-RH), ContextForge gateway
- mcp-proxy fleet: `sparfenyuk/mcp-proxy`, `mcp-proxy` aggregating multiple MCP HTTP/SSE URLs (not single-server stdio bridge alone)
- agentgateway: `agentgateway`, `AgentgatewayBackend`, `appProtocol: agentgateway.dev/mcp`, agentgateway MCP federation
- Envoy AI Gateway MCP: `envoyproxy/ai-gateway`, `MCPRoute`, Envoy AI Gateway aggregating MCP mode
- Custom Envoy MCP: Envoy `ext_proc` MCP router/broker without `mcp.kuadrant.io`; hand-rolled mcp-router/mcp-broker Deployments
- DIY reverse proxy: Nginx/sidecar “MCP aggregator”; merged `tools/list` / `tools/call` fan-out; hand-rolled `toolPrefix` / tool-name collision handling
- Multi-URL clients: Cursor/Claude/VS Code `mcpServers` with many distinct URLs; duplicated OAuth/API keys per server; comments/ADRs “federate MCP”, “aggregate MCP servers”
- TrueFoundry: `truefoundry` MCP/AI gateway as multi-server MCP control plane

## Row (for table)

| Docker MCP Gateway; IBM ContextForge; sparfenyuk/mcp-proxy fleet aggregators; Solo agentgateway MCP federation; Envoy AI Gateway MCPRoute; custom Envoy ext_proc MCP fan-out; Nginx/reverse-proxy/sidecar MCP aggregators; hand-rolled tool-name prefixing; DIY multi-MCP URL client configs; TrueFoundry MCP gateway | MCP Gateway | docker mcp gateway / docker/mcp-gateway / docker-mcp; mcp-contextforge-gateway / IBM/mcp-context-forge / Helm mcp-gateway (non-RH); sparfenyuk/mcp-proxy fleet; AgentgatewayBackend / agentgateway.dev/mcp; MCPRoute / envoyproxy/ai-gateway MCP; Envoy ext_proc mcp-router/broker without mcp.kuadrant.io; Nginx MCP aggregator; toolPrefix collision handling; N mcpServers URLs in IDE; truefoundry MCP gateway |
