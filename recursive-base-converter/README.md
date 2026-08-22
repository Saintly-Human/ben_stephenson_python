# Recursive Decimal Base Converter

A lightweight Python script that converts non-negative decimal (base-10) integers into any target number system from **base 2 to base 16** using a recursive algorithm.

## Features

- **Base Range**: Converts numbers to bases $2$ through $16$ (utilizing standard digits `0-9` and letters `A-F`).
- **Recursive Logic**: Performs base conversion using functional recursive steps (`//` and `%` operations).
- **Input Validation**: Safely handles invalid inputs and raises descriptive errors for out-of-bounds bases or negative numbers.

## How It Works

The conversion uses positional notation base arithmetic. The program continuously divides the decimal integer $N$ by the chosen target base $B$:

1. The remainder $N \pmod B$ gives the current digit position (mapped to `0-9` or `A-F`).
2. The integer quotient $N \mathbin{/\!/} B$ is recursively passed back to the conversion function.
3. Base cases trigger when $N < B$.

## Requirements

- Python 3.x (no external dependencies required)

## Usage

1. **Clone the repository:**

```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name
```

1. **Run the script:**

```bash
python main.py
```

## Example interaction

```plaintext
Enter a non-negative integer: 255
Enter the base of the number system (from 2 to 16): 16
Result (16-ary system): FF
```

```plaintext
Enter a non-negative integer: 42
Enter the base of the number system (from 2 to 16): 2
Result (2-ary system): 101010
```
