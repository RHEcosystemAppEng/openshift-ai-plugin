# Caikit TGIS ServingRuntime

Catalog: Caikit framework + Text Generation Inference Server (TGIS) ServingRuntime for KServe; gRPC/REST; NLP text-generation with streaming; needs KServe + S3-compatible model storage. Detection category: **Caikit + TGIS text generation**. Prefer this when Caikit task APIs / Caikit-format artifacts / dual Caikit+TGIS containers are present; plain OpenAI-style generative serving without Caikit maps elsewhere (e.g. upstream vLLM → **vLLM Serving Runtimes**).

## Peers

- **IBM / OpenDataHub TGIS (standalone)** — `IBM/text-generation-inference` / `opendatahub-io/text-generation-inference`; `text-generation-launcher`, gRPC engine, `tgi_*` metrics, no Caikit transformer. Closest engine peer the composite runtime wraps.
- **Hugging Face Text Generation Inference (TGI)** — `huggingface/text-generation-inference`, `ghcr.io/huggingface/text-generation-inference`, `text-generation-launcher --model-id=...`. Upstream TGI DIY serving; TGIS is an early IBM/ODH fork of this stack (TGI now maintenance-mode; landscapes often list vLLM/SGLang as successors).
- **Caikit + caikit-nlp DIY runtime** — PyPI/GitHub `caikit`, `caikit-nlp`; `python -m caikit.runtime`; `/api/v1/task/text-generation` (+ streaming); HF→Caikit `TextGeneration.bootstrap` / `*-caikit` dirs with `module_id`. Same task API layer without the managed RHOAI ServingRuntime.
- **caikit-tgis-backend + local TGIS** — PyPI `caikit-tgis-backend`; `backend_priority` / finder `TGIS` / `tgis-auto`, hostname `:8033`. DIY Compose/K8s wiring Caikit to a TGIS process.
- **opendatahub-io/caikit-tgis-serving (manual stack)** — dual-container TGIS + Caikit transformer demos/images (`quay.io/opendatahub/caikit-tgis-serving`, `text-generation-inference`) run outside the catalog runtime.
- **DIY HF Transformers text-generation servers** — `pipeline("text-generation")`, `AutoModelForCausalLM` + FastAPI/Flask/gRPC streaming wrappers; custom NLP generate/stream endpoints overlapping the Caikit+TGIS job without OpenAI chat schema.
- **PEFT soft-prompt / prompt-tuning custom serve** — PEFT-tuned prompts loaded at inference (TGIS PEFT support; caikit-nlp `PeftPromptTuning`) instead of Caikit modules + TGIS backend.

## Detection aliases

- Packages: `caikit`, `caikit-nlp`, `caikit-tgis-backend`, `caikit-tgis-serving`, `caikit-nlp-client`
- Imports / APIs: `import caikit_nlp`, `caikit_nlp.text_generation.TextGeneration`, `TextGeneration.bootstrap`, `PeftPromptTuning`, `python -m caikit.runtime`, `caikit_health_probe`
- HTTP/gRPC paths: `/api/v1/task/text-generation`, `/api/v1/task/server-streaming-text-generation`, JSON `{"model_id","inputs"}`, ports `8080`/`8085`
- Artifacts / config: `*-caikit` dirs, `module_id`, `RUNTIME_LIBRARY=caikit_nlp`, `runtime.library: caikit_nlp`, `backend_priority` / `tgis-auto`, `:8033`
- TGIS/TGI engine: `text-generation-launcher`, `text-generation-server download-weights`, `DEPLOYMENT_FRAMEWORK=tgis_native`, `MODEL_NAME`/`HF_HUB_CACHE`/`FLASH_ATTENTION`, metrics `tgi_*`
- Images / repos: `quay.io/opendatahub/caikit-tgis-serving`, `quay.io/opendatahub/text-generation-inference`, `ghcr.io/huggingface/text-generation-inference`, `opendatahub-io/text-generation-inference`, `IBM/text-generation-inference`, `huggingface/text-generation-inference`
- Manifests (DIY/KServe): `ServingRuntime` name `caikit-tgis-runtime`, `supportedModelFormats: caikit`, dual-container TGIS + `transformer-container`
- DIY phrases: “Caikit TGIS”, “caikit-nlp text generation”, “TGI/TGIS standalone”, HF `pipeline("text-generation")` custom server

## Row for `Caikit TGIS ServingRuntime`

| IBM/ODH TGIS standalone; Hugging Face TGI; Caikit+caikit-nlp DIY runtime; caikit-tgis-backend+local TGIS; manual caikit-tgis-serving stack; DIY HF Transformers text-gen servers; PEFT prompt-tuning custom serve | Caikit TGIS ServingRuntime | `caikit`, `caikit-nlp`, `caikit-tgis-backend`, `caikit-tgis-serving`, `import caikit_nlp`, `python -m caikit.runtime`, `/api/v1/task/text-generation`, `server-streaming-text-generation`, `*-caikit`/`module_id`, `text-generation-launcher`, `tgi_*`, `ghcr.io/huggingface/text-generation-inference`, `quay.io/opendatahub/{caikit-tgis-serving,text-generation-inference}`, `caikit-tgis-runtime`, `supportedModelFormats: caikit`, `pipeline("text-generation")` DIY |
