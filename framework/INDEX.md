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

| Metric | File |
|--------|------|
| Cost Savings | [metrics/pvl/cost-savings.md](metrics/pvl/cost-savings.md) |
| Revenue Growth | [metrics/pvl/revenue-growth.md](metrics/pvl/revenue-growth.md) |
| Risk Reduction | [metrics/pvl/risk-reduction.md](metrics/pvl/risk-reduction.md) |
| ESG & Sustainability | [metrics/pvl/esg-sustainability.md](metrics/pvl/esg-sustainability.md) |
| Productivity & Workflow Efficiency | [metrics/pvl/productivity-workflow.md](metrics/pvl/productivity-workflow.md) |

### Aggregated Business Outcomes (ABO) — 5 files

| Metric | File |
|--------|------|
| Optimised Portfolio Returns | [metrics/abo/optimised-portfolio-returns.md](metrics/abo/optimised-portfolio-returns.md) |
| Enhanced Operational Efficiency & Sustainability | [metrics/abo/operational-efficiency-sustainability.md](metrics/abo/operational-efficiency-sustainability.md) |
| Reduced Investment Risk & Improved Compliance | [metrics/abo/reduced-risk-compliance.md](metrics/abo/reduced-risk-compliance.md) |
| Increased Tenant Satisfaction & Retention | [metrics/abo/tenant-satisfaction-retention.md](metrics/abo/tenant-satisfaction-retention.md) |
| Streamlined Decision-Making & Workflow | [metrics/abo/streamlined-decision-making.md](metrics/abo/streamlined-decision-making.md) |

### Business Outcome-Driven Metrics (BODM) — 40 files

**Financial Performance**
| Metric | File |
|--------|------|
| Internal Rate of Return (IRR) | [metrics/bodm/irr.md](metrics/bodm/irr.md) |
| Net Present Value (NPV) | [metrics/bodm/npv.md](metrics/bodm/npv.md) |
| Equity Multiple | [metrics/bodm/equity-multiple.md](metrics/bodm/equity-multiple.md) |
| Loan-to-Value (LTV) | [metrics/bodm/ltv.md](metrics/bodm/ltv.md) |
| Debt Yield | [metrics/bodm/debt-yield.md](metrics/bodm/debt-yield.md) |
| Net Operating Income (NOI) | [metrics/bodm/noi.md](metrics/bodm/noi.md) |
| Weighted Average Cost of Capital (WACC) | [metrics/bodm/wacc.md](metrics/bodm/wacc.md) |

**Operational Efficiency**
| Metric | File |
|--------|------|
| Fault Detection Rate | [metrics/bodm/fault-detection-rate.md](metrics/bodm/fault-detection-rate.md) |
| Lease Event Processing Time Reduction % | [metrics/bodm/lease-event-processing-time-reduction.md](metrics/bodm/lease-event-processing-time-reduction.md) |
| Vacancy Data Accuracy % | [metrics/bodm/vacancy-data-accuracy.md](metrics/bodm/vacancy-data-accuracy.md) |
| Financial Dashboard Automation % | [metrics/bodm/financial-dashboard-automation.md](metrics/bodm/financial-dashboard-automation.md) |
| Asset Hierarchy Data Coverage % | [metrics/bodm/asset-hierarchy-data-coverage.md](metrics/bodm/asset-hierarchy-data-coverage.md) |
| Property Data Integration Rate % | [metrics/bodm/property-data-integration-rate.md](metrics/bodm/property-data-integration-rate.md) |
| Lease Data Integrity % | [metrics/bodm/lease-data-integrity.md](metrics/bodm/lease-data-integrity.md) |
| Rent Review Automation Rate % | [metrics/bodm/rent-review-automation-rate.md](metrics/bodm/rent-review-automation-rate.md) |
| Report Generation Time Reduction % | [metrics/bodm/report-generation-time-reduction.md](metrics/bodm/report-generation-time-reduction.md) |
| Tenant Record Duplication Rate % | [metrics/bodm/tenant-record-duplication-rate.md](metrics/bodm/tenant-record-duplication-rate.md) |
| Cybersecurity Incident Rate | [metrics/bodm/bodm-cybersecurity-incident-rate.md](metrics/bodm/bodm-cybersecurity-incident-rate.md) |

**ESG / Sustainability**
| Metric | File |
|--------|------|
| kWh/m² Reduction | [metrics/bodm/kwh-m2-reduction.md](metrics/bodm/kwh-m2-reduction.md) |
| Peak Demand Reduction | [metrics/bodm/peak-demand-reduction.md](metrics/bodm/peak-demand-reduction.md) |
| Carbon Emissions Reduction | [metrics/bodm/carbon-emissions-reduction.md](metrics/bodm/carbon-emissions-reduction.md) |
| Waste Reduction % | [metrics/bodm/waste-reduction.md](metrics/bodm/waste-reduction.md) |
| Green Lease Compliance Automation % | [metrics/bodm/green-lease-compliance-automation.md](metrics/bodm/green-lease-compliance-automation.md) |
| Climate Risk Exposure | [metrics/bodm/climate-risk-exposure.md](metrics/bodm/climate-risk-exposure.md) |
| Embodied Carbon Intensity | [metrics/bodm/embodied-carbon-intensity.md](metrics/bodm/embodied-carbon-intensity.md) |
| Construction Waste Reduction % | [metrics/bodm/construction-waste-reduction.md](metrics/bodm/construction-waste-reduction.md) |

**Tenant Outcomes & Market Performance**
| Metric | File |
|--------|------|
| Tenant Retention Rate | [metrics/bodm/tenant-retention-rate.md](metrics/bodm/tenant-retention-rate.md) |
| Tenant Payment Reliability Index (TPRI) | [metrics/bodm/tenant-payment-reliability-index.md](metrics/bodm/tenant-payment-reliability-index.md) |
| Average Daily Rate (ADR) | [metrics/bodm/average-daily-rate.md](metrics/bodm/average-daily-rate.md) |
| Market Rent vs Contract Rent | [metrics/bodm/market-rent-vs-contract-rent.md](metrics/bodm/market-rent-vs-contract-rent.md) |
| Tenant Utilization Rate | [metrics/bodm/tenant-utilization-rate.md](metrics/bodm/tenant-utilization-rate.md) |
| Market Absorption Rate | [metrics/bodm/market-absorption-rate.md](metrics/bodm/market-absorption-rate.md) |

**Development & Construction**
| Metric | File |
|--------|------|
| Time to Feasibility Study Completion | [metrics/bodm/time-to-feasibility-study.md](metrics/bodm/time-to-feasibility-study.md) |
| Development Density & Design Optimisation Index | [metrics/bodm/development-density-design-index.md](metrics/bodm/development-density-design-index.md) |
| Compliance Rate with Local Planning Policy | [metrics/bodm/planning-policy-compliance-rate.md](metrics/bodm/planning-policy-compliance-rate.md) |
| Gross Development Value (GDV) Optimisation | [metrics/bodm/gdv-optimisation.md](metrics/bodm/gdv-optimisation.md) |
| Construction Rework Reduction % | [metrics/bodm/construction-rework-reduction.md](metrics/bodm/construction-rework-reduction.md) |
| Construction Waste Reduction % | [metrics/bodm/construction-waste-reduction.md](metrics/bodm/construction-waste-reduction.md) |
| Accident Rate Reduction % | [metrics/bodm/accident-rate-reduction.md](metrics/bodm/accident-rate-reduction.md) |
| Compliance with Architects' Plans % | [metrics/bodm/architects-plans-compliance.md](metrics/bodm/architects-plans-compliance.md) |
| Development Pipeline Velocity | [metrics/bodm/development-pipeline-velocity.md](metrics/bodm/development-pipeline-velocity.md) |

### Technology-Outcome Driven Metrics (TODM) — 25 files

| Metric | File |
|--------|------|
| Energy Savings % | [metrics/todm/energy-savings-pct.md](metrics/todm/energy-savings-pct.md) |
| Data Capture Automation Rate % | [metrics/todm/data-capture-automation-rate.md](metrics/todm/data-capture-automation-rate.md) |
| Uptime / Availability of Automated Systems | [metrics/todm/system-uptime-availability.md](metrics/todm/system-uptime-availability.md) |
| AI-Generated Development Options per Assessment | [metrics/todm/ai-development-options-per-assessment.md](metrics/todm/ai-development-options-per-assessment.md) |
| Accuracy of AI-Generated Cost Estimates | [metrics/todm/ai-cost-estimate-accuracy.md](metrics/todm/ai-cost-estimate-accuracy.md) |
| Accuracy of Financial Models | [metrics/todm/financial-model-accuracy.md](metrics/todm/financial-model-accuracy.md) |
| Frequency of Automated Sell/Hold Recommendations | [metrics/todm/automated-sell-hold-frequency.md](metrics/todm/automated-sell-hold-frequency.md) |
| Discrepancy Detection Rate (Plans vs Site) | [metrics/todm/discrepancy-detection-rate.md](metrics/todm/discrepancy-detection-rate.md) |
| Lease Data Integrity % | [metrics/todm/todm-lease-data-integrity.md](metrics/todm/todm-lease-data-integrity.md) |
| Rent Review Automation Rate % | [metrics/todm/todm-rent-review-automation-rate.md](metrics/todm/todm-rent-review-automation-rate.md) |
| Lease Event Processing Time Reduction % | [metrics/todm/todm-lease-event-processing-time-reduction.md](metrics/todm/todm-lease-event-processing-time-reduction.md) |
| Vacancy Data Accuracy % | [metrics/todm/todm-vacancy-data-accuracy.md](metrics/todm/todm-vacancy-data-accuracy.md) |
| Tenant Record Duplication Rate % | [metrics/todm/todm-tenant-record-duplication-rate.md](metrics/todm/todm-tenant-record-duplication-rate.md) |
| Financial Dashboard Automation % | [metrics/todm/todm-financial-dashboard-automation.md](metrics/todm/todm-financial-dashboard-automation.md) |
| Report Generation Time Reduction % | [metrics/todm/todm-report-generation-time-reduction.md](metrics/todm/todm-report-generation-time-reduction.md) |
| Asset Hierarchy Data Coverage % | [metrics/todm/todm-asset-hierarchy-data-coverage.md](metrics/todm/todm-asset-hierarchy-data-coverage.md) |
| Property Data Integration Rate % | [metrics/todm/todm-property-data-integration-rate.md](metrics/todm/todm-property-data-integration-rate.md) |
| Green Lease Compliance Automation % | [metrics/todm/todm-green-lease-compliance-automation.md](metrics/todm/todm-green-lease-compliance-automation.md) |
| Data Model Alignment Accuracy % | [metrics/todm/data-model-alignment-accuracy.md](metrics/todm/data-model-alignment-accuracy.md) |
| Cybersecurity Incident Rate | [metrics/todm/todm-cybersecurity-incident-rate.md](metrics/todm/todm-cybersecurity-incident-rate.md) |
| IoT Sensor Health & Data Quality | [metrics/todm/iot-sensor-health-data-quality.md](metrics/todm/iot-sensor-health-data-quality.md) |
| Digital Twin Fidelity | [metrics/todm/digital-twin-fidelity.md](metrics/todm/digital-twin-fidelity.md) |
| Technology Adoption Rate | [metrics/todm/technology-adoption-rate.md](metrics/todm/technology-adoption-rate.md) |
| PropTech Investment ROI | [metrics/todm/proptech-investment-roi.md](metrics/todm/proptech-investment-roi.md) |
| Tenant Experience Tech Utilization | [metrics/todm/tenant-experience-tech-utilization.md](metrics/todm/tenant-experience-tech-utilization.md) |

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
