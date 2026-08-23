# 💱 Recursive Coin Change Combination Checker

A Python script that determines whether a specific target monetary amount can be formed using an **exact number of coins**.

Available coin denominations: **1, 5, 10, and 25 cents**.

---

## Task Description

Write a program that prompts the user for a target amount (in cents) and a specific coin count, then determines whether that amount can be made with that exact number of coins.

### Examples

- **$1.00 (100 cents):**
  - **4 coins:** Possible ($25 \times 4$)
  - **5 coins:** Impossible
  - **6 coins:** Possible ($25 \times 3 + 10 \times 2 + 5 \times 1$)
- **$1.25 (125 cents):**
  - **5 coins or 8 coins:** Possible
  - **4, 6, or 7 coins:** Impossible

### Constraint

The solution **must use recursion** without any iterative loops (`for`/`while`).

---

## Features

- **Pure Recursion:** Solves the combination problem recursively using the inclusion-exclusion principle for each coin denomination.
- **Zero-Loop Guarantee:** Contains no explicit loops (`for`, `while`).
- **Interactive Input:** Reads target values directly from standard input.

---

## Usage

Run the program via Python:

```bash
python main.py
```

---

## 💡 **Sample Output**

```plaintext
Enter target amount in cents (e.g., 100 for $1.00): 100
Enter target number of coins: 6
Yes, it is possible to make 100 cents with exactly 6 coins.
```

```plaintext
Enter target amount in cents (e.g., 100 for $1.00): 100
Enter target number of coins: 5
No, it is NOT possible to make 100 cents with exactly 5 coins.
```
