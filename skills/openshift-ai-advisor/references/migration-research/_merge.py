#!/usr/bin/env python3
"""Merge migration-research/*.md Row sections into signal-component-map.md."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / "signal-component-map.md"
RESEARCH = Path(__file__).resolve().parent

COMPONENTS = [
    "KServe (Single-Model Serving Platform)",
    "vLLM Serving Runtimes",
    "Distributed Inference with llm-d",
    "Models-as-a-Service (MaaS)",
    "Caikit TGIS ServingRuntime",
    "OpenVINO Model Server (OVMS)",
    "NVIDIA Triton Inference Server",
    "MLServer ServingRuntime",
    "Red Hat AI Model Optimization Toolkit (LLM Compressor)",
    "AI Inference Tool Calling",
    "Speculative Decoding (Speculators)",
    "OCI ModelCar Inference Serving",
    "Gateway API Inference Extensions",
    "Model Registry",
    "Model Catalog",
    "Llama Stack (Operator)",
    "RAG Stack Deployment",
    "AutoRAG",
    "MCP Gateway",
    "A2A Agent Registry",
    "Red Hat build of Agent Sandbox",
    "MCP Authorization Server",
    "MCP Catalog",
    "MCP Gateway Authorization",
    "Prompt Template Registry",
    "Kagenti Operator",
    "HITL Tool Approval",
    "MCP Tool Registry",
    "MCP server for OpenShift Container Platform",
    "Query-based Tool Filtering",
    "Camel Docling",
    "Workbenches",
    "Custom Notebook Images",
    "Data Science Pipelines (Kubeflow Pipelines)",
    "Kubeflow Spark Operator (KSO)",
    "Distributed Workloads (KubeRay, Training Operator)",
    "Model Customization (Fine-Tuning)",
    "AutoML",
    "LM Evaluation (LMEval)",
    "Guardrails (NeMo Guardrails)",
    "RAGAS Evaluation Provider",
    "EvalHub",
    "Automated Risk Assessment",
    "Model Monitoring (TrustyAI)",
    "Gen AI Playground",
    "MLflow Integration",
    "Feature Store",
    "Red Hat Connectivity Link (RHCL)",
    "Hardware Profiles & Accelerator Management",
]


def escape_cell(s: str) -> str:
    s = s.replace("\r", " ").replace("\n", " ").replace("|", "\\|")
    s = s.rstrip()
    while s.endswith("\\"):
        s = s[:-1].rstrip()
    return s.strip()


def extract_row(text: str, component: str) -> tuple[str, str] | None:
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            continue
        if component not in line:
            continue
        parts = [p.strip() for p in line.strip().strip("|").split("|")]
        parts = [p.replace("\\|", "|") for p in parts]
        if len(parts) >= 3 and parts[1] == component:
            return parts[0], parts[2]
        # also accept component-first rows
        if len(parts) >= 3 and parts[0] == component:
            return parts[1], parts[2]
    return None


def fallback(text: str) -> tuple[str, str] | None:
    peers = []
    for line in text.splitlines():
        if line.startswith("- ") and ("—" in line or " - " in line):
            sep = "—" if "—" in line else " - "
            peers.append(line[2:].split(sep, 1)[0].strip())
    aliases = []
    in_aliases = False
    for line in text.splitlines():
        if line.startswith("## Detection aliases"):
            in_aliases = True
            continue
        if in_aliases and line.startswith("## "):
            break
        if in_aliases and line.startswith("- "):
            aliases.append(line[2:].strip())
    if peers:
        return "; ".join(peers), "; ".join(aliases) if aliases else "—"
    return None


def main() -> None:
    rows_by_component: dict[str, tuple[str, str]] = {}
    for path in sorted(RESEARCH.glob("*.md")):
        if path.name.startswith("_"):
            continue
        text = path.read_text()
        m = re.search(r"^# (.+)$", text, re.M)
        if not m:
            continue
        component = m.group(1).strip()
        extracted = extract_row(text, component) or fallback(text)
        if extracted:
            rows_by_component[component] = extracted

    lines = [
        "# Migration component map",
        "",
        "Maps **non–OpenShift / non–OpenShift AI** peers (and concrete DIY patterns) to catalog components from `docs/openshift-ai-components.md`. Used by OpenShift AI Advisor step 4 to find migration candidates.",
        "",
        "One row per catalog component. Column order: suggested component first for scanning.",
        "",
        "| Suggested OpenShift / OpenShift AI component | Non-OpenShift / non-OpenShift AI peer (named + DIY) | Detection aliases (packages, images, CRDs, DIY phrases) |",
        "| --- | --- | --- |",
    ]
    done = 0
    pending = 0
    for component in COMPONENTS:
        if component in rows_by_component:
            peers, aliases = rows_by_component[component]
            lines.append(
                f"| {escape_cell(component)} | {escape_cell(peers)} | {escape_cell(aliases)} |"
            )
            done += 1
        else:
            lines.append(f"| {escape_cell(component)} | _pending research_ | _pending_ |")
            pending += 1

    # Important: no blank lines inside the table body (GFM stops the table on blank lines).
    MAP.write_text("\n".join(lines) + "\n")
    print(f"wrote {MAP}: {done} filled, {pending} pending")


if __name__ == "__main__":
    main()
