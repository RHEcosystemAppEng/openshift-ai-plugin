# MCP Tool Registry

Technology Preview `MCP_TOOL` artifact type in **Red Hat build of Apicurio Registry** 3.2 that versions MCP tool *definitions* (name, description, `inputSchema` / `outputSchema`) with validation, compatibility, and (when enabled) well-known discovery (`/.well-known/mcp-tools`). Peers are duplicated/scattered tool schemas, scrapers of live `tools/list`, DIY MCP tool catalogs, and other definition-governance stores that solve the same shared tool-*definition* catalog job—not live MCP execution.

## Peers

- **Duplicated tool schemas in ConfigMaps / YAML / prompts** — tool `name` + `inputSchema`/`outputSchema` copied into Helm values, Secrets, OpenAPI snippets, or hard-coded agent prompts with no central version history
- **Spreadsheets / wikis of “available tools”** — Confluence/Sheets/markdown parameter lists that agents or humans search by name or input param
- **Scrapers of live `tools/list`** — custom jobs/microservices that call MCP `tools/list` on many servers and re-expose a static JSON catalog of definitions
- **DIY `/.well-known/mcp-tools` catalogs** — hand-rolled FastAPI/Nginx services mimicking Apicurio search (`GET /.well-known/mcp-tools?name=…&parameter=…`, per-artifact retrieval) over a homemade store
- **DIY `MCP_TOOL` / tool-definition stores** — Postgres/JSON/Git “tool registry” with homemade `artifactType`-like tagging, schema validation, or compatibility checks outside Apicurio
- **Static Git / S3 / GitOps tool-schema catalogs** — monorepo or object-store folders of MCP tool JSON served as a flat catalog without `MCP_TOOL` lifecycle
- **Upstream / community Apicurio MCP tools (non-RH)** — `quay.io/apicurio/apicurio-registry` with `apicurio.mcp-tools.enabled` / experimental flags outside Red Hat build (migrate *into* catalog RH path)
- **Framework-local tool schema registries** — LangChain/LangChain4j/CrewAI in-process tool maps or baked schema bundles used as the org’s only “catalog” of definitions
- **Hard-coded client tool allowlists** — IDE/`mcpServers` or app config that embeds full tool JSON schemas instead of resolving from a shared registry

**Not peers (adjacent catalog jobs):** MCP server / MCP Gateway / MCP Catalog (execute, federate, or deploy *servers*); official MCP Registry / Smithery / Docker MCP Catalog (`server.json` / server metaregistry); A2A Agent Registry (`AGENT_CARD`); Query-based Tool Filtering (runtime relevance subset); Apicurio Registry MCP server alone (NL registry *ops*); plain Apicurio schema registry (Avro/Protobuf/JSON Schema only, no `MCP_TOOL`).

## Detection aliases

- Duplicated schemas: ConfigMap/Helm/YAML tool JSON; hard-coded `inputSchema` in prompts; OpenAPI-as-tool-schema copies; comments “don’t scatter tool schemas” / “central tool schema registry”
- Spreadsheets/wikis: “available tools” sheets; tool parameter wikis; agent catalog markdown without Apicurio
- `tools/list` scrapers: crawl/fetch loops over MCP `tools/list`; homemade “tool definition index” from live servers; static re-export of scraped tool JSON
- DIY well-known: custom `/.well-known/mcp-tools`, `/.well-known/mcp-tools/{id}`, homemade `McpToolSearchResults` / name+parameter search APIs outside Apicurio
- DIY stores: homemade `MCP_TOOL` DB/Git; schema compatibility checks on tool inputs; ADRs “govern MCP tool definitions” / “don’t rely on live servers alone for the catalog”
- Static catalogs: Git/S3 folders of `*tool*.json` / MCP tool schemas; GitOps tool-definition bundles without `artifactType: MCP_TOOL`
- Upstream Apicurio MCP tools: `quay.io/apicurio/apicurio-registry`, `apicurio.mcp-tools.enabled`, `apicurio.features.experimental.enabled`, `MCP_TOOL`, `X-Registry-ArtifactType: MCP_TOOL` (non-RH images/docs)
- Framework-local: LangChain/LangChain4j/CrewAI local tool schema maps; baked tool-definition bundles as sole catalog
- Hard-coded allowlists: full tool JSON in client config; IDE tool schema embeds with no shared registry resolve
- Protocol markers (need-for-registry): MCP schema `2025-11-25` tool defs; desire for `inputSchema` breaking-change governance; search tools by name/parameter before wiring clients

## Row (for table)

| Duplicated tool schemas in ConfigMaps/YAML/prompts; spreadsheets/wikis of available tools; scrapers of live tools/list into static catalogs; DIY /.well-known/mcp-tools search catalogs; DIY MCP_TOOL / tool-definition stores; static Git/S3/GitOps tool-schema catalogs; upstream/community Apicurio MCP tools (non-RH); framework-local LangChain/LangChain4j/CrewAI tool schema maps; hard-coded client tool JSON allowlists | MCP Tool Registry | ConfigMap/Helm tool inputSchema / hard-coded tool schemas in prompts; available-tools spreadsheet/wiki; scrape tools/list → static catalog; DIY /.well-known/mcp-tools / name+parameter search; homemade MCP_TOOL store / schema compatibility; Git/S3 tool JSON catalogs; quay.io/apicurio/apicurio-registry apicurio.mcp-tools.enabled (non-RH); MCP_TOOL outside RH build; LangChain/LangChain4j/CrewAI local tool maps; baked tool JSON in mcpServers/client config; govern MCP tool definitions ADR |
