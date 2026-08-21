# Paragraph Text Formatter

A Python script that reads a text file and formats it to a fixed maximum line length while preserving paragraph structures.

## Overview

When working with terminal outputs or text display systems, line lengths often vary. Long lines get wrapped awkwardly mid-sentence, while short lines leave empty, underutilized space.

This tool solves that issue by:

- Normalizing line lengths to a fixed target width (default: `50` characters).
- Intelligently moving words across lines (greedy packing algorithm).
- Preserving natural paragraph boundaries (identified by blank lines).

---

## Example

### Input Text (`alice.txt`)

```text
Alice was
beginning to get very tired of sitting by her
sister
on the bank, and of having nothing to do: once
or twice she had peeped into the book her sister
was reading, but it had
no
pictures or conversations in it, "and what is
the use of a book," thought Alice, "without
pictures or conversations?"
```

---

## How It Works

1. Paragraph Segmentation: Splits raw text on double newlines (\n\n) to isolate distinct paragraphs.
2. Word Extraction: Cleans whitespace and extracts raw words per paragraph.
3. Greedy Line Packing: Continuously appends words into the current buffer until adding another would exceed the specified line width.
4. Reassembly: Joins lines with single newlines and paragraphs with double newlines.

---

## Running the Script

Pass the path to your target text file as a command-line argument:

```bash
python main.py path/to/your/file.txt
```

If no path is provided, it defaults to looking for alice.txt in the current working directory.
