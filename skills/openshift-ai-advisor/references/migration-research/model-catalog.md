# Model Catalog

Curated, searchable **discovery of validated third-party / open-source models** ready to evaluate and deploy, with admin governance of which sources teams see. Peers are DIY Hub browsing, alternate public registries, hand-maintained allowlists, and internal model portals that replace (or precede) RHOAI Model Catalog. Distinct from **Model Registry** (lifecycle of *your* registered artifacts) and **MaaS** (hosted LLM APIs).

## Peers

- Hugging Face Hub browsing DIY — hunt models on huggingface.co, paste `org/name`, pull with Hub APIs/CLI
- Hugging Face Hub download scripts — `snapshot_download` / `hf_hub_download` / `hf download` / `hf://` into cluster or PVC storage
- Hardcoded Hub wget/curl / git-lfs — `huggingface.co/…/resolve/…` URLs or `git lfs clone` in Dockerfiles/CI
- `from_pretrained("org/name")` Hub bootstrap — Transformers/Diffusers/sentence-transformers used as the download/discovery path
- ModelScope — Alibaba ModelScope `snapshot_download` / Hub-equivalent public model registry browsing
- Hand allowlists / “paste a repo id” onboarding — spreadsheets, markdown “approved models”, Confluence lists, README paste-the-id flows
- Internal model portals — custom company catalogs/portals listing approved checkpoints without RHOAI Model Catalog
- Artifactory / Nexus Hugging Face remote repos — proxy/cache Hub with infra allow-lists (partial DIY source governance)
- OpenLLM / lm-eval / leaderboard shopping — pick models from public leaderboards/benchmarks then fetch Hub IDs ad hoc
- Copied Hub model cards — local `MODEL_CARD.md` / YAML `pipeline_tag`/`library_name`/`base_model` tracking candidates outside a shared catalog
- KServe `storageUri: hf://…` / init-container Hub pulls — serve-time Hub fetch as the org’s sourcing pattern
- Scattered `MODEL_NAME` / `PRETRAINED=` Hub IDs — Helm values, ConfigMaps, notebooks with no central approved source list

## Detection aliases

- HF Hub APIs/CLI: `huggingface_hub`, `snapshot_download`, `hf_hub_download`, `hf download`, `huggingface-cli download`, `hf://`, `HF_TOKEN`, `HUGGING_FACE_HUB_TOKEN`, `HF_HOME`, `HF_HUB_CACHE`
- HF Hub URLs / git-lfs: `https://huggingface.co/…/resolve/…`, `wget`/`curl` + Bearer for `.safetensors`/`.gguf`/`pytorch_model*`, `git lfs clone https://huggingface.co/`
- Hub `from_pretrained` bootstrap: `AutoModel*.from_pretrained("org/name")`, `diffusers`/`sentence-transformers` Hub IDs (download path, not local dir)
- ModelScope: `modelscope`, `from modelscope import snapshot_download`, ModelScope Hub browsing
- Hand allowlists / portals: “approved models”, “model allowlist”, “paste a repo id”, internal model portal/catalog docs; spreadsheets/markdown candidate lists
- Proxy / infra DIY governance: Artifactory/Nexus “Hugging Face” remote repository configs; JFrog AI Catalog-style Hub allow-lists without RHOAI catalog
- Model-card DIY tracking: `pipeline_tag:`, `library_name:`, `base_model:`, `MODEL_CARD.md`, copied Hub README cards
- Serve-time Hub pull: KServe/`InferenceService` `storageUri: hf://…`; init containers that `hf download` on every start
- Scattered Hub IDs: `repo_id=`, `MODEL_NAME=`, `PRETRAINED=` pointing at public `meta-llama/`/`mistralai/`/`ibm-granite/`/etc. with no catalog source config
- Already on RHOAI (confirm, don’t reinvent): Model catalog UI, “Red Hat AI models”, “Red Hat AI validated”, DSC `modelregistry: Managed`

## Row (for table)

| Hugging Face Hub browsing DIY; HF Hub download scripts (snapshot_download/hf download/hf://); hardcoded Hub wget/curl/git-lfs; from_pretrained Hub bootstrap; ModelScope; hand allowlists / paste-a-repo-id onboarding; internal model portals; Artifactory/Nexus HF remote repos; OpenLLM/lm-eval/leaderboard shopping; copied Hub model cards; KServe hf:// / init-container Hub pulls; scattered MODEL_NAME/PRETRAINED Hub IDs | Model Catalog | huggingface_hub / snapshot_download / hf_hub_download / hf download / hf:// / HF_TOKEN / HF_HUB_CACHE; huggingface.co/…/resolve/… wget/curl / git lfs clone; AutoModel*.from_pretrained("org/name"); modelscope / ModelScope snapshot_download; approved-models allowlist / paste repo id / internal model portal; Artifactory/Nexus Hugging Face remote; pipeline_tag / library_name / base_model / MODEL_CARD.md; storageUri hf:// / init-container hf download; repo_id / MODEL_NAME / PRETRAINED Hub IDs; Model catalog UI / Red Hat AI models / DSC modelregistry Managed |
