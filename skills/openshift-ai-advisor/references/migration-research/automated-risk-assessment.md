# Automated Risk Assessment

Technology Preview **pre-production adversarial safety probing** of an LLM (or model-plus-guardrails) OpenAI-compatible endpoint: generate harmful-category prompts, escalate attack strategies (baseline → system-prompt override → translation → TAP), and report bypasses via ASR / per-intent compliance—via EvalHub evaluations API (`garak-kfp` / `intents`) or Kubeflow Pipelines. Peers are DIY LLM vulnerability scanners, red-team frameworks, CI safety gates, and research attack suites that teams run instead of (or before) the RHOAI intents/Garak-KFP path.

## Peers

- **NVIDIA Garak (standalone)** — `garak` CLI / `python -m garak`; probes (`dan`, `promptinject`, `toxicity`, …); HTML/JSONL vuln reports; industry “nmap for LLMs” scanner outside RHOAI `garak-kfp`
- **Microsoft PyRIT** — Python Risk Identification Tool; `PromptSendingAttack`, multi-turn Crescendo/TAP/Skeleton Key; converters + scorers + memory DB; Microsoft AI Red Team automation
- **Promptfoo red-team** — `promptfoo redteam` / YAML plugins (jailbreak, injection, PII, agency); CI/PR-blocking safety regression; OWASP LLM Top 10 / NIST / MITRE ATLAS mappings
- **DeepTeam (Confident AI)** — `deepteam.red_team` / `RedTeamer`; tree/linear/crescendo jailbreak campaigns
- **HarmBench** — `centerforaisafety/HarmBench`; standardized automated red-team eval (GCG, PAIR, TAP, AutoDAN methods)
- **TAP / PAIR / AutoDAN DIY** — Tree-of-Attacks (`RICommunity/TAP`), PAIR (`JailbreakingLLMs`), AutoDAN repos or paper-impl notebooks as the attack loop
- **DIY jailbreak / harm-dataset campaigns** — AdvBench, DAN prompts, harmful-behavior CSVs; manual attacker+judge+target notebooks; custom ASR/promotion gates without a productized scanner
- **Cloud / alt red-team platforms** — Azure AI Red Teaming Agent / Foundry risk-safety evaluators; wandb `rai-toolkit` `rai assess`; SPLX Probe / ARGUS-style attack suites

**Not peers (adjacent catalog jobs):** **Guardrails (NeMo Guardrails)** (runtime request filtering, not offline adversarial campaigns); **EvalHub** alone as capability/multi-provider hub (MMLU/LightEval/GuideLLM without intents/Garak ASR focus—escalate when the *need* is escalating safety probing); **LM Evaluation (LMEval)** (harness accuracy/toxicity scoring, not progressive jailbreak strategies); **RAGAS** (RAG faithfulness/retrieval); **Model Monitoring (TrustyAI)** (tabular OVMS drift/bias); **Gen AI Playground** (qualitative chat, no reproducible ASR report).

## Detection aliases

- Garak DIY: `pip install garak`, `garak --list_probes`, `--probes dan|promptinject|toxicity`, `--model_type` / `--target_type`, `openai.OpenAICompatible`, garak.ai / “LLM vulnerability scanner”
- RHOAI already-on: `"id": "intents"`, `"provider_id": "garak-kfp"`, `garak_pipeline` / `PipelineRunner` / `benchmark="intents"`, `spo.SPOIntent*`, `multilingual.TranslationIntent`, `tap.TAPIntent`, `judge.MulticlassJudge`, ASR / `eval_threshold`, `llama-stack-provider-trustyai-garak`
- PyRIT: `pip install pyrit`, `pyrit_scan` / `pyrit_shell`, `from pyrit.prompt_target import OpenAIChatTarget`, `PromptSendingAttack`, Crescendo / Skeleton Key, “Python Risk Identification Tool”
- Promptfoo: `promptfoo redteam`, `promptfooconfig.yaml`, red-team plugins, GitHub Action red-team gates
- DeepTeam: `pip install deepteam`, `from deepteam import red_team`, `RedTeamer`
- HarmBench / research attacks: `HarmBench`, `centerforaisafety/HarmBench`, PAIR, `tree-of-attacks` / TAP, AutoDAN, GCG
- DIY campaigns: AdvBench, DAN prompts, harmful-behavior CSVs, attacker+judge+target trio, “AI red teaming”, “jailbreak testing”, “attack success rate”, “safety promotion gate”
- Alt platforms: Azure Red Teaming Agent / `builtin.indirect_attack`, `rai assess`, SPLX Probe

## Row (for table)

| NVIDIA Garak (standalone CLI/probes); Microsoft PyRIT (multi-turn red team); Promptfoo `redteam` / CI safety gates; DeepTeam `red_team`/`RedTeamer`; HarmBench (+ GCG/PAIR/TAP/AutoDAN); TAP/PAIR/AutoDAN DIY repos; DIY jailbreak/harm-dataset campaigns (AdvBench/DAN/attacker+judge+target); Azure Red Teaming Agent / wandb rai-toolkit / SPLX-style suites | Automated Risk Assessment | garak --probes / --list_probes / openai.OpenAICompatible; intents / garak-kfp / garak_pipeline / SPOIntent / TAPIntent / MulticlassJudge / ASR; pyrit / OpenAIChatTarget / PromptSendingAttack / Crescendo; promptfoo redteam / promptfooconfig.yaml; deepteam red_team / RedTeamer; HarmBench / PAIR / tree-of-attacks / AutoDAN; AdvBench / DAN / jailbreak datasets; attacker+judge+target; “AI red teaming” / “attack success rate” / safety promotion gate; Azure Red Teaming Agent / rai assess |
