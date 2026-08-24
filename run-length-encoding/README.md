# Run-Length Encoding (RLE) Encoder and Decoder in Python

An efficient, memory-friendly recursive implementation of the **Run-Length Encoding (RLE)** data compression algorithm in Python. 

This repository contains both **encoding** (compression) and **decoding** (decompression) algorithms optimized with index-based recursion to avoid expensive list slicing operations.

---

## 📌 How It Works

**Run-Length Encoding (RLE)** is a simple form of data compression in which runs of data (sequences in which the same data element occurs in many consecutive data elements) are stored as a single data value and count.

* **Original Data:** `['A', 'A', 'A', 'B', 'B', 'A']`
* **Compressed (Encoded) Data:** `['A', 3, 'B', 2, 'A', 1]`

---

## 🛠️ Implementation Details

Traditional recursive solutions in Python often rely on list slicing (e.g., `data[2:]`), which copies the remaining slice of the array on every call, yielding $O(N^2)$ time complexity. 

This implementation uses **index-based recursion** (`index=0`), passing the reference to the original list without allocating new sub-lists:

1. **`decrypt(data, index=0)`**: Reads consecutive `[symbol, count]` pairs using index increments of `2` and expands them using Python list multiplication (`[symbol] * count`).
2. **`encrypt(data, index=0)`**: Scans for identical consecutive elements starting at `index`, counts the run length, and recursively jumps ahead by `index + count`.

---

## 💻 Code Overview

```python
def decrypt(data, index=0):
    if index >= len(data):
        return []
    return [data[index]] * data[index + 1] + decrypt(data, index + 2)


def encrypt(data, index=0):
    if index >= len(data):
        return []

    target = data[index]
    count = 0

    while index + count < len(data) and data[index + count] == target:
        count += 1

    return [target, count] + encrypt(data, index + count)
```

---

## 💡 **Sample Output**

```plaintext
Decoded output:
['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B']

Encoded output:
['A', 12, 'B', 4, 'A', 6, 'B', 1]
```
