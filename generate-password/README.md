# Random Password Generator

A lightweight Python command-line utility that generates readable passwords by combining two words from a specified dictionary/wordlist file based on target length constraints.

## Features

- **Dynamic Word Matching:** Combines two capitalized words to form passwords ranging between 8 and 11 characters.
- **Robust Exception Handling:** Gracefully handles missing files, empty files, and I/O errors.
- **CLI Interface:** Accepts custom dictionary text files via command-line arguments.

## Requirements

- Python 3.10+ (compatible with Python 3.14+)

## Usage

1. Clone or download this repository.
2. Ensure you have a text file containing a list of words (one word per line).
3. Run the script from your terminal passing the path to your wordlist:

```bash
python main.py path/to/your/wordlist.txt
```

## Example Output

```plaintext
Your Generated Password: AppleCloud
```

## How It Works

1. Reads and sanitizes all words from the provided file.
2. Selects a target total password length between 8 and 11 characters.
3. Splits the length constraint into two sub-lengths (n1 and n2).
4. Filters the dictionary for candidate words matching n1 and n2.
5. Capitalizes and concatenates one random word from each candidate pool.

## Code Quality & Formatting

This project adheres to PEP 8 standards and is formatted using black and checked with flake8.
