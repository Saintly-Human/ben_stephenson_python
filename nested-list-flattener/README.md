# Recursive Nested List Flattener in Python

A Python program that flattens deeply nested list structures of arbitrary depth into a single flat list (e.g., `[1, [2, 3], [4, [5, [6, 7]]]]` $\rightarrow$ `[1, 2, 3, 4, 5, 6, 7]`).

This repository explores multiple implementations of list flattening: a pure recursive slicing approach, an optimized memory-efficient generator using `yield from`, and an iterative stack-based solution.

---

## 📌 Problem Description

Write a program that takes a multi-level nested list containing integers and sublists, and returns a new 1D list containing all individual values in their original order.

### Example

- **Input:** `[1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]`
- **Output:** `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`

---

## 💻 Implementations

### 1. Classical Recursive Slicing (Educational)

Uses head-tail recursion (`data[0]` and `data[1:]`) to evaluate elements sequentially.

```python
def flatten_recursive(data):
    if not data:
        return []
    if isinstance(data[0], list):
        return flatten_recursive(data[0]) + flatten_recursive(data[1:])
    return [data[0]] + flatten_recursive(data[1:])
```

- **Pros:** Demonstrates fundamental functional recursion principles.
- **Cons:** Slicing (data[1:]) creates temporary copies in memory on each call, leading to $O(N^2)$ time complexity for large lists.

### 2. Generator with yield from (Pythonic & Optimized)

Uses Python generators and lazy evaluation to extract elements without intermediate memory allocation.

```python
def flatten_generator(data):
    for item in data:
        if isinstance(item, list):
            yield from flatten_generator(item)
        else:
            yield item
```

- **Pros:** Highly memory-efficient ($O(N)$ time complexity), clean syntax, no list copying.
- **Cons:** Limited by Python's default recursion depth limit (~1000 calls).

### 3. Iterative Stack Approach (Production-Ready)

Uses an explicit stack to handle arbitrarily deep nesting without stack overflow risks.

```python
def flatten_iterative(data):
    result = []
    stack = [data]
    while stack:
        curr = stack.pop()
        if isinstance(curr, list):
            stack.extend(reversed(curr))
        else:
            result.append(curr)
    return result
```

---

## 🛠️ Usage

**Clone the repository and run main.py:**

```bash
git clone https://github.com/Saintly_Human/ben_stephenson_python.git
cd ben_stephenson_python/nested-list-flattener
```

---

## 💡 **Sample Output**

```plaintext
Input:  [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
