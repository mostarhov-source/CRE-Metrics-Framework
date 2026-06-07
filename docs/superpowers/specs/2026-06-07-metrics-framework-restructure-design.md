# CRE Metrics Framework — File Structure Redesign

**Date:** 2026-06-07
**Status:** Approved for implementation
**Author:** Maksim Ostarhov

---

## Why We Are Redesigning

### The Problem

The v1.0 framework organises metrics by type: four large aggregate files (`PVL_all.md`, `ABO_all.md`, `BODM_all.md`, `TODM_all.md`). This worked for human readers scanning a single layer, but fails for the actual primary use case.

**Primary consumers are AI/LLM tools** — used for case study analysis, research synthesis, and value chain traversal. These tools need to answer:

> "Which TODMs enable this BODM, and which PVL does it roll up to?"

With the current structure, that requires loading 4 separate files and stitching relationships that are never made explicit. Cross-type linking — the core mechanic of the framework — is invisible in the files.

**Secondary problems:**

- RAG chunking loses context: a chunk about "Fault Detection Rate" does not say it belongs to Risk Reduction or which chain it enables
- Consumers (e.g., CRE-AI-Intelligence) maintain hardcoded copies of the metrics dictionary that drift from the canonical source
- Community PRs collide on the same large files, creating merge conflicts
- As new asset classes are added (Office, Retail, Residential), the `_all.md` files will grow unmanageable

### The Goal

Make the value chain (PVL → ABO → BODM → TODM) the organising principle of the file structure itself. LLMs should be able to load one file and traverse the complete chain for a given value lever. Individual metric files remain atomic and RAG-friendly.

---

## New File Structure

```
framework/
│
├── chains/                              # LLM entry point — full value chain per lever
│   ├── cost-savings.md
│   ├── revenue-growth.md
│   ├── risk-reduction.md
│   ├── esg-sustainability.md
│   └── productivity-workflow.md
│
├── metrics/
│   ├── pvl/                             # 5 files, one per Primary Value Lever
│   │   ├── cost-savings.md
│   │   ├── revenue-growth.md
│   │   ├── risk-reduction.md
│   │   ├── esg-sustainability.md
│   │   └── productivity-workflow.md
│   ├── abo/                             # 5 files, one per Aggregated Business Outcome
│   │   ├── optimised-portfolio-returns.md
│   │   ├── operational-efficiency-sustainability.md
│   │   ├── reduced-risk-compliance.md
│   │   ├── tenant-satisfaction-retention.md
│   │   └── streamlined-decision-making.md
│   ├── bodm/                            # ~40 files, one per Business Outcome-Driven Metric
│   │   ├── irr.md
│   │   ├── noi.md
│   │   ├── fault-detection-rate.md
│   │   └── ...
│   └── todm/                            # ~25 files, one per Technology-Outcome Driven Metric
│       ├── energy-savings-pct.md
│       ├── data-capture-automation-rate.md
│       └── ...
│
├── interfaces/                          # Stable contract for consumers and LLMs
│   ├── README.md                        # How to consume this framework
│   ├── machine-readable/
│   │   ├── metrics-registry.yaml        # Canonical metric IDs, names, types, chains
│   │   └── chains-map.yaml             # Explicit PVL → ABO → BODM → TODM mapping
│   ├── llm-prompts/
│   │   ├── case-study-analysis.md       # Prompt pattern: map a case study to the chain
│   │   ├── metric-lookup.md             # Prompt pattern: find a metric by name/category
│   │   └── value-chain-traversal.md    # Prompt pattern: navigate full chain
│   └── consumers/
│       └── cre-ai-intelligence.md       # Integration contract for that project
│
└── INDEX.md                             # Master navigation (updated links)
```

The existing `_all.md` files are kept during transition as deprecated summaries and removed in v2.0 once consumers have migrated.

---

## File Formats

### Individual Metric File (BODM example)

```markdown
---
id: fault-detection-rate
name: Fault Detection Rate
type: BODM
category: Operational Efficiency
chains:
  - risk-reduction
  - cost-savings
related_bodm: []
related_todm:
  - uptime-availability-automated-systems
  - iot-sensor-health-data-quality
parent_abo: reduced-risk-compliance
formula: "Faults Detected ÷ Total Faults × 100"
target: "≥90%"
data_sources:
  - BMS telemetry
  - Maintenance logs
---

# Fault Detection Rate

**Category:** Operational Efficiency
**Definition:** % of system faults detected by monitoring systems before they cause downtime or damage.

**Why It Matters:** Early detection reduces downtime, unplanned repair costs, and tenant disruption.

**Formula:** Faults Detected ÷ Total Faults × 100

**Data Sources:** BMS telemetry, maintenance logs.

**Example Target / Benchmarks:** ≥90%.
```

The YAML frontmatter is machine-readable by any consumer. The body is human-readable and LLM-friendly.

### Chain File Format

Each chain file is self-contained — an LLM can load one file and answer chain traversal questions without fetching anything else.

~~~markdown
---
id: cost-savings
name: Cost Savings
type: chain
---

# Value Chain: Cost Savings

## Primary Value Lever (PVL)

**Cost Savings** — Reduction in operating, capital, or administrative costs without compromising service quality.

## Aggregated Business Outcomes (ABO)

- **Enhanced Operational Efficiency & Sustainability** — Lower operating costs, ESG compliance, tenant retention through efficient buildings.

## Business Outcome-Driven Metrics (BODM)

| Metric | Target | Formula |
|--------|--------|---------|
| kWh/m² Reduction | ≥10% | (Baseline – Current) ÷ Baseline × 100 |
| Fault Detection Rate | ≥90% | Faults Detected ÷ Total Faults × 100 |
| NOI | Growth 2–5% YoY | Rental Income – Operating Expenses |
| ...  | ... | ... |

## Technology-Outcome Driven Metrics (TODM)

| Metric | Target | Enables |
|--------|--------|---------|
| Energy Savings % | 10–20% | kWh/m² Reduction |
| IoT Sensor Health & Data Quality | ≥98% | Fault Detection Rate |
| Data Capture Automation Rate | ≥80% | Financial Dashboard Automation |
| ... | ... | ... |

## Example Value Chain

```
Cost Savings (PVL)
  ↓
Enhanced Operational Efficiency (ABO)
  ↓
kWh/m² reduced by 23% (BODM)
  ↓
Energy Savings % = 23% via AI-powered BMS (TODM)
  ↓
Financial Impact: £2.3M annual savings / £45M portfolio value lift
```
~~~

### metrics-registry.yaml (Stable Consumer Interface)

```yaml
version: "1.1"
last_updated: "2026-06-07"
metrics:
  - id: fault-detection-rate
    name: Fault Detection Rate
    canonical_name: "Fault Detection Rate"
    type: BODM
    category: Operational Efficiency
    chains:
      - risk-reduction
      - cost-savings
  - id: energy-savings-pct
    name: Energy Savings %
    canonical_name: "Energy Savings %"
    type: TODM
    category: Building Systems / ESG Tech
    chains:
      - cost-savings
      - esg-sustainability
  # ... all 75 metrics
```

This is the **only file** external consumers need to reference. The URL is stable across all future restructures:

```
https://raw.githubusercontent.com/mostarhov-source/CRE-Metrics-Framework/main/framework/interfaces/machine-readable/metrics-registry.yaml
```

---

## LLM Interfaces

Three prompt patterns are documented in `interfaces/llm-prompts/`. Each is a ready-to-use instruction block that tells an LLM how to use the framework for a specific task.

### Case Study Analysis

Instructs the LLM to: identify the PVL from the described deployment → find the matching chain file → extract BODM evidence from the case → map TODM capabilities claimed → calculate or estimate financial impact.

### Metric Lookup

Instructs the LLM to: fetch `metrics-registry.yaml` → filter by name, type, or chain → return the matching metric file path and canonical name.

### Value Chain Traversal

Instructs the LLM to: load the relevant chain file → traverse from PVL down to TODM (or reverse) → identify gaps where metrics are claimed but not evidenced.

---

## Migration Plan

| Phase | Action |
|-------|--------|
| Phase 1 | Create `interfaces/machine-readable/metrics-registry.yaml` and `chains-map.yaml` from current `_all.md` content |
| Phase 2 | Create `chains/` files (5 files) |
| Phase 3 | Create individual `metrics/` files (75 files) |
| Phase 4 | Create `interfaces/llm-prompts/` and `interfaces/consumers/` |
| Phase 5 | Update `INDEX.md` |
| Phase 6 | Add deprecation notice to `_all.md` files; remove in v2.0 |

---

## Contribution Guide (Summary)

When adding a new metric:
1. Create `metrics/{type}/{metric-id}.md` using the standard template
2. Add the metric to `interfaces/machine-readable/metrics-registry.yaml`
3. Add the metric to the relevant `chains/{chain-id}.md` file

One metric = one PR. Chain files and registry are updated in the same PR — never separately.

---

## What Does Not Change

- `examples/` — unchanged
- `templates/` — unchanged
- `README.md` — updated links only
- `SUPPLEMENT.md` — unchanged
- Metric definitions, formulas, targets, and benchmarks — unchanged

---

## Success Criteria

- An LLM can answer "what TODMs enable the Cost Savings chain?" by loading one file
- RAG retrieval returns individual metric files as clean, self-contained chunks
- A Perplexity or Claude agent can fetch `metrics-registry.yaml` from GitHub to get canonical metric names without loading any other file
- Community contributors can add a metric by touching exactly 3 files
- CRE-AI-Intelligence has no dependency on internal folder paths — only the registry URL
