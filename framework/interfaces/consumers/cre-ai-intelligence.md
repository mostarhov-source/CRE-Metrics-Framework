# Integration Contract: CRE-AI-Intelligence

This document defines how the CRE-AI-Intelligence project consumes the CRE Metrics Framework. It replaces any hardcoded metric dictionaries.

---

## Stable URL

The only URL the CRE-AI-Intelligence project needs to reference:

```
https://raw.githubusercontent.com/mostarhov-source/CRE-Metrics-Framework/main/framework/interfaces/machine-readable/metrics-registry.yaml
```

This URL is stable across all internal restructures. The file will not be moved.

---

## What to Fetch

On startup or cache refresh, fetch `metrics-registry.yaml` and extract:

| Field | Use |
|-------|-----|
| `id` | Stable identifier for internal lookups |
| `canonical_name` | Exact name to use in `### Framework Mapping` blocks in case studies |
| `type` | Filter metrics by layer (PVL / ABO / BODM / TODM) |
| `chains` | Filter metrics by value lever |
| `framework_version` | Detect breaking changes — log and alert if major version changes |

Do not hardcode metric names or IDs. Fetch from registry and cache locally.

---

## Version Handling

| Registry Version Change | Action Required |
|------------------------|-----------------|
| Minor bump (1.1 → 1.2) | No action — new metrics added, no existing ones changed |
| Major bump (1.x → 2.0) | Review `deprecated_name` entries — update any case study mappings that reference the old canonical name |

Check `version` field on every fetch. If the major version has changed since last fetch, emit a warning to the operator before applying.

---

## Case Study Mapping Format

When writing `### Framework Mapping` blocks, always use the `canonical_name` from the registry — never paraphrase. Example:

```markdown
### Framework Mapping

**Primary Value Lever:** Cost Savings
**Aggregated Business Outcome:** Enhanced Operational Efficiency & Sustainability

**BODM Evidence:**
| Metric | Claimed Value | Meets Target |
|--------|--------------|--------------|
| kWh/m² Reduction | 23% | ✅ (target ≥10%) |
| Fault Detection Rate | 94% | ✅ (target ≥90%) |

**TODM Capabilities:**
| Technology Metric | Status |
|-------------------|--------|
| Energy Savings % | Evidenced — 23% confirmed |
| IoT Sensor Health & Data Quality | Claimed — no independent measurement |
```

---

## Chain File Access

For case study analysis tasks that need full chain context, the agent may load chain files directly from the repo:

```
framework/chains/cost-savings.md
framework/chains/revenue-growth.md
framework/chains/risk-reduction.md
framework/chains/esg-sustainability.md
framework/chains/productivity-workflow.md
```

These files are LLM-friendly and self-contained. The agent does not need to load individual metric files for chain traversal.

---

## Prompt Patterns

Use the prompt patterns in `framework/interfaces/llm-prompts/` as instruction blocks for case study analysis agents:

- `case-study-analysis.md` — full framework mapping workflow
- `metric-lookup.md` — fetch and filter registry
- `value-chain-traversal.md` — navigate chains programmatically

---

## MCP Migration Path

When this project is ready to replace the `retrieve-metrics` skill with an MCP tool call:
1. The `interfaces/skills/retrieve-metrics.md` skill file is updated to call the MCP tool
2. No changes required in CRE-AI-Intelligence agents — the semantic interface is identical
3. The registry URL remains stable and unchanged
