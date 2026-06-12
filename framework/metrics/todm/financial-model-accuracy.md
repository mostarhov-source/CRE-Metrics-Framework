---
id: financial-model-accuracy
name: Accuracy of Financial Models
type: TODM
category: Finance Tech / Modelling
chains:
  - revenue-growth
enables_bodm:
  - irr
  - npv
formula: "1 – (|Model Output – Actual Performance| ÷ Actual Performance)"
target: "≥95% accuracy"
data_sources:
  - ERP
  - BI dashboards
  - Market comparables
metric_type: output
timing: lead
measurement_cadence: per-project
lead_relationship: causative
adoption_phase: explore
vanity_risk: none
last_updated: "2026-06-07"
---

# Accuracy of Financial Models

**Category:** Finance Tech / Modelling
**Definition:** Accuracy of automated financial models compared against actual performance (NOI, IRR).

**Why It Matters:** Ensures automated valuations are trustworthy for investment decisions.

**Formula:** 1 – (|Model Output – Actual Performance| ÷ Actual Performance)

**Data Sources:** ERP, BI dashboards, market comparables.

**Example Target / Benchmarks:** ≥95% accuracy.

**Enables:** Internal Rate of Return (IRR), Net Present Value (NPV)
