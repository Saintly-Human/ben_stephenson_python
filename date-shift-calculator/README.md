# Date Shift Calculator (Ordinal Date Converter)

A Python program that calculates a future date based on an initial date and a specific day shift (offset). It handles transitions across multiple years and fully supports leap years.

## 📖 Description

This project solves a classic calendar programming challenge. The program:
1. Takes a standard date (Day, Month, Year) and a number of days to shift.
2. Converts the initial date into an **ordinal date** (the day number of that year, from 1 to 365/366).
3. Adds the shift days and accurately calculates the new year by dynamically tracking leap years.
4. Converts the final ordinal date back into a human-readable format (`DD/MM/YYYY`) with leading zeros.

## 🚀 Features

- **Leap Year Support:** Dynamically checks if any year in the calculation period is a leap year (including the complex centurial year rules like 1900 vs 2000).
- **Multi-Year Transitions:** Easily handles big day offsets (e.g., +280 days for pregnancy term tracking or +1000 days).
- **Clean Formatting:** Outputs dates with proper leading zeros (e.g., `05/09/2026`).
- **DRY Architecture:** Uses a modular design with dedicated functions (`check_leap`, `ordinal_date`, `day_month_year`).

## 🛠️ How It Works

The program uses the following core logic:
- `check_leap(year)`: Evaluates if a given year has 366 days.
- `ordinal_date(day, month, year)`: Converts a regular date into a single day number from the start of the year.
- `day_month_year(ordinal_day, year)`: Converts the final day number back into a standard `DD/MM/YYYY` string.

### ⚙️ How To Run

1. **Clone the repository & navigate to this exercise:**:
```bash
git clone https://github.com/Saintly_Human/ben_stephenson_python.git
cd ben_stephenson_python/date-shift-calculator
```

2. Run the application:

```bash
python main.py
```
