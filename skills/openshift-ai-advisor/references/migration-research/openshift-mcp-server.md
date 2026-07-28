# MCP server for OpenShift Container Platform

Technology Preview Helm-deployed Model Context Protocol server that exposes OpenShift/Kubernetes inspection and management as MCP tools/resources (native Go API client—list pods, logs, events, GVK CRUD, optional Helm/metrics/KubeVirt/Tekton toolsets) so AI hosts can diagnose and act on live cluster state under RBAC, `read_only` / allowlists, and optional Connectivity Link MCP gateway. Peers are upstream/community Kubernetes MCP servers, kubectl/oc CLI wrappers, and agent patterns that shell cluster CLIs instead of adopting the productized **MCP server for OpenShift Container Platform**.

## Peers

- **containers/kubernetes-mcp-server** (npm/PyPI `kubernetes-mcp-server`, `npx`/`uvx`, image `quay.io/containers/kubernetes_mcp_server`) — upstream/community native API MCP server; local stdio or community Helm (`oci://ghcr.io/containers/charts/kubernetes-mcp-server`)
- **openshift/openshift-mcp-server** — OpenShift-oriented fork/docs/charts (`oci://ghcr.io/openshift/charts/openshift-mcp-server`); same job as the RH TP chart path
- **Flux159 / mcp-server-kubernetes** — TypeScript/Python MCP servers that wrap `kubectl_*` tools (`kubectl_get`, `kubectl_logs`, `kubectl_generic`, `kubectl_describe`) instead of a native API client
- **DIY kubectl/oc MCP wrappers** — hand-rolled MCP servers exposing cluster ops by shelling or embedding kubectl/oc
- **Agents shelling `oc` / `kubectl` / `helm`** — LangGraph/CrewAI/custom tools that exec CLI for chat assistants rather than MCP toolsets
- **Custom cluster-assistant APIs** — FastAPI/Flask (or similar) “cluster chatbot” backends with ad-hoc kube client CRUD for IDE agents
- **Per-developer kubeconfig-in-prompt patterns** — pasting kubeconfigs or `oc` output into agent context instead of a shared RBAC-scoped MCP `/mcp` endpoint

**Not peers (adjacent catalog jobs):** Connectivity Link **MCP Gateway** (federates/routes many MCP backends; does not implement `pods_list`); Lightspeed **Observability / Incident Detection MCP** (`cluster-health-mcp-server`—OLS-only, not general Cursor/Claude cluster CRUD); **OpenShift Lightspeed** console chat UI (may *consume* this server); **MCP Catalog** / Lifecycle Operator / **MCP Tool Registry** (discover/deploy/register definitions); classic **MachineConfigPool** (“MCP” CRD acronym collision).

## Detection aliases

- Upstream/community: `kubernetes-mcp-server`, `npx -y kubernetes-mcp-server`, `uvx kubernetes-mcp-server`, `containers/kubernetes-mcp-server`, `quay.io/containers/kubernetes_mcp_server`, `oci://ghcr.io/containers/charts/kubernetes-mcp-server`
- OpenShift fork/charts: `openshift/openshift-mcp-server`, `openshift-mcp-server`, `oci://ghcr.io/openshift/charts/openshift-mcp-server`, toolset `openshift`
- Product/Helm: `redhat-openshift-mcp-server`, `openshift-helm-charts/redhat-openshift-mcp-server`, ns/release `openshift-mcp-server`, client URL `…/mcp`, flags `--read-only` / `--toolsets` / `--disable-destructive`
- Native tools: `pods_list`, `pods_log`, `resources_*`, `helm_*`, `events_list`, `configuration_contexts_list`
- kubectl wrappers: `Flux159/mcp-server-kubernetes`, `mcp-server-kubernetes`, `kubectl_get`, `kubectl_logs`, `kubectl_generic`, `kubectl_describe`
- DIY CLI agents: tools/scripts exec `oc get` / `kubectl get` / `kubectl logs` / `helm`; comments “kubectl MCP”, “oc MCP wrapper”, “shell oc for the agent”
- Client wiring: `mcpServers` named `kubernetes` / `kubernetes-mcp-server` / `openshift`; Claude/Cursor/VS Code MCP JSON with local npx/uvx or HTTP `/mcp`

## Row (for table)

| containers/kubernetes-mcp-server (npx/uvx/npm/PyPI); openshift/openshift-mcp-server & community Helm charts; Flux159/mcp-server-kubernetes kubectl_* wrappers; DIY kubectl/oc MCP servers; agents shelling oc/kubectl/helm; custom FastAPI/Flask cluster-assistant kube CRUD; per-developer kubeconfig-in-prompt patterns | MCP server for OpenShift Container Platform | kubernetes-mcp-server / npx uvx kubernetes-mcp-server; containers/kubernetes-mcp-server; quay.io/containers/kubernetes_mcp_server; openshift/openshift-mcp-server; redhat-openshift-mcp-server / ns openshift-mcp-server; Flux159 mcp-server-kubernetes / kubectl_get kubectl_logs; DIY oc/kubectl MCP wrapper; agent exec oc kubectl helm; pods_list pods_log resources_* /mcp |
