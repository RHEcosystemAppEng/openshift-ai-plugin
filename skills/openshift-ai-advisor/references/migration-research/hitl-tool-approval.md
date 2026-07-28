# HITL Tool Approval

OpenShift Lightspeed **operation approvals** pause selected MCP tool calls for human confirmation in the console before the service executes them (`OLSConfig` `toolsApprovalConfig`: `approvalType` `never`|`always`|`tool_annotations`, `approvalTimeout` default 600s). Peers are framework/client pause-before-tool gates and DIY approval UIs that solve the same human-in-the-loop tool-execution job outside (or before adopting) Lightspeed HITL.

## Peers

- **LangGraph interrupt / resume** — `interrupt(...)` inside tools/nodes; `Command(resume=…)` with a checkpointer; pause graph until a human approves or edits
- **LangChain / Deep Agents HITL middleware** — `HumanInTheLoopMiddleware` / `interrupt_on={…}` (approve / edit / reject / respond before tool runs)
- **OpenAI Agents SDK approvals** — `needs_approval`, `require_approval` (`always`/`never`), `ToolApprovalItem`, `result.interruptions`, `state.approve` / `state.reject` (function tools and MCP servers)
- **CrewAI tool hooks** — `@before_tool_call` returning `False` to block; `context.request_human_input(...)` as an approval gate
- **AutoGen / MagenticOne HITL** — `UserProxyAgent`, `approval_func` / `ApprovalRequest`→`ApprovalResponse`, MagenticOne `hil_mode`
- **Claude Agent SDK / Claude Code permissions** — `canUseTool`, `PreToolUse` hooks, permission modes (`default`/`plan`/`bypassPermissions`), allow/ask/deny rules
- **LlamaIndex human-in-the-loop** — `InputRequiredEvent` / `HumanResponseEvent`, `ctx.wait_for_event(...)` before dangerous tools
- **Mastra (and similar) tool approval** — `requireToolApproval` plus MCP annotation-driven policy (`readOnlyHint` / `destructiveHint`)
- **MCP host / IDE confirmation dialogs** — Cursor/Claude/VS Code (and other hosts) prompting before `tools/call` for non-read or destructive tools
- **DIY pending-action approval UIs** — custom “approve before mutate” consoles, polling pending-action APIs, Impri-style wrappers around agent tools

**Not peers (adjacent catalog jobs):** MCP Gateway Authorization / Connectivity Link `AuthPolicy` (who-may-call-which-tool); MCP Authorization Server / Keycloak (OAuth AS); Query-based Tool Filtering (relevance selection, not execute approval); MCP Gateway alone (federation); plain RBAC / `read_only` allowlists (access ≠ human confirm-this-call); generic chat “ask the user” without gating tool side effects.

## Detection aliases

- LangGraph: `interrupt(`, `Command(resume=`, checkpointer + human resume; `HumanInTheLoopMiddleware`, `interrupt_on=`
- OpenAI Agents: `needs_approval`, `require_approval`, `ToolApprovalItem`, `result.interruptions`, `state.approve` / `state.reject`
- CrewAI: `@before_tool_call`, `before_tool_call`, `request_human_input`
- AutoGen: `UserProxyAgent`, `approval_func`, `ApprovalRequest`, `ApprovalResponse`, MagenticOne `hil_mode`
- Claude: `canUseTool`, `PreToolUse`, `bypassPermissions`, permission ask/deny rules
- LlamaIndex: `InputRequiredEvent`, `HumanResponseEvent`, `wait_for_event` before tools
- Mastra / annotation clients: `requireToolApproval`, MCP `readOnlyHint` / `destructiveHint` / `idempotentHint` / `openWorldHint` driving client confirms
- IDE/host UX: “require approval for non-read MCP tools”, confirmation before `tools/call`
- DIY: pending-action APIs, “approve before tools/call”, “pause agent until human confirms”, Impri-style approval services
- Design language: “human-in-the-loop tool approval”, “operation approvals”, HITL for mutating tools

## Row (for table)

| LangGraph `interrupt`/`Command(resume=)` + checkpointer; LangChain `HumanInTheLoopMiddleware`/`interrupt_on`; OpenAI Agents `needs_approval`/`require_approval`/`ToolApprovalItem`; CrewAI `@before_tool_call`/`request_human_input`; AutoGen `approval_func`/`UserProxyAgent`/MagenticOne `hil_mode`; Claude `canUseTool`/`PreToolUse`/permission modes; LlamaIndex `InputRequiredEvent`/`HumanResponseEvent`; Mastra `requireToolApproval` + MCP `readOnlyHint`/`destructiveHint`; IDE/MCP-host confirm-before-`tools/call`; DIY pending-action approval UIs | HITL Tool Approval | interrupt( / Command(resume=; HumanInTheLoopMiddleware / interrupt_on; needs_approval / require_approval / ToolApprovalItem / result.interruptions; @before_tool_call / request_human_input; UserProxyAgent / approval_func / hil_mode; canUseTool / PreToolUse / bypassPermissions; InputRequiredEvent / HumanResponseEvent; requireToolApproval; readOnlyHint / destructiveHint; confirm before tools/call; pending-action approval UI; “human-in-the-loop tool approval” |
