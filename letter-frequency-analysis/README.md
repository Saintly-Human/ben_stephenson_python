# Letter Frequency Analysis

A Python command-line utility that analyzes the letter frequency in a given text file while ignoring numbers, punctuation, spaces, and character casing.

This tool is useful for basic cryptography tasks, such as frequency analysis attacks on simple substitution ciphers.

This project is a solution to Exercise 156 from *The Python Workbook* by Ben Stephenson.

## Features

- **Case-Insensitive Analysis**: Converts all characters to lowercase so `A` and `a` are counted together.
- **Noise Filtering**: Automatically ignores numbers, punctuation marks, whitespace, and special characters.
- **Percentage Breakdown**: Displays both the absolute count and the relative percentage for each letter.
- **Sorted Output**: Orders results by frequency from most common to least common.
- **Robust CLI Validation**: Ensures exactly one argument is passed and handles missing files gracefully.

## Requirements

- Python 3.10 or higher

## Usage

Run the script from your terminal by providing the path to the text file as a command-line argument:
    ```bash
    python main.py <path_to_file>
    ```

## Example

Given a text file sample.txt containing:
    ```plaintext
    Hello, World! 123
    ```

Execution:
    ```bash
    python main.py sample.txt
    ```

Output:
    ```plaintext
    Total letters found: 10
    
    Letter  Count       Percentage
    ------------------------------
    l       3           30.00%
    o       2           20.00%
    h       1           10.00%
    e       1           10.00%
    w       1           10.00%
    r       1           10.00%
    d       1           10.00%
    ```
