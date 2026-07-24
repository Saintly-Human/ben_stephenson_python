def check_leap(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def ordinal_date(day: int, month: int, year: int):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if check_leap(year):
        days_in_month[1] = 29

    ordinal_day = sum(days_in_month[:month - 1]) + day

    return ordinal_day


def day_month_year(ordinal_day: int, year: int):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if check_leap(year):
        days_in_month[1] = 29

    month = 0
    while ordinal_day > days_in_month[month]:
        ordinal_day -= days_in_month[month]
        month += 1

    return f'{ordinal_day:02d}/{month + 1:02d}/{year:04d}'


def main():
    user_day = int(input("Enter day: "))
    user_month = int(input("Enter month: "))
    user_year = int(input("Enter year: "))
    user_shift = int(input("Enter shift: "))

    ordinal_day = ordinal_date(user_day, user_month, user_year)
    ordinal_day += user_shift

    while True:
        day_in_current_year = 366 if check_leap(user_year) else 365
        if ordinal_day > day_in_current_year:
            ordinal_day -= day_in_current_year
            user_year += 1
        else:
            break

    print(day_month_year(ordinal_day, user_year))

if __name__ == "__main__":
    main()