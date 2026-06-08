# Prompt Pattern: Case Study Analysis

Use this prompt pattern when an LLM agent needs to map a PropTech or AI deployment case study to the CRE Metrics Framework value chain.

---

## Instruction Block (paste into agent system prompt or user message)

```
You are analysing a CRE PropTech case study against the CRE Metrics Framework.

## Step 1: Identify the Primary Value Lever (PVL)

Read the case study and identify which PVL the deployment primarily targets:
- Cost Savings — reduced operating, capital, or administrative costs
- Revenue Growth — increased income from rents, leasing, or services
- Risk Reduction — mitigation of financial, operational, or compliance risks
- ESG & Sustainability — improved environmental or governance performance
- Productivity & Workflow Efficiency — faster, more accurate business processes

## Step 2: Load the Chain File

Based on the PVL, load the corresponding chain file:
- Cost Savings → framework/chains/cost-savings.md
- Revenue Growth → framework/chains/revenue-growth.md
- Risk Reduction → framework/chains/risk-reduction.md
- ESG & Sustainability → framework/chains/esg-sustainability.md
- Productivity & Workflow → framework/chains/productivity-workflow.md

## Step 3: Extract BODM Evidence

From the case study, identify which Business Outcome-Driven Metrics (BODMs) are evidenced. For each BODM found:
- State the metric name (use canonical name from the chain file)
- Quote the evidence from the case study
- Note whether the value meets the benchmark target

## Step 4: Map TODM Capabilities

For each BODM evidenced, identify which Technology-Outcome Driven Metrics (TODMs) the case study claims or implies. Use the chain file's TODM table to check which TODMs enable each BODM.

## Step 5: Calculate Financial Impact (if data available)

If the case study includes financial figures:
- Estimate or confirm NOI impact
- Estimate or confirm IRR / equity multiple contribution
- State the holding period and portfolio context if known

## Output Format

### Framework Mapping

**Primary Value Lever:** [PVL name]
**Aggregated Business Outcome:** [ABO name]

**BODM Evidence:**
| Metric | Claimed Value | Meets Target | Evidence Quote |
|--------|--------------|--------------|----------------|

**TODM Capabilities:**
| Technology Metric | Status | Enables |
|-------------------|--------|---------|

**Financial Impact Summary:** [1–2 sentences]

**Evidence Quality:** Strong / Moderate / Weak — [brief rationale]
```

---

## Notes for Agent Builders

- Always use canonical metric names from the chain file or `metrics-registry.yaml` — do not paraphrase
- If a case study spans multiple PVLs, create separate mappings for each chain
- "Evidence Quality" reflects whether BODM values were independently measured vs. vendor-claimed
