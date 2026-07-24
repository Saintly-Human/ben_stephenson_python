# Secure Password Generator

A lightweight and secure Python script designed to generate random, cryptographically strong passwords. 

Unlike standard implementations that rely on pseudo-random number generators, this project uses Python's built-in `secrets` module to ensure higher security suitable for real-world usage.

## 🌟 Features

* **Cryptographically Secure:** Uses Python's `secrets` module instead of `random` to prevent predictability.
* **Flexible Character Set:** Includes uppercase letters, lowercase letters, digits, and special characters (`string.punctuation`).
* **Variable Length:** Generates passwords with a randomized length between 7 and 10 characters.
* **Zero Dependencies:** Built entirely with standard Python libraries (`secrets`, `string`).

## 🛠️ Prerequisites

* **Python 3.6+** (no external packages required)

## 🚀 How to Run

1. **Clone the repository & navigate to this exercise:**
```bash
git clone https://github.com/Saintly_Human/ben_stephenson_python.git
cd ben_stephenson_python/secure-password-generator
```

2. **Run the script:**
```bash
python main.py
```

## 💡 **Example Output:**
```plaintext
Your password: k9#P!x2L
```
