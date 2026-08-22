# 💲 NATO Phonetic Alphabet Converter

A Python script that converts an input word or text into its corresponding **NATO Phonetic Alphabet** representation using a **recursive approach** (without iterative loops).

---

## Task Description

A phonetic alphabet assigns a distinct word to each letter to ensure clear voice communication, especially over noisy transmission channels (e.g., military or aviation radio). One of the most widely used phonetic alphabets was created by NATO.

### Problem Statement

Write a program that takes a word from the user and displays it on the screen converted into the corresponding phonetic word sequence.

- **Example:** Entering `Hello` should output `Hotel Echo Lima Lima Oscar`.
- **Constraint:** The solution **must use recursion** instead of iterative loops (`for`/`while`).
- **Non-alphabetic characters:** Non-alphabetic characters or symbols absent from the standard dictionary are preserved or skipped cleanly.

---

## Features

- **Recursive Processing:** Implements string decomposition recursively without loops.
- **Case Insensitive:** Automatically handles lowercase and uppercase input.
- **Safe Lookup:** Handles special characters gracefully without breaking or throwing key errors.
- **CLI Ready:** Command-line argument handling via `sys.argv`.

---

## Usage

Run the script from the terminal by passing a word as a command-line argument:

```bash
python main.py <your_word>
```

## Example Output

```bash
$ python main.py Hello
Hotel Echo Lima Lima Oscar

$ python main.py Code
Charlie Oscar Delta Echo
```
