def convert_from_decimal(n, base):
    digits = "0123456789ABCDEF"
    if base < 2 or base > 16:
        raise ValueError("The base of the number system should be from 2 to 16.")
    if n < base:
        return digits[n]
    return convert_from_decimal(n // base, base) + digits[n % base]
def main():
    try:
        num = int(input("Enter a non-negative integer: "))
        if num < 0:
            print("Error: the number should be a non-negative integer!")
            return
        base = int(input("Enter the base of the number system (from 2 to 16): "))
        result = convert_from_decimal(num, base)
        print(f"Result ({base}-ary system): {result}")
    except ValueError as e:
        print(f"Input error: {e}")
if __name__ == "__main__":
    main()