# Prompt Pattern: Metric Lookup

Use this prompt pattern when an LLM agent needs to find a specific metric by name, type, or chain membership.

---

## Instruction Block

```
You are looking up metrics from the CRE Metrics Framework.

## Step 1: Fetch the Registry

Fetch the metrics registry from:
https://raw.githubusercontent.com/mostarhov-source/CRE-Metrics-Framework/main/framework/interfaces/machine-readable/metrics-registry.yaml

## Step 2: Filter

Apply the requested filters:
- By name: match `name` or `canonical_name` field (case-insensitive, partial match OK)
- By type: filter `type` field — PVL, ABO, BODM, or TODM
- By chain: filter `chains` list — cost-savings, revenue-growth, risk-reduction, esg-sustainability, productivity-workflow
- By metric_type: filter `metric_type` field — process, output, outcome, or effect
- By timing: filter `timing` field — lead or lag
- By cadence: filter `measurement_cadence` field — daily, weekly, monthly, quarterly, annual, or per-project
- By health_metric: filter `health_metric: true` — vital signs requiring weekly threshold monitoring
- By vanity_risk: filter `vanity_risk` field — none, low, medium, or high
- By north_star_candidate: filter `north_star_candidate: true`, optionally with `north_star_context` — investment, esg, or operations
- By lead_relationship: filter `lead_relationship` field — causative, correlative, or n/a
- By adoption_phase: filter `adoption_phase` field — explore, exploit, or both

## Step 3: Return Results

For each matching metric, return:
- `id` — stable identifier
- `canonical_name` — the exact name to use in case studies and mappings
- `type` — PVL / ABO / BODM / TODM
- `metric_type` — process / output / outcome / effect (role in measurement chain)
- `timing` — lead / lag (predictive vs confirmatory)
- `measurement_cadence` — how frequently this metric is measured operationally
- `chains` — which value levers this metric belongs to
- `health_metric` — true if present; omit field means false
- `vanity_risk` — high/medium if present; absent means none
- `north_star_candidate` — true if present; `north_star_context` lists applicable stakeholder contexts
- `framework_version` — the `version` field from the registry header

## Step 4: Locate the Full Metric File

The metric file path is:
`framework/metrics/{type_lowercase}/{id}.md`

For example:
- BODM `fault-detection-rate` → `framework/metrics/bodm/fault-detection-rate.md`
- TODM `energy-savings-pct` → `framework/metrics/todm/energy-savings-pct.md`
```

---

## Example Invocations

```
retrieve-metrics  name="Fault Detection Rate"
retrieve-metrics  type=TODM  chain=esg-sustainability
retrieve-metrics  chain=cost-savings  type=BODM
retrieve-metrics  timing=lead  cadence=weekly
retrieve-metrics  metric_type=process
retrieve-metrics  type=BODM  timing=lead  cadence=monthly
retrieve-metrics  metric_type=effect  timing=lag
retrieve-metrics  health_metric=true
retrieve-metrics  north_star_candidate=true  north_star_context=investment
retrieve-metrics  vanity_risk=high
retrieve-metrics  vanity_risk=medium  type=TODM
retrieve-metrics  lead_relationship=causative  type=TODM
retrieve-metrics  adoption_phase=explore
retrieve-metrics  adoption_phase=both  timing=lead  cadence=monthly
```

---

## Notes

- Use `canonical_name` (not `name`) when referencing metrics in case study mappings
- If `deprecated_name` is present in a registry entry, the metric was recently renamed — update any hardcoded references
- `metric_type` describes where in the measurement chain a metric sits: process (workflow efficiency) → output (what was produced) → outcome (behavior change) → effect (strategic impact)
- `timing` is context-dependent: lead metrics are directly team-controllable and change within a goal cycle; lag metrics confirm results in hindsight. Measurement cadence (`measurement_cadence`) determines whether a metric functions as lead or lag in practice — a theoretically predictive metric measured only annually is operationally a lag indicator
- `health_metric: true` marks vital signs — threshold-based survival checks evaluated weekly, directly actionable within days. There are 5 health metrics in the framework: system-uptime-availability, bodm-cybersecurity-incident-rate, todm-cybersecurity-incident-rate, iot-sensor-health-data-quality, tenant-payment-reliability-index
- `vanity_risk` signals whether a metric can justify activity without indicating what to do. High/medium-risk metrics must be paired with a downstream BODM metric or an explicit decision rule to be non-vanity. Absent field = none
- `lead_relationship` — for lead metrics: `causative` means the lead action directly produces the lag result (safe for OKR key results); `correlative` means it accompanies but doesn't directly cause (valid warning signal, not sufficient for OKR target). `n/a` for all lag metrics
- `adoption_phase` — `explore` = validates whether technology works (pilot/PoC stage); `exploit` = measures returns at scale (post-proof); `both` = relevant throughout. Use explore-phase metrics for PropTech pilot case studies; switch to exploit-phase once technology is proven
- `north_star_candidate: true` marks metrics that satisfy the North Star eligibility tests: rate or ratio, behavior-change oriented, all subordinate metrics trace contribution to it. Context field indicates which stakeholder perspective it serves (investment / esg / operations). IRR, NPV, and Equity Multiple are explicitly excluded — they fail the behavior-change criterion
