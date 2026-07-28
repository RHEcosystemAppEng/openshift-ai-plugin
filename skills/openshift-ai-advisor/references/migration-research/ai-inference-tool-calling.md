# AI Inference Tool Calling

RHOAI / Red Hat AI Inference (vLLM) serving config that enables structured OpenAI-compatible `tools` / `tool_calls` via `--enable-auto-tool-choice`, model-family `--tool-call-parser`, and (when needed) `tool_chat_template_*.jinja`. The server formats model↔tool messages; the client executes tools. Peers are non-RHAIIS stacks that solve the same inference-layer job.

## Peers

- **SGLang tool calling** — `sglang.launch_server` / `sglang serve` with `--tool-call-parser` (`qwen25`, `pythonic`, …) and optional tool chat templates; OpenAI-compatible `tools` / `tool_choice`
- **Hugging Face TGI tools** — Text Generation Inference Messages API `/v1/chat/completions` with `tools` + `tool_choice` (grammar/guidance path)
- **TensorRT-LLM tool parsers** — `trtllm-serve --tool_parser` (`auto`, `qwen3`, `deepseek_v3`, `glm4`, …)
- **llama.cpp function calling** — `llama-server` with `--jinja` / tools-enabled chat templates (`chat_template_tool_use`, custom `.jinja`)
- **Ollama tools API** — local `/api/chat` or OpenAI-compat `/v1` with `tools` / `tool_calls` (no RHAIIS templates)
- **Upstream vLLM tool calling (non-RHOAI)** — plain `vllm serve` + `--enable-auto-tool-choice` + `--tool-call-parser` outside RHAIIS / RHOAI ServingRuntime (migrate *into* catalog path)
- **Outlines / Jsonformer / Guidance / XGrammar / LMQL** — constrained decoding / schema-guided generation used as a stand-in for function/tool-call argument emission
- **Instructor (local)** — Pydantic/`Mode.TOOLS` or JSON-schema retries against a local OpenAI base URL without RHAIIS parser/templates
- **DIY tool-call parsers** — hand-rolled regex/`json.loads` extraction of `name`/`arguments` from free-form model text; custom `ToolParser` plugins outside RHAIIS
- **Hand-rolled OpenAI tools loops** — client `tools=` + `message.tool_calls` + `role:"tool"` against Transformers/`from_pretrained`, HF Inference, or other local servers **without** RHAIIS `--tool-call-parser` / `tool_chat_template_*.jinja`

**Not peers (adjacent catalog jobs):** MCP Gateway / MCP Catalog / MCP Tool Registry (shared tool transport & governance); Kagenti / agent runtimes (planning, memory, multi-agent); cloud-only OpenAI/Anthropic tool APIs with no local inference stack.

## Detection aliases

- `sglang.launch_server`, `sglang serve`, SGLang `--tool-call-parser`, `FunctionCallParser`, `/parse_function_call`
- `text-generation-inference`, `ghcr.io/huggingface/text-generation-inference`, TGI `tools=` / Messages API tool_choice
- `trtllm-serve`, TensorRT-LLM `--tool_parser`, `ToolParserFactory`
- `llama-server`, `llama.cpp` function calling, `--jinja`, `chat_template_tool_use`, `parallel_tool_calls`
- `ollama`, `localhost:11434/api/chat`, Ollama `tools` / `tool_calls`
- upstream `vllm serve` / `python -m vllm.entrypoints.openai.api_server` + `--enable-auto-tool-choice` + `--tool-call-parser` (non-RHAIIS images/args)
- `outlines`, `jsonformer`, `guidance`, `xgrammar`, `lmql`, `guided_json` / grammar-constrained tool schemas
- `instructor`, `instructor.Mode.TOOLS`, `instructor.Mode.JSON` against local `base_url`
- DIY: `json.loads`/`re.search` for tool `name`/`arguments`; custom `ToolParser` / `ToolParserManager.register_module` outside RHAIIS; “parse function call from completion”
- Client loops: `tools=[{type:function…}]`, `tool_choice="auto"|"required"`, `message.tool_calls`, `role:"tool"` / `tool_call_id` against **local** OpenAI base URL without RHAIIS `tool_chat_template_*.jinja`

## Row (for table)

| SGLang `--tool-call-parser`; TGI Messages API tools; TensorRT-LLM `--tool_parser`; llama.cpp function calling (`llama-server --jinja`); Ollama tools API; upstream vLLM `--enable-auto-tool-choice` outside RHAIIS; Outlines / Jsonformer / Guidance / XGrammar / LMQL constrained decoding as tool-calling; Instructor local TOOLS/JSON modes; DIY regex/JSON tool-call parsers; hand-rolled OpenAI `tools`/`tool_calls` loops against local models without RHAIIS templates | AI Inference Tool Calling | sglang.launch_server / --tool-call-parser; FunctionCallParser; text-generation-inference tools; trtllm-serve --tool_parser; llama-server --jinja / chat_template_tool_use; ollama /api/chat tools; vllm serve --enable-auto-tool-choice (non-RHAIIS); outlines; jsonformer; guidance; xgrammar; lmql; guided_json; instructor.Mode.TOOLS; DIY json.loads tool name/arguments; tools=[{type:function}]; tool_choice; message.tool_calls; role:"tool" against local base_url without tool_chat_template_*.jinja |
