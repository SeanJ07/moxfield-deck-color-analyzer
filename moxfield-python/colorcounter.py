# Project premise: Return the amounts of cards in a public moxfield deck from url in a sorted group
#pseudo steps
#1. get url from user
#2. get the amount of colors used in deck
#3. return values
#Goal: a program that uses Moxtrice, an api that turns a public deck list into readable data for python. the output is a returned amount of colors in a deck

import requests

COLOR_MAP = {
    "W": "White",
    "U": "Blue",
    "B": "Black",
    "R": "Red",
    "G": "Green"
}

def get_card_data(card_name):
    """Query Scryfall API for a card's color identity and type line."""
    url = f"https://api.scryfall.com/cards/named?exact={card_name}"
    response = requests.get(url)
    if response.status_code != 200:
        return [], ""
    data = response.json()
    return data.get("color_identity", []), data.get("type_line", "")

def count_colors_in_deck(filename):
    land_counts = {color: 0 for color in COLOR_MAP.values()}
    nonland_counts = {color: 0 for color in COLOR_MAP.values()}
    total_lands = 0
    total_nonlands = 0
    seen_cards = set()

    with open(filename, encoding="utf-8") as f:
        for line in f:
            if not line.strip() or line.startswith("//"):
                continue
            parts = line.strip().split(' ', 1)
            if len(parts) != 2:
                continue
            qty, card_name = parts
            if card_name in seen_cards:
                continue
            seen_cards.add(card_name)
            try:
                qty = int(qty)
            except ValueError:
                continue
            color_identity, type_line = get_card_data(card_name)
            is_land = "Land" in type_line

            if is_land:
                total_lands += qty
                for color in color_identity:
                    land_counts[COLOR_MAP.get(color, color)] += qty
            else:
                total_nonlands += qty
                for color in color_identity:
                    nonland_counts[COLOR_MAP.get(color, color)] += qty

    return land_counts, nonland_counts, total_lands, total_nonlands

def main():
    filename = input("Enter the path to your downloaded Moxfield .txt decklist: ")
    try:
        land_counts, nonland_counts, total_lands, total_nonlands = count_colors_in_deck(filename)
        for color in COLOR_MAP.values():
            print(f"{land_counts[color]} out of {total_lands} lands produce {color.lower()} mana")
        for color in COLOR_MAP.values():
            print(f"{nonland_counts[color]} out of {total_nonlands} non land cards are {color.lower()}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()