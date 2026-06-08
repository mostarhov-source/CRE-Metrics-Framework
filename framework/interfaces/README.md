# CRE Metrics Framework — Consumer Interface Guide

This directory contains everything an external system, LLM agent, or community contributor needs to consume the CRE Metrics Framework without depending on internal file paths.

---

## Stable Entry Points

### 1. Metrics Registry (machine-readable)

The **only URL external consumers need to reference:**

```
https://raw.githubusercontent.com/mostarhov-source/CRE-Metrics-Framework/main/framework/interfaces/machine-readable/metrics-registry.yaml
```

This file lists all 75 metrics with their canonical IDs, names, types, and chain memberships. It is stable across all internal restructures. Version-bumped when breaking changes occur.

### 2. Chain Files (LLM entry points)

For LLM agents doing chain traversal or case study analysis, load the relevant chain file:

```
framework/chains/cost-savings.md
framework/chains/revenue-growth.md
framework/chains/risk-reduction.md
framework/chains/esg-sustainability.md
framework/chains/productivity-workflow.md
```

Each chain file is self-contained — an LLM can load one file and answer full PVL → ABO → BODM → TODM traversal questions without fetching anything else.

### 3. Individual Metric Files (RAG / atomic lookup)

For RAG pipelines or direct metric lookup, individual metric files are in:

```
framework/metrics/pvl/   — 5 files
framework/metrics/abo/   — 5 files
framework/metrics/bodm/  — 40 files
framework/metrics/todm/  — 25 files
```

Each file has YAML frontmatter with machine-readable fields (id, type, chains, formula, target) and a human/LLM-readable body.

---

## When to Use What

| Task | Use |
|------|-----|
| Look up a metric by name or chain | `metrics-registry.yaml` |
| Traverse a full value chain (PVL → TODM) | `chains/{chain-id}.md` |
| Map a case study to the framework | `chains/{chain-id}.md` + `llm-prompts/case-study-analysis.md` |
| RAG over individual metrics | `metrics/{type}/{metric-id}.md` files |
| Build an agent that retrieves metrics | `skills/retrieve-metrics.md` |

---

## Versioning

The registry uses semantic versioning:
- **Minor bump** (e.g., 1.1 → 1.2): new metric added — non-breaking
- **Major bump** (e.g., 1.x → 2.0): metric renamed or hierarchy changed — breaking, review required

Check `metrics-registry.yaml` → `version` field before assuming consumer compatibility.

---

## For Prompt Patterns

See `llm-prompts/` for ready-to-use instruction blocks:
- `case-study-analysis.md` — map a case study to the value chain
- `metric-lookup.md` — find a metric by name or category
- `value-chain-traversal.md` — navigate from PVL down to TODM (or reverse)

---

## For Integration Contracts

See `consumers/cre-ai-intelligence.md` for the integration contract with the CRE-AI-Intelligence project.
