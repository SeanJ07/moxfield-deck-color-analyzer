# moxfield-deck-color-analyzer

**Analyze your Magic: The Gathering decks with ease!**

This tool counts how many lands and nonland cards of each color are in a Moxfield decklist.

## Features

- Counts lands that produce each color of mana
- Counts nonland cards by color identity
- Uses the Scryfall API for accurate card data
- Simple command-line interface
- Available as standalone executable (no Python installation required!)

## Quick Start (Executable Version)

**Easiest way to use - no setup required!**

1. Download the latest executable from the [Releases](../../releases) page
2. Export your deck from [Moxfield](https://moxfield.com) as a `.txt` file
3. Run the executable and enter the path to your decklist when prompted
4. Press Enter to exit when you're done viewing the results

*Note: Windows may show a security warning since the executable isn't signed. Click "More info" then "Run anyway" to proceed.*

## Usage (Python Script)

If you prefer to run the Python script directly:

1. Export your deck from [Moxfield](https://moxfield.com) as a `.txt` file
2. Run the script in your terminal:
   ```bash
   python colorcounter.py
   ```
3. Enter the path to your decklist when prompted

## Example Output

```
=== Land Mana Production Analysis ===
White :  12 out of  24 lands (50.0%)
Blue  :   8 out of  24 lands (33.3%)
Black :   0 out of  24 lands (0.0%)
Red   :   0 out of  24 lands (0.0%)
Green :   4 out of  24 lands (16.7%)

=== Nonland Card Color Identity Analysis ===
White :  45 out of  76 nonlands (59.2%)
Blue  :  28 out of  76 nonlands (36.8%)
Black :   0 out of  76 nonlands (0.0%)
Red   :   0 out of  76 nonlands (0.0%)
Green :   8 out of  76 nonlands (10.5%)
```

## Requirements (Python Script Only)

- Python 3.x
- `requests` library (`pip install requests`)

## How to Export from Moxfield

1. Go to your deck on Moxfield
2. Click "Export" 
3. Select "Text" format
4. Save the file to your computer

---

*Created for Magic: The Gathering deck analysis. Enjoy!*
