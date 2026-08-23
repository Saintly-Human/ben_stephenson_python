# ☣️ Chemical Element Name Speller (Recursive)

A Python program that determines whether words (specifically, names of chemical elements from the Periodic Table) can be spelled entirely using chemical element symbols (e.g., `Si` + `Li` + `C` + `O` + `N` = `Silicon`).

---

## Task Description

Write a recursive function that checks whether a given word can be constructed exclusively using a list of available chemical element symbols.

### Requirements

- **Inputs:** A target `word` and a list of valid chemical `symbols`.
- **Output:** Returns a string of formatted symbols if the word can be spelled, or an empty string `""` if impossible.
- **Case-Insensitive:** Matching should ignore character casing.
- **Execution:** Reads all 118 chemical elements from an external dataset (`elements.txt`[cite: 1]), checks each element name, and prints those that can be represented via chemical symbols (e.g., *Silver can be represented as SiLVEr*).

---

## How It Works

The function uses **backtracking via recursion**:

1. It inspects prefixes of length 1, 2, and 3 from the target word.
2. If a prefix matches any chemical symbol (case-insensitive), it recursively attempts to spell the remainder of the word.
3. If the entire word is successfully matched down to an empty string, the chain of matched symbols is concatenated and returned.

---

## Usage

1. Place `elements.txt` in the same directory as `main.py`.
2. Run the script:

```bash
python main.py
```

## 💡 **Sample Output**

```plaintext
Elements that can be spelled using chemical symbols:

Silicon can be represented as SiLiCON
Iron can be represented as IrON
Silver can be represented as SiLVEr
Cobalt can be represented as CoBaLt
...
```
