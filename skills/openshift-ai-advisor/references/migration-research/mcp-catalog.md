# MCP Catalog

Developer Preview OpenShift AI **AI hub** catalog for a governed **discover → deploy → playground** path: browse curated MCP servers (Red Hat / partners / community), deploy via **mcp-lifecycle-operator** (`MCPServer` CR), then wire into gen AI studio. Peers are public/local MCP discovery catalogs, hardcoded client fleets, and DIY Compose/K8s deploy paths teams use instead of (or before) RHOAI **MCP Catalog**.

## Peers

- Smithery — hosted MCP install / remote server catalog used as the org “find a server” path
- Docker MCP Catalog / Toolkit — `hub.docker.com/mcp`, Desktop Catalog tab, MCP Toolkit profiles (local curated images; discovery-focused, not OpenShift AI hub deploy)
- Official MCP Registry — `registry.modelcontextprotocol.io` / `server.json` / `GET /v0.1/servers` as sole enterprise catalog
- PulseMCP / mcp.so / awesome-mcp-servers browsing — paste-from-list onboarding without on-cluster deploy
- mcp-lookup / registry scrapers — CLIs aggregating official registry + Smithery + PulseMCP into client configs
- Hardcoded `mcp.json` fleets — Cursor/Claude/VS Code `mcpServers` with many `command`/`args`/`url` entries as the shared install standard
- `npx` / `docker run` MCP install — `npx -y @modelcontextprotocol/server-*`, `docker run … mcp/…` as the org deploy path
- Docker Compose MCP stacks — multi-port `/sse` / streamable-HTTP Compose + shared `.env` tokens
- DIY K8s MCP Deployments — hand-rolled `Deployment`+`Service`+Route, `TRANSPORT`/`MCP_PORT`/SSE env, custom Dockerfiles from GitHub MCP sources
- Hand-maintained MCP allowlists — markdown/spreadsheet/Confluence “approved MCP servers” without AI-hub catalog
- ToolHive / non-SIG marketplace operators — OpenShift “marketplace substitute” outside RHOAI catalog + kubernetes-sigs lifecycle-operator

**Not peers (adjacent catalog jobs):** MCP Gateway / MCP Server Registration (federate or register *already-running* backends); MCP Gateway Authorization / MCP Authorization Server (tool RBAC / OAuth AS); MCP Tool Registry (Apicurio `MCP_TOOL` definitions); Kagenti (agent runtime/A2A—not MCP marketplace); authoring a one-off custom MCP server for a single IDE client.

## Detection aliases

- Smithery: Smithery install URLs, hosted remote MCP as org standard, “install from Smithery”
- Docker MCP Catalog: `hub.docker.com/mcp`, Docker Desktop MCP Catalog tab, MCP Toolkit profiles/catalogs, Docker MCP Catalog docs
- Official registry: `registry.modelcontextprotocol.io`, `server.json`, `GET /v0.1/servers`, `GET /v0/servers`, reverse-DNS server names
- Public lists / scrapers: PulseMCP, mcp.so, awesome-mcp-servers, `mcp-lookup` CLI aggregating registry+Smithery+PulseMCP
- Hardcoded fleets: `~/.cursor/mcp.json`, `claude_desktop_config.json`, VS Code `mcpServers` with many entries; shared IDE MCP templates
- Install scripts: `npx -y @modelcontextprotocol/server-*`, `docker run -i --rm … mcp/…`
- Compose DIY: `docker compose` stacks exposing MCP `/sse` or streamable HTTP + shared MCP tokens
- K8s DIY: Manual MCP `Deployment`/`Service`/Route; `TRANSPORT=http` / `MCP_PORT` / SSE; custom Dockerfile for third-party MCP from source
- Allowlists: “approved MCP servers”, hand-maintained MCP spreadsheet/markdown allowlists; “find MCP on GitHub, build image, figure out transport”
- Adjacent DIY operators: ToolHive (or similar) used as MCP marketplace on OpenShift without RHOAI catalog
- Already on path (confirm): AI hub **MCP catalog**, “Deploy MCP server”, `kind: MCPServer` / `mcp.x-k8s.io/v1alpha1`, `mcp-lifecycle-operator-system`, Deployments tab, `gen-ai-aa-mcp-servers` ConfigMap

## Row (for table)

| Smithery; Docker MCP Catalog/Toolkit; official MCP Registry (server.json); PulseMCP/mcp.so/awesome-mcp-servers browsing; mcp-lookup scrapers; hardcoded mcp.json / IDE mcpServers fleets; npx/docker-run MCP install; Docker Compose MCP stacks; DIY K8s MCP Deployment+Service+Route; hand-maintained MCP allowlists; ToolHive / non-SIG marketplace operators | MCP Catalog | Smithery install/hosted remote; hub.docker.com/mcp / Desktop MCP Catalog / Toolkit profiles; registry.modelcontextprotocol.io / server.json / GET /v0.1/servers; PulseMCP / mcp.so / awesome-mcp-servers; mcp-lookup; ~/.cursor/mcp.json / claude_desktop_config.json / VS Code mcpServers fleets; npx @modelcontextprotocol/server-* / docker run mcp/…; Compose MCP /sse stacks; DIY MCP Deployment+Service+Route / TRANSPORT=http / MCP_PORT; approved-MCP allowlists; ToolHive marketplace DIY; AI hub MCP catalog / MCPServer mcp.x-k8s.io / mcp-lifecycle-operator / gen-ai-aa-mcp-servers |
