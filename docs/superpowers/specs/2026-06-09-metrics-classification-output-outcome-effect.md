# Spec: Metrics Classification — Type × Lead / Lag × Cadence

**Date:** 2026-06-09  
**Revised:** 2026-06-09 (Gap 1 + Gap 6 blockers resolved — see gap analysis)  
**Status:** Reasoning Artefact — classification decisions implemented across all 75 metric files, INDEX.md, chain files, metrics-registry.yaml (v1.1), and metric-lookup.md prompt  
**Scope:** All 75 metrics across PVL, ABO, BODM, TODM layers  
**Source methodology:** RAG | Books | Metrics And Measurement (NotebookLM)

---

## 1. Purpose

This spec defines a three-dimensional classification system to be applied to every metric in the CRE Metrics Framework:

1. **Type axis** — Is the metric measuring a process, output, outcome, or effect?
2. **Timing axis** — Is the metric a leading or lagging indicator?
3. **Cadence** — How frequently is the metric measured? (determines timing classification in practice)

The goal is to make each metric's role in the value chain explicit, so that:
- AI agents selecting metrics for a case study know whether they're reaching for a leading signal or a final result
- OKR design work can distinguish process efficiency (process) from activity delivery (output) from behavior change (outcome) from strategic impact (effect)
- Metric consumers can build dashboards that balance predictive and confirmatory signals at the right review frequency

---

## 2. Methodology Definitions

*Grounded in the books in the RAG | Books | Metrics And Measurement notebook.*

### 2.1 Type Axis

The full measurement chain from the methodology is:

```
Input → Process → Output → Outcome → Impact
```

`input` type is not present in this framework — budgets, staff capacity, and data sources are prerequisites, not tracked metrics. The five active types are:

| Type | Definition | Role in measurement chain |
|------|-----------|--------------------------|
| **Process** | Efficiency or speed of work being performed — the *how fast / how well we're executing* | Identifies workflow bottlenecks; answers "are we executing efficiently?" |
| **Output** | Immediate deliverable or artifact produced by the activity — the *what was delivered* | Confirms tasks were completed; answers "did we do the work?" |
| **Outcome** | Behavior change or business result that arises after the output is delivered — the *so what* | Measures value created; answers "did it make a difference?" |
| **Effect** | Long-term strategic consequence of outcomes accumulating — the *why it ultimately matters* | Confirms strategic success; answers "did we move the business?" |

The "Why?" test: ask "Why does this metric matter?" repeatedly. The first answer is often Process or Output; the final answer is the Effect.

**Process vs Output distinction:** A process metric measures *how long* or *how efficiently* something is done. An output metric measures *what* was produced. "Time to Feasibility Study Completion" measures workflow duration (Process). "AI-Generated Options per Assessment" measures what the process produced (Output).

### 2.2 Timing Axis

| Timing | Definition | Characteristics |
|--------|-----------|----------------|
| **Lead** | Predictive — reflects team-controllable actions; changes frequently enough to course-correct within a goal cycle | Responsive but less certain; correlates with or causes future results |
| **Lag** | Confirmatory — reflects final or historical results; slow to change; often aggregates multiple teams' efforts | Certain but not actionable in-cycle; proves causation in hindsight |

**Key classification questions:**
- Can the team directly influence this metric? → Lead
- Does it change within a single OKR/reporting cycle? → Lead
- Does it only move after many things have already happened? → Lag
- Is it the ultimate result you're trying to prove? → Lag

**Context rule:** A metric's timing classification is perspective-dependent. TODM metrics are leading for a business outcome team but may be lagging for the infrastructure/technology team delivering the tech.

### 2.3 Measurement Cadence

Cadence is a required field because it directly determines whether a metric functions as lead or lag in practice. A metric that is theoretically predictive but only evaluated once a year is operationally a lag indicator — teams cannot course-correct based on it within a goal cycle.

**Rule:** Classification defaults to the most frequent operationally available measurement interval. When a metric is reported at a different (less frequent) cadence for compliance or investor purposes, that secondary use does not change the operational lead/lag classification.

**Example:** kWh/m² Reduction can be derived from IoT sensors monthly — it is classified Lead. The same data may be aggregated annually for GRESB reporting — that is a secondary reporting use. The classification stays Lead based on the monthly operational cadence.

| Value | Meaning |
|-------|---------|
| `daily` | Measured and available every day (system logs, IoT streams) |
| `weekly` | Reviewed every week (operational health checks) |
| `monthly` | Reviewed every month (operational KPI cycle) |
| `quarterly` | Reviewed every quarter (business performance cycle) |
| `annual` | Reviewed every year (financial reporting, ESG compliance) |
| `per-project` | Measured at project completion or milestone, not on a calendar cycle |

---

## 3. How CRE Layers Map to the Classification Grid

The existing framework layers (PVL → ABO → BODM → TODM) have a natural — but not rigid — correspondence with the classification grid.

```
Layer       | Default Type        | Default Timing | Default Cadence
------------|---------------------|----------------|---------------------------
PVL         | Effect              | Lag            | Annual
ABO         | Effect / Outcome    | Lag            | Annual / Quarterly
BODM        | Outcome / Output    | Lag / Lead     | Varies by category
TODM        | Output / Process    | Lead           | Monthly / Weekly / Daily
```

**Important:** These are defaults, not rules. Some BODM metrics are process-type (time-reduction metrics). Some TODM metrics lag (PropTech Investment ROI). Some BODM operational metrics are output-type (data quality metrics elevated from TODM layer).

---

## 4. Classification Rules for CRE Context

### Rule 1 — Financial returns metrics are always Lag, Effect-type
IRR, NPV, NOI, Equity Multiple, WACC, Debt Yield, LTV — these confirm accumulated past performance. They are Effect or Outcome-type and always lag. Cadence: annual or quarterly.

### Rule 2 — Automation rate metrics are Output + Lead
Any metric of the form "% automated" or "rate of automation" (Rent Review Automation Rate, Data Capture Automation Rate, Green Lease Compliance Automation) measures what technology produced — an output. These are leading indicators for operational efficiency outcomes. Cadence: monthly.

### Rule 3 — Data quality metrics are Output + Lead
Vacancy Data Accuracy, Lease Data Integrity, Asset Hierarchy Coverage, Tenant Record Duplication Rate — these measure the condition of a system output and directly predict downstream outcome quality. Cadence: monthly.

### Rule 4 — Tenant-facing results are Outcome + Lag
Tenant Retention Rate, Average Daily Rate — these measure business results confirmed at lease event or transaction. Cadence: annual or monthly respectively.

### Rule 5 — Energy and carbon metrics: cadence governs lead/lag
kWh/m² and Peak Demand Reduction are Outcome-type but their timing depends on measurement interval. IoT-derived monthly = Lead. Annually reported for compliance (Carbon Emissions Reduction, Embodied Carbon Intensity) = Lag. The metric_type is Outcome in both cases.

### Rule 6 — Time-reduction and velocity metrics are Process + Lead
Any metric measuring how fast or efficiently work is performed — Lease Event Processing Time Reduction, Report Generation Time Reduction, Time to Feasibility Study, Development Pipeline Velocity — is Process-type. These are not outputs (no deliverable is produced) and not outcomes (no behavior change in users). They measure workflow efficiency and are leading indicators for downstream cost and capacity outcomes. Cadence: monthly or per-project.

### Rule 7 — Market metrics are Effect + Lag
Market Rent vs Contract Rent, Market Absorption Rate — these reflect market behavior, not team actions. Confirmatory of investment thesis. Cadence: quarterly.

---

## 5. New Schema Fields

Add three fields to every metric file's YAML frontmatter:

```yaml
metric_type: process | output | outcome | effect
timing: lead | lag
measurement_cadence: daily | weekly | monthly | quarterly | annual | per-project
```

`input` is a reserved value in the `metric_type` enum for methodology completeness but has no metrics in this framework.

### Example — before:
```yaml
---
id: tenant-retention-rate
name: Tenant Retention Rate
type: BODM
category: Tenant Outcomes
...
---
```

### Example — after:
```yaml
---
id: tenant-retention-rate
name: Tenant Retention Rate
type: BODM
category: Tenant Outcomes
metric_type: outcome
timing: lag
measurement_cadence: annual
...
---
```

---

## 6. Full Classification Register

### PVL Layer — 5 metrics

| Metric | metric_type | timing | measurement_cadence | Rationale |
|--------|-------------|--------|---------------------|-----------|
| Revenue Growth | effect | lag | annual | Ultimate strategic outcome; aggregates many outcomes |
| Cost Savings | effect | lag | annual | Strategic lever; confirmed in financial statements |
| Risk Reduction | effect | lag | annual | Portfolio-level risk confirmed in hindsight |
| ESG & Sustainability | effect | lag | annual | Regulatory and market positioning; annual cycle |
| Productivity & Workflow Efficiency | effect | lag | annual | Strategic capability outcome; long-cycle confirmation |

### ABO Layer — 5 metrics

| Metric | metric_type | timing | measurement_cadence | Rationale |
|--------|-------------|--------|---------------------|-----------|
| Optimised Portfolio Returns | effect | lag | annual | IRR/NOI aggregate; confirms investment thesis |
| Enhanced Operational Efficiency & Sustainability | outcome | lag | annual | Confirms transformation programme; measured annually |
| Reduced Investment Risk & Improved Compliance | outcome | lag | annual | Confirms risk programme outcomes |
| Increased Tenant Satisfaction & Retention | outcome | lag | annual | Retention is confirmatory; NPS periodic |
| Streamlined Decision-Making & Workflow | outcome | lead | quarterly | Decision speed is more responsive than financial results |

### BODM Layer — 40 metrics

**Financial Performance**

| Metric | metric_type | timing | measurement_cadence | Rationale |
|--------|-------------|--------|---------------------|-----------|
| IRR | effect | lag | annual | Ultimate investment return; measured at exit or annually |
| NPV | effect | lag | annual | Confirms present value of future cash flows |
| Equity Multiple | effect | lag | per-project | Total return multiplier; only meaningful at exit |
| LTV | outcome | lag | quarterly | Confirms lending position; slow to change |
| Debt Yield | outcome | lag | quarterly | NOI / loan value; confirms debt serviceability |
| NOI | outcome | lag | quarterly | Core income metric; quarterly confirmed |
| WACC | effect | lag | annual | Cost of capital inputs; strategic financial parameter |

**Operational Efficiency**

| Metric | metric_type | timing | measurement_cadence | Rationale |
|--------|-------------|--------|---------------------|-----------|
| Fault Detection Rate | outcome | lead | weekly | Predicts maintenance cost and tenant satisfaction outcomes |
| Lease Event Processing Time Reduction % | process | lead | monthly | Measures workflow cycle time, not a deliverable or behavior change |
| Vacancy Data Accuracy % | output | lead | monthly | Data system output; predicts leasing decision quality |
| Financial Dashboard Automation % | output | lead | monthly | Automation output; predicts reporting time savings |
| Asset Hierarchy Data Coverage % | output | lead | monthly | System coverage; predicts data quality outcomes |
| Property Data Integration Rate % | output | lead | monthly | Integration completeness; predicts reporting accuracy |
| Lease Data Integrity % | output | lead | monthly | Data quality output; predicts downstream errors |
| Rent Review Automation Rate % | output | lead | monthly | Automation delivery; predicts review cycle efficiency |
| Report Generation Time Reduction % | process | lead | monthly | Measures process speed improvement, not a deliverable |
| Tenant Record Duplication Rate % | output | lead | monthly | Data quality signal; predicts CRM and billing accuracy |
| Cybersecurity Incident Rate | outcome | lag | monthly | Incidents confirm past exposure; hard to predict |

**ESG / Sustainability**

| Metric | metric_type | timing | measurement_cadence | Rationale |
|--------|-------------|--------|---------------------|-----------|
| kWh/m² Reduction | outcome | lead | monthly | IoT-derived monthly; default to most frequent available interval |
| Peak Demand Reduction | outcome | lead | monthly | Directly influenced by BMS/IoT interventions |
| Carbon Emissions Reduction | outcome | lag | annual | Scope 1–3 measured annually; confirms ESG programme |
| Waste Reduction % | outcome | lag | quarterly | Operational waste tracked quarterly |
| Green Lease Compliance Automation % | output | lead | monthly | Automation output; predicts compliance accuracy |
| Climate Risk Exposure | effect | lag | annual | Portfolio-level strategic risk; scenario-modelled annually |
| Embodied Carbon Intensity | effect | lag | per-project | Design-phase decision; confirmed per project completion |
| Construction Waste Reduction % | outcome | lag | per-project | Construction phase outcome; confirmed on completion |

**Tenant Outcomes & Market Performance**

| Metric | metric_type | timing | measurement_cadence | Rationale |
|--------|-------------|--------|---------------------|-----------|
| Tenant Retention Rate | outcome | lag | annual | Lease renewal confirmed at expiry; annual cycle |
| Tenant Payment Reliability Index (TPRI) | outcome | lead | monthly | Payment pattern signals early financial risk |
| Average Daily Rate (ADR) | outcome | lag | monthly | Rate confirmed per transaction; market-driven |
| Market Rent vs Contract Rent | effect | lag | quarterly | Market benchmark; confirmed externally |
| Tenant Utilization Rate | outcome | lead | monthly | Occupancy signal; predicts retention risk early |
| Market Absorption Rate | effect | lag | quarterly | Macro market signal; not team-controllable |

**Development & Construction**

| Metric | metric_type | timing | measurement_cadence | Rationale |
|--------|-------------|--------|---------------------|-----------|
| Time to Feasibility Study Completion | process | lead | per-project | Measures workflow duration; predicts GDV decision speed |
| Development Density & Design Optimisation Index | outcome | lead | per-project | Predicts GDV and planning success |
| Compliance Rate with Local Planning Policy | outcome | lead | per-project | Predicts planning approval and timeline risk |
| GDV Optimisation | effect | lag | per-project | Confirmed at planning approval or project delivery |
| Construction Rework Reduction % | outcome | lead | monthly | Quality signal during build; predicts cost and timeline |
| Construction Waste Reduction % | outcome | lag | per-project | Construction phase outcome; confirmed on completion |
| Accident Rate Reduction % | outcome | lag | monthly | Safety outcome; confirmed per reporting period |
| Compliance with Architects' Plans % | output | lead | monthly | Quality control output during construction |
| Development Pipeline Velocity | process | lead | monthly | Measures throughput pace; predicts delivery cadence and NOI timing |

### TODM Layer — 25 metrics

| Metric | metric_type | timing | measurement_cadence | Rationale |
|--------|-------------|--------|---------------------|-----------|
| Energy Savings % | outcome | lead | monthly | Technology-enabled saving; predicts kWh/m² reduction |
| Data Capture Automation Rate % | output | lead | monthly | Automation activity; directly controllable |
| Uptime / Availability of Automated Systems | output | lead | daily | System health; predicts data and automation reliability |
| AI-Generated Development Options per Assessment | output | lead | per-project | AI productivity measure; directly controllable |
| Accuracy of AI-Generated Cost Estimates | output | lead | per-project | Quality of AI output; predicts development cost risk |
| Accuracy of Financial Models | output | lead | per-project | Model quality; predicts decision reliability |
| Frequency of Automated Sell/Hold Recommendations | output | lead | monthly | AI output frequency; predicts decision speed |
| Discrepancy Detection Rate (Plans vs Site) | output | lead | per-project | AI detection output; predicts rework prevention |
| Lease Data Integrity % (TODM) | output | lead | monthly | Technology data quality output |
| Rent Review Automation Rate % (TODM) | output | lead | monthly | Technology output; predicts BODM review efficiency |
| Lease Event Processing Time Reduction % (TODM) | process | lead | monthly | Technology-driven cycle time; measures workflow speed |
| Vacancy Data Accuracy % (TODM) | output | lead | monthly | Technology data quality output |
| Tenant Record Duplication Rate % (TODM) | output | lead | monthly | Technology data quality output |
| Financial Dashboard Automation % (TODM) | output | lead | monthly | Automation delivery output |
| Report Generation Time Reduction % (TODM) | process | lead | monthly | Technology-driven process speed improvement |
| Asset Hierarchy Data Coverage % (TODM) | output | lead | monthly | System coverage output |
| Property Data Integration Rate % (TODM) | output | lead | monthly | Integration completeness output |
| Green Lease Compliance Automation % (TODM) | output | lead | monthly | Automation delivery output |
| Data Model Alignment Accuracy % | output | lead | monthly | Architecture quality; predicts integration reliability |
| Cybersecurity Incident Rate (TODM) | outcome | lag | monthly | Technology security outcome; hard to predict |
| IoT Sensor Health & Data Quality | output | lead | weekly | Sensor system output; predicts energy/building data quality |
| Digital Twin Fidelity | output | lead | quarterly | Model completeness; reviewed per major update cycle |
| Technology Adoption Rate | output | lead | monthly | Rollout activity; leading for all tech-enabled outcomes |
| PropTech Investment ROI | effect | lag | per-project | Returns confirmed in hindsight; investment-level result |
| Tenant Experience Tech Utilization | output | lead | monthly | Usage rate; predicts tenant satisfaction |

---

## 7. Cross-Classification Insights

### The framework's natural signal flow

```
TODM (Output/Process + Lead, Daily/Weekly/Monthly)
       ↓ enables
BODM operational (Output/Process/Outcome + Lead, Monthly)
       ↓ drives
BODM financial (Outcome/Effect + Lag, Quarterly/Annual)
       ↓ confirms
ABO (Outcome/Effect + Lag, Annual)
       ↓ proves
PVL (Effect + Lag, Annual)
```

This means:
- A CRE asset manager should watch **TODM and BODM-operational metrics weekly/monthly** — these are actionable signals
- **BODM financial and ABO metrics** confirm quarterly — these validate strategy
- **PVL metrics** are annual — these answer the investor thesis question

### Watch pairs — lead + lag for the same value chain

| Leading signal | cadence | Lagging confirmation | cadence |
|----------------|---------|---------------------|---------|
| Technology Adoption Rate | monthly | PropTech Investment ROI | per-project |
| Tenant Utilization Rate | monthly | Tenant Retention Rate | annual |
| Fault Detection Rate | weekly | NOI (maintenance cost line) | quarterly |
| Vacancy Data Accuracy % | monthly | Market Rent vs Contract Rent accuracy | quarterly |
| Development Pipeline Velocity | monthly | IRR / GDV Optimisation | per-project |
| Compliance with Architects' Plans % | monthly | Construction Rework Reduction % | monthly |
| kWh/m² Reduction | monthly | Carbon Emissions Reduction | annual |

---

## 8. Implementation Plan

### Phase 1 — Schema update
Add `metric_type`, `timing`, and `measurement_cadence` fields to every metric file's YAML frontmatter. Use the classification register in Section 6 as the source of truth.

**Files to update:** 75 metric files across `metrics/pvl/`, `metrics/abo/`, `metrics/bodm/`, `metrics/todm/`

### Phase 2 — INDEX update
Add columns `metric_type`, `timing`, and `measurement_cadence` to the index tables in `INDEX.md`.

### Phase 3 — Chain files
Annotate each chain file (`chains/*.md`) with the lead/lag flow for that value lever, showing which metrics to monitor at which cadence.

### Phase 4 — Machine-readable registry
Update `interfaces/machine-readable/metrics-registry.yaml` from v1.0 to v1.1 to include `metric_type`, `timing`, and `measurement_cadence` fields for all 75 entries.

### Phase 5 — LLM prompt update
Update `interfaces/llm-prompts/metric-lookup.md` to support queries filtered by `metric_type`, `timing`, and `measurement_cadence` (e.g., "give me leading output metrics for the cost-savings chain measured monthly").

---

## 9. Open Questions

1. **BODM/TODM duplication** — Several metrics appear in both BODM and TODM (e.g., Rent Review Automation Rate, Lease Data Integrity). Both layers correctly apply `output / lead / monthly` — the duplication is intentional, representing the business team's view (BODM) and the technology team's view (TODM) of the same metric. No collapse needed; layer-specific classification is consistent.

2. ~~Measurement frequency as a field~~ — **Resolved.** `measurement_cadence` is now a required field (Section 5). The dual-cadence ambiguity for kWh/m² is resolved in Section 2.3 and Rule 5.

3. **Perspective tagging** — The BODM/TODM layer distinction already encodes much of the stakeholder perspective separation. Full per-stakeholder tagging (Asset Manager vs Technology Team vs Investment Director) is a deferred enhancement once Phase 2 metadata fields (health metrics, North Star, vanity risk) are implemented.
