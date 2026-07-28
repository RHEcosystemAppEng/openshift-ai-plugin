# Red Hat AI Model Optimization Toolkit (LLM Compressor)

Pre-deployment **LLM quantization / compression** (PTQ, sparsity, calibrated recipes) so checkpoints fit memory and run faster on vLLM / Red Hat AI Inference. Peers are the fragmented GPTQ/AWQ/FP8 toolchains and DIY conversion pipelines that Red Hat’s Model Optimization Toolkit (upstream LLM Compressor → `compressed-tensors`) consolidates.

## Peers

- AutoGPTQ — archived GPTQ weight-only quantizer (`AutoGPTQForCausalLM`, `quantize_config.json`); common DIY → vLLM path
- AutoAWQ — archived AWQ weight-only quantizer (`AutoAWQForCausalLM`); RH blog names it as the fragmented ecosystem LLM Compressor unifies
- GPTQModel — maintained AutoGPTQ/AutoAWQ successor (GPTQ/AWQ + more) for HF/Transformers and vLLM-compatible checkpoints
- bitsandbytes — `BitsAndBytesConfig` / `load_in_4bit` / `load_in_8bit` / NF4 used as a deliberate compress-before-serve step (not QLoRA-only training)
- Hugging Face Transformers GPTQ/AWQ configs — `GPTQConfig` / `AwqConfig` + `from_pretrained(..., quantization_config=...)` conversion scripts that produce quantized HF dirs
- AutoFP8 — legacy Neural Magic FP8 PTQ toolkit called out alongside AutoGPTQ/AutoAWQ as the pre–LLM Compressor stack
- Intel Neural Compressor (INC) — SmoothQuant / WOQ / GPTQ / AWQ / AutoRound LLM compression on PyTorch/TF/ONNX (often Intel/Gaudi targets)
- AutoRound — Intel low-bit LLM WOQ (sign-gradient rounding); standalone or via INC; exports GPTQ/AWQ/GGUF-style artifacts
- Optimum Quanto — HF Optimum PyTorch quant backend (`optimum.quanto`, `QuantizedModelForCausalLM`) for int4/int8/fp8 weights/activations
- torchao — PyTorch-native quantization / low-bit dtypes library used instead of LLM Compressor for PTQ/export
- SparseML (Neural Magic) — legacy SparseGPT / Transformers→GPU sparsity recipes superseded by LLM Compressor for vLLM
- NVIDIA Model Optimizer (ModelOpt) — NVIDIA PTQ (FP8/NVFP4/INT4/AWQ/SmoothQuant) for TensorRT-LLM / unified HF export
- TensorRT-LLM quantize / convert_checkpoint — TRT-LLM-native FP8/INT8/AWQ checkpoint conversion (NVIDIA serving stack, not `compressed-tensors`)
- llama.cpp / GGUF convert — `convert_hf_to_gguf` / `llama-quantize` / Ollama Modelfile Q4_K_M-style local compression (CPU/Metal path)
- HQQ — Half-Quadratic Quantization (`hqq`) weight-only LLM compress packages
- DIY GPTQ/AWQ/SmoothQuant/SparseGPT scripts — ad-hoc calibration notebooks naming W4A16/W8A8/FP8 for vLLM without a unified library
- Upstream `llmcompressor` oneshot outside RH packaging — bare `pip install llmcompressor` / cloned `vllm-project/llm-compressor` examples without `registry.redhat.io/rhaii/model-opt-*` or RHOAI workbench/pipeline wrappers

## Detection aliases

- AutoGPTQ: `auto-gptq`, `auto_gptq`, `AutoGPTQForCausalLM`, `BaseQuantizeConfig`, `model.quantize(`, `save_quantized`, `quantize_config.json`
- AutoAWQ: `autoawq`, `auto_awq`, `awq`, `AutoAWQForCausalLM`, `model.quantize(tokenizer`, `quant_config=`
- GPTQModel: `gptqmodel`, `GPTQModel`, `from gptqmodel import`, ModelCloud GPTQModel
- bitsandbytes: `bitsandbytes`, `BitsAndBytesConfig`, `load_in_4bit`, `load_in_8bit`, `bnb_4bit_`, `NF4`
- HF Transformers GPTQ/AWQ: `GPTQConfig`, `AwqConfig`, `AWQConfig`, `quantization_config=gptq`, `quantization_config=awq`, `AutoModelForCausalLM.from_pretrained` + quant config to **produce** checkpoints
- AutoFP8: `auto_fp8`, `AutoFP8`, `neuralmagic` AutoFP8
- Intel Neural Compressor: `neural-compressor`, `neural_compressor`, `from neural_compressor`, `INC`, Intel Neural Compressor
- AutoRound: `auto-round`, `auto_round`, `AutoRound`, `intel/auto-round`
- Optimum Quanto: `optimum-quanto`, `optimum.quanto`, `from optimum.quanto`, `QuantizedModelForCausalLM`, `qint4`, `qint8`
- torchao: `torchao`, `torch.ao.quantization`, `from torchao`
- SparseML: `sparseml`, `SparseML`, `SparseGPT` recipes with Neural Magic SparseML (not llmcompressor modifiers)
- NVIDIA ModelOpt: `nvidia-modelopt`, `modelopt`, `mtq.quantize`, `NVFP4_DEFAULT_CFG`, `FP8_DEFAULT_CFG`, `Model-Optimizer`
- TensorRT-LLM quant: `tensorrt_llm`, `trtllm-build`, `convert_checkpoint.py`, `examples/quantization/quantize.py`
- llama.cpp / GGUF: `llama.cpp`, `convert_hf_to_gguf`, `llama-quantize`, `.gguf`, `Q4_K_M`, `Q5_K_M`, Ollama Modelfile `FROM` + quant tags
- HQQ: `hqq`, `HQQLinear`, `from hqq`
- DIY GPTQ/AWQ/SmoothQuant: scripts/docs naming `GPTQ`, `AWQ`, `SmoothQuant`, `SparseGPT`, `W4A16`, `W8A8`, `FP8` PTQ for LLMs; calibration sample loops without `llmcompressor`
- Upstream llmcompressor (non-RH): `pip install llmcompressor`, `from llmcompressor import oneshot`, `GPTQModifier` / `AWQModifier` / `SmoothQuantModifier` / `SparseGPTModifier`, `vllm-project/llm-compressor`, `examples/quantization_w4a16/`, `examples/awq/` — without `registry.redhat.io/rhaii/model-opt-cuda-rhel9` / `opendatahub/llmcompressor-workbench`

## Row (for table)

| AutoGPTQ; AutoAWQ; GPTQModel; bitsandbytes; HF Transformers GPTQ/AWQ configs; AutoFP8; Intel Neural Compressor; AutoRound; Optimum Quanto; torchao; SparseML; NVIDIA Model Optimizer; TensorRT-LLM quantize/convert_checkpoint; llama.cpp/GGUF convert; HQQ; DIY GPTQ/AWQ/SmoothQuant/SparseGPT scripts; upstream llmcompressor oneshot outside RH packaging | Red Hat AI Model Optimization Toolkit (LLM Compressor) | auto-gptq / AutoGPTQForCausalLM / quantize_config.json; autoawq / AutoAWQForCausalLM; gptqmodel / GPTQModel; BitsAndBytesConfig / load_in_4bit / load_in_8bit; GPTQConfig / AwqConfig; auto_fp8 / AutoFP8; neural-compressor / neural_compressor; auto-round / AutoRound; optimum.quanto / QuantizedModelForCausalLM; torchao; sparseml / SparseGPT; nvidia-modelopt / mtq.quantize / NVFP4; tensorrt_llm / trtllm-build / convert_checkpoint; llama.cpp / convert_hf_to_gguf / .gguf / Q4_K_M; hqq; DIY W4A16/W8A8/FP8 PTQ scripts; llmcompressor oneshot without rhaii/model-opt or llmcompressor-workbench |
