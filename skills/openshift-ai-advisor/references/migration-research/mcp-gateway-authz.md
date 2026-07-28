# MCP Gateway Authorization

Connectivity Link capability that enforces **tool- and prompt-level** authorization on MCP gateway `tools/call` (and optionally filtered `tools/list`) via Kuadrant `AuthPolicy` on the Gateway’s internal `mcps` listener—CEL and/or OPA against JWT claims (`resource_access` / `tool:` / `prompt:` roles) and headers such as `x-mcp-toolname`. Peers are other gateway-level or DIY MCP tool ACL patterns teams use instead of (or before) adopting Connectivity Link **MCP Gateway Authorization**.

## Peers

- OPA/CEL DIY tool ACL — hand-rolled Rego/CEL (or Authorino outside Connectivity Link CRs) that allow/deny `tools/call` by tool name vs JWT roles
- Traefik Hub MCP middleware TBAC — Traefik Hub `Middleware` `plugin.mcp` policies (`mcp.params.name`, `jwt.groups` / `allowed_tools`, task/tool/transaction TBAC)
- Solo agentgateway `mcpAuthorization` — CEL rules on `mcp.tool.name` / `mcp.prompt.name` + `jwt.roles` (or other JWT claims) at the MCP backend
- Per-server allowlists / AuthMiddleware — FastMCP / Express / Fastify (or similar) middleware gating `params.name` with JWT roles, duplicated across MCP servers
- Custom Envoy / ext_proc tool RBAC — sidecar or filter that parses MCP JSON-RPC and enforces tool ACL outside Kuadrant `AuthPolicy` on `mcps`
- Hand-rolled `tools/list` filtering — app or proxy code that hides unauthorized tools per user without infra AuthPolicy / wristband
- OSS “MCP security gateway” tool policies — community MCP security/gateway products that ship per-tool allow/deny at the edge
- Broad OAuth scopes + desire for tool ACL — over-permissive tokens covering all tools, with DIY deny lists or token-exchange + tool matrix instead of gateway AuthPolicy

**Not peers (adjacent catalog jobs):** MCP Gateway (federation / unified endpoint without tool RBAC); authN-only `AuthPolicy` on public `mcp` (identity, not tool ACL); **MCP Authorization Server** / Keycloak AS (issues tokens; does not enforce per-tool allow/deny at the gateway); per-server OAuth resource-server auth alone (identity for one server); **HITL Tool Approval** (human confirm before tool run); NetworkPolicy / mesh mTLS only (transport trust, not tool-name authorization).

## Detection aliases

- OPA/CEL DIY: custom Rego/`opa.rego` on `tools/call`; CEL/`checkToolAccess` / role×tool matrix outside `sectionName: mcps`; Authorino tool ACL without Connectivity Link AuthPolicy pattern
- Traefik TBAC: Traefik Hub `kind: Middleware` + `plugin.mcp` / `policies`; TBAC; `mcp.params.name`; `allowed_tools` / `authorized_tasks`; `defaultAction: deny`
- agentgateway: `mcpAuthorization` / `mcpAuthorization.rules`; `mcp.tool.name`; `mcp.prompt.name`; `"admin" in jwt.roles`; agentgateway.dev MCP authz docs
- Per-server allowlists: FastMCP/Express/Fastify `AuthMiddleware`; `params.name` allowlist; per-MCP-server deny lists; comments “tool ACL in each server”
- Custom Envoy/ext_proc: Envoy `ext_proc` / sidecar parsing MCP JSON-RPC for tool RBAC; homemade mcp-authz filter without Kuadrant `AuthPolicy`
- List filtering: hand-rolled filtered `tools/list`; DIY `x-authorized-tools` without `x-mcp-authorized` wristband / `MCPGatewayExtension` trusted headers
- OSS MCP security gateways: “MCP security gateway” tool policies; community edge tool RBAC products
- Need markers: `tool:` / `prompt:` role desire; “MCP Access denied” / 403 on tool call; ADR “gateway-level tool ACL”, “stop over-permissive MCP tokens”

## Row (for table)

| OPA/CEL DIY tool ACL; Traefik Hub MCP middleware TBAC; Solo agentgateway mcpAuthorization CEL; per-server FastMCP/Express/Fastify allowlists; custom Envoy/ext_proc MCP tool RBAC; hand-rolled tools/list filtering; OSS MCP security-gateway tool policies; broad OAuth scopes + DIY tool deny matrices | MCP Gateway Authorization | DIY OPA/CEL/Rego tools/call ACL; Traefik Hub Middleware plugin.mcp / TBAC / mcp.params.name / allowed_tools; mcpAuthorization.rules / mcp.tool.name / jwt.roles; FastMCP AuthMiddleware / params.name allowlist; Envoy ext_proc tool RBAC; hand-rolled filtered tools/list; OSS MCP security gateway tool policies; over-permissive MCP scopes + DIY tool ACL |
