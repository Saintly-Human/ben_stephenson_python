def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def is_magic_date(day, month, year):
    two_digit_year = year % 100
    return day * month == two_digit_year


def main():
    months = [
        'January', 'February', 'March', 'April',
        'May', 'June', 'July', 'August',
        'September', 'October', 'November', 'December'
    ]

    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    print("Magic dates in the 20th century:\n")
    magic_count = 0

    for year in range(1901, 2001):
        for month_idx, max_days in enumerate(days_in_months, start=1):

            if month_idx == 2 and is_leap_year(year):
                max_days = 29

            for day in range(1, max_days + 1):
                if is_magic_date(day, month_idx, year):
                    month_name = months[month_idx - 1]
                    print(f"{day} {month_name} {year}")
                    magic_count += 1

    print(f"\nTotal magic dates found: {magic_count}")


if __name__ == '__main__':
    main()