---
id: todm-rent-review-automation-rate
name: Rent Review Automation Rate %
type: TODM
category: Lease Management / Workflow Automation
chains:
  - productivity-workflow
enables_bodm:
  - rent-review-automation-rate
formula: "Automated Rent Reviews ÷ Total Rent Reviews × 100"
target: "≥80%"
data_sources:
  - Workflow logs
  - Document automation
metric_type: output
timing: lead
measurement_cadence: monthly
lead_relationship: causative
adoption_phase: both
vanity_risk: none
last_updated: "2026-06-07"
---

# Rent Review Automation Rate %

**Category:** Lease Management / Workflow Automation
**Definition:** % of rent review processes (calculations, reminders, approvals) executed automatically by the technology platform.

**Why It Matters:** Reduces errors and speeds up review cycles through workflow automation.

**Formula:** Automated Rent Reviews ÷ Total Rent Reviews × 100

**Data Sources:** Workflow logs, document automation.

**Example Target / Benchmarks:** ≥80%.

**Enables:** Rent Review Automation Rate % (BODM)
