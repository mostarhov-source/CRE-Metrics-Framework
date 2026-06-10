# Ryman Print Instructions — CRE Metrics Flashcard Deck

## Files to print

| File | Where to print | Notes |
|---|---|---|
| `output/flashcards-YYYY-MM-DD.pdf` | Ryman in-store or ryman.co.uk | 80 A6 cards, double-sided |
| `output/facilitation-script-YYYY-MM-DD.pdf` | Any printer (office or home) | A4, single-sided, black and white is fine |

---

## Ryman order settings — Flashcard deck

Hand this sheet to the Ryman print assistant, or use these settings on ryman.co.uk → Print Services → Document Printing.

| Setting | Value |
|---|---|
| **File** | `flashcards-YYYY-MM-DD.pdf` |
| **Paper size** | A6 (105 × 148 mm) |
| **Sides** | Double-sided (flip on short edge) |
| **Paper type** | Silk or gloss card |
| **Paper weight** | 350 gsm |
| **Finish** | Matt laminate (both sides) |
| **Colour** | Full colour |
| **Copies** | 1 set (adjust if printing for multiple facilitators) |

> **Why 350 gsm?** Cards need to be stiff enough to handle in a workshop without bending. 350 gsm silk card is the standard Ryman stock for business cards and postcards.

> **Why matt laminate?** Participants will write on the back of selected cards (Before AI / After AI / By when fields). Gloss laminate repels pen ink — matt accepts it.

---

## Facilitation script

Print `facilitation-script-YYYY-MM-DD.pdf` on standard A4 paper. Black and white is fine. The facilitator is the only person who reads this — no need for colour or card stock.

Suggested: print 2–3 copies so you have spares.

---

## Before you go to Ryman

1. Run the generator to produce today's dated PDFs:
   ```bash
   cd flashcards
   /opt/homebrew/bin/python3.13 generate.py
   ```
2. Open `output/flashcards-YYYY-MM-DD.pdf` and spot-check a few cards — verify chain colour stripes are visible, text is readable, Business Case block is on card backs.
3. Copy the PDF to a USB stick or upload to your email / cloud storage to transfer at the print counter.

---

## Recommended Ryman locations (Central London)

- **Ryman, Cheapside** — near Bank station, large print counter
- **Ryman, Holborn** — walk-in print service, usually same-day
- **Ryman, Victoria** — near mainline and coach if travelling from outside London

Any Ryman branch offers in-store print. For larger runs or guaranteed same-day, call ahead.

---

## Cost estimate

At current Ryman rates (2026):
- A6 double-sided colour card, matt laminate: ~£0.80–£1.20 per sheet
- 80 cards = ~£65–£95 per deck

For multiple decks (e.g. 3 facilitators), print in one order — per-unit cost drops.
