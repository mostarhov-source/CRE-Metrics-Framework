# Prompt Pattern: Value Chain Traversal

Use this prompt pattern when an LLM agent needs to navigate the full PVL → ABO → BODM → TODM chain, or traverse in reverse (TODM → PVL).

---

## Instruction Block

```
You are navigating the CRE Metrics Framework value chain.

## Forward Traversal (PVL → TODM)

To answer "what technology metrics support this business value lever?":

1. Identify the PVL (e.g., Cost Savings)
2. Load the chain file: framework/chains/{chain-id}.md
3. Read the ABO section — this is the strategic outcome
4. Read the BODM table — these are the business metrics to evidence
5. Read the TODM table — these are the technology capabilities that prove each BODM
6. Check the "Enables" column to see which BODM each TODM supports

## Reverse Traversal (TODM → PVL)

To answer "what business value does this technology metric contribute to?":

1. Identify the TODM (e.g., Energy Savings %)
2. Check its `enables_bodm` field in the metric file: framework/metrics/todm/{id}.md
3. For each enabled BODM, read the BODM file: framework/metrics/bodm/{id}.md
4. Check the BODM's `parent_abo` and `chains` fields
5. Load the chain file(s) listed in `chains` to confirm the full path

## Gap Identification

To identify gaps in a case study's evidence:

1. Load the relevant chain file
2. For each BODM in the chain's BODM table: check whether the case study provides evidence
3. For each TODM: check whether the case study claims or implies the capability
4. Flag BODMs with no TODM coverage as "technology-agnostic" (see Note block in chain file)
5. Flag BODMs with claimed TODMs but no measured outcome as "capability without impact"

## Output Format

**Chain:** [chain name]
**PVL → ABO:** [PVL name] → [ABO name]

**BODM Coverage:**
| BODM | Evidenced? | TODM Enabling It | Notes |
|------|-----------|-----------------|-------|

**Gaps:**
- [List uncovered BODMs]
- [List claimed TODMs with no BODM outcome]
```

---

## Notes

- Chain files include a `> Note:` block identifying BODMs that are intentionally technology-agnostic — do not flag these as gaps
- If a metric appears in multiple chains (e.g., NOI is in both cost-savings and revenue-growth), the case study evidence applies to all chains
