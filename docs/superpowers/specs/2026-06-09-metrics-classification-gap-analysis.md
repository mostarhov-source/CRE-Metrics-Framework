# Gap Analysis: Metrics Classification Spec vs Source Methodology

**Date:** 2026-06-09  
**Status:** Complete (Phase 2 implemented 2026-06-09, Phase 3 implemented 2026-06-09)  
**Amends:** `2026-06-09-metrics-classification-output-outcome-effect.md`  
**Source methodology:** RAG | Books | Metrics And Measurement (NotebookLM)

---

## 1. Executive Summary

The classification spec introduces a two-dimensional assessment of all 75 CRE metrics (type: output/outcome/effect; timing: lead/lag). The source methodology — drawn from the books in *RAG | Books | Metrics And Measurement* — defines a richer framework than the spec captured. Seven gaps were identified by comparing the spec against the full methodology. Two are blockers that must be resolved before Phase 1 (frontmatter updates to metric files) begins. Three are medium-priority enhancements for Phase 2. Two are low-priority additions deferred to Phase 3.

| # | Gap | Severity | Disposition |
|---|-----|----------|-------------|
| 1 | Type axis is 3-level; methodology defines 5-level — `process` type missing, 6 metrics misclassified | HIGH | **BLOCKER — fix before Phase 1** |
| 2 | No Health Metrics concept | MEDIUM | **IMPLEMENTED — Phase 2** |
| 3 | No North Star designation | MEDIUM | **IMPLEMENTED — Phase 2** |
| 4 | No Explore vs Exploit phase tagging | LOW | **IMPLEMENTED — Phase 3** |
| 5 | Vanity metric risk not flagged | MEDIUM | **IMPLEMENTED — Phase 2** |
| 6 | Measurement cadence unresolved (Open Question 2 in spec) | HIGH | **BLOCKER — fix before Phase 1** |
| 7 | Correlation vs causation not distinguished in lead indicators | LOW | **IMPLEMENTED — Phase 3** |

---

## 2. Source Methodology Reference

### 2.1 Full Measurement Chain (5 levels)

The methodology defines a complete cause-and-effect hierarchy:

```
Input → Process → Output → Outcome → Impact
```

| Level | Definition | CRE examples |
|-------|-----------|--------------|
| **Input** | Resources and assets invested before work begins | PropTech budget, staff capacity, raw data quality |
| **Process** | Efficiency and speed of the work being performed | Time to complete feasibility study, reporting cycle time |
| **Output** | Immediate deliverable or artifact produced by the activity | AI-generated development options, automation rate achieved |
| **Outcome** | Behavior change or business result arising after the output | Tenant retention, NOI, carbon reduction |
| **Impact** | Long-term strategic consequence of accumulated outcomes | IRR, portfolio valuation, ESG market positioning |

The spec uses three levels (Output / Outcome / Effect), which collapses Input and Process into "Output" and renames Impact as "Effect." This is acceptable for Impact/Effect, but loses the distinction between Process and Output — a distinction that matters for six CRE metrics.

### 2.2 Four Metric Archetypes

Beyond the chain, the methodology defines four archetypes that cut across the hierarchy:

**Health Metrics** — 5 to 7 vital signs of the business. Evaluated weekly (not monthly or annually). Threshold-based pass/fail logic, not target-based. The decision-maker has direct power to impact the number. Linked to the North Star. Distinguishes surviving from thriving.

**North Star Metrics** — Top-line metric representing the company's growth ambition and direction. Must be a rate or ratio (not a raw count). Behavior-change oriented. Aligns exploration metrics, OKRs, and team activities toward a shared vision. One or very few per organizational context.

**Exploration Metrics** — Applied before product/market fit. Minimum viable set. Focus on learning, improving, and validating assumptions. Used during the EXPLORE phase of technology or product adoption.

**Exploitation Metrics** — Applied after product/market fit. Focus on efficiency, scale, and profitability. Gross quantities and unit economics. Used during the EXPLOIT phase once a technology or approach is proven.

### 2.3 Vanity Metrics

Vanity metrics are numbers that look impressive, justify activity in presentations, but provide no indication of what concrete action to take. Examples from the methodology: number of ideas, number of patents, R&D spending, number of employees in innovation. Sanity check: if the metric went up, down, or stayed the same — what would the team do differently? If there is no clear answer, it is a vanity metric.

---

## 3. Gap Analyses

### Gap 1 — Type axis is 3-level; methodology defines 5-level (BLOCKER)

**Severity:** HIGH  
**Disposition:** Must be resolved before Phase 1 begins

#### What the methodology says

The full measurement chain is Input → Process → Output → Outcome → Impact. Process metrics specifically measure the efficiency and speed of work being performed — not what the work produced (Output), and not what changed as a result (Outcome). Canonical process metric examples from the books: *Time to complete product/market fit validation*, *Time-to-market for expansion of core value proposition*, *Number of training hours performed*.

#### What the spec missed

Spec Section 2.1 defines only three types: Output, Outcome, Effect. It states the chain is "Input → Process → **Output → Outcome → Effect**" but then only assigns values from the three bolded levels. This means any metric that measures workflow duration or cycle time gets misclassified as Output or Outcome, obscuring its nature.

`input` type is genuinely absent from this framework — budgets, staff capacity, and data source quality are prerequisites, not tracked metrics in the registry. But `process` type is present and six metrics are currently misclassified.

#### Affected metrics with reclassification

| Metric | Layer | Current in spec | Correct |
|--------|-------|-----------------|---------|
| Lease Event Processing Time Reduction % | BODM | outcome / lead | **process** / lead |
| Lease Event Processing Time Reduction % | TODM | output / lead | **process** / lead |
| Report Generation Time Reduction % | BODM | outcome / lead | **process** / lead |
| Report Generation Time Reduction % | TODM | output / lead | **process** / lead |
| Time to Feasibility Study Completion | BODM | output / lead | **process** / lead |
| Development Pipeline Velocity | BODM | outcome / lead | **process** / lead |

The test: a process metric answers "how fast or efficiently is the work being done?" An output metric answers "what was produced?" A cycle time reduction metric answers the efficiency question, not the deliverable question.

#### Proposed resolution

Extend the `metric_type` enum in spec Section 5 from `output | outcome | effect` to:

```yaml
metric_type: input | process | output | outcome | effect
```

Document `input` as reserved — it is defined for completeness with the methodology chain but currently has no metrics in this framework. Update the Section 6 classification register to apply `process` to the six metrics above. Update spec Section 3 (the layer-default table) to note that some BODM and TODM metrics are process-type.

---

### Gap 2 — No Health Metrics concept (MEDIUM)

**Severity:** MEDIUM  
**Disposition:** Enhancement — Phase 2

#### What the methodology says

Health metrics describe a business's vital signs. They differ from classic KPIs in four ways: (1) evaluated weekly, not monthly or annually; (2) decision-maker has direct impact on the numbers; (3) linked to the strategic North Star; (4) focused on thresholds (survive/fail), not targets (achieve X%). The methodology recommends 5 to 7 health metrics per business. They are especially valuable in turbulent conditions because they reveal whether the business is surviving vs thriving.

#### What the spec missed

The spec has no concept of this archetype. A metric classified as `output / lead` or `outcome / lead` gives no signal about whether it is an optional performance improvement metric or a survival-critical vital sign. These are fundamentally different in how they should be treated operationally.

#### CRE health metric candidates

| Metric | Rationale |
|--------|-----------|
| System Uptime / Availability (TODM) | Classic threshold check; zero-downtime expectation; directly within tech team's control |
| Cybersecurity Incident Rate (BODM/TODM) | Zero-tolerance threshold; survival signal for digital operations |
| IoT Sensor Health & Data Quality (TODM) | Weekly freshness check; if sensors degrade, all building-operations data is unreliable |
| Tenant Payment Reliability Index (BODM) | Early financial distress signal; directly actionable by AM team within days |

#### Proposed resolution

Add an optional boolean field to the spec's schema (Section 5):

```yaml
health_metric: true    # omit if false
```

Add spec rule: a metric qualifies as a health metric if it satisfies all three criteria: (1) it can be measured and acted upon weekly or more frequently; (2) the accountable team can directly change the outcome within days; (3) a threshold-based failure mode is defined (not just a target). Flag the four candidates above.

---

### Gap 3 — No North Star designation (MEDIUM)

**Severity:** MEDIUM  
**Disposition:** Enhancement — Phase 2

#### What the methodology says

A North Star metric focuses on the growth ambition and strategic direction of the organization. It must be a rate or ratio (not a raw count), behavior-change oriented, and understandable enough to align all subordinate metrics and team activities. There is typically one North Star per organizational context. For complex portfolios, one North Star per major strategic priority is acceptable.

The methodology gives three eligibility tests: (1) Is it a rate or ratio? (2) Does it reflect behavior change, not just an accounting result? (3) Can teams working on sub-metrics trace their contribution directly to the North Star?

#### What the spec missed

The spec places all PVL metrics as `effect / lag`, which is correct classification — but it does not distinguish which among them is the North Star that guides the entire measurement system. Without this, the classification register is a flat list. The methodology requires a hierarchy where the North Star sits at the apex and all other metrics are subordinate.

Note: IRR fails the North Star test despite being an `effect / lag` metric. It is a rate but it is not behavior-change oriented — it is an accounting calculation that only changes at project exit. The real North Star candidates in CRE are behavior-change metrics that teams can influence.

#### CRE North Star candidates by context

| Context | North Star candidate | Why |
|---------|---------------------|-----|
| Investment team | Tenant Retention Rate | Rate/ratio; behavior-change (lease renewals); teams across asset management, FM, and tech all trace contribution to it |
| ESG-led portfolio | Carbon Emissions Reduction | Rate; behavior-change (energy and construction decisions); links TODM → BODM → PVL directly |
| PropTech transformation | Technology Adoption Rate → NOI | During Explore: Adoption Rate; during Exploit: NOI; switch when tech is proven |

#### Proposed resolution

Add optional fields to spec Section 5:

```yaml
north_star_candidate: true                              # omit if false
north_star_context: [investment, esg, operations]       # required when north_star_candidate: true
```

Add spec rule stating the three eligibility criteria and flag that IRR, NPV, and Equity Multiple are explicitly excluded because they fail the behavior-change criterion.

---

### Gap 4 — No Explore vs Exploit phase tagging (LOW)

**Severity:** LOW  
**Disposition:** Enhancement — Phase 3

#### What the methodology says

Exploration metrics are used before product/market fit to inform decisions by measuring learning and progress. Exploitation metrics are used after product/market fit to measure scaling, efficiency, and growth. The mix of applicable metrics changes fundamentally depending on which phase a team is in.

#### What the spec missed

The spec does not tag which phase each metric applies to. This creates a practical problem for PropTech adoption cases: an asset manager piloting AI cost-estimation for the first time should be measuring a different set of metrics than one rolling it out at scale. Currently both contexts would receive the same full metric list.

#### CRE phase mapping examples

- `ai-development-options-per-assessment`, `digital-twin-fidelity`, `ai-cost-estimate-accuracy` — Explore-phase TODM metrics (validate whether the tech works before scaling)
- `noi`, `irr`, `gdv-optimisation`, `proptech-investment-roi` — Exploit-phase BODM/PVL metrics (only meaningful once technology is proven and deployed at scale)
- `technology-adoption-rate`, `data-capture-automation-rate` — bridge metrics applicable in both phases

#### Proposed resolution (deferred)

Add `adoption_phase: explore | exploit | both` to spec schema as Phase 3 enhancement. Primary value is in filtering the metric set for case studies and OKR design.

---

### Gap 5 — Vanity metric risk not flagged (MEDIUM)

**Severity:** MEDIUM  
**Disposition:** Enhancement — Phase 2

#### What the methodology says

Vanity metrics justify activity and look good on dashboards but do not indicate what concrete action to take. The sanity check: if this metric went up, went down, or stayed the same — what would the team do differently? If there is no clear answer, the metric is vanity. The methodology explicitly names raw counts (number of ideas, R&D spending, activity counts) as canonical vanity metrics.

#### What the spec missed

The spec has no actionability criterion. Some TODM metrics in the CRE framework are structurally similar to the canonical vanity archetypes: they count AI activities or measure technical properties without tying them to a decision.

#### At-risk CRE metrics

| Metric | Vanity risk reason | What would make it non-vanity |
|--------|-------------------|-------------------------------|
| `ai-development-options-per-assessment` | Counts AI options generated; quality and use are not measured | Restrict to "compliant options per appraisal" + require that options were used in a decision |
| `digital-twin-fidelity` | Completeness score is meaningless if nobody uses the twin for decisions | Pair with a usage metric: "decisions informed by digital twin this quarter" |
| `data-capture-automation-rate` | High automation of low-value data is still vanity | Pair with `data-model-alignment-accuracy` — are the right fields being automated? |
| `technology-adoption-rate` | Logins ≠ value generated | Pair with `proptech-investment-roi` or a downstream BODM metric |

#### Proposed resolution

Add to spec schema (Section 5):

```yaml
vanity_risk: none | low | medium | high
vanity_risk_note: "string"    # required when vanity_risk is medium or high
```

Add spec rule: any metric with `vanity_risk: medium` or higher must have at least one `enables_bodm` or `parent_abo` relationship defined in its metric file, and its metric file must include an explicit decision rule — what action the team takes when the metric crosses a threshold.

---

### Gap 6 — Measurement cadence unresolved (BLOCKER)

**Severity:** HIGH  
**Disposition:** Must be resolved before Phase 1 begins

#### What the methodology says

The methodology is explicit: how frequently a metric is measured changes its lead/lag classification. An NPS measurement evaluated once or twice a year is effectively a lagging indicator for a product team that needs weekly feedback — regardless of what it theoretically predicts. A metric that only changes annually does not allow a team to course-correct within a goal cycle, which is the defining property of a leading indicator.

#### What the spec missed

Spec Section 5 lists `timing: lead | lag` as the only timing-related field. Open Question 2 acknowledges the measurement frequency problem but defers it without resolution. This deferral means the spec's `timing` classifications are ambiguous for any metric that can be measured at multiple cadences.

The most significant ambiguity is `kWh/m² Reduction`, currently classified `outcome / lead`. If measured by IoT sensors daily, it is lead. If reported annually for GRESB submission, it is lag. The same metric value means different things in each context.

#### Proposed resolution

Add `measurement_cadence` as a required field alongside `timing` in spec Section 5:

```yaml
measurement_cadence: daily | weekly | monthly | quarterly | annual | per-project
```

Add spec rule: "When a metric can be measured at multiple cadences, the classification defaults to the most frequent operationally available measurement interval. If a metric is reported at a different cadence for compliance or investor purposes, both uses are valid — but the lead/lag classification applies to the operational cadence."

Apply resolved cadences to the Section 6 classification register as a new column. Representative values:

| Metric | timing | measurement_cadence |
|--------|--------|---------------------|
| kWh/m² Reduction | lead | monthly (IoT-derived) |
| Carbon Emissions Reduction | lag | annual |
| System Uptime / Availability | lead | daily |
| IRR | lag | annual |
| Tenant Retention Rate | lag | quarterly |
| Fault Detection Rate | lead | weekly |
| Technology Adoption Rate | lead | monthly |
| PropTech Investment ROI | lag | per-project |

The full resolved cadence table for all 75 metrics must be added to Section 6 of the original spec before Phase 1 begins.

---

### Gap 7 — Correlation vs causation not distinguished (LOW)

**Severity:** LOW  
**Disposition:** Enhancement — Phase 3

#### What the methodology says

Leading indicators can have two types of relationship to the lagging indicators they predict: causation (the leading action directly produces the lagging result) or correlation (the leading action accompanies the lagging result but does not directly cause it). Causation-based leads are far stronger OKR material because teams can prove their actions drove the outcome. Correlation-based leads are valid early-warning signals but should not be used as OKR key results without additional evidence.

#### What the spec missed

The spec's "watch pairs" table in Section 7 lists lead/lag pairings without distinguishing causal from correlative relationships. This means all lead indicators are presented as equally predictive of their lagged counterpart.

#### CRE examples of the distinction

| Leading indicator | Lagging indicator | Relationship | Rationale |
|-------------------|-------------------|--------------|-----------|
| Fault Detection Rate | NOI | **Causative** | Catching faults early directly reduces emergency maintenance cost, which directly improves NOI |
| Tenant Utilization Rate | Tenant Retention Rate | **Correlative** | Low utilization correlates with non-renewal, but tenants may renew regardless if lease terms are favourable |
| Technology Adoption Rate | PropTech Investment ROI | **Correlative** | Adoption is necessary but not sufficient — ROI depends on the quality of the technology and how it is used |
| Compliance with Architects' Plans % | Construction Rework Reduction % | **Causative** | Deviations from plans directly cause rework; reducing deviation directly reduces rework |

#### Proposed resolution (deferred)

Add `lead_relationship: causative | correlative | n/a` to spec schema as Phase 3 enhancement. `n/a` applies to all lag indicators. When implementing, revisit the watch pairs table in spec Section 7 and annotate each pair with its relationship type.

---

## 4. Consolidated Schema Changes

All changes to the `metric_type` enum and new fields, organized by implementation phase.

### Phase 1 — Blockers (required before frontmatter updates begin)

```yaml
# Extends existing 3-value enum to 5-value
metric_type: input | process | output | outcome | effect

# Unchanged from spec
timing: lead | lag

# NEW — required field
measurement_cadence: daily | weekly | monthly | quarterly | annual | per-project
```

### Phase 2 — Enhancements (add when updating individual metric files)

```yaml
# NEW — optional; omit entirely if false
health_metric: true

# NEW — required
vanity_risk: none | low | medium | high
# NEW — required when vanity_risk is medium or high
vanity_risk_note: "descriptive string"

# NEW — optional; omit entirely if false
north_star_candidate: true
# NEW — required when north_star_candidate is true
north_star_context: [investment, esg, operations]
```

### Phase 3 — Deferred enhancements

```yaml
# NEW — applies to PropTech/AI adoption lifecycle context
adoption_phase: explore | exploit | both

# NEW — required for all lead-timing metrics; n/a for lag
lead_relationship: causative | correlative | n/a
```

### Machine-readable registry impact

`metrics-registry.yaml` currently at version `1.0` with fields: `id`, `name`, `canonical_name`, `type`, `category`, `chains`. Adding Phase 1 fields (`metric_type`, `timing`, `measurement_cadence`) to all 75 entries constitutes a minor additive change. Per the framework versioning convention, this bumps the registry to version `1.1`. Phase 2 fields are sparse/optional — present only on metrics where they apply. The `chains-map.yaml` requires no changes — all gaps are metric-level metadata, not hierarchy changes.

---

## 5. Prioritized Amendment Queue

### Blockers — must land before Phase 1 frontmatter updates

1. **Gap 1:** Extend `metric_type` enum to include `process`. Update spec Sections 2.1, 3, 5, and 6. Reclassify the 6 affected metrics.

2. **Gap 6:** Add `measurement_cadence` as a required field. Add resolved cadence values for all 75 metrics to the Section 6 register. Write the dual-cadence resolution rule for kWh/m².

### Phase 2 enhancements — COMPLETE (implemented 2026-06-09)

3. **Gap 2:** ✓ `health_metric: true` added to 5 metric files (system-uptime-availability, bodm-cybersecurity-incident-rate, todm-cybersecurity-incident-rate, iot-sensor-health-data-quality, tenant-payment-reliability-index) and registry.

4. **Gap 5:** ✓ `vanity_risk` added to all 75 metric files. `high` on ai-development-options-per-assessment and digital-twin-fidelity; `medium` on data-capture-automation-rate and technology-adoption-rate. Registry carries sparse values only.

5. **Gap 3:** ✓ `north_star_candidate: true` + `north_star_context` added to tenant-retention-rate (investment), carbon-emissions-reduction (esg), technology-adoption-rate (operations). Registry updated. metric-lookup.md prompt updated to support all Phase 2 filter dimensions.

### Phase 3 — COMPLETE (implemented 2026-06-09)

6. **Gap 4:** ✓ `adoption_phase: explore | exploit | both` added to all 75 metric files and registry. explore = 6 tech-validation TODM metrics; exploit = 28 financial/strategic metrics; both = 41 operational metrics applicable throughout adoption lifecycle.

7. **Gap 7:** ✓ `lead_relationship: causative | correlative | n/a` added to all 75 metric files and registry. 34 causative leads (directly produce their lag counterpart); 11 correlative leads (accompany but don't directly cause); 30 lag metrics carry n/a. Registry bumped to v1.3. metric-lookup.md updated with new filter dimensions and guidance notes.

---

## 6. Resolution of Open Questions from the Original Spec

**Open Question 1 — BODM/TODM duplication:** Several metrics appear in both layers (Rent Review Automation Rate, Lease Data Integrity, etc.). The classification at BODM level should be `output / lead`; at TODM level it should also be `output / lead`. The duplication is intentional — BODM represents the business team's view of the metric, TODM the technology team's view. No collapse is needed; layer-specific classifications are consistent and both layers correctly represent the same metric from different perspectives.

**Open Question 2 — Measurement cadence as a field:** Resolved. See Gap 6. Add `measurement_cadence` as a required field before Phase 1.

**Open Question 3 — Perspective tagging (stakeholder view):** Partially resolved by Gap 3 (North Star context) and the BODM/TODM duplication answer in OQ1. Full stakeholder perspective tagging (e.g., "this metric is lead for the AM team but lag for the tech team") is a valid Phase 3 enhancement but is not required for the classification to be useful. The BODM/TODM layer distinction already encodes much of this perspective separation.
