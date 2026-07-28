# OCI ModelCar Inference Serving

Packages language-model weights as OCI-compliant **modelcar** images and inference-serves them via KServe (`storageUri: oci://…`) or Red Hat AI Inference so clusters pull models from a container registry instead of re-downloading from S3/Hugging Face on every pod start. Peers are DIY packaging/distribution paths and adjacent OCI/PVC/object-store approaches teams use instead of (or before) adopting ModelCar serving.

## Peers

- DIY weights-as-OCI Containerfile — hand-rolled `COPY … /models` (or multi-stage UBI → ubi-micro) images mounted or referenced ad hoc, without KServe ModelCar/`oci://` serving path
- ORAS model packaging — `oras push`/`oras pull` of weights as OCI artifacts (`application/x-mlmodel` or generic layers) for registry storage only (no GPU InferenceService)
- Skopeo artifact copy — `skopeo copy` of OCI/ML artifacts into Quay/Harbor without ModelCar sidecar / ImageVolume serving
- olot + Skopeo/ORAS layering — append model files onto a base layout then push; packaging helper short of RHAIIS/KServe ModelCar deploy
- `oci-modelcar` CLI packaging — HF → multi-layer OCI push helpers aimed at ImageVolume/KServe consumers, used as a standalone packaging pipeline
- KAITO / ORAS OCI-artifact models — models as non-runnable OCI artifacts pulled at init, separate from KServe modelcar layout
- Harbor + ORAS model artifacts — registry-side OCI artifact management for weights without ModelCar inference wiring
- KitOps ModelKits / CNCF ModelPack-style kits — kit/pack formats packaging models + metadata as OCI artifacts for distribution
- HF Hub cache on PVC DIY — `HF_HOME`/`TRANSFORMERS_CACHE`/`huggingface-hub` cache directory on a shared PVC across serving pods
- KServe `pvc://` model store — pre-seeded PVC with weights; `storageUri: pvc://…` instead of registry-cached modelcars
- KServe `hf://` / Hub download-per-pod — storage-initializer `snapshot_download` / `hf://` fetch on every cold start
- KServe `s3://` / URI storage-initializer — object-storage or HTTP(S) pull of weights into emptyDir on each pod start
- Git LFS / `git clone` weight trees — clone HF/git-lfs repos into cluster storage or bake into custom runtime images
- NFS / CephFS / shared filesystem model trees — POSIX shared mounts of weight directories for vLLM/TGI Deployments
- Dragonfly / Fluid P2P or data-cache acceleration — CNCF P2P/cache layers in front of registry or object storage (often with Harbor), used instead of ModelCar node image cache
- Kubernetes ImageVolume / OCI volume DIY — KEP-4639 image volumes mounting arbitrary OCI content outside KServe `oci+native://` ModelCar mode
- Monolithic runtime+weights image — bake safetensors into the vLLM/TGI/ServingRuntime image (rebuilt per model version)
- Direct local weight download — laptop/`oc rsync`/curl of Hub or S3 objects for single-node experiments (no registry packaging)

## Detection aliases

- DIY weights-as-OCI: `Containerfile`/`Dockerfile` with `COPY … /models`, `podman build --format=oci` of weight-only images, custom model image refs without `storageUri: oci://` or `enableModelcar`
- ORAS packaging: `oras push`, `oras pull`, `oras cp`, `application/x-mlmodel`, ORAS artifact media types for model blobs
- Skopeo packaging: `skopeo copy`, `skopeo inspect` of ML/OCI artifacts into Quay/Harbor (artifact transfer, not InferenceService)
- olot: `olot`, `oci_layers_on_top`, `containers/olot`, olot + skopeo/oras-py push of model layers
- oci-modelcar CLI: `oci-modelcar push`, `oci-modelcar`, `--hf-repo`, PyPI/`codanael/oci-modelcar` packaging pipeline
- KAITO OCI artifacts: KAITO `model-as-oci-artifacts`, ORAS-packaged KAITO model weights separate from runtime image
- Harbor/ORAS artifacts: Harbor model artifact repos, `goharbor` AI model management, ORAS→Harbor without ModelCar serving
- KitOps / ModelPack: `kitops`, `ModelKit`, `modelpack`, kit CLI push of model kits to OCI registries
- HF cache PVC DIY: `HF_HOME`, `TRANSFORMERS_CACHE`, `HUGGINGFACE_HUB_CACHE`, `HF_HUB_CACHE`, PVC mount of Hub cache; `snapshot_download` into shared volume
- PVC model store: `storageUri: pvc://`, `pvc://$(PVC_NAME)/…`, preloaded model PVC + InferenceService
- HF-per-pod: `storageUri: hf://`, KServe HF storage provider, init-container Hub download every start
- S3/URI initializer: `storageUri: s3://`, `storageUri: https://`, KServe storage-initializer copy into emptyDir
- Git LFS / clone: `git lfs`, `git clone` of model repos, `.gitattributes` LFS pointers as the release store
- Shared FS mounts: NFS/CephFS/`ReadWriteMany` PVC with `/models` tree mounted into DIY vLLM/TGI Deployments
- Dragonfly / Fluid: `dragonfly`, `fluid.io`, `Dataset`/`Runtime` (Fluid), Harbor P2P preheat for model blobs
- ImageVolume DIY: `imageVolume`, `spec.volumes[].image`, KEP-4639 OCI volume mounts outside `oci+native://` ModelCar
- Monolithic bake-in: ServingRuntime/Dockerfile `COPY` of `.safetensors` into runtime image; one image tag per model version
- Direct download: local `huggingface-cli download` / `hf download` / `curl` of weights with no registry push or `oci://` URI

## Row (for table)

| DIY weights-as-OCI Containerfile; ORAS model packaging; Skopeo artifact copy; olot + Skopeo/ORAS layering; oci-modelcar CLI packaging; KAITO/ORAS OCI-artifact models; Harbor + ORAS model artifacts; KitOps ModelKits / ModelPack; HF Hub cache on PVC DIY; KServe pvc:// model store; KServe hf:// Hub download-per-pod; KServe s3:// / URI storage-initializer; Git LFS / git clone weight trees; NFS/CephFS shared filesystem model trees; Dragonfly/Fluid P2P or data-cache; Kubernetes ImageVolume DIY; monolithic runtime+weights image; direct local weight download | OCI ModelCar Inference Serving | DIY `COPY … /models` Containerfile / `podman build --format=oci` without `oci://` serving; `oras push`/`oras pull`/`application/x-mlmodel`; `skopeo copy` of ML artifacts; `olot`/`oci_layers_on_top`; `oci-modelcar push`/`--hf-repo`; KAITO OCI artifacts; Harbor ORAS model repos; `kitops`/`ModelKit`/`modelpack`; `HF_HOME`/`TRANSFORMERS_CACHE`/`HUGGINGFACE_HUB_CACHE` on PVC; `storageUri: pvc://`; `storageUri: hf://` / per-pod `snapshot_download`; `storageUri: s3://` / HTTPS initializer; `git lfs` / clone of weights; NFS/CephFS `/models` mounts; `dragonfly` / Fluid `Dataset`; KEP-4639 `imageVolume` DIY; baked `.safetensors` in runtime image; local `hf download`/`curl` weights |
