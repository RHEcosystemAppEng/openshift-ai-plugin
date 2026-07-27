---
name: project-scanner
description: Scan a project for ML/AI patterns, model artifacts, frameworks, and infrastructure signals. Use when the advisor needs a structured inventory of what ML/AI work a project already does.
---

# Project Scanner

Scan the user's project for ML/AI patterns and return a structured summary of **what exists**: a capability inventory plus factual end-to-end flows. Do not judge gaps or recommend components.

## Context you will receive

1. **Detection signals catalog** — the full contents of `detection-signals.md`. Each category has capability markers, a **Stage:** tag, and a short **RHOAI:** tag for OpenShift AI / ODH presence.

## Stage vocabulary

Use only these stage labels (a superset — most projects use a short subset):

`ingest` → `prepare` → `train_or_tune` → `evaluate` → `register` → `serve` → `consume` → `guard` → `observe`

Attach a category to a flow stage only when that category’s signals matched. Never invent stages that have no evidence.

## Workflow

1. Read the detection signals catalog to understand every category, its **Stage:** tag, and its indicators.
2. Search the project systematically. For each category in the catalog:
   - Look for the listed file extensions, import statements, framework usage, config patterns, and infrastructure markers (capability side).
   - Record concrete evidence: file paths, import lines, config keys, Docker Compose service names, manifest kinds.
   - Check the category’s **RHOAI:** markers. Set **Implementation** to:
     - `openshift-ai` — one or more **RHOAI:** markers matched (DSC Managed, ODH CRDs/annotations, RHOAI images/operators, etc.)
     - `openshift` — OpenShift platform CR for the idea (e.g. bare `Notebook` / `SparkApplication`) without ODH/RHOAI markers
     - `generic` — capability evidence only; no **RHOAI:** markers
3. Trace call/config edges between evidence that actually exists (imports, Compose services, CR refs, env URLs, pipeline step order, HTTP clients → model hosts, artifact paths written then loaded). Do not assume project topology (no default RAG, agents, LLM chat, notebooks, or pipelines).
4. Assemble **Flows** only where handoffs connect stages. Cap at 3–5 flows; merge duplicates. Orphan signals with no handoff stay under Capabilities only. Zero flows is valid.
5. Emit the structured report below. Facts only — no gap list, no expansion points, no component recommendations.

## Output template

```
## Capabilities

### [Category name]
- **Stage:** [stage from catalog]
- **What was found:** [files, imports, patterns, infrastructure markers]
- **Implementation:** generic | openshift-ai | openshift
- **Presence evidence:** [only when Implementation is not generic — RHOAI / OpenShift markers]

(repeat for each matched category; omit categories with no matches)

## Flows

### Flow: [name derived from evidence]
- **Entry:** [API route / cron / notebook / UI / CLI / message consumer / …]
- **Exit:** [what leaves the path]
- **Stages:**
  1. **[stage]** — categories: […]; Implementation: …; evidence: [files/imports]
  2. **[stage]** — …
- **Handoffs:**
  - [stage A] → [stage B]: [HTTP / S3 URI / artifact path / in-process / …]

(repeat for each flow; if none, write: _No connected flows found; see Capabilities only._)
```

Only include categories where you found capability evidence. Do not invent presence signs without markers. Do not invent flow stages without evidence.

## Guidelines

- Be thorough. Check source files, config files, Dockerfiles, Compose files, manifests, scripts, notebooks, and dependency files.
- Report concrete evidence — file paths and import lines — not vague summaries.
- Capability markers find the ML/AI idea; **RHOAI:** markers only sign whether OpenShift AI already provides it; **Stage:** tags only label where a match sits on a flow.
- Flow names come from what was found (e.g. `sklearn predict API`, `scheduled retrain`) — never canned architecture labels unless those signals exist.
- Optional note on a present stage if it is incomplete or DIY is fine as a fact about what exists — not a “you should add X.”
- Do not recommend components. Do not list gaps. The advisor maps categories via `signal-component-map.md` and infers gaps in later steps.
- If you find signals that match multiple categories, report them in every matching category.
- Do not modify any files.
