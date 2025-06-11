# moxfield-deck-color-analyzer

**Analyze your Magic: The Gathering decks with ease!**

This tool counts how many lands and nonland cards of each color are in a Moxfield decklist.

## Features

- Counts lands that produce each color of mana
- Counts nonland cards by color identity
- Uses the Scryfall API for accurate card data
- Simple command-line interface
- No Python installation required!

## How to Use

1. **Download the executable:** Navigate to `DeckAnalyzer/dist/colorcounter.exe` in this repository and download it
2. **Export your deck from Moxfield:** 
   - On your deck page, look at the top left area above your card list
   - Click **"More"** → **"Export"** → **"Download for MTGO"**
   - This will download a `.txt` file to your computer
3. **Run the program:** Double-click `colorcounter.exe` 
4. **Enter the file path:** When prompted, enter the full path to your downloaded `.txt` file
5. **View results:** The analysis will display, then press Enter to close

*Note: Windows may show a security warning since the executable isn't signed. Click "More info" then "Run anyway" to proceed.*

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

## File Location

The executable can be found at: `DeckAnalyzer/dist/colorcounter.exe`

---

*Created for Magic: The Gathering deck analysis. Enjoy!*
