# Project Structure Detection — Shared Reference

Every `add-openshift-ai-*` skill MUST detect the user's project structure before generating files.
Read this file after completing cluster checks.

## Detection Algorithm

Scan the workspace root for the following indicators, in order of priority:

### 1. Helm

Look for `Chart.yaml` files:
```bash
find . -name "Chart.yaml" -maxdepth 3
```

If found, the project uses Helm. Note the chart location(s). Generated output should be:
- Helm values in the appropriate `values.yaml`
- Templates in the chart's `templates/` directory
- If multiple charts exist, ask the user which one to add to

### 2. Kustomize

Look for `kustomization.yaml` or `kustomization.yml` files:
```bash
find . -name "kustomization.yaml" -o -name "kustomization.yml" -maxdepth 3
```

If found, the project uses Kustomize. Generated output should be:
- Resources as standalone YAML files
- Entries added to the `resources:` list in `kustomization.yaml`
- If an `overlays/` directory exists, ask if the user wants base or overlay placement

### 3. GitOps (ArgoCD / Flux)

Look for ArgoCD `Application` or `ApplicationSet` CRDs, or Flux `Kustomization`/`HelmRelease` CRDs:
```bash
grep -rl "kind: Application" --include="*.yaml" --include="*.yml" . 2>/dev/null | head -5
grep -rl "kind: HelmRelease" --include="*.yaml" --include="*.yml" . 2>/dev/null | head -5
```

If found, the project uses GitOps. Generated output should be:
- Standalone YAML files in the appropriate directory
- Follow the existing directory convention (e.g., `apps/`, `manifests/`, `clusters/`)

### 4. Raw YAML

If none of the above are detected, or if only plain `.yaml`/`.yml` files exist, treat as raw YAML.

Generated output should be:
- Standalone YAML files
- Suggest a directory like `openshift-ai/<component-name>/`

## Output Format Decision

After detection, report to the user:

> "I detected your project uses **[Helm / Kustomize / GitOps / raw YAML]**. I'll generate the manifests in that format.
> Suggested location: `<path>`
> Do you want to proceed, or place the files somewhere else?"

Wait for user confirmation before generating files.

## Multiple Format Handling

If multiple formats are detected (e.g., a Helm chart AND Kustomize overlays), ask the user which one to target:

> "I found both Helm charts and Kustomize overlays in your project. Which format should I generate for?"

## Empty Project

If the project is empty or has no recognizable structure, default to raw YAML and suggest:

> "No existing Kubernetes manifest structure detected. I'll generate raw YAML files. Consider running the `init-openshift-ai-project` skill first to set up a project structure."
