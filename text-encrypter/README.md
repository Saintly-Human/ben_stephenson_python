# Caesar Cipher (Bilingual)

A Python implementation of the classic **Caesar Cipher** algorithm supporting both **English** and **Russian** alphabets simultaneously.

---

## ✨ Highlights

- **Full Bilingual Support:** Works seamlessly with English (`a-z`, `A-Z`) and Russian (`а-я`, `А-Я`, including `ё`/`Ё`) text in the same string.
- **Encryption & Decryption:** Supports shifting in both directions using positive or negative values.
- **Formatting Preservation:** Retains original letter casing, whitespace, numbers, and special characters.
- **User-Friendly Interactive Interface:** Prompts for action type and handles input validation gracefully.

---

## 🚀 How to Run

1. **Clone the repository & navigate to this exercise:**

```bash
git clone https://github.com/Saintly_Human/ben_stephenson_python.git
cd ben_stephenson_python/text-encrypter
```

2. **Run the script:**

```bash
python main.py
```

---

## 💡 **Example Output:**

Encrypting Mixed Text

```plaintext
Select an action:
1 — Encrypt text
2 — Decrypt text
Your choice (1 or 2): 1
Enter a message: Hello, Мир! 2026
Enter the shift: 3

Encrypted text: Khoor, Плх! 2026
```

Decrypting Text

```plaintext
Select an action:
1 — Encrypt text
2 — Decrypt text
Your choice (1 or 2): 2
Enter a message: Khoor, Плх! 2026
Enter the shift: 3

Decrypted text: Hello, Мир! 2026
```
