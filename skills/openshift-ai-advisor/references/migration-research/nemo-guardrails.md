# Guardrails (NeMo Guardrails)

TrustyAI-managed **request-time** LLM input/output safety and policy plane on OpenShift AI: sensitive-data (Presidio), regex/content filters, topic/custom Colang rails, guarded `/v1/chat/completions` and `/v1/guardrail/checks`—not offline eval. Peers are DIY/cloud moderation, PII redaction, Llama Guard sidecars, Guardrails AI Hub validators, and standalone `nemoguardrails` stacks used instead of (or before) the RHOAI **NemoGuardrails** CR.

## Peers

- **Standalone NVIDIA NeMo Guardrails** — `nemoguardrails` / `LLMRails` / `RailsConfig` / Colang outside RHOAI (local server, app-embedded, non-TrustyAI deploy)
- **Guardrails AI** — `guardrails` package, `Guard`, Hub validators (`hub://guardrails/…`), RAIL specs (alone or via NeMo `guardrails_ai.validators`)
- **Microsoft Presidio (standalone)** — PII detect/anonymize around chat I/O without NeMo `sensitive_data_detection` flows
- **Llama Guard / ShieldGemma / content-safety DIY** — InferenceService or sidecar classifier that filters prompts/responses before vLLM
- **Moderation sidecars / proxies** — custom FastAPI/Envoy middleware: forbidden-word lists, topic allowlists, toxicity models, then proxy to the LLM
- **OpenAI Moderation API** — `omni-moderation` / `text-moderation` as the sole policy plane
- **Azure AI Content Safety** — cloud prompt/response harm categories + blocklists
- **AWS Bedrock Guardrails** — managed topic/PII/word/contextual grounding filters on Bedrock
- **Lakera / similar SaaS guard APIs** — hosted prompt-injection / content-risk screening
- **LangChain moderation chains** — `OpenAIModerationChain` / custom moderation runnables as the only rails layer
- **Hand-rolled regex / keyword / length gates** — app middleware screening prompts/responses with no dedicated guardrails product

**Not peers (adjacent catalog jobs):** **LMEval** / **EvalHub** (offline capability/toxicity jobs); **RAGAS** (RAG faithfulness metrics); **Automated Risk Assessment** (pre-prod adversarial probing); **Model Monitoring (TrustyAI)** (tabular drift/bias on OVMS); **Gen AI Playground** (exploratory chat without a policy plane). Legacy FMS **GuardrailsOrchestrator** is a superseded RH path—prefer NeMo, not a migration *to* Orchestrator.

## Detection aliases

- Standalone NeMo: `nemoguardrails`, `pip install nemoguardrails`, `from nemoguardrails import LLMRails, RailsConfig`, `RailsConfig.from_path`, `rails.generate` / `generate_async`, `rails.check` / `check_async`, `RailStatus.BLOCKED`, `nemoguardrails server --config`, `@action(is_system_action=True)`, Colang `define flow` / `rails/*.co`
- Config rails: `rails.input.flows` / `rails.output.flows`, `detect sensitive data on input`, `self check input` / `output`, `content safety check`, `topic safety check`, `jailbreak detection`, `llama guard check input`, `rails.config.sensitive_data_detection`, `rails.config.regex_detection`, `rails.config.guardrails_ai.validators`
- Guardrails AI: `guardrails` / `guardrails-ai`, `from guardrails import Guard`, `hub://guardrails/`, RAIL / `Guard.from_rail`
- Presidio DIY: `presidio-analyzer`, `presidio-anonymizer`, `AnalyzerEngine`, `AnonymizerEngine`, entity lists (`EMAIL_ADDRESS`, `CREDIT_CARD`, …) wrapping `chat.completions`
- Llama Guard / classifiers: Llama Guard / ShieldGemma / Nemotron Content Safety / “content-safety-detector” as pre-chat filter; sidecar moderation Deployments
- Cloud moderation: OpenAI `moderations.create` / `omni-moderation`; Azure Content Safety; Bedrock `CreateGuardrail` / `ApplyGuardrail` / `guardrailIdentifier`; Lakera API clients
- LangChain: `OpenAIModerationChain`, moderation runnables / “moderation chain” before LLM
- DIY middleware: forbidden-word lists, topic allowlists, PII regex before/after LLM; “block PII leakage”, “jailbreak filter”, “output validators”
- Already-on RHOAI NeMo: `kind: NemoGuardrails` (`trustyai.opendatahub.io`), `spec.nemoConfigs`, `/v1/guardrail/checks`, guarded `/v1/chat/completions`, `oc get nemoguardrails`
- Legacy distinguish: `kind: GuardrailsOrchestrator` (FMS)—prefer NeMo going forward

## Row (for table)

| Standalone nemoguardrails / LLMRails / Colang (no RHOAI CR); Guardrails AI Guard / Hub validators / RAIL; Presidio Analyzer/Anonymizer DIY; Llama Guard / ShieldGemma / content-safety sidecars; moderation proxies (FastAPI/Envoy keyword/toxicity); OpenAI Moderation API; Azure Content Safety; AWS Bedrock Guardrails; Lakera (and similar SaaS); LangChain OpenAIModerationChain; hand-rolled regex/PII/topic middleware | Guardrails (NeMo Guardrails) | nemoguardrails / LLMRails / RailsConfig / rails.generate / Colang *.co / input.flows; guardrails Guard / hub://guardrails / from_rail; presidio-analyzer / AnonymizerEngine; Llama Guard / ShieldGemma sidecar; moderations.create / omni-moderation; Azure Content Safety; Bedrock ApplyGuardrail; Lakera; OpenAIModerationChain; forbidden-word / PII regex middleware; NemoGuardrails CR / /v1/guardrail/checks (already-on) |
