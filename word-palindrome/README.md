# 🔄 Word-Level Palindrome Checker

A Python script that determines whether a user-provided string is a **word-level palindrome** (ignoring punctuation, spaces, and letter case).

---

## 📜 Task Description / Описание задачи

### 🇬🇧 English Description
> In previous exercises, we examined word-level palindromes on a character-by-character basis. However, the concept of a palindrome can be extended to full sentences.
> 
> A **word-level palindrome** is a sequence of words that reads the same forwards and backwards on a **word** level rather than a character level, ignoring punctuation and capitalization. 
> 
> **Examples:**
> * *"Is it crazy how saying sentences backwards creates backwards sentences saying how crazy it is?"*
> * *"Herb the sage eats sage, the herb"*
> * *"Information school graduate seeks graduate school information"*
> 
> **Task:** Write a program that prompts the user for a string and determines whether or not it is a word-level palindrome.

---

### 🇷🇺 Оригинальное условие
> В упражнениях 75 и 76 мы уже имели дело со словами, являющимися палиндромами. Тогда мы анализировали буквы в слове с начала и конца, игнорируя пробелы и знаки препинания, чтобы понять, совпадает ли его написание в прямом и обратном направлениях. И хотя палиндромами обычно называют слова, это понятие вполне можно расширить. 
> 
> Например, английская фраза *«Is it crazy how saying sentences backwards creates backwards sentences saying how crazy it is?»* является словесным палиндромом, поскольку если читать ее по словам, игнорируя при этом знаки препинания и заглавные буквы, в обоих направлениях она будет звучать одинаково. Еще примеры английских словесных палиндромов: *«Herb the sage eats sage, the herb»* и *«Information school graduate seeks graduate school information»*.
> 
> **Задача:** Напишите программу, которая будет запрашивать строку у пользователя и оповещать его о том, является ли она словесным палиндромом. Не забывайте игнорировать знаки препинания при выявлении результата.

---

## 🛠️ Implementation Details

1. **Lowercasing**: Convert the input text to lowercase to make the check case-insensitive (`text.lower()`).
2. **Word Extraction**: Use Regular Expressions (`re`) to extract words while ignoring standard punctuation, but preserving English apostrophes inside contractions (e.g., `don't`, `it's`).
3. **Palindrome Logic**: Compare the resulting list of words against its reversed copy (`words == words[::-1]`).

---

## 🚀 Examples of Usage

### Example 1 (Valid Word-Level Palindrome)

```text
Enter your text: Herb the sage eats sage, the herb.
Your text is palindrome ( •̀ ω •́ )✧
```

### Example 2 (Another Valid Palindrome)

```text
Enter your text: Is it crazy how saying sentences backwards creates backwards sentences saying how crazy it is?
Your text is palindrome ( •̀ ω •́ )✧
```

### Example 3 (Character Palindrome, but NOT Word-Level)

```text
Enter your text: Аргентина манит негра
Your text is NOT palindrome .·´¯`(>▂<)´¯`·.
```

## ⚙️ How to Run

1. Make sure you have Python installed (version 3.6+).

2. Clone the repository & navigate to this exercise::

```bash
git clone https://github.com/Saintly_Human/ben_stephenson_python.git
cd ben_stephenson_python/word-palindrome
```

3. Run the script in your terminal:

```bash
python main.py
```
