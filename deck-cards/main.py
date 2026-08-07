import random

def create_deck():
    ranks = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A')
    suits = ('s', 'h', 'd', 'c')
    deck = []

    for r in ranks:
        for s in suits:
            deck.append(f"{r}{s}")

    return deck

def shuffle(items):
    deck = list(items)

    for i in range(len(deck) - 1, 0, -1):
        j = random.randint(0, i)
        deck[i], deck[j] = deck[j], deck[i]

    return deck

def main():
    print("Card decks are being generated!!!")
    not_shf = create_deck()
    shf = shuffle(not_shf)

    print(f"Deck size: {len(not_shf)} cards")

    print("\n" + "=" * 50)
    print("ORIGINAL DECK:")
    print(not_shf)

    print("\n" + "=" * 50)
    print("Hand-shuffled deck:")
    print(shf)

if __name__ == "__main__":
    main()