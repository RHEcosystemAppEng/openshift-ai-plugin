# Cluster Checks — Shared Reference

Every `add-openshift-ai-*` skill MUST run these checks before doing anything else.
Read this file at the start of every component skill execution.

## Step 1: Verify `oc` CLI

Run `which oc` (or `command -v oc`).

- If **not found**, tell the user: "The `oc` CLI is required but not found in your PATH. Install it from https://mirror.openshift.com/pub/openshift-v4/clients/ocp/stable/ and try again."
- If **found**, proceed.

## Step 2: Check cluster connectivity

Run `oc whoami` and `oc whoami --show-server`.

- If the command **fails**, tell the user: "You are not logged into an OpenShift cluster. Run `oc login <cluster-url>` first." Stop here until they connect.
- If **successful**, note the username and server URL for context.

## Step 3: Detect OpenShift AI version

Run:
```bash
oc get csv -n redhat-ods-operator -o jsonpath='{.items[?(@.spec.displayName=="Red Hat OpenShift AI")].spec.version}'
```

If no CSV is found, try the namespace `openshift-operators`:
```bash
oc get csv -n openshift-operators -o jsonpath='{.items[?(@.spec.displayName=="Red Hat OpenShift AI")].spec.version}'
```

- If **no version found**, warn the user: "Red Hat OpenShift AI operator not found on this cluster. The operator must be installed before adding components."
- If **version found**, store it. Currently supported: **3.4.x**. If the version is different, warn: "This plugin targets OpenShift AI 3.4. Your cluster runs version X.Y. Generated manifests may need adjustments."

## Step 4: Inspect DataScienceCluster CR

Run:
```bash
oc get datasciencecluster default-dsc -o yaml
```

- If **not found**, warn: "No DataScienceCluster CR (`default-dsc`) found. This is unusual — it should have been created by the operator. Check that the OpenShift AI operator installed correctly."
- If **found**, parse the YAML. Extract `spec.components` to determine which components are already enabled (`managementState: Managed`) vs disabled (`managementState: Removed`).

Report to the user:
- Cluster: `<server-url>`
- User: `<username>`
- OpenShift AI version: `<version>`
- Currently enabled components: `<list>`

## Step 5: Check component-specific status

Each component skill provides its own DSC field path (e.g., `spec.components.kserve.managementState`).

- If already `Managed`, inform the user: "KServe is already enabled in your DataScienceCluster. You can proceed to configure it, or skip the DSC patch."
- If `Removed` or missing, inform the user that the component needs to be enabled and that a DSC patch will be generated. **Ask for permission** before including the patch in the output.

## Step 6: Check component dependencies

Each component skill declares its prerequisites. For each prerequisite:

1. Check if the prerequisite is enabled in `default-dsc`
2. If not enabled, tell the user: "This component requires `<prerequisite>` which is not currently enabled."
3. Offer to run the prerequisite's `add-openshift-ai-*` skill first
4. **Ask for permission** before proceeding with dependency installation

Dependencies must be resolved before generating the main component's manifests.
