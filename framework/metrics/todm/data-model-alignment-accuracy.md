---
id: data-model-alignment-accuracy
name: Data Model Alignment Accuracy %
type: TODM
category: Data Governance / Quality
chains:
  - productivity-workflow
enables_bodm:
  - financial-dashboard-automation
formula: "Aligned Forms ÷ Total Forms × 100"
target: "≥95%"
data_sources:
  - BI configs
  - Data governance logs
last_updated: "2026-06-07"
---

# Data Model Alignment Accuracy %

**Category:** Data Governance / Quality
**Definition:** % of eForms, reports, and dashboards aligned with the master CRE data model.

**Why It Matters:** Prevents data inconsistencies between platforms that would corrupt analytics outputs.

**Formula:** Aligned Forms ÷ Total Forms × 100

**Data Sources:** BI configs, data governance logs.

**Example Target / Benchmarks:** ≥95%.

**Enables:** Financial Dashboard Automation %
