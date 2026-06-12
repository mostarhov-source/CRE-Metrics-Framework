---
id: todm-cybersecurity-incident-rate
name: Cybersecurity Incident Rate
type: TODM
category: IT Infrastructure / Operations
chains:
  - risk-reduction
enables_bodm:
  - bodm-cybersecurity-incident-rate
formula: "Number of Incidents ÷ Total Systems Monitored × 100"
target: "<1 incident per 100 monitored systems annually"
data_sources:
  - IT security logs
  - Incident reports
  - Audit trails
metric_type: outcome
timing: lag
measurement_cadence: monthly
lead_relationship: n/a
adoption_phase: both
health_metric: true
vanity_risk: none
last_updated: "2026-06-07"
---

# Cybersecurity Incident Rate

**Category:** IT Infrastructure / Operations
**Definition:** The number of detected cybersecurity breaches or fraud incidents per year within CRE IT systems, as measured by security monitoring tools.

**Why It Matters:** Minimises disruptions, data loss, and reputational damage from cyber threats.

**Formula:** Number of Incidents ÷ Total Systems Monitored × 100

**Data Sources:** IT security logs, incident reports, audit trails.

**Example Target / Benchmarks:** <1 incident per 100 monitored systems annually.

**Enables:** Cybersecurity Incident Rate (BODM)
