# Sieve of Eratosthenes — Step-by-Step vs. Optimized Implementation

This repository contains two Python implementations of the classic **Sieve of Eratosthenes** algorithm for finding all prime numbers up to a given integer $N$. 

The goal of this project is to showcase both an **educational, step-by-step approach** that closely mirrors the literal mathematical instructions of the sieve, and a **highly optimized Pythonic approach** built for performance and efficiency.

---

## 📁 Files Overview

| File Name | Function Name | Approach & Key Features | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- | :--- |
| `sieve_step_by_step.py` | `simple_numbers(num)` | **Step-by-Step / Educational:** Explicitly zero-out non-primes, checks full list iterations, manual pointer incrementing. | $\mathcal{O}(N^2)$ (due to full list passes) | $\mathcal{O}(N)$ |
| `sieve_optimized.py` | `pure_sieve(n)` | **Optimized / Standard Sieve:** Boolean flag array, starts cross-outs at $p^2$, loop limit at $\sqrt{N}$, efficient slice stepping. | $\mathcal{O}(N \log \log N)$ | $\mathcal{O}(N)$ |

---

## 💡 Detailed Algorithm Comparison

### 1. `sieve_step_by_step.py` (Educational Approach)

This version prioritizes explicit tracking of the sieve process step-by-step:

* **List Representation:** Maintains a list of actual numbers `[0, 0, 2, 3, 4, ...]` where non-primes are zeroed out (`0`).
* **Outer Loop Condition:** Iterates while prime candidate `p < num`.
* **Cross-out Logic:** Iterates over the entire list to check modulo operations (`all_nums[i] % p == 0`), setting composites to `0`.
* **Pointer Movement:** Manually increments `p` and skips zeroed elements to find the next active prime candidate.

### 2. `sieve_optimized.py` (Production/Optimized Approach)

This version applies mathematical optimizations and efficient Python constructs:

* **Boolean Array (`is_prime`):** Uses a lean array of `True`/`False` flags indexed directly by integer value, reducing lookup and comparison overhead.
* **Early Termination ($\sqrt{N}$ Limit):** Stops the outer loop at `p * p <= n` because any composite number $\le N$ must have a prime factor $\le \sqrt{N}$.
* **Cross-out Optimization ($p^2$ Start):** Starts marking multiples from $p^2$ instead of $2p$, as smaller multiples ($2p, 3p, \dots$) have already been marked by smaller prime factors.
* **Step Slicing:** Uses Python's native `range(p * p, n + 1, p)` step iteration instead of scanning every index with conditional checks.

---

## 🚀 How to Run

1. Clone the repository & navigate to this exercise::

```bash
git clone https://github.com/Saintly_Human/ben_stephenson_python.git
cd ben_stephenson_python/sieve-of-eratosthenes
```

2. **Run the Step-by-Step version:**

   ```bash
   python sieve_step_by_step.py
   ```

3. **Run the Optimized version:**

    ```bash
    python sieve_optimized.py
    ```
