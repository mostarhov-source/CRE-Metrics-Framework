---
id: iot-sensor-health-data-quality
name: IoT Sensor Health & Data Quality
type: TODM
category: Building Systems / ESG Tech
chains:
  - cost-savings
  - risk-reduction
enables_bodm:
  - fault-detection-rate
formula: "Valid Sensor Reports ÷ Total Installed Sensors × 100"
target: "≥98% sensor uptime and data validity"
data_sources:
  - Sensor telemetry logs
  - Monitoring dashboards
metric_type: output
timing: lead
measurement_cadence: weekly
lead_relationship: causative
adoption_phase: both
health_metric: true
vanity_risk: none
last_updated: "2026-06-07"
---

# IoT Sensor Health & Data Quality

**Category:** Building Systems / ESG Tech
**Definition:** Percentage of operational IoT sensors reporting valid, high-quality data continuously as expected.

**Why It Matters:** Ensures reliability of data streams for analytics, automation, and fault detection.

**Formula:** Valid Sensor Reports ÷ Total Installed Sensors × 100

**Data Sources:** Sensor telemetry logs, monitoring dashboards.

**Example Target / Benchmarks:** ≥98% sensor uptime and data validity.

**Enables:** Fault Detection Rate
