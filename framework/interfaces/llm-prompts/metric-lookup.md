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

## Step 3: Return Results

For each matching metric, return:
- `id` — stable identifier
- `canonical_name` — the exact name to use in case studies and mappings
- `type` — PVL / ABO / BODM / TODM
- `chains` — which value levers this metric belongs to
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
```

---

## Notes

- Use `canonical_name` (not `name`) when referencing metrics in case study mappings
- If `deprecated_name` is present in a registry entry, the metric was recently renamed — update any hardcoded references
