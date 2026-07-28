# Gen AI Playground

Interactive **dashboard experimentation** with deployed (and external) generative models **before** application integration: prompt/parameter tuning, optional RAG knowledge, MCP tools, side-by-side comparison, and Python starter export. Peers are self-hosted chat playgrounds, code-first Gradio/Streamlit/Chainlit LLM demos, and curl-only try-the-model workflows that teams use instead of (or before) adopting RHOAI Gen AI studio Playground. Technology Preview—not a production chat product or eval/guardrails/RAG platform substitute.

## Peers

- Open WebUI — self-hosted ChatGPT-style UI on Ollama / OpenAI-compatible / vLLM endpoints (Compose, Helm, OpenShift blogs)
- LibreChat — multi-endpoint chat UI with `librechat.yaml` custom `baseURL` to cluster inference
- AnythingLLM / LobeChat / Hugging Face chat-ui / chatbot-ui — self-hosted ChatGPT clones pointed at OpenAI-compatible bases
- oobabooga / text-generation-webui — local interactive model try-out UI
- Gradio `ChatInterface` / `Chatbot` demos — HF Spaces / `app.py` chat + temperature/system-prompt `additional_inputs`
- Streamlit `st.chat_*` apps — conversational demos with sidebar temperature/model/system-prompt controls
- Chainlit — code-first `@cl.on_message` chat UI (often MCP-aware) against served models
- Ollama + Open WebUI Compose stacks — local “AI playground” equivalent of dashboard try-out
- curl / Postman / httpx-only try-the-model — scripts to `/v1/chat/completions` with no product UI
- Notebook prompt loops — hardcoded prompt/temperature cells or dual-tab InferenceService compare spreadsheets

## Detection aliases

- Open WebUI: `ghcr.io/open-webui/open-webui`, `open-webui/open-webui`, `OLLAMA_BASE_URL`, `OPENAI_API_BASE_URL(S)`, `OPENAI_API_KEYS`, `ENABLE_OPENAI_API`, `WEBUI_AUTH`, volume `/app/backend/data`, service `open-webui`, port `3000:8080`
- LibreChat: `librechat.yaml`, `endpoints.custom`, `baseURL`, `ghcr.io/danny-avila/librechat`
- Other self-hosted chat UIs: `anythingllm`, LobeChat, `huggingface/chat-ui` (`OPENAI_BASE_URL`), `mckaywrigley/chatbot-ui`, `oobabooga` / `text-generation-webui` / `textgen`
- Gradio: `gr.ChatInterface(`, `gradio.ChatInterface`, `gr.Chatbot`, `additional_inputs=[` + `gr.Slider` Temperature / max tokens / top_p, `demo.launch()`, HF Spaces chatbot `app.py`
- Streamlit: `st.chat_message`, `st.chat_input`, `st.write_stream`, `st.sidebar.slider("Temperature"`, `chat.completions.create`
- Chainlit: `chainlit`, `@cl.on_message`, `chainlit run`
- DIY / qualitative try-out: `curl` / Postman / `httpx` to `/v1/chat/completions`; paths/titles `playground`, `chat_demo`, `llm_demo`, `model_sandbox`, `prompt_playground`; “try the model before app integration”
- RHOAI playground (already adopted): Gen AI studio → Playground; Settings tabs Model / Prompt / Knowledge / MCP; ConfigMap `gen-ai-aa-mcp-servers` in `redhat-ods-applications`; Prompt tab → MLflow saved prompts

## Row (for table)

| Open WebUI; LibreChat; AnythingLLM / LobeChat / HF chat-ui / chatbot-ui; oobabooga / text-generation-webui; Gradio ChatInterface / Chatbot demos; Streamlit st.chat_* apps; Chainlit; Ollama+Open WebUI Compose; curl/Postman/httpx-only try-the-model; notebook prompt/temperature loops | Gen AI Playground | open-webui / ghcr.io/open-webui/open-webui / OLLAMA_BASE_URL / OPENAI_API_BASE_URL / WEBUI_AUTH; librechat.yaml / ghcr.io/danny-avila/librechat; anythingllm / huggingface/chat-ui / chatbot-ui / text-generation-webui; gr.ChatInterface / gradio.ChatInterface / gr.Chatbot / additional_inputs Temperature; st.chat_message / st.chat_input / st.write_stream; chainlit / @cl.on_message; curl|/v1/chat/completions try-out; playground/chat_demo/llm_demo paths; gen-ai-aa-mcp-servers / Gen AI studio Playground |
