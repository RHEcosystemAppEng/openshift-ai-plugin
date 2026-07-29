# OpenShift AI Advisor — demo

Ran on: https://github.com/rh-ai-quickstart/ai-driven-network-remediation

```text
/openshift-ai-advisor
```

---

Alot of thinking...

---

## Ranked recommendations

### Additions worth doing

✅ **RAGAS Evaluation Provider** (Verification)  
Problem: AutoRAG tunes chunking (`CHUNK_SIZE_TOKENS` / golden set in `hub/autorag/test-data.json`) but the RAG→analyze path (`rag_retrieval.py` → `analyze.py`) has no faithfulness / context-recall gate, so bad retrieval can still drive remediation RCA.  
Solution: Enable TrustyAI’s RAGAS provider against LlamaStack retrieval + completions; score the existing golden set in CI/pipeline before promoting ingest params.

✅ **Guardrails (NeMo Guardrails)** (Production readiness)  
Problem: The remediation graph calls the LLM for RCA and then invokes mutating MCP tools (`launch_job`, OpenShift writes) with no request-time input/output safety on `analyze.py` / the LlamaStack chat path.  
Solution: Deploy NeMo Guardrails via TrustyAI and route agent (and optionally chatbot) LLM calls through the guarded check/chat endpoints before tool execution.

### Future improvements (not worth it now)

⚠️ **Models-as-a-Service (MaaS)** (Impact: medium, Complexity: low)  
Why not now: Easy config retarget of `ADNR_LLM_*`, but it’s governance/quotas—not a clear AI outcome-quality win on the remediation flow.

⚠️ **Prompt Template Registry** (Impact: medium, Complexity: low)  
Why not now: Easy swap of hardcoded prompts in `analyze.py` / `chat.py`, but versioning alone doesn’t raise RCA/chat quality without an eval loop.

⚠️ **MCP Gateway** (Impact: medium, Complexity: low)  
Why not now: Cleaner federation of the six `noc-*` MCP URIs, but packaging/routing alone doesn’t improve answer or remediation quality until tool authz is layered on.

⚠️ **MCP Gateway Authorization** (Impact: high, Complexity: high)  
Why not now: Real safety win for mutating tools, but needs Connectivity Link + MCP Gateway + AuthPolicy + IdP claim wiring—too heavy as a first step.

⚠️ **MCP server for OpenShift** (Impact: medium, Complexity: high)  
Why not now: Severe tool-contract mismatch with DIY `noc-openshift` (`rollout_restart` / `patch_deployment_memory` vs mostly read-oriented official tools).

⚠️ **Automated Risk Assessment** (Impact: high, Complexity: high)  
Why not now: Valuable pre-prod red-team, but EvalHub + KFP + judge-model setup is a large adoption.

⚠️ **LMEval / Gen AI Playground / MCP Catalog** (Impact: medium or low, Complexity: medium–high)  
Why not now: Capability sandboxes or catalog packaging don’t fix RAG groundedness or agent safety on the live remediation path; Playground/Catalog don’t replace the NOC chat or custom MCP servers.

---

## What would you like to do?

1. **Add RAGAS Evaluation Provider**
2. **Add Guardrails (NeMo Guardrails)**
3. **RAG bundle** (RAGAS + NeMo Guardrails; you already have Llama Stack / AutoRAG)
