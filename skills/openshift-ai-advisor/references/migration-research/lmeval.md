# LM Evaluation (LMEval)

Batch / job-based **LLM capability scoring** on lm-evaluation-harness–style tasks (MMLU, GSM8K, HellaSwag, ARC, toxicity, perplexity, custom YAML tasks) via TrustyAI `LMEvalJob`. Peers are standalone harnesses, leaderboard frameworks, Unitxt recipes, and DIY MMLU-style notebooks/CI that teams run instead of (or before) the RHOAI CRD path.

## Peers

- EleutherAI lm-evaluation-harness (standalone) — `lm-eval` / `lm_eval` CLI + `simple_evaluate()` against HF/vLLM/API models; primary upstream of TrustyAI LMEval
- HELM (Stanford CRFM) — Holistic Evaluation of Language Models (`crfm-helm`, `helm-run`) multi-scenario capability leaderboards
- OpenCompass — Shanghai AI Lab open LLM evaluation platform (`opencompass`, configs for MMLU/CMMLU/… suites)
- LightEval (Hugging Face) — `lighteval` CLI/package for HF/vLLM model capability benches (DIY single-framework; multi-provider hub → **EvalHub**)
- DIY MMLU / GSM8K / HellaSwag / ARC notebooks — hand-rolled accuracy loops and comparison tables without a harness CR
- Unitxt (standalone) — `unitxt` cards/templates/recipes (`cards.*`, `templates.*`) outside `LMEvalJob` `taskRecipes`
- Open LLM Leaderboard reproduction — HF leaderboard / `leaderboard*` task-group scripts cloning BBH, GPQA, MMLU-Pro, IFEval, MATH-hard
- OpenAI Evals — `oaieval` / `evals` registry YAML evals for model capability/regression gates
- PromptBench (Microsoft) — prompt robustness + standard benchmark suite runner against LLMs
- InstructEval — instruction-following / capability eval toolkit used as a harness substitute
- BIG-bench / BBH DIY — Google BIG-bench or BIG-bench Hard task runners outside Eleuther packaging
- Hugging Face `evaluate` + task metrics — `evaluate.load("accuracy"|"mmlu"|…)` notebooks scoring generative models
- Forked / vendor harness trees — `red-hat-data-services/lm-evaluation-harness` or org forks with `--include_path` custom tasks
- CI bake-offs vs completions endpoints — GitHub Actions/Tekton/Jenkins installing harness and hitting `/v1/completions` for score gates only

**Not peers (adjacent catalog jobs):** **EvalHub** (multi-provider orchestration + collections/SDK across lm-eval + Garak + GuideLLM + LightEval); **RAGAS** (RAG faithfulness/retrieval, not standalone LLM harness); **Automated Risk Assessment** (adversarial safety ASR, not MMLU leaderboards); **Guardrails** (runtime rails); **Model Monitoring (TrustyAI)** (tabular/OVMS drift/bias); **Gen AI Playground** (interactive try-out, not systematic scoring). App-level pytest LLM assertions (DeepEval/Braintrust prompt unit tests) are also out of scope.

## Detection aliases

- Eleuther harness: `lm-eval`, `lm_eval`, `lm-evaluation-harness`, `import lm_eval`, `lm_eval.simple_evaluate`, `EleutherAI/lm-evaluation-harness`, `--tasks mmlu|hellaswag|gsm8k|arc_`, `--model hf|vllm|local-completions|openai-completions`
- HELM: `crfm-helm`, `helm-run`, `helm-summarize`, `stanford-crfm/helm`, `from helm.`
- OpenCompass: `opencompass`, `from opencompass`, `open-compass/opencompass`, OpenCompass configs/suites
- LightEval: `lighteval`, `pip install lighteval`, `lighteval accelerate`, `HuggingFaceH4/lighteval`, `from lighteval`
- DIY notebooks: notebooks/scripts titled eval/benchmark/leaderboard; tables comparing models on MMLU/GSM8K/HellaSwag/ARC accuracy; manual `model(...).loss` / perplexity loops for checkpoint compare
- Unitxt: `unitxt`, `cards.`, `templates.`, `tasks.classification`, `"__type__": "task_card"`, `load_hf` in recipe JSON
- Open LLM Leaderboard: `leaderboard`, `leaderboard_*`, “Open LLM Leaderboard”, BBH/GPQA/MMLU-Pro/IFEval/MATH-hard reproduction
- OpenAI Evals: `oaieval`, `openai/evals`, `evals.elsuite`, registry YAML under `evals/`
- PromptBench: `promptbench`, `microsoft/promptbench`, `from promptbench`
- InstructEval: `instruct-eval`, `instruct_eval`, InstructEval harness scripts
- BIG-bench / BBH: `bigbench`, `BIG-bench`, `bbh`, `bigbench_hard`
- HF evaluate: `import evaluate`, `evaluate.load(`, `evaluate` metric + generative model scoring notebooks
- Forked harness: `red-hat-data-services/lm-evaluation-harness`, `--include_path`, custom `lm_eval/tasks/*.yaml` with `doc_to_text` / `output_type: multiple_choice|loglikelihood`
- CI vs completions: CI installing `lm-eval`/`lm_eval` against InferenceService `…/v1/completions` for scoring only; `loglikelihood_rolling` / `bits_per_byte` result dumps
- RHOAI already-on path: `kind: LMEvalJob`, `trustyai.opendatahub.io`, `spec.taskList.taskNames`, `taskRecipes`, DSC `trustyai.eval.lmeval.permitOnline`

## Row (for table)

| EleutherAI lm-evaluation-harness (standalone); HELM; OpenCompass; LightEval (DIY); DIY MMLU/GSM8K/HellaSwag/ARC notebooks; Unitxt (standalone); Open LLM Leaderboard reproduction; OpenAI Evals; PromptBench; InstructEval; BIG-bench/BBH DIY; HF evaluate + task metrics; forked/vendor harness trees; CI bake-offs vs completions endpoints | LM Evaluation (LMEval) | lm-eval / lm_eval / simple_evaluate / EleutherAI/lm-evaluation-harness / --tasks mmlu|hellaswag|gsm8k; crfm-helm / helm-run; opencompass / open-compass; lighteval / HuggingFaceH4/lighteval; DIY MMLU notebooks / leaderboard tables; unitxt / cards.* / templates.*; leaderboard_* / Open LLM Leaderboard; oaieval / openai/evals; promptbench; instruct-eval; bigbench / bbh; evaluate.load(; red-hat-data-services/lm-evaluation-harness / --include_path; CI lm-eval vs /v1/completions; LMEvalJob / trustyai.opendatahub.io |
