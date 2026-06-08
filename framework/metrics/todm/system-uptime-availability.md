---
id: system-uptime-availability
name: Uptime / Availability of Automated Systems
type: TODM
category: IT Infrastructure / Operations
chains:
  - risk-reduction
  - productivity-workflow
enables_bodm:
  - fault-detection-rate
  - financial-dashboard-automation
  - rent-review-automation-rate
  - lease-event-processing-time-reduction
formula: "(System Uptime Hours ÷ Total Hours) × 100"
target: "≥99.5% for critical systems"
data_sources:
  - System logs
  - Monitoring dashboards
  - SLA reports
last_updated: "2026-06-07"
---

# Uptime / Availability of Automated Systems

**Category:** IT Infrastructure / Operations
**Definition:** The percentage of time that AI/automation systems (BMS optimisation, IoT monitoring, RPA bots) are fully operational.

**Why It Matters:** High uptime ensures reliability of automation investments and prevents downtime costs.

**Formula:** (System Uptime Hours ÷ Total Hours) × 100

**Data Sources:** System logs, monitoring dashboards, SLA reports.

**Example Target / Benchmarks:** ≥99.5% for critical systems.

**Enables:** Fault Detection Rate, Financial Dashboard Automation %, Rent Review Automation Rate %, Lease Event Processing Time Reduction %
