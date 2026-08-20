# Add Line Numbers to File

A simple Python CLI tool that reads a source text file, prepends a line number to each line, and saves the output to a new file.

This project is a solution to Exercise 151 from *The Python Workbook* by Ben Stephenson.

## Features

- Reads the contents of any input file line by line.
- Formats each line as `lineNumber: originalContent`.
- Handles file operations safely with contextual managers (`with`).
- Includes error handling for missing files and I/O errors.

## Requirements

- Python 3.10 or higher

## Usage

Run the script from the command line, passing the paths to the source file and the output file as arguments:

```bash
python main.py <source_file> <target_file>
```

## Example

Suppose you have an input file input.txt with the following content:

```plaintext
First line
Second line
Third line
```

Run the command:

```bash
python main.py input.txt output.txt
```

The resulting output.txt will look like this:

```plaintext
1: First line
2: Second line
3: Third line
```
