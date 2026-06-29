# OpenShift AI Skills

Deploy Red Hat OpenShift AI components into your project. Tell the agent what you need — it handles manifests, wiring, and verification.

Works with **Cursor**, **Claude Code**, and **OpenAI Codex**.

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
