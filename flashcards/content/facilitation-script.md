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
