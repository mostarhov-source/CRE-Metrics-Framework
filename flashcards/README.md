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
