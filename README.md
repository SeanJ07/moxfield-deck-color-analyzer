# Moxfield Deck Color Analyzer

A small Python tool that breaks down the color distribution of any Magic: The Gathering deck exported from Moxfield. Useful for quickly seeing how your mana base is weighted and whether your nonland cards actually match what your lands can produce.

Pulls card data from the Scryfall API. No install required — there's a prebuilt Windows executable if you don't want to touch Python.

---

### How to Use

**Option A — Windows executable (no Python needed)**

1. Download `DeckAnalyzer/dist/colorcounter.exe` from this repo
2. Export your deck from Moxfield: deck page → **More** → **Export** → **Download for MTGO** — saves as a `.txt` file
3. Double-click `colorcounter.exe`, enter the path to your file when prompted

> Windows may flag the executable since it's unsigned. Click "More info" → "Run anyway" to proceed.

**Option B — Run the script directly**

```bash
cd DeckAnalyzer
python colorcounter.py
```

---

### Example Output
=== Land Mana Production ===
White :  12 / 24 lands  (50.0%)
Blue  :   8 / 24 lands  (33.3%)
Black :   0 / 24 lands   (0.0%)
Red   :   0 / 24 lands   (0.0%)
Green :   4 / 24 lands  (16.7%)
=== Nonland Card Color Identity ===
White :  45 / 76 nonlands  (59.2%)
Blue  :  28 / 76 nonlands  (36.8%)
Black :   0 / 76 nonlands   (0.0%)
Red   :   0 / 76 nonlands   (0.0%)
Green :   8 / 76 nonlands  (10.5%)

---

### Requirements (if running from source)

- Python 3.x
- `requests` library (`pip install requests`)
- Internet connection (for Scryfall API lookups)

---

*Built for personal use. Works well enough that I kept it.*
