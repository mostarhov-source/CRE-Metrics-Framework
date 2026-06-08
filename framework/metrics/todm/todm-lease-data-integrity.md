---
id: todm-lease-data-integrity
name: Lease Data Integrity %
type: TODM
category: Lease Management / Data Quality
chains:
  - productivity-workflow
  - risk-reduction
enables_bodm:
  - lease-data-integrity
formula: "Validated Lease Records ÷ Total Lease Records × 100"
target: "≥95%"
data_sources:
  - Lease DB
  - ERP
  - Scanned lease documents
last_updated: "2026-06-07"
---

# Lease Data Integrity %

**Category:** Lease Management / Data Quality
**Definition:** % of lease records validated against authoritative sources (ERP, legal documents) via automated checking.

**Why It Matters:** Ensures accuracy of rent rolls and financial reporting through systematic data validation.

**Formula:** Validated Lease Records ÷ Total Lease Records × 100

**Data Sources:** Lease DB, ERP, scanned lease documents.

**Example Target / Benchmarks:** ≥95%.

**Enables:** Lease Data Integrity % (BODM)
