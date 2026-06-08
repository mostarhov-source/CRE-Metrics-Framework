---
id: todm-tenant-record-duplication-rate
name: Tenant Record Duplication Rate %
type: TODM
category: CRM / Data Quality
chains:
  - productivity-workflow
enables_bodm:
  - tenant-record-duplication-rate
formula: "Duplicate Records ÷ Total Records × 100"
target: "≤1%"
data_sources:
  - CRM
  - Lease DB
last_updated: "2026-06-07"
---

# Tenant Record Duplication Rate %

**Category:** CRM / Data Quality
**Definition:** % of duplicate tenant entries across systems, detected and flagged by data quality tooling.

**Why It Matters:** Avoids confusion and supports accurate reporting and tenant management.

**Formula:** Duplicate Records ÷ Total Records × 100

**Data Sources:** CRM, Lease DB.

**Example Target / Benchmarks:** ≤1%.

**Enables:** Tenant Record Duplication Rate % (BODM)
