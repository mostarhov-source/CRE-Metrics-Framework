# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## What This Repo Is

A knowledge framework (not a software project — no build system, no tests, no CI) for measuring business value from PropTech and AI investments in Commercial Real Estate. The primary output is structured markdown and YAML consumed by LLM agents, RAG pipelines, and the sister project [CRE-AI-Intelligence](https://github.com/mostarhov-source/CRE-AI-Intelligence).

**There are no commands to run.** Changes are validated by reading files, not executing code.

---

## Architecture

### Four-layer hierarchy
```
PVL (Primary Value Levers — 5)
  → ABO (Aggregated Business Outcomes — 5)
    → BODM (Business Outcome-Driven Metrics — 40)
      → TODM (Technology-Outcome Driven Metrics — 25)
```

### File structure
```
framework/
  chains/          ← 5 self-contained chain files (LLM entry points, load one per value lever)
  metrics/pvl/     ← 5 metric files
  metrics/abo/     ← 5 metric files
  metrics/bodm/    ← 40 metric files
  metrics/todm/    ← 25 metric files
  interfaces/
    machine-readable/metrics-registry.yaml   ← canonical stable URL for all consumers
    machine-readable/chains-map.yaml
    llm-prompts/                             ← 3 prompt patterns
    skills/retrieve-metrics.md              ← Claude Code skill
    consumers/cre-ai-intelligence.md        ← integration contract
docs/superpowers/specs/                     ← reasoning artefacts from design sessions
```

### Every metric file has:
- YAML frontmatter: `id`, `type`, `category`, `chains`, `metric_type`, `timing`, `measurement_cadence`, `formula`, `target`, `data_sources`, `last_updated`
- Human-readable body: definition, why it matters, formula, data sources, benchmarks

### The stable consumer URL (never change this path):
```
https://raw.githubusercontent.com/mostarhov-source/CRE-Metrics-Framework/main/framework/interfaces/machine-readable/metrics-registry.yaml
```

---

## Metric Classification Fields (added 2026-06-09)

Every metric now carries three classification fields grounded in the *RAG | Books | Metrics And Measurement* methodology:

| Field | Values | Meaning |
|-------|--------|---------|
| `metric_type` | `process \| output \| outcome \| effect` | Where in the measurement chain (Process = workflow speed; Output = deliverable produced; Outcome = behaviour change; Effect = strategic impact) |
| `timing` | `lead \| lag` | Lead = team-controllable, predictive, changes within a goal cycle. Lag = confirmatory, historical |
| `measurement_cadence` | `daily \| weekly \| monthly \| quarterly \| annual \| per-project` | Operational measurement frequency — determines whether a metric functions as lead or lag in practice |

**Methodology source (NotebookLM):** https://notebooklm.google.com/notebook/d082f969-0133-4ac3-a117-e2e6d3b7b401  
Full classification reasoning is in `docs/superpowers/specs/2026-06-09-metrics-classification-output-outcome-effect.md`.

---

## Key Design Rules

- **Chain files are self-contained.** An LLM loading one chain file can answer all PVL → BODM → TODM traversal questions without reading anything else. Don't add cross-chain dependencies to chain files.
- **`metrics-registry.yaml` is the only stable interface.** All external consumers reference it. When adding metrics or changing schema, bump the version (`1.x` minor = additive, `2.0` major = breaking rename/hierarchy change).
- **Individual metric files are atomic.** Each is independently readable. Don't add content that only makes sense relative to another metric file.
- **Legacy `_all.md` files** (`PVL_all.md`, `ABO_all.md`, etc.) are deprecated — kept for migration reference, will be removed in v2.0. Do not add new content to them.

---

## When Adding a New Metric

1. Create the metric file in `framework/metrics/{pvl|abo|bodm|todm}/{id}.md` following existing frontmatter schema
2. Add the entry to `framework/interfaces/machine-readable/metrics-registry.yaml` (bump minor version)
3. Add it to the relevant chain file(s) in `framework/chains/`
4. Add it to `framework/INDEX.md`

---

## Reasoning Artefacts

Design decisions are preserved in `docs/superpowers/specs/`. Key files:
- `2026-06-07-metrics-framework-restructure-design.md` — v2 architecture decisions
- `2026-06-09-metrics-classification-output-outcome-effect.md` — classification system spec (reasoning artefact)
- `2026-06-09-metrics-classification-gap-analysis.md` — gap analysis against source methodology

These are permanent records, not temporary scaffolding.
