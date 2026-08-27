---
name: migration-evaluator
description: Evaluate whether migrating existing code or infrastructure to a specific OpenShift AI component is feasible. Use when the advisor needs a migration difficulty verdict for a single component.
disable-model-invocation: true
---

# Migration Evaluator

Determine whether migrating existing project code or infrastructure to a specific OpenShift AI component is easy or more complex.

## Context you will receive

1. **Component name** — the OpenShift AI component being considered.
2. **Component description** — the catalog entry for the component (requirements, when to use).
3. **Project analysis summary** — step 2 output: **Capabilities** (category evidence + Implementation signs) and **Flows** (observed stages, handoffs, entry/exit). There is no precomputed gap list — use the flow facts to judge coupling along the path.

## Workflow

1. Identify which existing code or infrastructure in the project does the same job as the component. Use the capabilities and the relevant flow(s); explore the specific files they reference.
2. Assess migration difficulty against these four dimensions. Ground each in specific files; record counts where possible:
   - **Blast radius** — how many files must change to replace the current implementation (count them).
   - **Coupling** — whether the implementation sits behind a swappable boundary, or is interleaved with application/business logic.
   - **Downstream dependents** — how many other modules, services, or later flow stages depend on the current API, data format, or behavior.
   - **Interface mismatch** — whether the OpenShift AI component’s inputs/outputs map cleanly (1:1 or thin adapter) or require a non-trivial rewrite.
3. Return exactly one verdict:

**More complex to migrate** — if any of the following is true:
   - Blast radius ≥ 10 files, or the change spans ≥ 3 packages/services
   - Two or more of: high coupling, ≥ 2 downstream dependents, severe interface mismatch
   - Severe interface mismatch alone (no thin adapter; consumers must change contract)
   - Insufficient evidence to judge (default to more complex)

   State what gets replaced, which dimensions fired, and the file/path evidence.

**Easy to migrate** — none of the above. State what gets replaced, which files are affected, and what the migration involves.

Do not factor in project maturity, priority vs other components, or whether the work is worth doing now — that belongs to the advisor’s step 5 suggested-flow rubric (impact, then complexity).

## Guidelines

- Ground every claim in specific files and code paths — do not speculate.
- Prefer the flow(s) that include the overlapping stage when judging dependents and handoffs.
- If you cannot find enough evidence to judge difficulty, say so and default to more complex.
- Do not modify any files.
