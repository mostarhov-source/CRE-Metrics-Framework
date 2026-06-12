---
id: todm-vacancy-data-accuracy
name: Vacancy Data Accuracy %
type: TODM
category: Portfolio Data / Quality
chains:
  - productivity-workflow
enables_bodm:
  - vacancy-data-accuracy
formula: "Correct Vacancy Records ÷ Total Records × 100"
target: "≥98%"
data_sources:
  - Lease DB
  - CRM
  - Property management system
metric_type: output
timing: lead
measurement_cadence: monthly
lead_relationship: causative
adoption_phase: both
vanity_risk: none
last_updated: "2026-06-07"
---

# Vacancy Data Accuracy %

**Category:** Portfolio Data / Quality
**Definition:** % of reported vacancies matching actual occupancy status, maintained via automated data synchronisation.

**Why It Matters:** Accurate vacancy data supports valuations and rent forecasting.

**Formula:** Correct Vacancy Records ÷ Total Records × 100

**Data Sources:** Lease DB, CRM, property management system.

**Example Target / Benchmarks:** ≥98%.

**Enables:** Vacancy Data Accuracy % (BODM)
