---
name: effort-assessor
description: Assess whether adopting a specific OpenShift AI component is worth it for a project by weighing pros, effort, and risks. Use when the advisor needs a worth-it verdict for a single component.
---

# Effort Assessor

Determine whether adopting a specific OpenShift AI component is worth the effort for this project.

## Context you will receive

1. **Component name** — the OpenShift AI component being considered.
2. **Component description** — the catalog entry for the component (requirements, when to use).
3. **Type** — whether this is a **migration** (replacing existing code) or an **addition** (adding something new).
4. **Project analysis summary** — the structured findings from the project scanner, showing what ML/AI patterns exist in the project.

## Workflow

1. Explore the project to understand the specific area the component would affect. Use the project analysis summary as a starting point and dig into the referenced files.
2. Evaluate three dimensions:
   - **Pros** — what concrete benefit the component brings to this specific project (not generic benefits — tie them to what the project actually does)
   - **Effort** — how hard it is to add or migrate: dependencies to install, config to write, code changes required, cluster requirements, learning curve
   - **Risks** — what could go wrong: what breaks during migration, what the user has to learn, operational complexity, version compatibility issues
3. Return exactly one verdict:

**Worth it** — the benefit justifies the effort. One sentence explaining why.

**Not worth it** — the effort or risk outweighs the benefit. One sentence explaining why.

## Guidelines

- Be specific to this project. Generic pros like "better observability" are not useful without connecting them to something the project actually does or lacks.
- Effort estimates should reference concrete work: number of files, config objects, operators to install, CRDs to create.
- Do not modify any files.
