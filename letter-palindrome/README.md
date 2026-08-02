# 🔤 Character-Level Palindrome Checker

A Python script that checks whether a user-provided string is a **character-level palindrome** (ignoring spaces, punctuation, symbols, and letter case).

---

## 📜 Task Description

A **character-level palindrome** is a sequence of characters (letters and digits) that reads the same forwards and backwards. 

When determining if a phrase is a palindrome, all non-alphanumeric characters (such as spaces, commas, periods, and exclamation marks) as well as letter casing are ignored.

### 💡 Examples:
* **"Madam, I'm Adam"** $\rightarrow$ Cleaned: `madamimadam` *(Palindrome)*
* **"А роза упала на лапу Азора"** $\rightarrow$ Cleaned: `арозаупаланалапуазора` *(Palindrome)*
* **"Аргентина манит негра"** $\rightarrow$ Cleaned: `аргентинаманитнегра` *(Palindrome)*

---

## 🛠️ How It Works

1. **Case Normalization**: Converts the entire input string to lowercase using `.lower()`.
2. **Filtering Non-Alphanumeric Characters**: Uses Regular Expressions (`re.findall(r"\w", text)`) to extract only letters and digits, stripping away spaces and punctuation marks.
3. **Reversal & Comparison**: Merges the extracted characters into a single string and compares it against its reversed copy using Python's slicing operator (`cleaned_text[::-1]`).

---

## 🚀 Examples of Usage

### Example 1 (English Phrase)
```text
Enter your text: Madam, I'm Adam
Your text is palindrome (^///^)
```

### Example 2 (Cyrillic Phrase)
```text
Enter your text: Аргентина манит негра
Your text is palindrome (^///^)
```

### Example 3 (Not a Palindrome)
```text
Enter your text: Hello world!
Your text is NOT palindrome (´。＿。｀)
```
