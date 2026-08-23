# Chemical Element Chain Game (Longest Path Recursion)

A Python implementation of the word-chain game using chemical elements from the Periodic Table. Starting from a user-provided element, the program recursively computes the **maximum possible sequence** where each subsequent element starts with the last letter of the previous one without repeating elements.

---

## 📜 Task Description

In this game, players align chemical elements into a chain such that each element begins with the letter that the previous element ends with (e.g., `Hydrogen` $\rightarrow$ `Nickel` $\rightarrow$ `Lithium`). Elements cannot be reused.

### Requirements

- **Input:** A starting element provided by the user.
- **Goal:** Find the **longest possible** sequence using recursion (backtracking).
- **Validation:** Displays an error message if the user enters a non-existent chemical element.
- **Dataset:** Imports elements from an external `elements.txt` file[cite: 1].

---

## Algorithm Explanation

The program uses **exhaustive recursive backtracking** to explore all valid continuation paths:

1. Identifies all candidate elements starting with the current element's last character.
2. For every candidate, it recursively generates a sub-chain using the remaining unvisited elements.
3. Compares sub-chain lengths and selects the **longest** option at each decision level.

---

## ⚙️ Usage

1. Place `elements.txt` in the same directory[cite: 1].
2. Run the program:

```bash
python main.py
```

## 💡 Example Usage

```plaintext
=== Chemical Element Word Game ===
Please enter starting element: Hydrogen

Max chain length (9 elements) starting with Hydrogen:
1. Hydrogen
2. Nickel
3. Lithium
4. Magnesium
5. Mercury
6. Ytterbium
7. Bismuth
8. Hafnium
9. Manganese
```

```plaintext
=== Chemical Element Word Game ===
Please enter starting element: Unobtanium

Error: Element 'Unobtanium' is NOT valid or not in database.
```
