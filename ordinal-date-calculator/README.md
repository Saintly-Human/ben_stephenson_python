## 🕙 Project: Ordinal Date Calculator

A lightweight Python script that calculates the **ordinal date** (the day number of the year, from 1 to 366) for any given Gregorian calendar date.

### 📝 Description

An ordinal date consists of a year and a day number representing the elapsed days within that year. This format is highly efficient for computing elapsed intervals, such as tracking 90-day return policies, expiration dates, or project milestones, without dealing with complex calendar month logic.

The program handles leap years strictly according to the rules of the Gregorian calendar:
- A year is a leap year if it is divisible by 4.
- However, if it is divisible by 100, it is **not** a leap year, **unless** it is also divisible by 400.

### 🚀 Key Features

- **Leap Year Awareness:** Accurately adjusts February to 29 days when necessary.
- **Modular Design:** The core calculation logic is isolated within the `ordinalDate` function, making it easy to reuse.
- **Execution Safeguard:** Uses the `if __name__ == "__main__":` idiom to ensure the interactive CLI runs only when executed directly, preventing unexpected behavior if imported as a module.
- **Robustness:** Includes basic error handling for invalid integer inputs.

### ⚙️ How To Run

1. **Clone the repository & navigate to this exercise:**:
```bash
git clone https://github.com/Saintly_Human/ben_stephenson_python.git
cd ben_stephenson_python/ordinal-date-calculator
```

2. Run the application:

```bash
python main.py
```
