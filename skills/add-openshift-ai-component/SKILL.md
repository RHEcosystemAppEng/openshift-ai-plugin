---
name: add-openshift-ai-component
description: Add a Red Hat OpenShift AI component to an existing project, wire it into the application, and verify it on every deployment target. Use when the user wants to add, deploy, or integrate a specific OpenShift AI component such as KServe, vLLM, Model Registry, Data Science Pipelines, or any component from the catalog.
---

# Add OpenShift AI Component

Add a single OpenShift AI component to the user's project, wire it in, and verify it works on every deployment target.

## Phase 1: Ground

Read [openshift-ai-components.md](../../docs/openshift-ai-components.md). If the user hasn't named a component, ask. The component must be from the catalog. Confirm the choice before proceeding.

Navigate to https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed and find the sub-link for the chosen component. Read the official installation and configuration instructions. Use these as the authoritative source for CRDs, operator settings, and deployment steps throughout all later phases.

Use explore subagents to understand the project in parallel with confirming the component. Look for languages, frameworks, project structure, deployment methods (Helm, Kustomize, compose, raw manifests), how the project currently handles the concern the component addresses, and existing test infrastructure. Match the project's patterns throughout all later phases.

Identify how the user currently deploys and runs the application. Suggest all detected deployment methods and let them pick which one to use for verification. If no deployment method is detected, ask the user to provide one.

Before verifying changes, ask whether it is safe to undeploy and redeploy the current project. Wait for acceptance.

Ask how to run existing tests. Suggest detected options (e.g., `pytest`, `npm test`, `make test`) and let the user pick or type their own command.

Ask what namespace to workon if he choose the cluster deployment.

Summarize findings to the user. Ask one question at a time.

## Phase 2: Check targets and feasibility

Ask the user where to deploy and test. Typical targets are an OpenShift cluster (ask which namespace) or local (compose). If the user picks multiple, complete one fully before starting the next.

**Cluster targets.** Use `oc` for all cluster commands, never `kubectl`. Read and follow [cluster-checks.md](../../common/cluster-checks.md). If `oc` commands fail, check permissions with `oc auth can-i`. If CRDs are missing, check the operator and DataScienceCluster status. If the cluster version is incompatible, stop and explain. 

If the target environment cannot support required CRDs (e.g., local), tell the user and propose a workable alternative for that target that include the Openshift AI component.

**All targets.** Read and follow [project-detection.md](../../common/project-detection.md) to detect the deployment style and confirm the output format with the user.

**Feasibility.** Read the official OpenShift AI docs for the chosen component (linked in the catalog) before generating any manifests. If supported, proceed. If partially supported, explain the gap, propose a migration path, and get approval. If not supported, explain why, suggest an alternative from the catalog, or recommend skipping. If the model or data format is unsupported, suggest an alternative runtime or format. If replacing an existing solution, verify the removal won't break the system. If it would, tell the user what breaks and ask how to proceed.

## Phase 3: Plan

Build the implementation plan autonomously for straightforward parts (file naming, placement following existing conventions, boilerplate config with obvious defaults). When you encounter a **high-impact decision**, stop and present it to the developer before continuing.

A decision is high-impact when it affects:
- Authentication or secrets management (security implications)
- Wiring pattern when multiple valid approaches exist (architecture)
- Breaking changes or migrations
- Resource sizing when the component is latency or cost sensitive
- Replacing an existing solution (risk of regression)

For each high-impact decision, present 2-3 concrete options with a one-line tradeoff per option. Wait for the developer to choose before continuing to the next decision. Resolve decisions one at a time.

After all decisions are resolved, present the complete plan: component name and version, every file to create or modify with a one-line description, how the component wires into existing code, what deployment assets land where, and any risks or breaking changes. Wait for explicit approval. If the user requests changes, revise and present again.

## Phase 4: Implement

For the current deployment target:

**Manifests and config.** Generate the resources the component needs. Match the project's deployment style and place them alongside existing deployment assets. Prefer OpenDataHub images over downstream when available. The component must be managed by the OpenShift AI operator — enable it via the DataScienceCluster CR so the operator installs its CRDs. If additional CRDs beyond what the operator provides are needed, ask the user for explicit permission before installing them. Never guess CRD schemas or field names.

**Wire into the project.** Connect the component to application code (endpoints, env vars, SDK clients). This step is required, not optional. Limit changes to the minimum wiring needed.

**Document.** Add a section to the project README or a dedicated doc explaining what was added, how it integrates, how to configure it, and how to verify it.

**Implementation checkpoints.** If during implementation you encounter a high-impact choice that was not anticipated in the Phase 3 plan, stop before proceeding. Explain why the decision matters, present 2-3 options with short code or config snippets showing each alternative, and proceed only with the developer's chosen approach. If no unanticipated important decisions arise, execute without interruption.

Do not expand scope. The goal is to add the component and connect it to the project. Do not build UI flows, APIs, or behavior the project did not already have unless strictly required for wiring. If integration suggests a larger feature, note it and ask before implementing.

## Phase 5: Test

Launch the **`unbiased-test-writer`** agent. It must not have access to this conversation or the Phase 4 implementation. Pass it the component name and catalog entry, the public contract (endpoints, CRD status fields, health checks, expected behaviors from the official docs), the deployment target and namespace, and the project's test conventions (framework, directory, naming, run command) only.


## Phase 6: Deploy and verify

Ask the user for permission to deploy. Once approved, deploy using the method from Phase 2, run the tests from Phase 5, and fix any failures. Confirm no regressions in existing tests.

If the user chose multiple targets, move to the next one. Adapt the Phase 4 implementation, ensure all tests pass, and keep target-specific config isolated (separate overlay, separate compose file, env-specific values). Repeat until all targets are covered.

Report the results to the user: all tests pass on all targets, no regressions, documentation updated.
