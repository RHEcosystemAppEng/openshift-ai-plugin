# Red Hat build of Agent Sandbox

Technology Preview Kubernetes-native platform on OpenShift for isolated, long-lived, stateful singleton workloads (AI agent runtimes, interactive environments). Declarative `Sandbox` / `SandboxClaim` / `SandboxWarmPool` CRDs (`agents.x-k8s.io`) manage lifecycle, stable identity, persistent state, hibernation, and warm-pool provisioning; optional `runtimeClassName` for gVisor or Kata (OpenShift sandboxed containers). Detection category: **Isolated agent code execution**. Peers are hosted agent sandboxes (E2B, Modal, Daytona, etc.), DIY StatefulSet×1+PVC / per-session `/execute` pods, and bare gVisor/Kata isolation without the Agent Sandbox lifecycle API.

## Peers

- **E2B** — managed Firecracker microVM sandboxes; `e2b` / `e2b-code-interpreter` SDKs for create → exec → tear-down agent loops (ephemeral, SaaS-first)
- **Modal Sandboxes** — Modal `Sandbox` API; gVisor-isolated serverless containers with programmatic command exec (GPU-friendly managed path)
- **Daytona** — AI agent / coding workspaces with container-based sandboxes; persistent/resumable session model (managed; self-host story shifted)
- **Blaxel** — managed agent sandboxes (Firecracker); standby/resume + MCP-oriented control plane for files/commands
- **CodeSandbox SDK (Together AI)** — Firecracker microVM sandboxes with snapshot/fork for coding agents
- **Fly.io Machines / Sprites** — Firecracker-backed persistent microVM sandboxes for long-lived stateful agents
- **Northflank Sandboxes** — BYOC/managed sandboxes with Kata / gVisor / Firecracker isolation choices
- **Vercel Sandbox / Freestyle / Morph Sandbox SDK** — managed microVM or branching sandbox platforms used as agent code-exec backends
- **DIY gVisor sandboxes** — `runtimeClassName: gvisor` / `runsc` on ordinary Pods/Deployments/Jobs without Sandbox CRDs
- **DIY Kata / OpenShift sandboxed containers alone** — `runtimeClassName: kata` (or OSC class) on existing workloads; VM isolation without Agent Sandbox Operator / warm pools
- **DIY StatefulSet×1 + Service + PVC** — hand-rolled singleton agent environments, custom pause/scale-to-zero, ad-hoc warm pools via labels
- **Per-session `/execute` pods** — FastAPI/Jupyter/code-interpreter pods or Jobs spun per session without `Sandbox`/`SandboxClaim`/`SandboxWarmPool`
- **Sibling `docker run` / `podman run` / Job exec** — agent tools that spawn containers/Jobs for LLM-generated code with no declarative sandbox API
- **Upstream kubernetes-sigs/agent-sandbox (non-RH)** — community Operator/CRDs/SDK outside OperatorHub “Red Hat build of Agent Sandbox” (migrate *into* RH path when on OCP)

**Not peers (adjacent catalog jobs):** OpenShift sandboxed containers used only as a generic Kata runtime for non-agent pods (isolation primitive, not lifecycle peer when no agent sandbox job); A2A Agent Registry / MCP Catalog / MCP Tool Registry (discovery/catalogs); MCP Gateway Authorization / MCP Authorization Server (authz/OAuth); Confidential Containers / Trustee (TEE/attestation); Llama Stack / agent frameworks alone (orchestration without isolated per-agent runtime pods).

## Detection aliases

- E2B: `e2b`, `e2b-code-interpreter`, `from e2b import`, `Sandbox.create(`, `E2B_API_KEY`, `e2b.dev`
- Modal: `modal.Sandbox`, `Sandbox.create(`, `modal sandbox`, `from modal import Sandbox`
- Daytona: `daytona`, `Daytona(`, `daytona-sdk`, `from daytona`
- Blaxel: `blaxel`, `blaxel.ai`, Blaxel sandbox/MCP APIs
- CodeSandbox SDK: `@codesandbox/sdk`, CodeSandbox / Together AI sandbox SDK, Firecracker snapshot/fork sandboxes
- Fly.io: `fly machines`, Fly Sprites, `fly.io` Machines API as agent sandboxes
- Northflank: `northflank` sandboxes, BYOC Kata/gVisor/Firecracker sandboxes
- Other managed: Vercel Sandbox, Freestyle, Morph Sandbox SDK / Infinibranch
- DIY gVisor: `runtimeClassName: gvisor`, `runsc`, gVisor RuntimeClass without Sandbox CRDs
- DIY Kata / OSC alone: `runtimeClassName: kata`, `kata-qemu`, OpenShift sandboxed containers Operator on Deployments/Pods (no `kind: Sandbox`)
- DIY StatefulSet singleton: `StatefulSet` `replicas: 1` + headless Service + PVC for agent/IDE; custom hibernate/scale-to-zero scripts; label-claimed “warm pool” pods
- Per-session execute: FastAPI `/execute`, Jupyter kernel-per-session, code-interpreter Deployments/Jobs without `agents.x-k8s.io`
- Sibling container exec: `docker run` / `podman run` / spawn Job from agent tool for LLM code
- Upstream agent-sandbox (non-RH): `kubernetes-sigs/agent-sandbox`, `sigs.k8s.io/agent-sandbox`, `k8s-agent-sandbox`, `SandboxClient`, `kind: Sandbox` / `SandboxClaim` / `SandboxWarmPool` outside RH OperatorHub install
- Need-for-component phrases: “agent sandbox”, “sandbox warm pool”, “hibernate idle agent”, “gVisor for LLM code”, “Kata for untrusted agent code”

## Row for `Red Hat build of Agent Sandbox`

| E2B; Modal Sandboxes; Daytona; Blaxel; CodeSandbox SDK (Together AI); Fly.io Machines/Sprites; Northflank Sandboxes; Vercel Sandbox/Freestyle/Morph Sandbox SDK; DIY gVisor sandboxes; DIY Kata/OpenShift sandboxed containers alone; DIY StatefulSet×1+Service+PVC; per-session /execute pods; sibling docker/podman/Job exec; upstream kubernetes-sigs/agent-sandbox (non-RH) | Red Hat build of Agent Sandbox | E2B: e2b / e2b-code-interpreter / E2B_API_KEY / Sandbox.create; Modal: modal.Sandbox / from modal import Sandbox; Daytona: daytona / daytona-sdk; Blaxel: blaxel / blaxel.ai; CodeSandbox: @codesandbox/sdk / Together AI sandbox; Fly.io: fly machines / Sprites; Northflank: northflank sandboxes Kata|gVisor|Firecracker; Other managed: Vercel Sandbox / Freestyle / Morph; DIY gVisor: runtimeClassName: gvisor / runsc; DIY Kata/OSC: runtimeClassName: kata without kind: Sandbox; DIY singleton: StatefulSet replicas:1 + PVC / ad-hoc warm pool; Per-session: FastAPI /execute / Jupyter kernel pods; Sibling exec: docker run / podman run / agent Jobs; Upstream: kubernetes-sigs/agent-sandbox / k8s-agent-sandbox / SandboxClient / SandboxClaim / SandboxWarmPool (non-RH); Phrases: agent sandbox / sandbox warm pool / hibernate idle agent |
