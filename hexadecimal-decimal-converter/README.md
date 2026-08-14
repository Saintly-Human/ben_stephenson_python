# Hexadecimal and Decimal Converter Functions

A lightweight Python module providing utilities to convert single-character values between the **hexadecimal** (base-16) and **decimal** (base-10) numeral systems, complete with input validation and case-insensitive matching.

---

## Task Description

### 📝 Original Task (Russian)
> Напишите две функции с именами `hex2int` и `int2hex` для конвертации значений из шестнадцатеричной системы счисления (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E и F) в десятичную (по основанию 10) и обратно. Функция `hex2int` должна принимать на вход строку с единственным символом в шестнадцатеричной системе и преобразовывать его в число от нуля до 15 в десятичной системе, тогда как функция `int2hex` будет выполнять обратное действие – принимать десятичное число из диапазона от 0 до 15 и возвращать шестнадцатеричный эквивалент. Обе функции должны принимать единственный параметр со входным значением и возвращать преобразованное число. Удостоверьтесь, что функция `hex2int` корректно обрабатывает буквы в верхнем и нижнем регистрах. Если введенное пользователем значение выходит за допустимые границы, вы должны вывести сообщение об ошибке.

### 📝 English Translation
> Write two functions named `hex2int` and `int2hex` to convert values between hexadecimal (0–9, A–F) and decimal (base-10) systems. 
> * The `hex2int` function should accept a single-character string representing a hexadecimal digit and convert it into a decimal integer between `0` and `15`.
> * The `int2hex` function performs the reverse operation, taking an integer from `0` to `15` and returning its hexadecimal string representation.
> 
> Both functions must accept a single parameter and return the converted value. Ensure that `hex2int` properly handles both uppercase and lowercase input letters. If the user input is out of bounds or invalid, an appropriate error message should be displayed.

---

## 🚀 Features

- **Case-Insensitive Input:** `hex2int` handles lowercase and uppercase letters seamlessly (e.g., `'a'` and `'A'` both evaluate to `10`).
- **Robust Validation:** Checks boundaries for integer values (`0` to `15`) and string length constraints.
- **Interactive CLI Interface:** Included `main()` function automatically detects user input type and executes the corresponding conversion.

---

### ⚙️ How To Run

1. **Clone the repository & navigate to this exercise:**:
```bash
git clone https://github.com/Saintly_Human/ben_stephenson_python.git
cd ben_stephenson_python/hexadecimal-decimal-converter
```

2. Run the application:

```bash
python main.py
```

## 💡 **Example Output:**

Inputting a decimal number:

```plaintext
Enter a value (0-15 or 0-F): 14
DEC -> HEX: 14 = 'E'
```

Inputting a hexadecimal character:

```plaintext
Enter a value (0-15 or 0-F): e
HEX -> DEC: 'E' = 14
```

Handling out-of-bounds input:

```plaintext
Enter a value (0-15 or 0-F): 20
Error: the number 20 is outside the valid range (0–15)!
```
