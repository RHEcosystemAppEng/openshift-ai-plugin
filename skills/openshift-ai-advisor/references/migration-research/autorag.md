# AutoRAG

RHOAI **Technology Preview** automated pipeline that searches RAG hyperparameters—chunk size/overlap, embedding models, top-k, vector vs hybrid—against a golden QA set and ranks patterns (leaderboard + notebooks). Requires Llama Stack + remote Milvus + Documents RAG Optimization Pipeline. Peers are upstream AutoML-RAG frameworks, ParamTuner/Optuna/Ray Tune sweeps, and DIY chunk×embedding×retrieval bake-offs that teams run instead of (or before) catalog AutoRAG.

## Peers

- Upstream AutoRAG (Marker-Inc-Korea) — OSS RAG AutoML (`pip install AutoRAG` / YAML `node_lines` / `module_type: llama_index_chunk`); **name collision** with RHOAI AutoRAG—same *need* class, different product
- LlamaIndex ParamTuner — `ParamTuner` / `RayTuneParamTuner` / `llama-index-experimental-param-tuner` grid/Ray sweeps over RAG callables (`chunk_size`, `similarity_top_k`, …)
- rag-opt / RAGOpt (GaiaAI-Hub) — automated RAG pipeline optimization toolkit competing on the same search job
- Optuna RAG sweeps — `optuna.create_study` + `trial.suggest_int("chunk_size"|`top_k`|…)` / embedding-id categoricals scoring faithfulness or recall@k
- Ray Tune RAG HPO — `tune.Tuner` / Ray objectives over chunking, retrieval, or embedding choices (often with LlamaIndex RayTuneParamTuner)
- DIY nested chunk / top_k bake-offs — `for chunk_size in [256,512,1024]` × overlap × `top_k` loops; LangChain `RecursiveCharacterTextSplitter` A/B notebooks; embedding-model bake-offs (`BAAI/bge-*`, `e5-*`, …)
- Dense vs hybrid / BM25 A/B scripts — retrieval-strategy comparisons reindexing and scoring the same golden set without a unified optimizer
- Custom leaderboard / compare harnesses — `leaderboard.csv`, `summary.csv`, `compare_results.py`, `benchmark_*.py`, Pareto charts ranking RAG configs
- RAGAS-scored config grids — nested eval loops calling `ragas.evaluate` (faithfulness / answer_correctness / context_*) as the *objective* while hand-rolling the search (metric alone → RAGAS catalog; search driver → AutoRAG)
- Vectara-style / cookbook chunk×embedding benchmarks — one-off corpus studies and HF/LangChain “comparing techniques” notebooks used as standing tuning practice

**Not peers (adjacent catalog jobs):** **RAG Stack** (deploy a fixed ingest→retrieve stack without search); **RAGAS Evaluation Provider** alone (score/gate quality, not drive the sweep); plain LLM eval (**LMEval** / EvalHub); classical tabular AutoML (**AutoML**).

## Detection aliases

- Upstream AutoRAG: `autorag`, `from autorag`, `from autorag.chunker import Chunker`, `AutoRAG`, Marker-Inc-Korea/AutoRAG, YAML `module_type: llama_index_chunk` with `chunk_size: [512, 1024]`, `node_lines`, `summary.csv` from AutoRAG runs
- LlamaIndex ParamTuner: `ParamTuner`, `RayTuneParamTuner`, `llama-index-experimental-param-tuner`, `param_dict = {"chunk_size": [...], "top_k": [...]}`
- rag-opt: `rag-opt`, `rag_opt`, `RAGOpt`, GaiaAI-Hub/rag-opt
- Optuna: `optuna.create_study`, `trial.suggest_int("chunk_size"`, `suggest_categorical` over embedding model ids with RAG metrics
- Ray Tune: `ray.tune`, `tune.Tuner`, Ray objectives naming `chunk_size` / `chunk_overlap` / `top_k` / embedding
- DIY sweeps: `CHUNK_SIZES`, `CHUNK_OVERLAPS`, `for chunk_size in`, `chunk_sizes = [256, 512, 1024]`, `similarity_top_k` / `top_k` / `num_chunks` lists `[3,5,10]`, dense vs hybrid flags in eval scripts
- Bake-off / harness: `leaderboard.csv`, `compare_results.py`, `benchmark_rag`, “optimal chunk size”, “embedding comparison”, “RAG hyperparameter tuning”, “retrieval A/B”
- RAGAS-as-objective: `ragas` / `from ragas import evaluate` **paired with** nested config loops or Optuna (not a lone `evaluate()` gate)
- RHOAI already-on path (migrate *into* / detect product use): `documents-rag-optimization-pipeline`, `pipelines/training/autorag/`, Gen AI studio AutoRAG, `pattern.json` + `indexing_notebook.ipynb` / `inference_notebook.ipynb` artifacts, IBM `ai4rag`

## Row (for table)

| Upstream AutoRAG (Marker-Inc-Korea); LlamaIndex ParamTuner / RayTuneParamTuner; rag-opt / RAGOpt; Optuna RAG sweeps; Ray Tune RAG HPO; DIY nested chunk/top_k/embedding bake-offs; dense vs hybrid A/B scripts; custom leaderboard/compare harnesses; RAGAS-scored config grids (search driver); Vectara-style / cookbook chunk×embedding benchmarks | AutoRAG | autorag / from autorag.chunker / Marker-Inc-Korea AutoRAG / module_type: llama_index_chunk / node_lines; ParamTuner / RayTuneParamTuner / llama-index-experimental-param-tuner / param_dict chunk_size top_k; rag-opt / RAGOpt; optuna.create_study / trial.suggest_int("chunk_size"; ray.tune / tune.Tuner over RAG params; CHUNK_SIZES / for chunk_size in / similarity_top_k [3,5,10]; dense vs hybrid A/B; leaderboard.csv / compare_results.py / “RAG hyperparameter tuning”; ragas.evaluate inside nested sweeps; documents-rag-optimization-pipeline / ai4rag / pattern.json |
