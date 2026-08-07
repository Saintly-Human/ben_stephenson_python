# 🃏 Card Deck Generator & Manual Shuffler (Python)

A Python program that generates a standard 52-card deck and shuffles it manually using the **Fisher–Yates (Knuth) Shuffle algorithm** without relying on built-in shuffling methods like `random.shuffle()`.

---

## 📌 Features

- **Deck Generation:** Combines 13 ranks and 4 suits to construct a standard 52-card deck.
- **Manual Shuffling:** Implements the Fisher–Yates algorithm for uniform, unbiased $O(N)$ random permutation.
- **Immutability Protection:** Creates a shallow copy of the list before shuffling to keep the original deck intact.

---

## 🛠️ How It Works

### 1. `create_deck()`

Generates 52 unique card strings by pairing every rank (`2–10`, `J`, `Q`, `K`, `A`) with every suit:

- `s` — Spades (♠️)
- `h` — Hearts (♥️)
- `d` — Diamonds (♦️)
- `c` — Clubs (♣️)

### 2. `shuffle(items)`

Performs an in-place-style manual shuffle on a copy of the deck:

1. Iterates backwards from the last element (index `51`) down to index `1`.
2. Picks a random index `j` between `0` and the current index `i`.
3. Swaps the elements at indices `i` and `j`.

---

## 🖥️ **Example Output:**

```plaintext
Card decks are being generated!!!
Deck size: 52 cards

==================================================
ORIGINAL DECK:
['2s', '2h', '2d', '2c', '3s', '3h', '3d', '3c', '4s', '4h', '4d', '4c', '5s', '5h', '5d', '5c', '6s', '6h', '6d', '6c', '7s', '7h', '7d', '7c', '8s', '8h', '8d', '8c', '9s', '9h', '9d', '9c', '10s', '10h', '10d', '10c', 'Js', 'Jh', 'Jd', 'Jc', 'Qs', 'Qh', 'Qd', 'Qc', 'Ks', 'Kh', 'Kd', 'Kc', 'As', 'Ah', 'Ad', 'Ac']

==================================================
Hand-shuffled deck:
['7d', 'Kh', '2s', 'Jc', '10s', '4c', 'Ah', '8d', 'Qc', '3h', '9s', '5d', '2c', 'Ks', '6h', '4s', 'Ac', 'Jh', '7s', '10c', '9d', '3s', '5c', '8s', 'Qd', '2d', '6c', '8c', '10d', 'As', '4d', '5s', 'Jd', '9c', 'Kc', '3d', '7c', '2h', '8h', '6s', '4h', 'Qh', 'Kd', '10h', '3c', 'Js', '7h', '5h', 'Ad', '9h', 'Qs', '6d']
```
