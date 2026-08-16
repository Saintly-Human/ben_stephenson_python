# Recursive Subset Generator (Backtracking)

A Python implementation for generating all possible subsets (the power set) of a list using **recursive backtracking**. 

Unlike simple contiguous sublist slicing, this algorithm explores **all $2^N$ unique combinations** of elements regardless of whether they are adjacent, utilizing state restoration (`backtrack` / `pop`) to manage memory efficiently.

---

## 💡 How It Works

The algorithm builds a **decision tree** where each step chooses whether to include or exclude a specific element, diving deeper until all possibilities from that branch are explored.

### Key Concepts

1. **Decision & Recursion:** At index `i`, the algorithm appends `items[i]` to `current_combo` and recursively calls `backtrack(i + 1, ...)`.
2. **State Restoration (Backtracking):** After returning from a deeper recursive call, `current_combo.pop()` removes the last element. This restores the state so the loop can safely try the next branch without mutating other paths.
3. **Paused Iteration:** Each call stack frame maintains its own `for` loop state, resuming right where it left off after child calls return.

---

## 🚀 Code Implementation

```python
def get_all_subsets(numbers: list) -> list[list]:
    """
    Generates all unique subsets of a given list using recursive backtracking.
    """
    result = []

    def backtrack(start: int, current_combo: list):
        # Store a copy of the current valid combination
        if current_combo:
            result.append(list(current_combo))

        # Explore remaining elements
        for i in range(start, len(numbers)):
            # 1. Do: Make a choice
            current_combo.append(numbers[i])

            # 2. Recurse: Move to the next index
            backtrack(i + 1, current_combo)

            # 3. Undo: Backtrack state for the next loop iteration
            current_combo.pop()

    backtrack(0, [])
    return result


if __name__ == "__main__":
    data = [10, 20, 30]
    subsets = get_all_subsets(data)

    print(f"Input: {data}")
    print(f"Total Subsets Generated: {len(subsets)}\n")
    for combo in subsets:
        print(combo)
```

---

## 📊 **Example Output**

```text
For the input array [10, 20, 30], the algorithm produces all 7 non-empty subsets ($2^3 - 1$):
```

```plaintext
Input: [10, 20, 30]
Total Subsets Generated: 7

[10]
[10, 20]
[10, 20, 30]
[10, 30]
[20]
[20, 30]
[30]
```
