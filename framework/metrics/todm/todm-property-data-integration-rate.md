---
id: todm-property-data-integration-rate
name: Property Data Integration Rate %
type: TODM
category: Data Management / Integration
chains:
  - productivity-workflow
enables_bodm:
  - property-data-integration-rate
formula: "Integrated Systems ÷ Total Systems × 100"
target: "≥90%"
data_sources:
  - Integration logs
  - Data warehouse
metric_type: output
timing: lead
measurement_cadence: monthly
lead_relationship: causative
adoption_phase: both
vanity_risk: none
last_updated: "2026-06-07"
---

# Property Data Integration Rate %

**Category:** Data Management / Integration
**Definition:** % of property-level data sources integrated into a central BI/ERP environment via APIs or ETL pipelines.

**Why It Matters:** Reduces silos and improves reporting consistency across the portfolio.

**Formula:** Integrated Systems ÷ Total Systems × 100

**Data Sources:** Integration logs, data warehouse.

**Example Target / Benchmarks:** ≥90%.

**Enables:** Property Data Integration Rate % (BODM)
