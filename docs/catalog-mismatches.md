# Catalog mismatches (removed from component catalog)

These entries were removed from [`openshift-ai-components.md`](openshift-ai-components.md) because they fail the **strict** catalog bar used for Core candidates: they are generic OpenShift/platform enablers (or metadata), not direct LLM / agent / MLOps solutions.

They may still appear as **requirements** on real AI components (for example KServe Knative mode needing Serverless + Service Mesh). They are not catalog solutions to recommend as AI capabilities.

| Component | Why it is a mismatch |
|-----------|----------------------|
| **Data Science Projects** | Namespace + RBAC packaging / tenancy. Organizational boundary, not an ML/LLM/agent capability. |
| **S3-Compatible Object Storage Connections** | Generic S3 wiring for any workload. Useful for datasets and artifacts, but not AI-specific (vector storage such as ODF S3 Vectors is a different, AI-relevant item). |
| **OpenShift Serverless (Knative Serving)** | Generic serverless scale-to-zero. Only relevant as a dependency of KServe Knative mode / bursty inference, not as an AI solution itself. |
| **OpenShift Service Mesh (Istio)** | Generic service mesh (mTLS, routing, observability). Required by some AI stacks (Knative KServe, Llama Stack), not an AI capability. |
| **Usage Telemetry** | Operator/admin platform usage reporting. No project-facing model, agent, RAG, or MLOps lifecycle value. |
| **Stable API Tiers** | Documentation/support-tier metadata for APIs. Not a deployable component or AI solution. |

## Borderline (kept in catalog for now)

These are platform-adjacent but still AI-oriented enough to remain in `openshift-ai-components.md` unless you decide otherwise later:

- **Workbenches** — interactive DS/AI IDEs
- **Custom Notebook Images** — org-standard workbench images
- **Hardware Profiles & Accelerator Management** — GPU/accelerator allocation for AI workloads
