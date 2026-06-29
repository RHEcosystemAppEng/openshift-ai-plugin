# OpenShift AI Skills

- **Discovery** — knowing what OpenShift AI offers and which components are relevant to your project takes time.
- **Integration** — deploying and wiring OpenShift AI components into an existing codebase is not straightforward.

This plugin provides an AI advisor that solves both problems. It analyzes your repository, recommends OpenShift AI components — both migrations from your current infrastructure and net-new additions — and then implements the selected components while you stay in the loop.

### Example

Suppose your project already contains a RAG pipeline. The advisor will suggest:

1. **Migrate** to the OpenShift AI RAG Stack.
2. **Add** RAGAS for evaluation.
3. **Add** AutoRAG for chunking optimization.

You pick what to adopt — for example, only the RAG Stack migration. The agent then proposes implementation approaches, wires the component into your project, and verifies it works in your environment. You do not need prior knowledge of OpenShift AI; the advisor handles the details.

Works with **Cursor**, **Claude Code**, and **OpenAI Codex**.

Tested and refined across multiple repositories over 40+ iterations.

## Install

### Cursor

```
/add-plugin openshift-ai-skills
```

Or clone manually:

```bash
git clone https://github.com/ikatav/openshift-ai-skills.git \
  ~/.cursor/plugins/local/openshift-ai-skills
```

### Claude Code

```bash
claude --plugin-dir ./openshift-ai-skills
```

Or install from a marketplace once published.

### OpenAI Codex

Clone into your plugins directory:

```bash
git clone https://github.com/ikatav/openshift-ai-skills.git \
  ~/.agents/plugins/openshift-ai-skills
```

Then use `@plugin-creator` to add it to your personal marketplace, or invoke skills directly with `@openshift-ai-skills`.

## Skills

| Skill | What it does |
|-------|-------------|
| `openshift-ai-advisor` | Analyzes your project and recommends which OpenShift AI components to add |
| `add-openshift-ai-component` | Adds a component, wires it into your app, tests it, verifies on each deployment target |

### Invoking by provider

| Provider | Advisor | Add Component |
|----------|---------|---------------|
| Cursor | `/openshift-ai-advisor` | `/add-openshift-ai-component` |
| Claude Code | `/openshift-ai-skills:openshift-ai-advisor` | `/openshift-ai-skills:add-openshift-ai-component` |
| OpenAI Codex | `@openshift-ai-skills openshift-ai-advisor` | `@openshift-ai-skills add-openshift-ai-component` |

## How it works

1. Detects your cluster state (OpenShift AI version, enabled components, operator status).
2. Detects your project structure (Helm, Kustomize, raw YAML, compose).
3. Generates manifests matching your version and deployment style.
4. Wires the component into your application code.
5. Writes tests via an unbiased sub-agent (black-box, contract-only).
6. Deploys and verifies — nothing is applied without your approval.

All generated manifests and tests align with the OpenShift AI version running on your cluster, not a hardcoded default.

## Prerequisites

- `oc` CLI installed and logged into an OpenShift cluster
- Red Hat OpenShift AI operator installed on the cluster

## License

Apache-2.0
