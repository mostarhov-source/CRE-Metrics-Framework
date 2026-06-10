# CRE Metrics Flashcard Deck

Physical A6 facilitation cards + A4 script. Run from inside the `flashcards/` directory.

## Requirements

Python 3.11+ with Homebrew (macOS). WeasyPrint requires system libraries (pango, gobject) that are only available via Homebrew Python — the macOS system Python will not work.

```bash
brew install python@3.13   # if not already installed
```

## Setup

```bash
cd flashcards
/opt/homebrew/bin/pip3.13 install -r requirements.txt
```

## Generate

```bash
/opt/homebrew/bin/python3.13 generate.py
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

Re-run `/opt/homebrew/bin/python3.13 generate.py`. All metric content is read directly from `../framework/metrics/`.
Only `content/` files need manual editing (orientation cards, facilitator card, facilitation script).
