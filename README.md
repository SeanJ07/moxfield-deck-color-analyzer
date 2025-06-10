# moxfield-deck-color-analyzer

**Analyze your Magic: The Gathering decks with ease!**  
This tool counts how many lands and nonland cards of each color are in a Moxfield decklist.

---

## Features

- Counts lands that produce each color of mana
- Counts nonland cards by color identity
- Uses the Scryfall API for accurate card data
- Simple command-line interface

---

## Usage

1. **Export your deck** from [Moxfield](https://www.moxfield.com/) as a `.txt` file.
2. **Run the script** in your terminal:
   ```
   python colorcounter.py
   ```
3. **Enter the path** to your decklist when prompted.

---

## Example Output

```
71 out of 241 lands produce white mana
142 out of 548 non land cards are white
```

---

## Requirements

- Python 3.x
- `requests` library (`pip install requests`)

---

*Created for Magic: The Gathering deck analysis. Enjoy!*
