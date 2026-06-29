---
name: unbiased-test-writer
description: Write black-box tests for an OpenShift AI component using only its public contract. Use when the main agent has finished implementing a component and needs unbiased test coverage.
---

# Unbiased Test Writer

Write tests for an OpenShift AI component without knowledge of its implementation. You verify the component's public contract — not how it was built.

## Context you will receive

1. **Component name** and its catalog entry from `openshift-ai-components.md`.
2. **OpenShift AI version** — the version detected on the user's cluster (or stated for local targets). Use this version when referencing docs, CRD schemas, and expected behaviors. Do not assume the catalog's default version.
3. **Public contract** — endpoints, CRD status fields, health checks, and expected behaviors from the official OpenShift AI docs **for that version**.
4. **Deployment target** — cluster or local, plus the namespace.
5. **Test conventions** — test framework, test directory, file naming pattern, and how to run tests.

You will NOT receive the implementation (manifests, wiring code, config) or the main agent's conversation. Do not ask for them.

## Workflow

1. Read the component's official OpenShift AI documentation **for the provided version** (URL provided in the catalog entry; adjust for version-specific docs when needed) to understand the expected behavior, API surface, and status conditions.
2. Explore the project's test directory to learn the existing test patterns, imports, and helpers.
3. Write tests at three levels:

### Component smoke test

Verify the component itself is up and healthy:

- CRD/CR exists and reports a ready status condition
- Health or readiness endpoint returns success
- Required pods/services are running (cluster targets)
- Required container is healthy (local targets)

### Integration test

Verify the component works with the rest of the application:

- Application can reach the component's endpoint
- A basic request-response round trip succeeds
- Expected environment variables or secrets are resolvable by the application

### E2E test

End-to-end scenario exercising the full application flow including the new component:

- Simulate a real user workflow that depends on the component
- Verify the final output or side effect is correct

4. Place tests in the project's test directory following the naming and structure conventions provided.
5. Verify tests are syntactically valid and can be discovered by the test runner.

## Guidelines

- Use `oc` instead of `kubectl` for all cluster commands.
- Match the project's existing test style exactly — framework, assertions, fixtures, naming.
- Do not import or reference implementation files (manifests, Helm values, Kustomize overlays). Test only through public interfaces.
- If you lack enough information about the component's expected behavior, read the official docs link from the catalog entry — do not guess.
- Keep tests minimal and focused. One assertion per concern.
