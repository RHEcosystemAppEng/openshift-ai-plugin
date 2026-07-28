# Query-based Tool Filtering

OpenShift Lightspeed capability that uses hybrid RAG (dense semantic + sparse/keyword) to select a small, relevant subset of MCP tools per user query before the LLM sees them—cutting token cost and tool-selection interference on large catalogs. Enable via `OLSConfig` `featureGates: ToolFiltering` and tune with `toolFilteringConfig` (`alpha`, `topK`, `threshold`). Peers are other query-time tool-retrieval / semantic tool-filter stacks teams use instead of (or before) Lightspeed **Query-based Tool Filtering**.

## Peers

- LiteLLM MCP Semantic Tool Filter — `litellm_settings.mcp_semantic_tool_filter` (`enabled`, `embedding_model`, `top_k`, `similarity_threshold`); headers `x-litellm-semantic-filter` / `x-litellm-semantic-filter-tools`
- Portkey mcp-tool-filter — `@portkey-ai/mcp-tool-filter` / `MCPToolFilter`; embed tool name/description → cosine top-K + `minScore` / `alwaysInclude`
- dmcp — meta-tool discovery (`search_tools` / vector index over MCP tools, then load schemas on demand)
- mcpfind — RAG-style MCP tool finder / on-demand schema load
- ToolPicker — hybrid BM25 + embeddings (+ RRF / weighted α) for tool routing
- LangChain `LLMToolSelectorMiddleware` — LLM-as-selector (`max_tools`, `always_include`); same *need* (shrink tool list per query), different mechanism than embedding RAG
- Cascade / reranker tool selectors — embeddings → reranker → micro-LLM pick (`tool-selector-cascade` and similar)
- WRITER RAG-MCP / “RAG-MCP” prototypes — retrieve tools then expose schemas
- DIY embed/BM25 over tools — hand-rolled cosine/ANN or BM25 over tool catalogs → `top_k` + threshold; custom hybrid lexical+semantic indexes
- Meta `search_tools` then load schemas — agent exposes a search meta-tool instead of full `tools/list` in every prompt

**Not peers (adjacent catalog jobs):** MCP Gateway Authorization / Kuadrant AuthPolicy / wristband user-based tool ACL (who may call which tool); HITL Tool Approval (human confirm before execute); MCP Gateway (federation only); MCP Tool Registry / MCP Catalog (inventory); Lightspeed `queryFilters` (regex redaction of user questions); static allowlists (`enabled_tools`, hard-coded proxy tool lists) with no query-driven retrieval.

## Detection aliases

- LiteLLM: `mcp_semantic_tool_filter`, `SemanticMCPToolFilter`, `SemanticToolFilterHook`, `litellm_settings.mcp_semantic_tool_filter.enabled`, `embedding_model` / `top_k` / `similarity_threshold`, `x-litellm-semantic-filter`, `x-litellm-semantic-filter-tools`
- Portkey: `@portkey-ai/mcp-tool-filter`, `Portkey-AI/mcp-tool-filter`, `MCPToolFilter`, `minScore`, `alwaysInclude` / `always_include` (Portkey filter options)
- dmcp: `Grep-Juub/dmcp`, dmcp `search_tools` / vector tool index
- mcpfind: `jcgs2503/mcpfind`, mcpfind tool discovery
- ToolPicker: `AshwinUgale/toolpicker`, ToolPicker BM25+embeddings / hybrid tool selection
- LangChain: `LLMToolSelectorMiddleware`, `langchain.agents.middleware.LLMToolSelectorMiddleware`, `max_tools`, `always_include` (middleware)
- Cascade / RAG-MCP: `tool-selector-cascade`, “RAG-MCP”, Writer engineering RAG-MCP, “semantic tool discovery”, “tool retrieval before function calling”
- DIY: embed tool descriptions → cosine/ANN → `top_k` / `similarity_threshold` / `minScore`; BM25/TF-IDF over tool names/descriptions; hybrid lexical+semantic + RRF; meta-tool `search_tools` then load schema; comments/ADRs “too many MCP tools in prompt”, “reduce tool catalog for LLM”

## Row (for table)

| LiteLLM mcp_semantic_tool_filter; Portkey @portkey-ai/mcp-tool-filter; dmcp; mcpfind; ToolPicker (BM25+embeddings); LangChain LLMToolSelectorMiddleware; cascade/reranker tool selectors; WRITER RAG-MCP; DIY embed/BM25/hybrid over tool catalogs; meta search_tools then load schemas | Query-based Tool Filtering | mcp_semantic_tool_filter / SemanticMCPToolFilter / x-litellm-semantic-filter; @portkey-ai/mcp-tool-filter / MCPToolFilter / minScore / alwaysInclude; Grep-Juub/dmcp search_tools; jcgs2503/mcpfind; AshwinUgale/toolpicker; LLMToolSelectorMiddleware / max_tools / always_include; tool-selector-cascade; RAG-MCP; DIY cosine/ANN/BM25 top_k over tools; meta search_tools |
