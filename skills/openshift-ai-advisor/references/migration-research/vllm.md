# vLLM Serving Runtimes

## Peers
- SGLang — production OpenAI-compatible LLM/VLM server with RadixAttention continuous batching
- TensorRT-LLM — NVIDIA compiled-engine generative serving via `trtllm-serve` / Triton backends
- Hugging Face Text Generation Inference (TGI) — HF Rust/Python generative HTTP server (Messages API)
- LMDeploy (TurboMind) — InternLM/OpenMMLab high-throughput OpenAI-compatible LLM/VLM server
- llama.cpp (`llama-server`) — C/C++ GGUF inference with built-in OpenAI-compatible HTTP
- Ollama — single-command local LLM runner exposing OpenAI-compatible APIs
- Hugging Face transformers generate loops — DIY `AutoModelForCausalLM` / `pipeline("text-generation")` + `model.generate`
- FastAPI/Flask DIY CausalLM servers — custom `/generate` or `/v1/chat/completions` around loaded HF weights
- Aphrodite Engine — community PagedAttention fork with OpenAI + Kobold APIs for quantized serving
- ExLlamaV2/V3 + TabbyAPI — EXL2/EXL3 GPU engine behind an OpenAI-compatible FastAPI server
- DeepSpeed-MII / DeepSpeed-FastGen — Microsoft continuous-batching LLM serving (Dynamic SplitFuse)
- LightLLM — lightweight TokenAttention continuous-batching OpenAI-style API server
- MLC-LLM — TVM-compiled cross-platform (CUDA/ROCm/Metal/Vulkan/Web) LLM deployment
- LocalAI — drop-in OpenAI-compatible multi-backend self-hosted gateway/server
- NVIDIA NIM (self-hosted) — NGC containerized OpenAI-compatible LLM microservices
- OpenLLM (BentoML) — `openllm serve` packaging any open LLM as an OpenAI-compatible API
- text-generation-webui (oobabooga) — local Gradio/API host with multiple generative backends
- KoboldCpp — llama.cpp-based local HTTP API for GGUF generative models
- mistral.rs — Rust LLM inference engine with OpenAI-compatible HTTP server
- LM Studio (local server) — desktop runner exposing localhost OpenAI-compatible endpoints
- CTranslate2 — fast Transformer generative decode used in DIY/self-hosted LLM APIs
- ipex-llm — Intel XPU/CPU local LLM acceleration stack (often via Ollama/llama.cpp paths)
- IBM TGIS (standalone) — older Text Generation Inference Server patterns outside RHOAI Caikit

## Detection aliases
- SGLang: `sglang`, `sglang serve`, `python -m sglang.launch_server`, `lmsysorg/sglang`, `from sglang`, RadixAttention
- TensorRT-LLM: `tensorrt_llm`, `trtllm-serve`, `tensorrt-llm`, `trtllm_ckpt`, `trtllm_engine`, `NVIDIA/TensorRT-LLM`
- TGI: `text-generation-inference`, `ghcr.io/huggingface/text-generation-inference`, `text_generation_server`, `/generate_stream`, Messages API `model":"tgi"`
- LMDeploy: `lmdeploy`, `lmdeploy serve api_server`, `from lmdeploy import pipeline`, `TurbomindEngineConfig`, `openmmlab/lmdeploy`, TurboMind
- llama.cpp: `llama.cpp`, `llama-server`, `llama_cpp`, `GGUF`, `libllama`, `-ngl`, `ggml`
- Ollama: `ollama`, `ollama serve`, `ollama run`, `OLLAMA_HOST`, image `ollama/ollama`, `/api/chat`, `:11434`
- HF transformers DIY: `AutoModelForCausalLM`, `LlamaForCausalLM`, `pipeline("text-generation")`, `model.generate(`, `TextIteratorStreamer`, `device_map="auto"`
- DIY HTTP CausalLM: FastAPI/Flask/uvicorn `/v1/chat/completions` or `/generate` loading HF CausalLM; `torch.cuda` + `.safetensors` chat models
- Aphrodite: `aphrodite`, `aphrodite-engine`, `aphrodite.endpoints.openai.api_server`, `PygmalionAI/aphrodite-engine`
- ExLlama/TabbyAPI: `exllamav2`, `exllamav3`, `tabbyAPI`, `theroyallab/tabbyAPI`, `EXL2`, `EXL3`, `.exl2`
- DeepSpeed-MII: `deepspeed-mii`, `mii`, `deepspeed.mii`, `DeepSpeed-FastGen`, `from mii import`
- LightLLM: `lightllm`, `python -m lightllm.server.api_server`, `ghcr.io/modeltc/lightllm`, `TokenAttention`
- MLC-LLM: `mlc-llm`, `mlc_llm`, `mlc.llm`, `mlc-ai/mlc-llm`, `mlc_chat`
- LocalAI: `local-ai`, `localai`, `localai/localai`, `mudler/LocalAI`, OpenAI base URL to LocalAI host
- NVIDIA NIM: `nvcr.io/nim/`, `NIM_MODEL_NAME`, `NGC_API_KEY`, `nvidia-nim`, NIM LLM containers on `:8000`
- OpenLLM: `openllm`, `openllm serve`, `openllm start`, `bentoml/OpenLLM`, `import openllm`
- text-generation-webui: `text-generation-webui`, `oobabooga`, `oobabooga/text-generation-webui`, `TGWUI`
- KoboldCpp: `koboldcpp`, `KoboldCpp`, `koboldcpp.exe`, Kobold-compatible `/api/v1/generate`
- mistral.rs: `mistralrs`, `mistral.rs`, `mistralrs-server`, `EricLBuehler/mistral.rs`
- LM Studio: `LM Studio`, `lmstudio`, local `1234` OpenAI server, `lms` CLI
- CTranslate2: `ctranslate2`, `ctranslate2.Generator`, `CTranslate2`, `ct2-transformers-converter`
- ipex-llm: `ipex-llm`, `ipex_llm`, `bigdl-llm`, `intel-analytics/ipex-llm`
- TGIS standalone: `text-generation-inference` IBM/`tgis`, `TGIS`, `grpc` text-generation stubs without Caikit RHOAI runtime names

## Row (for table)
| SGLang; TensorRT-LLM; Hugging Face TGI; LMDeploy; llama.cpp; Ollama; HF transformers generate loops; FastAPI/Flask DIY CausalLM servers; Aphrodite Engine; ExLlamaV2/V3 + TabbyAPI; DeepSpeed-MII/FastGen; LightLLM; MLC-LLM; LocalAI; NVIDIA NIM (self-hosted); OpenLLM; text-generation-webui; KoboldCpp; mistral.rs; LM Studio; CTranslate2; ipex-llm; IBM TGIS standalone | vLLM Serving Runtimes | `sglang`/`sglang.launch_server`/`lmsysorg/sglang`; `trtllm-serve`/`tensorrt_llm`/`trtllm_engine`; `text-generation-inference`/`ghcr.io/huggingface/text-generation-inference`; `lmdeploy serve api_server`/`TurbomindEngineConfig`/`openmmlab/lmdeploy`; `llama-server`/`llama.cpp`/`GGUF`; `ollama`/`ollama/ollama`/`:11434`; `AutoModelForCausalLM`/`pipeline("text-generation")`/`model.generate(`; DIY FastAPI `/v1/chat/completions`+CausalLM; `aphrodite`/`aphrodite-engine`; `exllamav2`/`exllamav3`/`tabbyAPI`/`EXL2`; `deepspeed-mii`/`mii`/`DeepSpeed-FastGen`; `lightllm.server.api_server`/`ghcr.io/modeltc/lightllm`; `mlc-llm`/`mlc_llm`; `localai`/`mudler/LocalAI`; `nvcr.io/nim/`/`NGC_API_KEY`; `openllm serve`; `oobabooga`/`text-generation-webui`; `koboldcpp`; `mistralrs`/`mistral.rs`; LM Studio local OpenAI server; `ctranslate2`; `ipex-llm`/`bigdl-llm`; standalone `TGIS` |
