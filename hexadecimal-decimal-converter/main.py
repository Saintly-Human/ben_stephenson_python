HEX_DIGITS = "0123456789ABCDEF"

def hex2int(hex_str: str) -> int | None:
    if not isinstance(hex_str, str) or len(hex_str) != 1:
        print("Error: the input value must be exactly one character!")
        return None

    char = hex_str.upper()

    if char in HEX_DIGITS:
        return HEX_DIGITS.index(char)
    else:
        print(f"Error: '{hex_str}' is not a valid hexadecimal character!")
        return None

def int2hex(num: int) -> str | None:
    if isinstance(num, int) and not isinstance(num, bool) and 0 <= num <= 15:
        return HEX_DIGITS[num]
    else:
        print(f"Error: the number {num} is outside the valid range (0–15)!")
        return None

def main():
    user_input = input("Enter a value (0-15 or 0-F): ").strip()

    if user_input.isdigit():
        num = int(user_input)
        if 0 <= num <= 15:
            hex_val = int2hex(num)
            print(f"DEC -> HEX: {num} = '{hex_val}'")
        else:
            print("Error: Enter a decimal number between 0 and 15.")

    elif len(user_input) == 1 and user_input.upper() in HEX_DIGITS:
        dec_val = hex2int(user_input)
        print(f"HEX -> DEC: '{user_input.upper()}' = {dec_val}")

    else:
        print("Error: Invalid input. Please enter a single hex digit (0-9, A-F).")


if __name__ == "__main__":
    main()