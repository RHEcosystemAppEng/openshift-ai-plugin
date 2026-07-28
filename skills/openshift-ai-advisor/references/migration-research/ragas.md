# RAGAS Evaluation Provider

Objective **RAG pipeline quality metrics**—retrieval quality (context precision/recall), answer relevance, and factual consistency / faithfulness to retrieved context—via TrustyAI / Llama Stack evaluation provider modes (inline vs remote/pipeline). Measures RAG config quality for iteration and CI gates; does not replace the RAG stack or enforce request-time policy. Peers are standalone Ragas, TruLens/DeepEval/LangSmith RAG evaluators, Phoenix/trace groundedness judges, and DIY claim-vs-context / faithfulness harnesses that teams run instead of (or before) the RHOAI provider.

## Peers

- Standalone Ragas (vibrantlabsai / explodinggradients) — `pip install ragas`, `from ragas import evaluate`, Faithfulness / AnswerRelevancy / ContextPrecision / ContextRecall metrics over `(question, contexts, answer)` datasets; primary upstream of the RHOAI provider
- TruLens RAG triad — `trulens` / `trulens-eval` groundedness, context_relevance, answer_relevance dashboards and feedback functions
- DeepEval RAG metrics — `deepeval` `FaithfulnessMetric`, `ContextualPrecisionMetric`, `ContextualRecallMetric`, `HallucinationMetric`; pytest-plugin CI gates
- LangSmith / LangChain RAG evaluators — dataset evaluators and trace scorers for groundedness / context relevance on RAG runs
- Arize Phoenix / OpenInference span evals — trace-based “hallucination vs retrieved context” / groundedness labels on RAG spans
- DIY faithfulness / groundedness judges — claim decomposition or NLI-style “is claim supported by context?” loops; custom hallucination-rate / citation-accuracy scripts over retrieved chunks
- DIY RAG eval harnesses — notebooks logging `question` + retrieved contexts + answer, then scoring with a judge LLM or hand thresholds (`faithfulness ≥ 0.8`)
- LlamaIndex / LangChain eval modules (standalone) — built-in faithfulness / relevancy evaluators outside TrustyAI provider wiring
- ARES / RAGChecker / similar OSS RAG evaluators — research/framework alternatives scoring retrieval + generation quality on golden sets
- Continuous RAG regression CI — GitHub Actions / Tekton / CircleCI jobs failing on faithfulness / context_recall / answer_relevancy thresholds without RHOAI CRs

**Not peers (adjacent catalog jobs):** **LM Evaluation (LMEval)** / **EvalHub** (standalone LLM capability harnesses, not retrieval/faithfulness); **Guardrails (NeMo Guardrails)** (runtime content/PII/topic filtering); **Model Monitoring (TrustyAI)** (tabular/OVMS drift/bias); **RAG Stack** (deploy ingest→retrieve infra); **AutoRAG** (search/sweep chunk×embedding×retrieval *using* these metrics as objectives); **Gen AI Playground** (qualitative try-out, not reproducible metric jobs).

## Detection aliases

- Standalone Ragas: `ragas`, `pip install ragas`, `from ragas import evaluate`, `EvaluationDataset`, `ragas.evaluate`, explodinggradients/ragas, vibrantlabsai/ragas, docs.ragas.io
- Ragas metrics / columns: `Faithfulness`, `AnswerRelevancy` / `answer_relevancy`, `ContextPrecision` / `context_precision`, `ContextRecall` / `context_recall`, `LLMContextRecall`, `FactualCorrectness`, `answer_correctness`, `answer_similarity`; dataset cols `question`/`user_input`, `answer`/`response`, `contexts`/`retrieved_contexts`, `ground_truth`/`reference`
- Judge wiring: `ragas.llms.llm_factory`, `LangchainLLMWrapper`, evaluator `llm=` / `embeddings=`
- TruLens: `trulens`, `trulens-eval`, RAG triad `groundedness` / `context_relevance` / `answer_relevance`
- DeepEval: `deepeval`, `FaithfulnessMetric`, `ContextualPrecisionMetric`, `ContextualRecallMetric`, `HallucinationMetric`, deepeval pytest plugin
- LangSmith / LangChain: LangSmith RAG dataset evaluators, groundedness / context-relevance scorers on RAG traces
- Phoenix / DIY: Arize Phoenix span evals “hallucination vs retrieved context”; claim-vs-context / NLI faithfulness loops; “faithfulness ≥ …”, “retrieval regression gate”, “groundedness”
- Vocabulary (framework-agnostic): faithfulness, groundedness, answer relevancy/relevance, context precision, context recall, factual consistency to retrieved context
- RHOAI already-on path: `ENABLE_RAGAS: "true"`, `trustyai_ragas` / `trustyai_ragas_inline` / `trustyai_ragas_remote`, `inline::trustyai_ragas` / `remote::trustyai_ragas`, `llama-stack-provider-ragas`, `kubeflow-ragas-config`, `EMBEDDING_MODEL` / `TRUSTYAI_EMBEDDING_MODEL`, `client.alpha.eval.run_eval` with ragas `benchmark_id` / scoring functions, `trustyai-explainability/llama-stack-provider-ragas`

## Row (for table)

| Standalone Ragas (vibrantlabsai/explodinggradients); TruLens RAG triad; DeepEval Faithfulness/Contextual* metrics; LangSmith/LangChain RAG evaluators; Arize Phoenix span groundedness evals; DIY faithfulness/groundedness/claim-vs-context judges; DIY RAG eval harnesses + CI threshold gates; LlamaIndex/LangChain standalone eval modules; ARES/RAGChecker-style OSS RAG evaluators | RAGAS Evaluation Provider | ragas / from ragas import evaluate / Faithfulness / AnswerRelevancy / ContextPrecision / ContextRecall / EvaluationDataset; trulens / trulens-eval / groundedness / context_relevance / answer_relevance; deepeval / FaithfulnessMetric / ContextualPrecisionMetric / ContextualRecallMetric; LangSmith RAG evaluators / groundedness scorers; Phoenix hallucination-vs-context; DIY claim-vs-context / faithfulness ≥; ENABLE_RAGAS / trustyai_ragas / llama-stack-provider-ragas / kubeflow-ragas-config |
