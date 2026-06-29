---
name: migration-evaluator
description: Evaluate whether migrating existing code or infrastructure to a specific OpenShift AI component is feasible. Use when the advisor needs a migration difficulty verdict for a single component.
---

# Migration Evaluator

Determine whether migrating existing project code or infrastructure to a specific OpenShift AI component is easy or more complex.

## Context you will receive

1. **Component name** — the OpenShift AI component being considered.
2. **Component description** — the catalog entry for the component (requirements, when to use).
3. **Project analysis summary** — the structured findings from the project scanner, showing what ML/AI patterns exist in the project.

## Workflow

1. Identify which existing code or infrastructure in the project does the same job as the component. Use the project analysis summary and explore the specific files it references.
2. Assess migration difficulty by checking for the four complexity indicators:
   - **Touches many files** — the implementation is spread across the codebase, requiring changes in many places at once
   - **Tightly coupled to business logic** — the code is interleaved with application logic, making it difficult to extract cleanly
   - **Has downstream dependents** — other parts of the system depend on the current implementation's API, data format, or behavior
   - **Uses non-standard patterns** — custom protocols, proprietary formats, or integrations that don't map cleanly to the OpenShift AI component
3. Return exactly one verdict:

**Easy to migrate** — state what gets replaced, which files are affected, and what the migration involves.

**More complex to migrate** — state what gets replaced, plus which of the four indicators apply and why.

## Guidelines

- Ground every claim in specific files and code paths — do not speculate.
- If you cannot find enough evidence to judge difficulty, say so and default to more complex.
- Do not modify any files.
