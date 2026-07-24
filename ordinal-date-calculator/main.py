def ordinalDate(day, month, year):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    if is_leap:
        days_in_month[1] = 29

    ordinal_day = sum(days_in_month[:month - 1]) + day
    return ordinal_day

if __name__ == "__main__":
    print("<----- The program for calculating the ordinal date ----->")

    try:
        user_day = int(input("Enter day (1-31): "))
        user_month = int(input("Enter month number (1-12): "))
        user_year = int(input("Enter year: "))

        result = ordinalDate(user_day, user_month, user_year)
        print(f'The ordinal number of the day in {user_year} year: {result}')

    except ValueError:
        print("Error: Please enter only integers.")
