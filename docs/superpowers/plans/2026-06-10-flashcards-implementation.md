# Flashcard Facilitation Deck — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a Python generation pipeline that reads `framework/metrics/` and outputs two print-ready PDFs — 80 A6 flashcards and an A4 facilitation script — ready to upload to Ryman UK.

**Architecture:** `generate.py` (run from inside `flashcards/`) reads all metric markdown files via `python-frontmatter`, builds an in-memory registry, resolves breadcrumbs and chain colours, renders Jinja2 HTML templates, and uses WeasyPrint to produce two dated PDFs in `flashcards/output/`. Static card content (orientation cards, facilitator card, facilitation script) is authored in `flashcards/content/` and read at generation time.

**Tech Stack:** Python 3.11+, python-frontmatter, Jinja2, WeasyPrint, PyYAML, Markdown, pytest.

---

## File Map

| File | Responsibility |
|---|---|
| `flashcards/generate.py` | Entry point; orchestrates load → render → PDF |
| `flashcards/requirements.txt` | Pinned dependencies |
| `flashcards/README.md` | How to generate, how to print at Ryman |
| `flashcards/templates/styles.css` | A6/A4 print dimensions, chain colour vars, typography |
| `flashcards/templates/card-metric.html` | A6 metric card — front + back (2 pages per card) |
| `flashcards/templates/card-orientation.html` | A6 orientation card — front + back |
| `flashcards/templates/card-facilitator.html` | A6 facilitator prompt card — front + back |
| `flashcards/templates/facilitation-script.html` | A4 multi-page facilitation script wrapper |
| `flashcards/content/orientation-cards.yaml` | Static copy for 4 orientation cards |
| `flashcards/content/facilitator-card.yaml` | Static copy for facilitator prompt card |
| `flashcards/content/facilitation-script.md` | Full facilitation script (markdown) |
| `flashcards/tests/test_parser.py` | Unit tests for metric loading and parsing functions |

---

## Task 1: Project scaffold

**Files:**
- Create: `flashcards/requirements.txt`
- Create: `flashcards/README.md`
- Create: `flashcards/tests/__init__.py`
- Modify: `.gitignore`

- [ ] **Step 1: Create the directory structure**

```bash
mkdir -p flashcards/templates flashcards/content flashcards/output flashcards/tests
touch flashcards/tests/__init__.py
```

- [ ] **Step 2: Create `flashcards/requirements.txt`**

```
weasyprint==62.3
jinja2==3.1.4
python-frontmatter==1.1.0
pyyaml==6.0.2
markdown==3.6
pytest==8.2.2
```

- [ ] **Step 3: Create `flashcards/README.md`**

```markdown
# CRE Metrics Flashcard Deck

Physical A6 facilitation cards + A4 script. Run from inside the `flashcards/` directory.

## Setup

```bash
cd flashcards
pip install -r requirements.txt
```

## Generate

```bash
python generate.py
```

Outputs to `output/`:
- `flashcards-YYYY-MM-DD.pdf` — 80 A6 cards, double-sided. Upload to Ryman UK.
- `facilitation-script-YYYY-MM-DD.pdf` — A4 multi-page. Print yourself.

## Ryman UK print spec

- Paper: 350gsm silk or gloss card
- Size: A6 (105 × 148mm)
- Finish: Matt laminate (recommended)
- Sides: Double-sided
- File: `output/flashcards-YYYY-MM-DD.pdf`

## Regenerating after metric changes

Re-run `python generate.py`. All metric content is read directly from `../framework/metrics/`.
Only `content/` files need manual editing (orientation cards, facilitator card, facilitation script).
```

- [ ] **Step 4: Add `flashcards/output/` to `.gitignore`**

Open `.gitignore` at the repo root and append:

```
flashcards/output/
```

- [ ] **Step 5: Commit**

```bash
git add flashcards/ .gitignore
git commit -m "feat: scaffold flashcards directory structure"
```

---

## Task 2: Content files — orientation cards and facilitator card

**Files:**
- Create: `flashcards/content/orientation-cards.yaml`
- Create: `flashcards/content/facilitator-card.yaml`

- [ ] **Step 1: Create `flashcards/content/orientation-cards.yaml`**

```yaml
cards:
  - layer_number: 1
    layer_name: PVL
    layer_full_name: Primary Value Levers
    position_indicator: "[PVL] → ABO → BODM → TODM"
    definition: "The strategic reasons your organisation invests in AI and PropTech — the big 'why'."
    examples:
      - Revenue Growth
      - Cost Savings
      - Risk Reduction
      - ESG / Sustainability
      - Productivity / Workflow
    session_guidance: "Start here when framing the AI use case — which lever does this investment pull?"

  - layer_number: 2
    layer_name: ABO
    layer_full_name: Aggregated Business Outcomes
    position_indicator: "PVL → [ABO] → BODM → TODM"
    definition: "The business results your AI investment produces — what changes for the organisation."
    examples:
      - Optimised Portfolio Returns
      - Tenant Satisfaction & Retention
      - Operational Efficiency & Sustainability
      - Streamlined Decision-Making
      - Reduced Risk & Compliance
    session_guidance: "Use ABO cards to anchor the business case at outcome level — these are what you report to leadership."

  - layer_number: 3
    layer_name: BODM
    layer_full_name: Business Outcome-Driven Metrics
    position_indicator: "PVL → ABO → [BODM] → TODM"
    definition: "The measurable indicators that prove a business outcome is being achieved — what you track monthly or quarterly."
    examples:
      - Net Operating Income (NOI)
      - Tenant Retention Rate
      - Carbon Emissions Reduction
      - IRR
      - Fault Detection Rate
    session_guidance: "BODM cards are where the business case numbers live — fill in Before / After / By when on the back."

  - layer_number: 4
    layer_name: TODM
    layer_full_name: Technology Outcome-Driven Metrics
    position_indicator: "PVL → ABO → BODM → [TODM]"
    definition: "The technology-level proof points that show the AI system is working as intended — what the tech team tracks."
    examples:
      - PropTech Investment ROI
      - Digital Twin Fidelity
      - IoT Sensor Health & Data Quality
      - Technology Adoption Rate
      - AI Cost Estimate Accuracy
    session_guidance: "TODM cards support the business case — they prove the AI is functioning, but they don't replace BODM as the primary evidence."
```

- [ ] **Step 2: Create `flashcards/content/facilitator-card.yaml`**

```yaml
front:
  title: FACILITATION GUIDE
  steps:
    - "1. Share inputs — Use Case / Contract / Data artifacts on the table"
    - "2. Orientation round — all participants read orientation cards (5 min)"
    - "3. Pull chain subset — pre-select by colour stripe before the session"
    - "4. Card by card: 'Does this AI move this metric?'"
    - "5. Fill Before / After / By when on the back of each selected card"
    - "6. Selected card stack = the business case"

back:
  hierarchy:
    - layer: "PVL (5)"
      description: "Why we invest"
    - layer: "ABO (5)"
      description: "Business result"
    - layer: "BODM (40)"
      description: "Measurable outcome"
    - layer: "TODM (25)"
      description: "Tech proof point"
  chains:
    - name: "Revenue Growth"
      colour: "deep blue"
    - name: "Cost Savings"
      colour: "green"
    - name: "Risk Reduction"
      colour: "amber"
    - name: "ESG / Sustainability"
      colour: "teal"
    - name: "Productivity"
      colour: "purple"
  pitfalls:
    - "Group picks only TODM — ask: 'What business outcome does this produce?'"
    - "Before AI blank — push: 'What's the current cost / rate / frequency?'"
    - "Too many cards — cap selection at 5–7 per use case"
    - "Contract cost unmapped — find proptech-investment-roi or wacc card"
    - "Data gap found — note on card back as a data roadmap item"
```

- [ ] **Step 3: Commit**

```bash
git add flashcards/content/orientation-cards.yaml flashcards/content/facilitator-card.yaml
git commit -m "feat: add orientation and facilitator card content"
```

---

## Task 3: Content file — facilitation script

**Files:**
- Create: `flashcards/content/facilitation-script.md`

- [ ] **Step 1: Create `flashcards/content/facilitation-script.md`**

```markdown
# CRE AI Use Case — ROI Business Case Facilitation Script

**Session duration:** ~60 minutes  
**Participants:** Mixed room — business stakeholders + technical practitioners  
**Inputs required:** AI Use Case document, AI Contract document, Data Required document (from prior sessions)  
**Output:** Completed metric card stack = filled-in business case

---

## Before the Session

**Pre-select a card subset by value chain.**  
Review the AI Use Case document and identify which of the 5 value chains the use case primarily serves:

| Chain | Colour stripe | When to select |
|---|---|---|
| Revenue Growth | Deep blue | Use case drives rent, occupancy, or returns |
| Cost Savings | Green | Use case reduces operating costs |
| Risk Reduction | Amber | Use case reduces compliance or operational risk |
| ESG / Sustainability | Teal | Use case reduces energy use or carbon |
| Productivity / Workflow | Purple | Use case automates or accelerates internal processes |

Pull the relevant chain(s) from the full deck. A typical session works with 15–25 cards, not all 75.

**Review the three input artifacts before the session:**
- AI Use Case: what does the AI do, and what is the expected behaviour change?
- AI Contract: what does it cost, what SLAs are committed, what data does the vendor require?
- Data Required: what data must exist for the AI to function — and do we have it?

Flag any data gaps before the session. They will surface during card selection.

---

## 1. Opening (10 minutes)

Place the three input artifacts face-up on the table where all participants can see them.

**Suggested opening script:**

> "Today we're going to build a business case for [AI Use Case name]. We're not evaluating the technology — we've already done that. Today's job is to agree on which business metrics this AI will move, by how much, and by when.
>
> We'll use these cards to do it. Each card is a metric our organisation already tracks — or should track. By the end of the session, the cards we select with numbers on the back are the business case."

**Frame the three inputs:**

> "These three documents are our anchors. The Use Case tells us what the AI does. The Contract tells us what it costs and what the vendor has committed. The Data document tells us what we need to have in place for it to work. We'll refer back to these as we go through the cards."

---

## 2. Orientation Round (5 minutes)

Hand out the 4 orientation cards (one per participant if ≤4 people, or place them on the table).

Ask participants to read their card and answer:
1. What layer is this?
2. What does it mean in plain language?
3. Which card type will we spend most time on today?

**Expected answer to question 3:** BODM cards — that's where the measurable business case numbers live.

If participants are confused about the difference between BODM and TODM, use this redirect:

> "BODM is what the business measures — NOI, retention rate, carbon reduction. TODM is what the tech team measures — uptime, data accuracy, model confidence. Both matter, but the business case is built on BODM."

---

## 3. Card Selection (20 minutes)

Work through the pre-selected card subset one card at a time.

**For each card, ask:**

> "Does this AI use case move this metric?"

**If yes:** Place card face-up in the Selected pile.  
**If no:** Place card face-down in the Reviewed pile.  
**If unsure:** Place card aside in a Parking pile — return to it after the main pass.

**Useful probes during selection:**

- "Is this metric currently tracked? Who owns it?"
- "If the AI works as described in the Use Case, which direction does this metric move?"
- "Is this something we'd report to leadership, or just something the tech team monitors?"
- "Does the Contract commit the vendor to any outcome related to this metric?"

**Managing debate:**  
If the group spends >3 minutes debating a single card, park it and move on. Return to parked cards at the end. A card that requires this much debate is often one where the AI's impact is indirect or uncertain — note that on the back.

---

## 4. Business Case Fill-In (15 minutes)

For each card in the Selected pile, work through the back of the card together.

**Before AI:**  
The current baseline value of this metric. Push for a number, not a description.

> "What is our NOI today? What was it last year? If we don't know, what's the best estimate?"

If the group genuinely doesn't have a baseline, write "Unknown — needs measurement" and flag it as a pre-condition for the AI deployment.

**After AI:**  
The expected value of this metric after the AI is deployed and performing as contracted.

> "If the AI does what the Use Case says, what does this number become? The Contract may have a committed improvement — check it."

Reference the AI Contract SLAs where relevant. If the contract doesn't commit to a metric outcome, note that as a risk.

**By when:**  
The timeframe for the After AI value to be realised.

> "Is this a 6-month result or a 3-year result? What does the Contract say about deployment timeline?"

---

## 5. Synthesis (10 minutes)

Arrange the selected cards on the table in hierarchy order: PVL at the top, then ABO, then BODM, then TODM.

Read the stack from top to bottom:

> "We're investing in [AI Use Case] because it serves our [PVL] lever. The business outcome we expect is [ABO]. We'll measure it through [BODM metrics]. The technology will demonstrate it's working via [TODM metrics]."

**Check the stack for coherence:**
- Does every BODM card connect upward to an ABO?
- Does every TODM card connect downward to a BODM?
- Is there a clear line from the AI Use Case → TODM → BODM → ABO → PVL?

If a card floats without a connection, either find its missing link or remove it from the stack.

**Photograph or scan the completed card stack.** This is the business case record from this session.

---

## 6. Common Pitfalls

**Group picks only TODM cards**  
Tech practitioners often default to technology metrics. Redirect:  
> "That tells us the AI is working — but what business outcome does it produce? Which BODM card does this TODM support?"

**Before AI field left blank**  
Without a baseline, the business case has no ROI. Push for an estimate rather than accepting "unknown":  
> "If we had to guess — what are we spending today on this problem? What's the rough order of magnitude?"

**All metrics selected**  
A business case with 20 metrics has none. If more than 7 cards are selected, ask:  
> "If you had to pick the 3 metrics you'd stake the investment decision on, which are they?"

**Contract cost not mapped to any metric**  
Check if there's a `proptech-investment-roi` or `wacc` card in the deck. If the contract cost can't be offset by a selected metric, it's a gap in the business case — flag it explicitly.

**Data Required artifact reveals a gap**  
If the AI use case needs data the organisation doesn't have, do not discard the card — note the gap on the card back:  
> "Data gap: [what's missing]. Required before deployment."  
This becomes a data roadmap item, not a reason to abandon the metric.
```

- [ ] **Step 2: Commit**

```bash
git add flashcards/content/facilitation-script.md
git commit -m "feat: add facilitation script content"
```

---

## Task 4: CSS — print layout and chain colours

**Files:**
- Create: `flashcards/templates/styles.css`

- [ ] **Step 1: Create `flashcards/templates/styles.css`**

```css
:root {
    --colour-revenue-growth: #1a3a6b;
    --colour-cost-savings: #2d7a3a;
    --colour-risk-reduction: #b85c00;
    --colour-esg-sustainability: #0a6b6b;
    --colour-productivity-workflow: #5a1a8a;
    --colour-default: #444444;
}

/* ── Card page (A6) ─────────────────────────────────── */

@page card {
    size: 105mm 148mm;
    margin: 0;
}

.card-page {
    page: card;
    page-break-after: always;
    width: 105mm;
    height: 148mm;
    box-sizing: border-box;
    padding: 0 6mm 6mm 6mm;
    display: flex;
    flex-direction: column;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 8pt;
    color: #222;
    overflow: hidden;
    position: relative;
}

/* ── Chain stripe ────────────────────────────────────── */

.chain-stripe {
    height: 7mm;
    width: 105mm;
    margin: 0 -6mm 4mm -6mm;
    flex-shrink: 0;
}

.chain-stripe.revenue-growth   { background: var(--colour-revenue-growth); }
.chain-stripe.cost-savings     { background: var(--colour-cost-savings); }
.chain-stripe.risk-reduction   { background: var(--colour-risk-reduction); }
.chain-stripe.esg-sustainability { background: var(--colour-esg-sustainability); }
.chain-stripe.productivity-workflow { background: var(--colour-productivity-workflow); }
.chain-stripe.default          { background: var(--colour-default); }
.chain-stripe.orientation      { background: #222222; }
.chain-stripe.facilitator      { background: #333333; }

/* ── Badges ──────────────────────────────────────────── */

.badge-row {
    display: flex;
    gap: 2mm;
    margin-bottom: 2mm;
    flex-wrap: wrap;
}

.badge {
    display: inline-block;
    padding: 0.5mm 2mm;
    border-radius: 1.5mm;
    font-size: 6pt;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 0.03em;
    background: #eee;
    color: #444;
    flex-shrink: 0;
}

.badge.pvl  { background: #dce8f5; color: var(--colour-revenue-growth); }
.badge.abo  { background: #dff0e3; color: var(--colour-cost-savings); }
.badge.bodm { background: #fdefd8; color: var(--colour-risk-reduction); }
.badge.todm { background: #d8f0f0; color: var(--colour-esg-sustainability); }

/* ── Metric card front ───────────────────────────────── */

.metric-name {
    font-size: 13pt;
    font-weight: bold;
    color: #111;
    margin: 0 0 1.5mm 0;
    line-height: 1.2;
}

.breadcrumb {
    font-size: 6pt;
    color: #888;
    margin-bottom: 3mm;
    line-height: 1.4;
}

.definition {
    font-size: 8pt;
    color: #333;
    margin-bottom: 2mm;
    line-height: 1.4;
}

.why-label {
    font-size: 6pt;
    font-weight: bold;
    text-transform: uppercase;
    color: #aaa;
    margin-bottom: 1mm;
}

.why-text {
    font-size: 7.5pt;
    color: #555;
    line-height: 1.4;
}

.classification-row {
    display: flex;
    gap: 2mm;
    margin-top: auto;
    padding-top: 2mm;
    flex-wrap: wrap;
}

/* ── Metric card back ────────────────────────────────── */

.back-section {
    margin-bottom: 3mm;
}

.section-label {
    font-size: 6pt;
    font-weight: bold;
    text-transform: uppercase;
    color: #aaa;
    margin-bottom: 1mm;
}

.formula-box {
    background: #f5f5f5;
    border-radius: 1.5mm;
    padding: 2mm 3mm;
    font-size: 7.5pt;
    color: #333;
    line-height: 1.4;
}

.target-text, .sources-text {
    font-size: 7.5pt;
    color: #444;
    line-height: 1.4;
}

.business-case-block {
    border: 0.75pt solid #bbb;
    border-radius: 2mm;
    padding: 2mm 3mm;
    margin-top: auto;
}

.business-case-title {
    font-size: 6.5pt;
    font-weight: bold;
    text-transform: uppercase;
    color: #888;
    margin-bottom: 2mm;
    letter-spacing: 0.05em;
}

.bc-field {
    display: flex;
    align-items: baseline;
    border-bottom: 0.5pt solid #ddd;
    padding: 2.5mm 0;
    font-size: 7.5pt;
    color: #555;
}

.bc-field:last-child {
    border-bottom: none;
}

.bc-label {
    flex-shrink: 0;
    width: 22mm;
    font-weight: bold;
    color: #333;
}

.bc-line {
    flex: 1;
    border-bottom: 0.5pt solid #ccc;
    height: 3mm;
}

/* ── Orientation card ────────────────────────────────── */

.orientation-layer-number {
    font-size: 7pt;
    font-weight: bold;
    color: #aaa;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 1mm;
}

.orientation-layer-name {
    font-size: 22pt;
    font-weight: bold;
    color: #111;
    margin-bottom: 0.5mm;
    line-height: 1;
}

.orientation-full-name {
    font-size: 9pt;
    color: #555;
    margin-bottom: 3mm;
}

.orientation-position {
    font-size: 7.5pt;
    color: #888;
    font-family: 'Courier New', monospace;
    margin-bottom: 4mm;
    letter-spacing: 0.02em;
}

.orientation-definition {
    font-size: 8.5pt;
    color: #333;
    line-height: 1.5;
    margin-bottom: auto;
}

.orientation-examples-label {
    font-size: 6pt;
    font-weight: bold;
    text-transform: uppercase;
    color: #aaa;
    margin-bottom: 1.5mm;
}

.orientation-examples {
    list-style: none;
    padding: 0;
    margin: 0 0 3mm 0;
}

.orientation-examples li {
    font-size: 7.5pt;
    color: #444;
    padding: 1mm 0;
    border-bottom: 0.5pt solid #eee;
}

.orientation-guidance {
    font-size: 7pt;
    color: #666;
    font-style: italic;
    line-height: 1.4;
    margin-top: auto;
    padding-top: 3mm;
    border-top: 0.5pt solid #ddd;
}

/* ── Facilitator card ────────────────────────────────── */

.fac-title {
    font-size: 9pt;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #333;
    margin-bottom: 4mm;
}

.fac-steps {
    list-style: none;
    padding: 0;
    margin: 0;
    flex: 1;
}

.fac-step {
    font-size: 8pt;
    color: #222;
    padding: 2.5mm 0;
    border-bottom: 0.5pt solid #eee;
    line-height: 1.4;
}

.fac-step:last-child {
    border-bottom: none;
}

.fac-hierarchy {
    margin-bottom: 4mm;
}

.fac-hier-row {
    display: flex;
    align-items: baseline;
    gap: 2mm;
    padding: 1.5mm 0;
    border-bottom: 0.5pt solid #eee;
    font-size: 7.5pt;
}

.fac-hier-layer {
    font-weight: bold;
    color: #222;
    width: 22mm;
    flex-shrink: 0;
}

.fac-hier-desc {
    color: #666;
}

.fac-chains-label, .fac-pitfalls-label {
    font-size: 6pt;
    font-weight: bold;
    text-transform: uppercase;
    color: #aaa;
    margin: 3mm 0 1.5mm 0;
}

.fac-chain-row {
    display: flex;
    align-items: center;
    gap: 2mm;
    font-size: 7pt;
    color: #444;
    margin-bottom: 1.5mm;
}

.fac-chain-swatch {
    width: 4mm;
    height: 4mm;
    border-radius: 1mm;
    flex-shrink: 0;
}

.fac-pitfall {
    font-size: 6.5pt;
    color: #555;
    padding: 1.5mm 0;
    border-bottom: 0.5pt solid #eee;
    line-height: 1.4;
}

.fac-pitfall:last-child {
    border-bottom: none;
}

/* ── Facilitation script (A4) ────────────────────────── */

@page script {
    size: A4;
    margin: 20mm 22mm;
}

.script-page {
    page: script;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 9.5pt;
    color: #222;
    line-height: 1.6;
}

.script-page h1 {
    font-size: 16pt;
    color: #111;
    margin-bottom: 2mm;
    border-bottom: 1.5pt solid #222;
    padding-bottom: 3mm;
}

.script-page h2 {
    font-size: 12pt;
    color: #222;
    margin-top: 8mm;
    margin-bottom: 3mm;
    padding-left: 3mm;
    border-left: 3pt solid #1a3a6b;
}

.script-page h3 {
    font-size: 10pt;
    color: #333;
    margin-top: 5mm;
    margin-bottom: 2mm;
}

.script-page p {
    margin-bottom: 3mm;
}

.script-page ul, .script-page ol {
    padding-left: 6mm;
    margin-bottom: 3mm;
}

.script-page li {
    margin-bottom: 1.5mm;
}

.script-page table {
    width: 100%;
    border-collapse: collapse;
    font-size: 8.5pt;
    margin-bottom: 4mm;
}

.script-page th {
    background: #f0f0f0;
    text-align: left;
    padding: 2mm 3mm;
    border: 0.5pt solid #ccc;
    font-weight: bold;
}

.script-page td {
    padding: 2mm 3mm;
    border: 0.5pt solid #ccc;
    vertical-align: top;
}

.script-page blockquote {
    background: #f8f8f8;
    border-left: 3pt solid #bbb;
    margin: 3mm 0;
    padding: 3mm 4mm;
    font-style: italic;
    color: #444;
}

.script-page hr {
    border: none;
    border-top: 0.5pt solid #ddd;
    margin: 6mm 0;
}

.script-page strong {
    color: #111;
}
```

- [ ] **Step 2: Commit**

```bash
git add flashcards/templates/styles.css
git commit -m "feat: add A6/A4 print CSS with chain colour system"
```

---

## Task 5: Metric card HTML template

**Files:**
- Create: `flashcards/templates/card-metric.html`

Each metric produces **two consecutive pages**: front then back. WeasyPrint pairs them for double-sided printing.

- [ ] **Step 1: Create `flashcards/templates/card-metric.html`**

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" href="styles.css">
</head>
<body>

{# ── FRONT ─────────────────────────────────────────── #}
<div class="card-page">
  <div class="chain-stripe {{ metric.chain_class }}"></div>

  <div class="badge-row">
    <span class="badge {{ metric.type | lower }}">{{ metric.type }}</span>
  </div>

  <h1 class="metric-name">{{ metric.name }}</h1>

  <p class="breadcrumb">{{ metric.breadcrumb }}</p>

  <p class="definition">{{ metric.definition }}</p>

  {% if metric.why_it_matters %}
  <p class="why-label">Why it matters</p>
  <p class="why-text">{{ metric.why_it_matters }}</p>
  {% endif %}

  <div class="classification-row">
    <span class="badge">{{ metric.metric_type }}</span>
    <span class="badge">{{ metric.timing }}</span>
    <span class="badge">{{ metric.measurement_cadence }}</span>
  </div>
</div>

{# ── BACK ──────────────────────────────────────────── #}
<div class="card-page">
  <div class="chain-stripe {{ metric.chain_class }}"></div>

  {% if metric.formula %}
  <div class="back-section">
    <p class="section-label">Formula</p>
    <div class="formula-box">{{ metric.formula }}</div>
  </div>
  {% endif %}

  {% if metric.target %}
  <div class="back-section">
    <p class="section-label">Target / Benchmark</p>
    <p class="target-text">{{ metric.target }}</p>
  </div>
  {% endif %}

  {% if metric.data_sources %}
  <div class="back-section">
    <p class="section-label">Data Sources</p>
    <p class="sources-text">{{ metric.data_sources | join(', ') }}</p>
  </div>
  {% endif %}

  <div class="business-case-block">
    <p class="business-case-title">Business Case</p>
    <div class="bc-field">
      <span class="bc-label">Before AI</span>
      <span class="bc-line"></span>
    </div>
    <div class="bc-field">
      <span class="bc-label">After AI</span>
      <span class="bc-line"></span>
    </div>
    <div class="bc-field">
      <span class="bc-label">By when</span>
      <span class="bc-line"></span>
    </div>
  </div>
</div>

</body>
</html>
```

- [ ] **Step 2: Commit**

```bash
git add flashcards/templates/card-metric.html
git commit -m "feat: add metric card HTML template (front + back)"
```

---

## Task 6: Orientation and facilitator card templates

**Files:**
- Create: `flashcards/templates/card-orientation.html`
- Create: `flashcards/templates/card-facilitator.html`

- [ ] **Step 1: Create `flashcards/templates/card-orientation.html`**

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" href="styles.css">
</head>
<body>

{# ── FRONT ─────────────────────────────────────────── #}
<div class="card-page">
  <div class="chain-stripe orientation"></div>

  <p class="orientation-layer-number">Layer {{ card.layer_number }} of 4</p>
  <h1 class="orientation-layer-name">{{ card.layer_name }}</h1>
  <p class="orientation-full-name">{{ card.layer_full_name }}</p>
  <p class="orientation-position">{{ card.position_indicator }}</p>
  <p class="orientation-definition">{{ card.definition }}</p>
</div>

{# ── BACK ──────────────────────────────────────────── #}
<div class="card-page">
  <div class="chain-stripe orientation"></div>

  <p class="orientation-examples-label">Examples at this layer</p>
  <ul class="orientation-examples">
    {% for example in card.examples %}
    <li>{{ example }}</li>
    {% endfor %}
  </ul>

  <p class="orientation-guidance">{{ card.session_guidance }}</p>
</div>

</body>
</html>
```

- [ ] **Step 2: Create `flashcards/templates/card-facilitator.html`**

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" href="styles.css">
</head>
<body>

{# ── FRONT — Session flow ──────────────────────────── #}
<div class="card-page">
  <div class="chain-stripe facilitator"></div>

  <p class="fac-title">{{ card.front.title }}</p>

  <ul class="fac-steps">
    {% for step in card.front.steps %}
    <li class="fac-step">{{ step }}</li>
    {% endfor %}
  </ul>
</div>

{# ── BACK — Quick reference ────────────────────────── #}
<div class="card-page">
  <div class="chain-stripe facilitator"></div>

  <div class="fac-hierarchy">
    {% for row in card.back.hierarchy %}
    <div class="fac-hier-row">
      <span class="fac-hier-layer">{{ row.layer }}</span>
      <span class="fac-hier-desc">{{ row.description }}</span>
    </div>
    {% endfor %}
  </div>

  <p class="fac-chains-label">Value chains</p>
  {% for chain in card.back.chains %}
  <div class="fac-chain-row">
    <span class="fac-chain-swatch" style="background: var(--colour-{{ chain.name | lower | replace(' ', '-') | replace('/', '-') | replace('&', '') | replace('--', '-') }}, #666);"></span>
    <span>{{ chain.name }}</span>
  </div>
  {% endfor %}

  <p class="fac-pitfalls-label">Common pitfalls</p>
  {% for pitfall in card.back.pitfalls %}
  <p class="fac-pitfall">{{ pitfall }}</p>
  {% endfor %}
</div>

</body>
</html>
```

- [ ] **Step 3: Commit**

```bash
git add flashcards/templates/card-orientation.html flashcards/templates/card-facilitator.html
git commit -m "feat: add orientation and facilitator card templates"
```

---

## Task 7: Facilitation script HTML template

**Files:**
- Create: `flashcards/templates/facilitation-script.html`

- [ ] **Step 1: Create `flashcards/templates/facilitation-script.html`**

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div class="script-page">
    {{ content }}
  </div>
</body>
</html>
```

- [ ] **Step 2: Commit**

```bash
git add flashcards/templates/facilitation-script.html
git commit -m "feat: add facilitation script A4 HTML template"
```

---

## Task 8: Unit tests for metric parser

**Files:**
- Create: `flashcards/tests/test_parser.py`

Tests cover the pure functions in `generate.py` before the module exists — write them failing first, then implement.

- [ ] **Step 1: Write failing tests in `flashcards/tests/test_parser.py`**

```python
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest
from generate import (
    extract_definition,
    extract_why_it_matters,
    build_breadcrumb,
    get_chain_class,
    CHAIN_DISPLAY,
)


# ── extract_definition ─────────────────────────────────

def test_extract_definition_single_line():
    body = "**Definition:** Income after operating expenses, before financing and taxes."
    assert extract_definition(body) == "Income after operating expenses, before financing and taxes."

def test_extract_definition_missing_returns_empty():
    body = "# Some Metric\n\nNo definition here."
    assert extract_definition(body) == ""

def test_extract_definition_ignores_other_bold_lines():
    body = "**Category:** Financial\n**Definition:** The real one.\n**Formula:** x + y"
    assert extract_definition(body) == "The real one."


# ── extract_why_it_matters ─────────────────────────────

def test_extract_why_single_line():
    body = "**Why It Matters:** Core driver of valuations and investor returns."
    assert extract_why_it_matters(body) == "Core driver of valuations and investor returns."

def test_extract_why_bullet_list():
    body = "**Why It Matters:**\n- Tenant renewals stabilise cash flow.\n- Strong satisfaction drives reputation."
    assert extract_why_it_matters(body) == "Tenant renewals stabilise cash flow."

def test_extract_why_missing_returns_empty():
    body = "**Definition:** Something.\n\nNo why here."
    assert extract_why_it_matters(body) == ""


# ── build_breadcrumb ───────────────────────────────────

MOCK_REGISTRY = {
    "revenue-growth": {
        "id": "revenue-growth",
        "name": "Revenue Growth",
        "layer": "pvl",
        "chains": ["revenue-growth"],
    },
    "optimised-portfolio-returns": {
        "id": "optimised-portfolio-returns",
        "name": "Optimised Portfolio Returns",
        "layer": "abo",
        "chains": ["revenue-growth"],
        "pvl": ["revenue-growth"],
    },
    "noi": {
        "id": "noi",
        "name": "Net Operating Income (NOI)",
        "layer": "bodm",
        "chains": ["revenue-growth", "cost-savings"],
        "parent_abo": "optimised-portfolio-returns",
    },
    "proptech-investment-roi": {
        "id": "proptech-investment-roi",
        "name": "PropTech Investment ROI",
        "layer": "todm",
        "chains": ["revenue-growth", "cost-savings"],
        "enables_bodm": ["noi"],
    },
}

def test_breadcrumb_pvl():
    metric = MOCK_REGISTRY["revenue-growth"]
    assert build_breadcrumb(metric, MOCK_REGISTRY) == "Revenue Growth"

def test_breadcrumb_abo():
    metric = MOCK_REGISTRY["optimised-portfolio-returns"]
    assert build_breadcrumb(metric, MOCK_REGISTRY) == "Revenue Growth → Optimised Portfolio Returns"

def test_breadcrumb_bodm():
    metric = MOCK_REGISTRY["noi"]
    result = build_breadcrumb(metric, MOCK_REGISTRY)
    assert result == "Revenue Growth → Optimised Portfolio Returns → Net Operating Income (NOI)"

def test_breadcrumb_todm_with_enables_bodm():
    metric = MOCK_REGISTRY["proptech-investment-roi"]
    result = build_breadcrumb(metric, MOCK_REGISTRY)
    assert result == "Revenue Growth → Net Operating Income (NOI) → PropTech Investment ROI"


# ── get_chain_class ────────────────────────────────────

def test_chain_class_known_chain():
    metric = {"chains": ["revenue-growth"]}
    assert get_chain_class(metric) == "revenue-growth"

def test_chain_class_multi_chain_returns_first():
    metric = {"chains": ["cost-savings", "revenue-growth"]}
    assert get_chain_class(metric) == "cost-savings"

def test_chain_class_no_chains_returns_default():
    metric = {"chains": []}
    assert get_chain_class(metric) == "default"
```

- [ ] **Step 2: Run tests — verify they all fail**

```bash
cd flashcards && python -m pytest tests/test_parser.py -v
```

Expected: `ImportError` or `ModuleNotFoundError` — `generate.py` does not exist yet.

---

## Task 9: `generate.py` — parser + renderer + main

**Files:**
- Create: `flashcards/generate.py`

- [ ] **Step 1: Create `flashcards/generate.py`**

```python
import os
import glob
from datetime import date

import frontmatter
import yaml
import markdown as markdown_lib
from jinja2 import Environment, FileSystemLoader
import weasyprint

# ── Constants ──────────────────────────────────────────

LAYER_ORDER = ["pvl", "abo", "bodm", "todm"]

CHAIN_DISPLAY = {
    "revenue-growth": "Revenue Growth",
    "cost-savings": "Cost Savings",
    "risk-reduction": "Risk Reduction",
    "esg-sustainability": "ESG / Sustainability",
    "productivity-workflow": "Productivity",
}

# ── Parser functions (pure, unit-tested) ───────────────

def extract_definition(body: str) -> str:
    for line in body.split("\n"):
        if line.startswith("**Definition:**"):
            return line.replace("**Definition:**", "").strip()
    return ""


def extract_why_it_matters(body: str) -> str:
    lines = body.split("\n")
    in_section = False
    for line in lines:
        if "**Why It Matters" in line:
            in_section = True
            rest = line.split("**Why It Matters")[-1]
            rest = rest.lstrip("*:").strip()
            if rest:
                return rest.lstrip("- ").strip()
            continue
        if in_section and line.strip():
            return line.strip().lstrip("- ").strip()
    return ""


def get_chain_class(metric: dict) -> str:
    chains = metric.get("chains", [])
    if chains:
        return chains[0]
    return "default"


def build_breadcrumb(metric: dict, registry: dict) -> str:
    layer = metric["layer"]
    chains = metric.get("chains", [])
    primary_chain = chains[0] if chains else ""
    chain_label = CHAIN_DISPLAY.get(primary_chain, primary_chain)
    name = metric["name"]

    if layer == "pvl":
        return name
    elif layer == "abo":
        return f"{chain_label} → {name}"
    elif layer == "bodm":
        parent_id = metric.get("parent_abo", "")
        parent = registry.get(parent_id, {})
        parent_name = parent.get("name", parent_id)
        return f"{chain_label} → {parent_name} → {name}"
    elif layer == "todm":
        enables = metric.get("enables_bodm", [])
        if enables:
            parent = registry.get(enables[0], {})
            parent_name = parent.get("name", enables[0])
            return f"{chain_label} → {parent_name} → {name}"
        return f"{chain_label} → {name}"
    return name


# ── Loader ─────────────────────────────────────────────

def load_metrics(metrics_root: str) -> dict:
    registry = {}
    for layer in LAYER_ORDER:
        pattern = os.path.join(metrics_root, layer, "*.md")
        for path in sorted(glob.glob(pattern)):
            post = frontmatter.load(path)
            meta = dict(post.metadata)
            meta["body"] = post.content
            meta["layer"] = layer
            meta["definition"] = extract_definition(post.content)
            meta["why_it_matters"] = extract_why_it_matters(post.content)
            registry[meta["id"]] = meta
    return registry


# ── Renderer ───────────────────────────────────────────

def render_cards(registry: dict, env: Environment) -> str:
    pages = []

    # Orientation cards
    with open("content/orientation-cards.yaml") as f:
        orientation_data = yaml.safe_load(f)
    tmpl = env.get_template("card-orientation.html")
    for card in orientation_data["cards"]:
        pages.append(tmpl.render(card=card))

    # Metric cards — sorted by layer then name
    metric_tmpl = env.get_template("card-metric.html")
    for layer in LAYER_ORDER:
        layer_metrics = [m for m in registry.values() if m["layer"] == layer]
        layer_metrics.sort(key=lambda m: m["name"])
        for metric in layer_metrics:
            metric["breadcrumb"] = build_breadcrumb(metric, registry)
            metric["chain_class"] = get_chain_class(metric)
            pages.append(metric_tmpl.render(metric=metric))

    # Facilitator card
    with open("content/facilitator-card.yaml") as f:
        facilitator_data = yaml.safe_load(f)
    fac_tmpl = env.get_template("card-facilitator.html")
    pages.append(fac_tmpl.render(card=facilitator_data))

    return "\n".join(pages)


def render_script(env: Environment) -> str:
    with open("content/facilitation-script.md") as f:
        script_md = f.read()
    script_html = markdown_lib.markdown(
        script_md,
        extensions=["tables", "fenced_code"]
    )
    tmpl = env.get_template("facilitation-script.html")
    return tmpl.render(content=script_html)


# ── Main ───────────────────────────────────────────────

def main():
    today = date.today().isoformat()
    os.makedirs("output", exist_ok=True)

    metrics_root = os.path.join("..", "framework", "metrics")
    registry = load_metrics(metrics_root)
    print(f"Loaded {len(registry)} metrics")

    env = Environment(loader=FileSystemLoader("templates"), comment_start_string="{#", comment_end_string="#}")

    # Cards PDF
    cards_html = render_cards(registry, env)
    weasyprint.HTML(string=cards_html, base_url=os.path.abspath("templates") + "/").write_pdf(
        f"output/flashcards-{today}.pdf"
    )
    print(f"✓ output/flashcards-{today}.pdf")

    # Script PDF
    script_html = render_script(env)
    weasyprint.HTML(string=script_html, base_url=os.path.abspath("templates") + "/").write_pdf(
        f"output/facilitation-script-{today}.pdf"
    )
    print(f"✓ output/facilitation-script-{today}.pdf")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run the unit tests — verify they all pass**

```bash
cd flashcards && python -m pytest tests/test_parser.py -v
```

Expected output:
```
tests/test_parser.py::test_extract_definition_single_line PASSED
tests/test_parser.py::test_extract_definition_missing_returns_empty PASSED
tests/test_parser.py::test_extract_definition_ignores_other_bold_lines PASSED
tests/test_parser.py::test_extract_why_single_line PASSED
tests/test_parser.py::test_extract_why_bullet_list PASSED
tests/test_parser.py::test_extract_why_missing_returns_empty PASSED
tests/test_parser.py::test_breadcrumb_pvl PASSED
tests/test_parser.py::test_breadcrumb_abo PASSED
tests/test_parser.py::test_breadcrumb_bodm PASSED
tests/test_parser.py::test_breadcrumb_todm_with_enables_bodm PASSED
tests/test_parser.py::test_chain_class_known_chain PASSED
tests/test_parser.py::test_chain_class_multi_chain_returns_first PASSED
tests/test_parser.py::test_chain_class_no_chains_returns_default PASSED

13 passed in 0.XXs
```

- [ ] **Step 3: Run the generator end-to-end**

```bash
cd flashcards && pip install -r requirements.txt && python generate.py
```

Expected output:
```
Loaded 75 metrics
✓ output/flashcards-2026-06-10.pdf
✓ output/facilitation-script-2026-06-10.pdf
```

- [ ] **Step 4: Open and visually inspect both PDFs**

Check:
- Cards PDF: first 8 pages = 4 orientation cards (front + back each); chain colour stripe visible; breadcrumb on metric card fronts; Business Case block on metric card backs
- Script PDF: A4 layout, all 6 sections present, tables rendered, blockquotes styled

- [ ] **Step 5: Commit**

```bash
git add flashcards/generate.py flashcards/tests/test_parser.py
git commit -m "feat: add generate.py with parser, renderer, and unit tests"
```

---

## Self-Review

**Spec coverage check:**

| Spec requirement | Task |
|---|---|
| 4 orientation cards, front + back | Task 2 (content), Task 6 (template) |
| 75 metric cards, front + back | Task 5 (template), Task 9 (renderer) |
| 1 facilitator prompt card | Task 2 (content), Task 6 (template) |
| Chain colour stripe on metric cards | Task 4 (CSS), Task 9 (`get_chain_class`) |
| Hierarchy breadcrumb on metric card front | Task 9 (`build_breadcrumb`) |
| Business case block (Before/After/By when) | Task 5 (template back) |
| Facilitation script as A4 PDF | Task 3 (content), Task 7 (template), Task 9 (renderer) |
| `flashcards/output/` gitignored | Task 1 |
| Run from `flashcards/` directory | Task 9 (main, relative paths) |
| All content auto-generated from `framework/metrics/` | Task 9 (`load_metrics`) |

**Placeholder scan:** No TBDs or incomplete steps. All code blocks are complete. ✓

**Type consistency:** `get_chain_class` returns a string CSS class name matching the stripe class names in `styles.css`. `build_breadcrumb` takes `metric: dict, registry: dict` consistently across tests and implementation. `render_cards` passes `metric["chain_class"]` to template which uses `{{ metric.chain_class }}`. ✓
