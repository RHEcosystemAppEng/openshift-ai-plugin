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

Spawn a `project-scanner` subagent. Pass it the contents of `references/detection-signals.md`. Each category lists capability patterns, a **Stage:** tag, and a short **RHOAI:** tag for OpenShift AI / ODH presence. The subagent returns **Capabilities** (per category, with Implementation `generic` | `openshift-ai` | `openshift`) plus factual **Flows** (observed stage chains and handoffs). Step 2 records what exists only — no gaps, no component pitches.

Summarize to the user before proceeding:

- Lead with each discovered **flow** as a stage chain. Name concrete files, imports, and handoffs.
- Per stage, call out **OpenShift AI** / **OpenShift** versus generic DIY/third-party.
- Add a compact **Capabilities** appendix for categories that did not join a flow.
- Do not suggest missing components here.

### 3. Identify beneficial additions

Read `references/adoption-bundles.md` and `references/signal-component-map.md`. Using the step 2 **flow map and capabilities**, identify components the project is **missing** that would bring the most value. Prefer suggestions that extend an **observed** flow over “category not found globally.” Each Problem must cite a flow (or capability evidence) that makes the addition relevant.

Categorize each suggestion:

- **Observability** — drift detection, bias monitoring (TrustyAI)
- **Verification** — model evaluation, RAG quality scoring (LMEval, RAGAS)
- **Production readiness** — autoscaling, canary rollouts, guardrails (KServe, Serverless, NeMo Guardrails)
- **Governance** — versioning, audit trails, stage promotion (Model Registry, Model Catalog)
- **Automation** — pipelines, experiment tracking (KFP, MLflow)

For each suggestion, state the category and explain it with Problem / Solution. Build this as an internal categorized list — **do not show it to the user**; carry it to step 5. Do not include components the project already has.

```
[Category]
✅ [Component]
    Problem: [1-2 sentences — concrete gap from the scan, with file/pattern evidence]
    Solution: [1-2 sentences — what this component does and the first step to adopt it]
```

### 4. Evaluate migration candidates

Read `references/signal-component-map.md`. Cross-reference with step 2 findings to find where existing code **already does what an OpenShift AI component does**.

For each overlap that isn't identified as an addition at step 3, spawn a `migration-evaluator` subagent. Pass it the component name, its description from the catalog, and the full project analysis from step 2 (capabilities **and** the relevant flow(s) with stages and handoffs). Each subagent returns an easy or more complex verdict.

Launch all subagents in parallel. Build this as an internal checklist — **do not show it to the user**; carry it to step 5:

```
Migration Candidates:
Easy to implement:
✅ [Component] — [what gets replaced, file paths]
More complex:
⚠️ [Component] — [what gets replaced, why it's more complex]
```

Both easy and more complex migrations carry forward to step 5.

### 5. Rank suggested flows (impact, then complexity)

First recommendation surface after step 2. Assess **all** step 3 additions and step 4 migrations yourself (no subagent).

Read `references/suggested-flow-rubric.md`. For each candidate:

1. Build one **suggested flow** = one step-2 observed flow + one component (one component per suggested flow). Keep the pairing internal — do not invent display labels.
2. Score **Impact** (`high` / `medium` / `low`) and **Complexity** (`low` / `medium` / `high`) per the rubric. Impact=`high` only when the change improves AI outcome quality on that flow (correctness, eval, safety, reliability) — not platform packaging alone. Complexity follows touch count (files/model/config/operators).
3. Rank lexicographically: Impact high→low, then Complexity low→high.
4. **Cut:** worth doing only if Impact=`high` **and** Complexity is `low` or `medium`. Everything else → Future (including high impact + high complexity).

Only worth-doing suggested flows carry forward to step 6.

#### Show the results

Populate from the cut only:
- **Migrations worth doing** ← step 4 suggested flows that pass the cut
- **Additions worth doing** ← step 3 suggested flows that pass the cut
- **Future improvements** ← suggested flows that fail the cut

Present worth-doing lists in rank order. Show the **component name** only (no suggested-flow labels). Do not print internal score sheets. Output the following to the user, using simple and understandable language:

```
Migrations worth doing:

✅ (show this emoji) [Component] (easy|more complex)
    Replaces: [what existing code/infra it replaces]
    Problem: [1-2 sentences — concrete gap from the scan, with file/pattern evidence]
    Solution: [1-2 sentences — what this component does and the first step to adopt it]

✅ ...

Additions worth doing:

✅ (show this emoji) [Component] ([category])
    Problem: [1-2 sentences — concrete gap from the scan, with file/pattern evidence]
    Solution: [1-2 sentences — what this component does and the first step to adopt it]

✅ ...

Future improvements (not worth it now):

⚠️ (show this emoji) [Component] (Impact: …, Complexity: …)
    Why not now: [a sentence — impact too low, not a quality win, or complexity too high]

⚠️ ...
```

Omit any section that has zero items.

### 6. Ask the user's goal

Read `references/adoption-bundles.md`. Cross-reference step 2 findings against each bundle's prerequisites. A bundle qualifies when 2+ prerequisites appear **on the same flow** (not scattered unrelated hits). Most projects qualify for 0 bundles. Never suggest more than 2.

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
- Never dump raw step 3/4 candidates; only step 5’s ranked suggested flows.

**Reply:** the execution plan from step 7, confirmed by the user, then the results of each component addition.
