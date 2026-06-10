# Flashcard Facilitation Deck — Design Spec

**Date:** 2026-06-10  
**Status:** Approved  
**Purpose:** Physical A6 card deck + A4 facilitation script for ROI business case sessions on AI use cases in CRE.

---

## 1. Context and Purpose

The flashcard deck is a facilitation tool, not a learning tool. It is used in mixed rooms (business stakeholders + technical practitioners) to build a filled-in business case for a specific AI use case.

**Session inputs (physical artifacts from prior sessions):**
- AI Use Case document
- AI Contract document
- Data Required for the AI Use Case document

**Session output:**
- A stack of completed metric cards where each card has Before AI / After AI / By when filled in on the back — collectively forming the business case.

The facilitator owns the connective tissue between the three input artifacts and the metric cards. Cards stand alone; the facilitator guides the mapping.

---

## 2. Card Types

### Type 1 — Orientation Cards (4 cards)
One per hierarchy layer: PVL, ABO, BODM, TODM.

**Purpose:** Participants read these first (5 minutes) to build a shared mental model of the framework before touching metric cards.

**Front:**
- Layer number and name (large)
- Plain-language definition of what this layer represents
- Visual hierarchy indicator: e.g. `PVL → [ABO] → BODM → TODM`

**Back:**
- 3–5 example metrics at this layer
- One sentence on how to use this layer's cards in the session

**Content source:** `flashcards/content/orientation-cards.yaml` (static, hand-authored).

---

### Type 2 — Metric Cards (75 cards)
One per metric: 5 PVL + 5 ABO + 40 BODM + 25 TODM.

**Front:**
- Type badge (PVL / ABO / BODM / TODM)
- Chain colour stripe (top edge, one of 5 colours — see Section 4)
- Metric name (large)
- Hierarchy breadcrumb: e.g. `Revenue Growth → Optimised Portfolio Returns → NOI`
- One-sentence definition
- Why it matters (1–2 sentences)
- Classification badges: `metric_type` · `timing` · `measurement_cadence`

**Back:**
- Formula (if applicable)
- Target / benchmark
- Data sources
- Business case block (writable space):
  ```
  Before AI: _______________
  After AI:  _______________
  By when:   _______________
  ```

**Content source:** Auto-generated from `framework/metrics/{layer}/{id}.md` frontmatter and body. No manual authoring required for metric cards.

---

### Type 3 — Facilitator Prompt Card (1 card)
Single double-sided card held by the facilitator throughout the session. Not distributed to participants.

**Front — Session Flow:**
1. Share inputs — Use Case / Contract / Data artifacts
2. Orientation round — all participants read orientation cards (5 min)
3. Pre-select card subset by chain colour
4. Card by card: "Does this AI use this metric?"
5. Fill Before / After / By when on back of each selected card
6. Selected card stack = business case

**Back — Quick Reference:**
- Hierarchy map with plain-language layer descriptions
- 5 chain colours with names
- Common pitfalls (see Section 6)

**Content source:** `flashcards/content/facilitator-card.yaml` (static, hand-authored).

---

## 3. Facilitation Script

A separate A4 multi-page document for the facilitator. Authored as markdown, rendered to PDF alongside the card deck.

**File:** `flashcards/content/facilitation-script.md`

**Sections:**

| Section | Duration | Content |
|---|---|---|
| 1. Before the session | — | How to pre-select card subsets by value chain; how to review the three input artifacts |
| 2. Opening | 10 min | How to introduce the inputs to the room; framing the session goal |
| 3. Orientation round | 5 min | Walk through the 4 hierarchy cards; check shared understanding |
| 4. Card selection | 20 min | Questions to ask; how to handle debate; when to move on |
| 5. Business case fill-in | 15 min | Talking points for Before / After / By when fields |
| 6. Synthesis | 10 min | How to arrange selected cards into a value chain narrative |
| 7. Common pitfalls | — | Reference section (see Section 6 below) |

---

## 4. Colour System

Five chain colours, printed as a top-edge stripe on every metric card. Enables the facilitator to pull a relevant card subset before the session, reducing 75 cards to a manageable working set.

| Chain | Colour |
|---|---|
| Revenue Growth | Deep blue |
| Cost Savings | Green |
| Risk Reduction | Amber |
| ESG / Sustainability | Teal |
| Productivity / Workflow | Purple |

Metrics that belong to multiple chains carry the primary chain colour (first chain listed in frontmatter).

---

## 5. Physical Specifications

| Item | Spec |
|---|---|
| Card size | A6 (105 × 148 mm) |
| Sides | Double-sided (front + back) |
| Total cards | 80 (4 orientation + 75 metric + 1 facilitator) |
| Script | A4, multi-page, single-sided |
| Print target | Ryman UK (or equivalent print centre) |
| File format | PDF/X-1a or standard PDF |

**Ryman guidance:** Upload `output/flashcards-YYYY-MM-DD.pdf` as the card file. Print `output/facilitation-script-YYYY-MM-DD.pdf` separately on A4.

---

## 6. Common Facilitation Pitfalls

These are included in both the facilitator card (abbreviated) and the facilitation script (full):

- **Group picks only TODM cards** — redirect: "That tells us the tech works, but what business outcome does it produce?" Pull up the parent BODM card.
- **Before AI field left blank** — without a baseline, the business case has no ROI. Push for an estimate: "What's the current cost / rate / frequency?"
- **All metrics selected** — a business case with 20 metrics has none. Cap selection at 5–7 per use case.
- **Contract cost not mapped to any metric** — check if there's a `proptech-investment-roi` or `wacc` card on the table. If the contract cost can't be offset by a selected metric, flag it.
- **Data Required artifact reveals a gap** — if the AI use case needs data the organisation doesn't have, note it on the card back rather than discarding the card. It becomes a data roadmap item.

---

## 7. Generation Pipeline

**Approach:** Python script → HTML/CSS → WeasyPrint → PDF.

```
flashcards/
  README.md                         ← print instructions, regeneration command
  generate.py                       ← entry point
  requirements.txt                  ← weasyprint, jinja2, python-frontmatter
  │
  templates/
    card-metric.html                ← A6 metric card (front + back)
    card-orientation.html           ← A6 orientation card (front + back)
    card-facilitator.html           ← A6 facilitator card (front + back)
    facilitation-script.html        ← A4 multi-page script template
    styles.css                      ← A6/A4 print dimensions, chain colour vars
  │
  content/
    orientation-cards.yaml          ← static copy for 4 orientation cards
    facilitator-card.yaml           ← static copy for facilitator prompt card
    facilitation-script.md          ← full facilitation script (markdown)
  │
  output/                           ← gitignored
    flashcards-YYYY-MM-DD.pdf
    facilitation-script-YYYY-MM-DD.pdf
```

**Data flow:**
- `generate.py` reads all `framework/metrics/{layer}/*.md` files via `python-frontmatter`
- Renders each metric through `card-metric.html` Jinja2 template
- Renders orientation and facilitator cards from YAML content files
- Renders facilitation script from `facilitation-script.md`
- Outputs two PDFs to `output/`

**Command:**
```bash
cd flashcards && pip install -r requirements.txt && python generate.py
```

---

## 8. What Is Not In Scope

- Digital / Miro version (future consideration)
- Editing metric content via the card deck — all content changes go to `framework/metrics/`
- Localisation / translation
- Interactive or fillable PDF (participants write on physical cards)
