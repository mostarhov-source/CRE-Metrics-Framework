# CRE Metrics Framework — Navigation Index

This framework organises metrics for Industrial & Logistics Commercial Real Estate (I&L CRE) across four layers: **Primary Value Levers (PVL)** → **Aggregated Business Outcomes (ABO)** → **Business Outcome–Driven Metrics (BODM)** → **Technology-Outcome Driven Metrics (TODM)**.

---

## Quick Start

**For LLM agents doing case study analysis:** Load one chain file. It contains the full PVL → ABO → BODM → TODM traversal for that value lever.

**For RAG pipelines:** Index the individual metric files in `metrics/`. Each file is atomic and self-contained.

**For external consumers:** Fetch `interfaces/machine-readable/metrics-registry.yaml`. It is the only stable URL you need.

---

## 🔗 Value Chain Entry Points

| Chain | File | Primary Outcomes |
|-------|------|-----------------|
| Cost Savings | [chains/cost-savings.md](chains/cost-savings.md) | NOI growth, energy efficiency, OpEx reduction |
| Revenue Growth | [chains/revenue-growth.md](chains/revenue-growth.md) | IRR, tenant retention, market rent uplift |
| Risk Reduction | [chains/risk-reduction.md](chains/risk-reduction.md) | LTV, compliance, fault detection |
| ESG & Sustainability | [chains/esg-sustainability.md](chains/esg-sustainability.md) | Carbon reduction, green lease, embodied carbon |
| Productivity & Workflow | [chains/productivity-workflow.md](chains/productivity-workflow.md) | Automation, reporting speed, data quality |

---

## 📊 Individual Metric Files

### Primary Value Levers (PVL) — 5 files

| Metric | type | timing | cadence | File |
|--------|------|--------|---------|------|
| Cost Savings | effect | lag | annual | [metrics/pvl/cost-savings.md](metrics/pvl/cost-savings.md) |
| Revenue Growth | effect | lag | annual | [metrics/pvl/revenue-growth.md](metrics/pvl/revenue-growth.md) |
| Risk Reduction | effect | lag | annual | [metrics/pvl/risk-reduction.md](metrics/pvl/risk-reduction.md) |
| ESG & Sustainability | effect | lag | annual | [metrics/pvl/esg-sustainability.md](metrics/pvl/esg-sustainability.md) |
| Productivity & Workflow Efficiency | effect | lag | annual | [metrics/pvl/productivity-workflow.md](metrics/pvl/productivity-workflow.md) |

### Aggregated Business Outcomes (ABO) — 5 files

| Metric | type | timing | cadence | File |
|--------|------|--------|---------|------|
| Optimised Portfolio Returns | effect | lag | annual | [metrics/abo/optimised-portfolio-returns.md](metrics/abo/optimised-portfolio-returns.md) |
| Enhanced Operational Efficiency & Sustainability | outcome | lag | annual | [metrics/abo/operational-efficiency-sustainability.md](metrics/abo/operational-efficiency-sustainability.md) |
| Reduced Investment Risk & Improved Compliance | outcome | lag | annual | [metrics/abo/reduced-risk-compliance.md](metrics/abo/reduced-risk-compliance.md) |
| Increased Tenant Satisfaction & Retention | outcome | lag | annual | [metrics/abo/tenant-satisfaction-retention.md](metrics/abo/tenant-satisfaction-retention.md) |
| Streamlined Decision-Making & Workflow | outcome | lead | quarterly | [metrics/abo/streamlined-decision-making.md](metrics/abo/streamlined-decision-making.md) |

### Business Outcome-Driven Metrics (BODM) — 40 files

**Financial Performance**
| Metric | type | timing | cadence | File |
|--------|------|--------|---------|------|
| Internal Rate of Return (IRR) | effect | lag | annual | [metrics/bodm/irr.md](metrics/bodm/irr.md) |
| Net Present Value (NPV) | effect | lag | annual | [metrics/bodm/npv.md](metrics/bodm/npv.md) |
| Equity Multiple | effect | lag | per-project | [metrics/bodm/equity-multiple.md](metrics/bodm/equity-multiple.md) |
| Loan-to-Value (LTV) | outcome | lag | quarterly | [metrics/bodm/ltv.md](metrics/bodm/ltv.md) |
| Debt Yield | outcome | lag | quarterly | [metrics/bodm/debt-yield.md](metrics/bodm/debt-yield.md) |
| Net Operating Income (NOI) | outcome | lag | quarterly | [metrics/bodm/noi.md](metrics/bodm/noi.md) |
| Weighted Average Cost of Capital (WACC) | effect | lag | annual | [metrics/bodm/wacc.md](metrics/bodm/wacc.md) |

**Operational Efficiency**
| Metric | type | timing | cadence | File |
|--------|------|--------|---------|------|
| Fault Detection Rate | outcome | lead | weekly | [metrics/bodm/fault-detection-rate.md](metrics/bodm/fault-detection-rate.md) |
| Lease Event Processing Time Reduction % | process | lead | monthly | [metrics/bodm/lease-event-processing-time-reduction.md](metrics/bodm/lease-event-processing-time-reduction.md) |
| Vacancy Data Accuracy % | output | lead | monthly | [metrics/bodm/vacancy-data-accuracy.md](metrics/bodm/vacancy-data-accuracy.md) |
| Financial Dashboard Automation % | output | lead | monthly | [metrics/bodm/financial-dashboard-automation.md](metrics/bodm/financial-dashboard-automation.md) |
| Asset Hierarchy Data Coverage % | output | lead | monthly | [metrics/bodm/asset-hierarchy-data-coverage.md](metrics/bodm/asset-hierarchy-data-coverage.md) |
| Property Data Integration Rate % | output | lead | monthly | [metrics/bodm/property-data-integration-rate.md](metrics/bodm/property-data-integration-rate.md) |
| Lease Data Integrity % | output | lead | monthly | [metrics/bodm/lease-data-integrity.md](metrics/bodm/lease-data-integrity.md) |
| Rent Review Automation Rate % | output | lead | monthly | [metrics/bodm/rent-review-automation-rate.md](metrics/bodm/rent-review-automation-rate.md) |
| Report Generation Time Reduction % | process | lead | monthly | [metrics/bodm/report-generation-time-reduction.md](metrics/bodm/report-generation-time-reduction.md) |
| Tenant Record Duplication Rate % | output | lead | monthly | [metrics/bodm/tenant-record-duplication-rate.md](metrics/bodm/tenant-record-duplication-rate.md) |
| Cybersecurity Incident Rate | outcome | lag | monthly | [metrics/bodm/bodm-cybersecurity-incident-rate.md](metrics/bodm/bodm-cybersecurity-incident-rate.md) |

**ESG / Sustainability**
| Metric | type | timing | cadence | File |
|--------|------|--------|---------|------|
| kWh/m² Reduction | outcome | lead | monthly | [metrics/bodm/kwh-m2-reduction.md](metrics/bodm/kwh-m2-reduction.md) |
| Peak Demand Reduction | outcome | lead | monthly | [metrics/bodm/peak-demand-reduction.md](metrics/bodm/peak-demand-reduction.md) |
| Carbon Emissions Reduction | outcome | lag | annual | [metrics/bodm/carbon-emissions-reduction.md](metrics/bodm/carbon-emissions-reduction.md) |
| Waste Reduction % | outcome | lag | quarterly | [metrics/bodm/waste-reduction.md](metrics/bodm/waste-reduction.md) |
| Green Lease Compliance Automation % | output | lead | monthly | [metrics/bodm/green-lease-compliance-automation.md](metrics/bodm/green-lease-compliance-automation.md) |
| Climate Risk Exposure | effect | lag | annual | [metrics/bodm/climate-risk-exposure.md](metrics/bodm/climate-risk-exposure.md) |
| Embodied Carbon Intensity | effect | lag | per-project | [metrics/bodm/embodied-carbon-intensity.md](metrics/bodm/embodied-carbon-intensity.md) |
| Construction Waste Reduction % | outcome | lag | per-project | [metrics/bodm/construction-waste-reduction.md](metrics/bodm/construction-waste-reduction.md) |

**Tenant Outcomes & Market Performance**
| Metric | type | timing | cadence | File |
|--------|------|--------|---------|------|
| Tenant Retention Rate | outcome | lag | annual | [metrics/bodm/tenant-retention-rate.md](metrics/bodm/tenant-retention-rate.md) |
| Tenant Payment Reliability Index (TPRI) | outcome | lead | monthly | [metrics/bodm/tenant-payment-reliability-index.md](metrics/bodm/tenant-payment-reliability-index.md) |
| Average Daily Rate (ADR) | outcome | lag | monthly | [metrics/bodm/average-daily-rate.md](metrics/bodm/average-daily-rate.md) |
| Market Rent vs Contract Rent | effect | lag | quarterly | [metrics/bodm/market-rent-vs-contract-rent.md](metrics/bodm/market-rent-vs-contract-rent.md) |
| Tenant Utilization Rate | outcome | lead | monthly | [metrics/bodm/tenant-utilization-rate.md](metrics/bodm/tenant-utilization-rate.md) |
| Market Absorption Rate | effect | lag | quarterly | [metrics/bodm/market-absorption-rate.md](metrics/bodm/market-absorption-rate.md) |

**Development & Construction**
| Metric | type | timing | cadence | File |
|--------|------|--------|---------|------|
| Time to Feasibility Study Completion | process | lead | per-project | [metrics/bodm/time-to-feasibility-study.md](metrics/bodm/time-to-feasibility-study.md) |
| Development Density & Design Optimisation Index | outcome | lead | per-project | [metrics/bodm/development-density-design-index.md](metrics/bodm/development-density-design-index.md) |
| Compliance Rate with Local Planning Policy | outcome | lead | per-project | [metrics/bodm/planning-policy-compliance-rate.md](metrics/bodm/planning-policy-compliance-rate.md) |
| Gross Development Value (GDV) Optimisation | effect | lag | per-project | [metrics/bodm/gdv-optimisation.md](metrics/bodm/gdv-optimisation.md) |
| Construction Rework Reduction % | outcome | lead | monthly | [metrics/bodm/construction-rework-reduction.md](metrics/bodm/construction-rework-reduction.md) |
| Construction Waste Reduction % | outcome | lag | per-project | [metrics/bodm/construction-waste-reduction.md](metrics/bodm/construction-waste-reduction.md) |
| Accident Rate Reduction % | outcome | lag | monthly | [metrics/bodm/accident-rate-reduction.md](metrics/bodm/accident-rate-reduction.md) |
| Compliance with Architects' Plans % | output | lead | monthly | [metrics/bodm/architects-plans-compliance.md](metrics/bodm/architects-plans-compliance.md) |
| Development Pipeline Velocity | process | lead | monthly | [metrics/bodm/development-pipeline-velocity.md](metrics/bodm/development-pipeline-velocity.md) |

### Technology-Outcome Driven Metrics (TODM) — 25 files

| Metric | type | timing | cadence | File |
|--------|------|--------|---------|------|
| Energy Savings % | outcome | lead | monthly | [metrics/todm/energy-savings-pct.md](metrics/todm/energy-savings-pct.md) |
| Data Capture Automation Rate % | output | lead | monthly | [metrics/todm/data-capture-automation-rate.md](metrics/todm/data-capture-automation-rate.md) |
| Uptime / Availability of Automated Systems | output | lead | daily | [metrics/todm/system-uptime-availability.md](metrics/todm/system-uptime-availability.md) |
| AI-Generated Development Options per Assessment | output | lead | per-project | [metrics/todm/ai-development-options-per-assessment.md](metrics/todm/ai-development-options-per-assessment.md) |
| Accuracy of AI-Generated Cost Estimates | output | lead | per-project | [metrics/todm/ai-cost-estimate-accuracy.md](metrics/todm/ai-cost-estimate-accuracy.md) |
| Accuracy of Financial Models | output | lead | per-project | [metrics/todm/financial-model-accuracy.md](metrics/todm/financial-model-accuracy.md) |
| Frequency of Automated Sell/Hold Recommendations | output | lead | monthly | [metrics/todm/automated-sell-hold-frequency.md](metrics/todm/automated-sell-hold-frequency.md) |
| Discrepancy Detection Rate (Plans vs Site) | output | lead | per-project | [metrics/todm/discrepancy-detection-rate.md](metrics/todm/discrepancy-detection-rate.md) |
| Lease Data Integrity % | output | lead | monthly | [metrics/todm/todm-lease-data-integrity.md](metrics/todm/todm-lease-data-integrity.md) |
| Rent Review Automation Rate % | output | lead | monthly | [metrics/todm/todm-rent-review-automation-rate.md](metrics/todm/todm-rent-review-automation-rate.md) |
| Lease Event Processing Time Reduction % | process | lead | monthly | [metrics/todm/todm-lease-event-processing-time-reduction.md](metrics/todm/todm-lease-event-processing-time-reduction.md) |
| Vacancy Data Accuracy % | output | lead | monthly | [metrics/todm/todm-vacancy-data-accuracy.md](metrics/todm/todm-vacancy-data-accuracy.md) |
| Tenant Record Duplication Rate % | output | lead | monthly | [metrics/todm/todm-tenant-record-duplication-rate.md](metrics/todm/todm-tenant-record-duplication-rate.md) |
| Financial Dashboard Automation % | output | lead | monthly | [metrics/todm/todm-financial-dashboard-automation.md](metrics/todm/todm-financial-dashboard-automation.md) |
| Report Generation Time Reduction % | process | lead | monthly | [metrics/todm/todm-report-generation-time-reduction.md](metrics/todm/todm-report-generation-time-reduction.md) |
| Asset Hierarchy Data Coverage % | output | lead | monthly | [metrics/todm/todm-asset-hierarchy-data-coverage.md](metrics/todm/todm-asset-hierarchy-data-coverage.md) |
| Property Data Integration Rate % | output | lead | monthly | [metrics/todm/todm-property-data-integration-rate.md](metrics/todm/todm-property-data-integration-rate.md) |
| Green Lease Compliance Automation % | output | lead | monthly | [metrics/todm/todm-green-lease-compliance-automation.md](metrics/todm/todm-green-lease-compliance-automation.md) |
| Data Model Alignment Accuracy % | output | lead | monthly | [metrics/todm/data-model-alignment-accuracy.md](metrics/todm/data-model-alignment-accuracy.md) |
| Cybersecurity Incident Rate | outcome | lag | monthly | [metrics/todm/todm-cybersecurity-incident-rate.md](metrics/todm/todm-cybersecurity-incident-rate.md) |
| IoT Sensor Health & Data Quality | output | lead | weekly | [metrics/todm/iot-sensor-health-data-quality.md](metrics/todm/iot-sensor-health-data-quality.md) |
| Digital Twin Fidelity | output | lead | quarterly | [metrics/todm/digital-twin-fidelity.md](metrics/todm/digital-twin-fidelity.md) |
| Technology Adoption Rate | output | lead | monthly | [metrics/todm/technology-adoption-rate.md](metrics/todm/technology-adoption-rate.md) |
| PropTech Investment ROI | effect | lag | per-project | [metrics/todm/proptech-investment-roi.md](metrics/todm/proptech-investment-roi.md) |
| Tenant Experience Tech Utilization | output | lead | monthly | [metrics/todm/tenant-experience-tech-utilization.md](metrics/todm/tenant-experience-tech-utilization.md) |

---

## 🔌 Consumer Interfaces

| Resource | Location | Purpose |
|----------|----------|---------|
| Metrics Registry (YAML) | [interfaces/machine-readable/metrics-registry.yaml](interfaces/machine-readable/metrics-registry.yaml) | Stable canonical source for all metric IDs and chain memberships |
| Chains Map (YAML) | [interfaces/machine-readable/chains-map.yaml](interfaces/machine-readable/chains-map.yaml) | Explicit PVL→ABO→BODM→TODM hierarchy |
| Consumer Interface Guide | [interfaces/README.md](interfaces/README.md) | How to consume this framework |
| Case Study Analysis Prompt | [interfaces/llm-prompts/case-study-analysis.md](interfaces/llm-prompts/case-study-analysis.md) | Prompt pattern for case study mapping |
| Metric Lookup Prompt | [interfaces/llm-prompts/metric-lookup.md](interfaces/llm-prompts/metric-lookup.md) | Prompt pattern for metric retrieval |
| Value Chain Traversal Prompt | [interfaces/llm-prompts/value-chain-traversal.md](interfaces/llm-prompts/value-chain-traversal.md) | Prompt pattern for chain navigation |
| CRE-AI-Intelligence Contract | [interfaces/consumers/cre-ai-intelligence.md](interfaces/consumers/cre-ai-intelligence.md) | Integration contract for sister project |
| retrieve-metrics Skill | [interfaces/skills/retrieve-metrics.md](interfaces/skills/retrieve-metrics.md) | Claude Code skill for metric retrieval |

---

## 📂 Legacy Files (Deprecated — v2.0 Transition)

The following files are kept for reference during migration and will be removed in v2.0:

- [PVL_all.md](PVL_all.md) — superseded by `metrics/pvl/` and `chains/`
- [ABO_all.md](ABO_all.md) — superseded by `metrics/abo/` and `chains/`
- [BODM_all.md](BODM_all.md) — superseded by `metrics/bodm/`
- [TODM_all.md](TODM_all.md) — superseded by `metrics/todm/`
- [SUPPLEMENT.md](SUPPLEMENT.md) — methodology notes, unchanged

---

*Framework version: v1.1 (v2.0 structure, v1.0 metrics content)*
