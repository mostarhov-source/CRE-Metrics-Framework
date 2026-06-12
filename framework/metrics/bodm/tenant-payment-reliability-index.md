---
id: tenant-payment-reliability-index
name: Tenant Payment Reliability Index (TPRI)
type: BODM
category: Tenant Outcomes
chains:
  - risk-reduction
  - revenue-growth
parent_abo: tenant-satisfaction-retention
formula: "100 – (0.4×Overdue% + 0.3×Avg DPD + 0.3×Default Rate)"
target: "Target ≥85; intervention threshold <70"
data_sources:
  - ERP
  - Finance
  - Tenant CRM
metric_type: outcome
timing: lead
measurement_cadence: monthly
lead_relationship: causative
adoption_phase: both
health_metric: true
vanity_risk: none
last_updated: "2026-06-07"
---

# Tenant Payment Reliability Index (TPRI)

**Category:** Tenant Outcomes
**Definition:** Composite index of overdue receivables, days past due, and default rate.

**Why It Matters:** Forward indicator of credit health and NOI resilience.

**Formula:** 100 – (0.4×Overdue% + 0.3×Avg DPD + 0.3×Default Rate)

**Data Sources:** ERP, Finance, Tenant CRM

**Example Target / Benchmarks:** Target ≥85; intervention threshold <70
