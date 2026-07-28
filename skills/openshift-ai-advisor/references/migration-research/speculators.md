# Speculative Decoding (Speculators)

Technology Preview **Eagle 3 draft/speculator train→store→serve** path for Red Hat AI Inference / vLLM: a small draft proposes tokens the verifier LLM checks in parallel (lossless vs verifier distribution). Peers are other draft-training stacks, multi-head / self-speculative recipes, and engine-native `speculative_config` / draft-model paths used instead of (or before) RH Speculators + `RedHatAI/*-speculator.eagle3`.

**Catalog when-not / confusion (not peers):** untuned speculation that worsens cost/perf; GPU memory that cannot hold draft+verifier; TP unacceptable for SLAs; confusing Speculators with quantization (**LLM Compressor**); preferring plain vLLM when latency is already fine.

## Peers

- SafeAILab EAGLE — original EAGLE / EAGLE-2 / EAGLE-3 research code and draft-head training (`SafeAILab/EAGLE`, `yuhuili/EAGLE*` HF heads)
- SpecForge — SGLang-team EAGLE-3 (and related) draft training framework; SpecBundle HF drafts for SGLang serve
- FasterDecoding Medusa — multi-head Medusa-1/2 training and local generate (`FasterDecoding/Medusa`, Medusa heads on target)
- NVIDIA Model Optimizer speculative — `modelopt.torch.speculative` / `mtsp.convert` Medusa & EAGLE head convert+finetune for TRT-LLM
- Upstream `speculators` (non-RH) — bare `pip install speculators` / `vllm-project/speculators` train/convert without RHAIIS / `RedHatAI/*-speculator.*` packaging
- vLLM engine `speculative_config` DIY — upstream `vllm serve` `--speculative-config` / `--speculative-model` with `eagle3`/`eagle`/`ngram`/`mtp`/`medusa`/`suffix`/`draft_model`/`mlp_speculator` outside RH Speculators checkpoints
- SGLang speculative decoding — `sglang.launch_server` `--speculative-algorithm EAGLE3|EAGLE|NGRAM|STANDALONE|NEXTN` + `--speculative-draft-model-path`
- TensorRT-LLM speculative decoding — `Eagle3DecodingConfig` / YAML `decoding_type: Eagle3` / Medusa / draft-model engines via `trtllm-serve` / Triton TRT-LLM
- IBM MLP Speculator — Medusa-inspired multi-stage MLP accelerators (`method: mlp_speculator`; `ibm-ai-platform/*-accelerator`, `ibm-granite/*-accelerator`)
- Hugging Face assisted generation — Transformers `generate(..., assistant_model=...)` / Universal Assisted Generation (cross-tokenizer)
- HF prompt-lookup / n-gram DIY — `prompt_lookup_num_tokens` or engine `method: ngram` / prompt-lookup without a trained draft
- LayerSkip self-speculation — early-exit draft + deep verify (`assistant_early_exit`, LayerSkip-trained Llama/CodeLlama)
- Lookahead decoding — target-only n-gram / Jacobi-style lookahead (no draft weights)
- llama.cpp speculative — `llama-server` `--model-draft` / `--spec-type draft-eagle3|draft-simple|ngram-*|draft-mtp|draft-dflash`
- LM Studio speculative decoding — desktop draft-model pairing on llama.cpp / MLX engines
- DIY draft+verifier loops — smaller same-family CausalLM propose-K + verifier accept/reject notebooks/scripts outside a serving engine

## Detection aliases

- SafeAILab EAGLE: `SafeAILab/EAGLE`, `yuhuili/EAGLE`, `yuhuili/EAGLE3-`, `EAGLE-LLaMA`, eagle draft head training scripts
- SpecForge: `SpecForge`, `sgl-project/SpecForge`, `SpecBundle`, `lmsys/SGLang-EAGLE3-`, `lmsys/sglang-EAGLE-`
- Medusa: `FasterDecoding/Medusa`, `medusa_heads`, `MedusaModel`, `medusa_model.py`, Medusa-1 / Medusa-2
- NVIDIA ModelOpt speculative: `modelopt.torch.speculative`, `mtsp.convert`, ModelOpt Medusa/EAGLE speculative guides
- Upstream speculators: `pip install speculators`, `from speculators`, `vllm-project/speculators`, `Eagle3Speculator` / `Eagle3DraftModel` without `RedHatAI/` or `rhaii/vllm-cuda-rhel9`
- vLLM speculative_config: `speculative_config`, `--speculative-config`, `--speculative-model`, `--num-speculative-tokens`, `num_speculative_tokens`, methods `eagle3`/`eagle`/`ngram`/`mtp`/`medusa`/`suffix`/`draft_model`/`mlp_speculator`/`dflash`, `draft_tensor_parallel_size`, `prompt_lookup_max`/`prompt_lookup_min`
- SGLang speculative: `--speculative-algorithm`, `--speculative-draft-model-path`, `--speculative-num-steps`, `--speculative-eagle-topk`, `--speculative-num-draft-tokens`, `EAGLE3`/`EAGLE`/`NGRAM`/`STANDALONE`
- TensorRT-LLM speculative: `Eagle3DecodingConfig`, `decoding_type: Eagle3`, `--speculative_decoding_mode`, TRT-LLM Medusa/EAGLE/draft speculative engines
- IBM MLP Speculator: `mlp_speculator`, `ibm-ai-platform/llama3-8b-accelerator`, `ibm-granite/*-accelerator`, `SPECULATOR_NAME`, fms-extras `paged_speculative_inference`
- HF assisted generation: `assistant_model=`, `assisted_decoding`, Universal Assisted Generation, `assistant_tokenizer=`
- Prompt-lookup / n-gram: `prompt_lookup_num_tokens`, `prompt_lookup_decoding`, `method: ngram`, `ngram_gpu`
- LayerSkip: `LayerSkip`, `assistant_early_exit`, self-speculative early exit
- Lookahead: Lookahead decoding, Jacobi decoding / target-only lookahead n-grams
- llama.cpp speculative: `--model-draft`, `-md`, `--spec-draft-model`, `--spec-type`, `draft-eagle3`, `ngram-simple`, `llama-server` draft flags
- LM Studio speculative: LM Studio draft model selector / speculative decoding sidebar (llama.cpp/MLX)
- DIY draft+verifier: ad-hoc small+large `generate` propose/verify loops; acceptance-rate / `k` draft-token tuning scripts without Speculators/`speculators_config`

## Row (for table)

| SafeAILab EAGLE; SpecForge/SpecBundle; FasterDecoding Medusa; NVIDIA ModelOpt speculative; upstream speculators (non-RH); vLLM speculative_config DIY (eagle/ngram/mtp/medusa/suffix/draft/mlp); SGLang --speculative-algorithm; TensorRT-LLM Eagle3/Medusa/draft speculative; IBM MLP Speculator; HF assisted generation; HF prompt-lookup / n-gram; LayerSkip self-speculation; Lookahead decoding; llama.cpp --model-draft/--spec-type; LM Studio draft pairing; DIY draft+verifier loops | Speculative Decoding (Speculators) | SafeAILab/EAGLE / yuhuili/EAGLE*: SpecForge / SpecBundle / lmsys/SGLang-EAGLE3-; FasterDecoding/Medusa / MedusaModel / medusa_heads; modelopt.torch.speculative / mtsp.convert; pip install speculators / vllm-project/speculators without RedHatAI; speculative_config / --speculative-config / eagle3|eagle|ngram|mtp|medusa|suffix|mlp_speculator; --speculative-algorithm / --speculative-draft-model-path / EAGLE3; Eagle3DecodingConfig / decoding_type: Eagle3 / --speculative_decoding_mode; mlp_speculator / ibm-*-accelerator; assistant_model= / prompt_lookup_num_tokens; LayerSkip / assistant_early_exit; Lookahead decoding; llama-server --model-draft / --spec-type; LM Studio draft model; DIY propose-K verify loops / acceptance-rate tuning |
