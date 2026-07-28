# Llama Stack (Operator)

Turnkey **agentic + RAG runtime** on OpenShift AI: inference, embeddings, vector storage, and retrieval behind OpenAI-compatible Chat Completions / Responses APIs, managed via `LlamaStackDistribution`. Peers are multi-agent frameworks, DIY tool loops, and standalone Llama Stack / Compose “AI platform” stacks used instead of (or before) the RHOAI Llama Stack Operator.

## Peers

- LangGraph — graph/`StateGraph` multi-step tool agents (`create_react_agent`, `ToolNode`)
- CrewAI — multi-agent `Agent`/`Task`/`Crew`/`Process` (and Flows) orchestration
- AutoGen / AG2 — `AssistantAgent` tool loops, `GroupChat` / legacy `UserProxyAgent` crews
- OpenAI Agents SDK — `Agent`/`Runner`/`function_tool` multi-turn tool agents
- Semantic Kernel Agents — `ChatCompletionAgent` / `FunctionChoiceBehavior.Auto` (.NET/Python)
- LlamaIndex agents — `FunctionAgent` / `ReActAgent` / `AgentWorkflow`
- DIY agent loops — hand-rolled `while tool_calls` / `max_iterations` ReAct dispatchers
- Standalone llama-stack — upstream `llama-stack` / `LlamaStackClient` without RHOAI operator
- Homegrown agent platform Compose/Helm — vLLM + vector DB + custom agent API bundled by hand
- LangChain `ChatOpenAI(base_url=…)` + `bind_tools` / react agents against a self-hosted multi-turn stack

## Detection aliases

- LangGraph: `langgraph`, `langgraph-prebuilt`, `StateGraph`, `create_react_agent`, `ToolNode`, `tools_condition`, `MemorySaver`, `CompiledGraph`, `add_conditional_edges`
- CrewAI: `crewai`, `crewai-tools`, `from crewai import Agent, Task, Crew, Process`, `@CrewBase`, `@agent`/`@task`/`@crew`, `Process.sequential`/`Process.hierarchical`, `crewai.flow`
- AutoGen / AG2: `autogen-agentchat`, `autogen-core`, `AssistantAgent`, `GroupChat`, `GroupChatManager`, `max_tool_iterations`, `pyautogen`, `from autogen import AssistantAgent, UserProxyAgent, ConversableAgent`, `OAI_CONFIG_LIST`
- OpenAI Agents SDK: `openai-agents`, `from agents import Agent, Runner, function_tool`, `Runner.run` / `Runner.run_sync`
- Semantic Kernel: `semantic-kernel`, `Microsoft.SemanticKernel.Agents`, `ChatCompletionAgent`, `FunctionChoiceBehavior.Auto`
- LlamaIndex agents: `FunctionAgent`, `ReActAgent`, `AgentWorkflow`, `llama_index.core.agent`
- DIY loops: `while`/`for` around `chat.completions.create(..., tools=...)` until `not message.tool_calls`; `role: "tool"` + `tool_call_id`; `max_iterations`/`max_turns`/`max_tool_iterations`; custom `TOOLS = {...}` / `register_tool` maps
- OpenAI-compatible stack clients: `client.responses.create(` / `responses.create` with tools; `ChatOpenAI(base_url=...)` + `bind_tools` against non-`api.openai.com`
- Standalone / already-on Llama Stack: `llama-stack`, `llama-stack-client`, `LlamaStackClient`; `kind: LlamaStackDistribution` (`llamastack.io`); DSC `llamastackoperator: Managed`; `app=llama-stack`, service `:8321` / `…/v1`; OGX rename `OGXServer` / `ogx.io` / `ogx-k8s-operator`
- Homegrown platform: Compose/Helm bundling vLLM + pgvector/Milvus/Qdrant + custom agent API; docs “multi-agent” / “agent swarm” / “ReAct agent” / “orchestrator agent”

## Row (for table)

| LangGraph; CrewAI; AutoGen/AG2; OpenAI Agents SDK; Semantic Kernel Agents; LlamaIndex agents; DIY while-tool_calls / max_iterations loops; standalone llama-stack / LlamaStackClient (no RHOAI operator); homegrown Compose/Helm vLLM+vector+agent API; LangChain ChatOpenAI(base_url)+bind_tools against self-hosted multi-turn stack | Llama Stack (Operator) | langgraph / StateGraph / create_react_agent / ToolNode; crewai / Agent,Task,Crew,Process / @CrewBase; autogen-agentchat / AssistantAgent / GroupChat / pyautogen / UserProxyAgent; openai-agents / Agent,Runner,function_tool; semantic-kernel / ChatCompletionAgent; FunctionAgent/ReActAgent/AgentWorkflow; max_iterations/max_tool_iterations / role:tool tool_call_id; responses.create + tools; ChatOpenAI(base_url)+bind_tools; llama-stack / LlamaStackClient / LlamaStackDistribution / llamastackoperator Managed / :8321/v1; OGXServer/ogx.io |
