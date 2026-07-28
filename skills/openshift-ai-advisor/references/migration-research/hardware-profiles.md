# Hardware Profiles & Accelerator Management

Administrator-configured **named GPU/accelerator allocations** (identifiers, CPU/memory bounds, node selectors, tolerations) so workbenches, serving, and pipelines land on the right hardware—backed by NFD + vendor GPU/Spyre operators. Peers are DIY scheduling matrices, local `--gpus` stacks, bare device-plugin/operator setups, and cloud GPU node-pool DIY that teams use instead of (or before) adopting RHOAI Hardware Profiles.

## Peers

- Manual GPU nodeSelector / tolerations / taint matrices — hand-maintained docs and manifests telling every team which labels/taints to copy onto pods
- Per-team Small/Medium/Large GPU size YAMLs — duplicated resource+selector snippets instead of admin HardwareProfile CRs + UI picker
- Docker Compose / Podman `--gpus` DIY — `deploy.resources.reservations.devices` / `--gpus all` / `CUDA_VISIBLE_DEVICES` as the only “scheduling” story
- Standalone device plugin DaemonSets — NVIDIA/AMD/Gaudi/Spyre device plugins alone advertising `nvidia.com/gpu` (etc.) with no profile UX
- NFD + GPU Operator without Hardware Profiles — ClusterPolicy/DeviceConfig capacity on nodes, teams still hand-edit requests and targeting
- Deprecated AcceleratorProfiles — ODH/RHOAI `kind: AcceleratorProfile` (`dashboard.opendatahub.io`) + old notebook/model-server size selectors
- Karpenter GPU NodePools / NodeClaims DIY — Karpenter provisioners for GPU instance types without RHOAI profile abstraction
- Cluster Autoscaler / MachineSet GPU node pools DIY — ASG/MachineSet GPU pools + manual selectors/tolerations
- Cloud managed GPU node pools — EKS/GKE/AKS GPU node groups with ad-hoc `nodeSelector`/`tolerations` in app charts
- Volcano / batch GPU sharing DIY — Volcano GPU binpack/share policies used as the allocation layer
- DRA ResourceClaim / DeviceClass DIY — claim-based MIG/attribute selection without HardwareProfile identifiers
- Shared SSH / bastion GPU boxes — team SSH + `nvidia-smi` / `CUDA_VISIBLE_DEVICES` on a fixed host (no cluster profile lifecycle)
- Cloud ML instance-type pickers — SageMaker `ml.p*`/`ml.g*`, Vertex `acceleratorType`, Azure ML GPU SKUs as the “hardware profile”

## Detection aliases

- Manual matrices: GPU `nodeSelector`/`nodeAffinity` (`nvidia.com/gpu.product`, `nvidia.com/gpu.present`); `tolerations` for `nvidia.com/gpu`/`amd.com/gpu`/`habana.ai/gaudi`/custom GPU taints; ADRs “taint GPU nodes and tell every team the toleration”
- Per-team size YAMLs: duplicated Small/Medium/Large GPU resource blocks; comments “AcceleratorProfile” / “hardware profile” / “Settings → Hardware profiles”
- Compose / `--gpus` DIY: `docker-compose` + `driver: nvidia` / `capabilities: [gpu]`, `--gpus all`, `CUDA_VISIBLE_DEVICES`, `nvidia-smi` as sole scheduling runbook
- Device plugin alone: NVIDIA/AMD/Gaudi/Spyre device-plugin DaemonSet; node capacity `nvidia.com/gpu`/`amd.com/gpu`/`habana.ai/gaudi`/`ibm.com/spyre_*` without `kind: HardwareProfile`
- NFD + GPU Operator only: `NodeFeatureDiscovery`, NFD PCI/`amd-gpu` labels; NVIDIA `ClusterPolicy`/`gpu-cluster-policy`; AMD `DeviceConfig`; Habana `ClusterPolicy`; `SpyreClusterPolicy`—no dashboard Hardware profiles
- AcceleratorProfiles: `kind: AcceleratorProfile`, `apiVersion: dashboard.opendatahub.io/*`, `disableAcceleratorProfiles`
- Karpenter DIY: `kind: NodePool`/`NodeClaim`/`EC2NodeClass` with GPU instance families; Karpenter GPU provisioner docs
- Autoscaler / MachineSet pools: Cluster Autoscaler GPU ASGs; OpenShift `MachineSet`/`MachinePool` GPU flavors + manual pod targeting
- Cloud node pools: EKS/GKE/AKS GPU node groups; chart values wiring GPU selectors per service
- Volcano GPU DIY: `volcano.sh` GPU sharing/binpack for accelerator placement
- DRA DIY: `ResourceClaim`, `DeviceClass`, CEL attribute selectors / MIG claims instead of opaque counts + HardwareProfile
- SSH GPU boxes: shared bastion + `nvidia-smi` / `CUDA_VISIBLE_DEVICES`; no CRD/profile picker
- Cloud instance pickers: SageMaker `ml.p`/`ml.g` instance types; Vertex `acceleratorType`/`acceleratorCount`; Azure ML GPU compute SKUs
- Cross-cutting extended resources: `nvidia.com/gpu`/`amd.com/gpu`/`habana.ai/gaudi`/`ibm.com/spyre_*` in requests/limits; MIG/`nvidia.com/mig-*`; GFD labels; `opendatahub.io/recommended-accelerators`; `kind: HardwareProfile` (`infrastructure.opendatahub.io`)

## Row for `Hardware Profiles & Accelerator Management`

| Manual GPU nodeSelector/tolerations/taint matrices; per-team Small/Medium/Large GPU size YAMLs; Docker Compose/Podman --gpus DIY; standalone device plugin DaemonSets; NFD+GPU Operator without Hardware Profiles; deprecated AcceleratorProfiles; Karpenter GPU NodePools/NodeClaims DIY; Cluster Autoscaler/MachineSet GPU pools DIY; EKS/GKE/AKS managed GPU node pools; Volcano GPU sharing DIY; DRA ResourceClaim/DeviceClass DIY; shared SSH/bastion GPU boxes; cloud ML instance-type pickers (SageMaker/Vertex/Azure ML) | Hardware Profiles & Accelerator Management | GPU nodeSelector/nodeAffinity / nvidia.com/gpu.product / gpu.present; tolerations nvidia.com/gpu / amd.com/gpu / habana.ai/gaudi; per-team GPU size YAML; docker-compose driver:nvidia / --gpus all / CUDA_VISIBLE_DEVICES / nvidia-smi; device-plugin DaemonSet + nvidia.com/gpu capacity alone; NodeFeatureDiscovery / ClusterPolicy / DeviceConfig / SpyreClusterPolicy without HardwareProfile; kind: AcceleratorProfile / dashboard.opendatahub.io; Karpenter NodePool/NodeClaim GPU; MachineSet/ASG GPU pools; EKS/GKE/AKS GPU node groups; volcano.sh GPU share; ResourceClaim / DeviceClass / MIG claims; SSH bastion + nvidia-smi; SageMaker ml.p*/ml.g* / Vertex acceleratorType / Azure ML GPU SKU; nvidia.com/gpu / amd.com/gpu / habana.ai/gaudi / ibm.com/spyre_* / kind: HardwareProfile / opendatahub.io/recommended-accelerators |
