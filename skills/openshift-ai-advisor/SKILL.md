---
name: openshift-ai-advisor
description: Analyze a project and recommend OpenShift AI components. Use when the user wants guidance on OpenShift AI architecture, asks "what should I deploy", or wants to integrate OpenShift AI into an existing project.
disable-model-invocation: true
---

# OpenShift AI Advisor

**Scan the user's project for ML/AI patterns and recommend which OpenShift AI components replace or improve what exists.**

## Steps

### 1. Load the component catalog

Read [openshift-ai-components.md](../../docs/openshift-ai-components.md). This is the full list of available components with requirements and descriptions.

### 2. Analyze the project

Spawn a `project-scanner` subagent. Pass it the contents of `references/detection-signals.md`. Each category lists capability patterns plus a short **RHOAI:** tag for OpenShift AI / ODH presence. The subagent returns a structured summary grouped by category, with an Implementation sign (`generic` | `openshift-ai` | `openshift`) on each finding.

Summarize the findings to the user before proceeding. Name concrete files, imports, and patterns discovered. Explicitly call out which capabilities are already on **OpenShift AI** or **OpenShift** versus generic DIY/third-party implementations.

### 3. Identify beneficial additions

Read `references/adoption-bundles.md` and `references/signal-component-map.md`. Based on step 2 findings, identify components the project is **missing** that would bring the most value. Categorize each suggestion:

- **Observability** — drift detection, bias monitoring (TrustyAI)
- **Verification** — model evaluation, RAG quality scoring (LMEval, RAGAS)
- **Production readiness** — autoscaling, canary rollouts, guardrails (KServe, Serverless, NeMo Guardrails)
- **Governance** — versioning, audit trails, stage promotion (Model Registry, Model Catalog)
- **Automation** — pipelines, experiment tracking (KFP, MLflow)

For each suggestion, state the category and a one-line reason why it matters for this project. Present as a categorized list. Do not include components the project already has.

### 4. Evaluate migration candidates

Read `references/signal-component-map.md`. Cross-reference with step 2 findings to find where existing code **already does what an OpenShift AI component does**.

For each overlap, spawn a `migration-evaluator` subagent. Pass it the component name, its description from the catalog, and the project analysis summary from step 2. Each subagent returns an easy or more complex verdict.

Launch all subagents in parallel. Present as a checklist:

```
Migration Candidates:
Easy to implement:
✅ [Component] — [what gets replaced, file paths]
More complex:
⚠️ [Component] — [what gets replaced, why it's more complex]
```

Both easy and more complex migrations carry forward to step 5.

### 5. Assess effort vs. value

Go over **all** suggestions from steps 3 and 4. For each candidate (both additions and migrations), spawn an `effort-assessor` subagent. Pass it the component name, its description from the catalog, whether it is a migration or addition, and the project analysis summary from step 2. Each subagent returns a worth-it or not-worth-it verdict.

Launch all subagents in parallel. Present the results. Only components marked "worth it" carry forward to step 6. Components marked "not worth it" go into a "future improvements" note with the reason.

#### Show the results

Output the following to the user, filling in one entry per component:

```
Migrations worth doing:

✅ [Component] (easy)
    Replaces: [what existing code/infra it replaces]
    Why here: [2-3 sentences — why this component fits this project specifically, referencing concrete files or patterns found]
    Tip: [one actionable suggestion — e.g. order of migration, what to test first, or a gotcha to watch for]

Additions worth doing:

✅ [Component] ([category])
    Why here: [2-3 sentences — what gap it fills in this project, tied to specific findings from the scan]
    Tip: [one actionable suggestion — e.g. start with X before Y, pair with Z, or a quick win to try first]

Future improvements (not worth it now):

⚠️ [Component] (more complex)
    Why not now: [a sentence — what makes the effort or risk too high right now]
```

Omit any section that has zero items.

### 6. Ask the user's goal

Read `references/adoption-bundles.md`. Cross-reference step 2 findings against each bundle's prerequisites. A bundle qualifies when 2+ prerequisites are already present. Most projects qualify for 0 bundles. Never suggest more than 2.

The user already saw the full details in step 5. Build `AskQuestion` options as short labels only. Title: "What would you like to do?" Include only the options that apply:

1. **Migrate to [component names]** — list the migration candidates approved in step 5. Example: *"Migrate to KServe + MLflow"*
2. **Add [component name]** — one option per approved addition. Example: *"Add NeMo Guardrails"*
3. **[Bundle name] bundle** (0-2 options) — just the bundle name. Example: *"RAG bundle"*

If the user picks a bundle, its components go straight to step 7. If none of the options fit, ask the user to state their goal. One question at a time.

### 7. Compile and execute

Present a numbered execution plan:

```
Execution Plan:
1. [Component] — [what gets added and where]
   Context: "[paths, runtimes, integration points]"
2. ...
```

**Wait for explicit user confirmation.**

When confirmed, run one subagent per component, sequentially. Each subagent reads the `add-openshift-ai-component` skill and receives the component name plus the context string from the plan.

## Guardrails

- Analyze the project first. Never skip straight to asking what to add.
- Only suggest components relevant to what was found. Do not dump the catalog.
- One clarifying question at a time. Do not overwhelm with options.
- Prefer the simplest component set that solves the problem.
- Mention dependencies so the user knows the full deployment scope.
- If the use case spans multiple categories, break it into phases.
- Never run execution subagents until the user confirms the plan.
- Keep the direct-fits list to 2-4 items. Move anything requiring significant rework to "future improvements."

**Reply:** the execution plan from step 7, confirmed by the user, then the results of each component addition.
