import random

def create_deck ():
    ranks = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A')
    suits = ('s', 'h', 'd', 'c')
    return [f"{r}{s}" for r in ranks for s in suits]

def shuffle (items):
    deck = list(items)
    for i in range(len(deck) - 1, 0, -1):
        j = random.randint(0, i)
        deck[i], deck[j] = deck[j], deck[i]
    return deck

def deal (decks, folks=4, cards=5):
    hands = [[] for _ in range(folks)]
    for _ in range(cards):
        for hand in hands:
            if decks:
                hand.append(decks.pop(0))
    return hands

def main ():
    try:
        folks = int(input("How many folks are playing? (integer ONLY): "))
        cards = int(input("How many cards for each person? (integer ONLY): "))
        if folks <= 0 or cards <= 0:
            raise ValueError
    except ValueError:
        print('YOU DID SOMETHING WRONG !!! Please enter positive integers.')
        return

    decks = create_deck()
    shuffled_decks = shuffle(decks)

    if folks * cards > len(shuffled_decks):
        print(
            f'Not enough cards! Need {folks * cards}, but deck has'
            f' {len(shuffled_decks)}.'
        )
        return

    hands = deal (shuffled_decks, folks, cards)

    print('THE GAME IS STARTING !!!')
    print(f'{folks} players with {cards} cards per person')

    for i, hand in enumerate(hands, 1):
        print(f'{i} player has these cards:')
        print(f"{', '.join(hand)}\n")

    print(f"{len(shuffled_decks)} left in deck: {', '.join(shuffled_decks)}")

if __name__ == "__main__":
    main()