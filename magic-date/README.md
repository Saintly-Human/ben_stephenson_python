# Magic Dates Detector (20th Century)

A Python script that finds and displays all **"Magic Dates"** in the 20th century. A date is considered "magic" if the product of the day and the month equals the two-digit representation of the year (e.g., June 10, 1960 $\rightarrow$ $10 \times 6 = 60$).

---

## 📜 Problem Statement / Условие задачи

### 🇬🇧 English

A magic date is a date where the day times the month is equal to the two-digit year. For example, June 10, 1960 is a magic date because $10 \times 6 = 60$.

Write a function that determines whether or not a date is a magic date. Use your function to create a main program that finds and displays all of the magic dates in the 20th century. 

---

### 🇷🇺 Русский (Оригинал)

Магическими называются даты, в которых произведение дня и месяца составляет последние две цифры года. Например, 10 июня 1960 года – магическая дата, поскольку $10 \times 6 = 60$. 

Напишите функцию, определяющую, является ли введенная дата магической. Используйте написанную функцию в главной программе для отображения всех магических дат в XX веке.

---

## 📝 Implementation Details & Notes

> **Note on Leap Years:**  
> February has 29 days in leap years. The algorithm includes a helper function `is_leap_year()` to dynamically adjust the number of days in February for accurate processing.

---

## 🚀 How to Run

1. Make sure you have Python installed (version 3.6+).

2. Clone the repository & navigate to this exercise::

```bash
git clone https://github.com/Saintly_Human/ben_stephenson_python.git
cd ben_stephenson_python/magic-date
```

3. Run the script in your terminal:

```bash
python magic_dates.py
```
