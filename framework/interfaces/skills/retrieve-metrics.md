# Skill: retrieve-metrics

**Purpose:** Abstract all metric retrieval from the CRE Metrics Framework registry. Agents call this skill with semantic parameters — never with raw file paths or YAML parsing logic.

**Location:** `framework/interfaces/skills/retrieve-metrics.md`

---

## Interface (Stable Contract)

### Inputs

At least one parameter is required. Parameters can be combined.

| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| `chain` | string | Filter by value lever | `chain=cost-savings` |
| `type` | string | Filter by metric type | `type=BODM` |
| `name` | string | Lookup by canonical name (partial match OK) | `name="Fault Detection Rate"` |

### Example Invocations

```
retrieve-metrics  chain=cost-savings  type=BODM
retrieve-metrics  name="Fault Detection Rate"
retrieve-metrics  type=TODM
retrieve-metrics  chain=esg-sustainability
retrieve-metrics  chain=revenue-growth  type=TODM
```

### Output

A filtered list of metrics. Each entry contains:

| Field | Description |
|-------|-------------|
| `id` | Stable identifier |
| `canonical_name` | Exact name to use in case studies and mappings |
| `type` | PVL / ABO / BODM / TODM |
| `chains` | Which value levers this metric belongs to |
| `target` | Benchmark target (from registry or metric file) |
| `framework_version` | Version of the registry at fetch time |

---

## Implementation (Internal — Subject to Change)

### Current: Registry Fetch

1. Fetch `metrics-registry.yaml` from the stable URL:
   ```
   https://raw.githubusercontent.com/mostarhov-source/CRE-Metrics-Framework/main/framework/interfaces/machine-readable/metrics-registry.yaml
   ```
2. Filter by the provided parameters:
   - `chain`: match any entry in the metric's `chains` list
   - `type`: exact match on `type` field
   - `name`: case-insensitive partial match on `name` or `canonical_name`
3. For each matching metric, fetch the full metric file at `framework/metrics/{type_lowercase}/{id}.md` to retrieve the `target` field
4. Return the filtered subset in a consistent structured format

### MCP Migration Path

When the project is ready for MCP, this skill file is updated to call an MCP tool with identical inputs and outputs. Agents calling `retrieve-metrics` require no changes — only this file is updated.

---

## Error Handling

- If the registry is unreachable: return a cached version if available, otherwise report `REGISTRY_UNAVAILABLE`
- If no metrics match the filters: return an empty list with a note: `"No metrics found matching the provided filters"`
- If `deprecated_name` is present in a matched metric: include a warning: `"Note: canonical name changed from '{deprecated_name}' — update any hardcoded references"`

---

## Notes

- Always use `canonical_name` in output — never the raw `name` field if they differ
- The `id` field is stable across versions; the `canonical_name` may change on major version bumps
- Do not expose internal file paths in skill output — the interface is semantic, not file-based
