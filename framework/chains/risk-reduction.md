---
id: risk-reduction
name: Risk Reduction
type: chain
---

# Value Chain: Risk Reduction

## Primary Value Lever (PVL)

**Risk Reduction** — Mitigation of financial, operational, compliance, and reputational risks that threaten asset or portfolio performance.

## Aggregated Business Outcomes (ABO)

- **Reduced Investment Risk & Improved Compliance** — Minimisation of financial, operational, and compliance risks across the property lifecycle.

## Business Outcome-Driven Metrics (BODM)

| Metric | timing | cadence | Target | Formula |
|--------|--------|---------|--------|---------|
| Internal Rate of Return (IRR) | lag | annual | 8–12% core | Solve for r in: NPV = Σ[Ct/(1+r)^t] = 0 |
| Loan-to-Value (LTV) | lag | quarterly | ≤60% core, ≤70% value-add | Loan Balance ÷ Property Value |
| Debt Yield | lag | quarterly | ≥10% | NOI ÷ Loan Amount |
| Fault Detection Rate | lead | weekly | ≥90% | Faults Detected ÷ Total Faults × 100 |
| Lease Data Integrity % | lead | monthly | ≥95% | Validated Lease Records ÷ Total Lease Records × 100 |
| Tenant Payment Reliability Index (TPRI) | lead | monthly | ≥85 | 100 – (0.4×Overdue% + 0.3×Avg DPD + 0.3×Default Rate) |
| Compliance Rate with Local Planning Policy | lead | per-project | ≥95% | Compliant Options ÷ Total Options × 100 |
| Climate Risk Exposure | lag | annual | <10% portfolio in high-risk | Weighted risk scores by asset value |
| Accident Rate Reduction % | lag | monthly | ≥25% | (Baseline Accidents – Current) ÷ Baseline × 100 |
| Compliance with Architects' Plans % | lead | monthly | ≥95% | Compliant Works ÷ Total Works × 100 |
| Cybersecurity Incident Rate | lag | monthly | <1 per 100 systems/year | Incidents ÷ Systems × 100 |

## Technology-Outcome Driven Metrics (TODM)

| Metric | timing | cadence | Target | Enables |
|--------|--------|---------|--------|---------|
| Uptime / Availability of Automated Systems | lead | daily | ≥99.5% | Fault Detection Rate |
| Discrepancy Detection Rate (Plans vs Site) | lead | per-project | ≥90% | Compliance with Architects' Plans % |
| Lease Data Integrity % | lead | monthly | ≥95% | Lease Data Integrity % (BODM) |
| IoT Sensor Health & Data Quality | lead | weekly | ≥98% | Fault Detection Rate |
| Cybersecurity Incident Rate | lag | monthly | <1 per 100 systems/year | Cybersecurity Incident Rate (BODM) |

> **Note:** Several BODMs in this chain are tracked through traditional financial and operational processes rather than AI/PropTech tools: IRR, Loan-to-Value (LTV), Debt Yield, Tenant Payment Reliability Index (TPRI), Climate Risk Exposure, Accident Rate Reduction %, and Compliance Rate with Local Planning Policy. These have no TODM enablers in this chain.

## Example Value Chain

```
Risk Reduction (PVL)
  ↓
Reduced Investment Risk & Improved Compliance (ABO)
  ↓
Fault Detection Rate = 94% (BODM)
  ↓
IoT Sensor Health & Data Quality = 99% sensor uptime (TODM)
  ↓
Operational Impact: 0 unplanned system failures in Q3, £180K avoided repair costs
```
