def transform_text(text: str, shift: int) -> str:
    ru_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    ru_upper = ru_lower.upper()
    en_lower = "abcdefghijklmnopqrstuvwxyz"
    en_upper = en_lower.upper()
    result = []
    for char in text:
        if char in ru_lower:
            result.append(ru_lower[(ru_lower.index(char) + shift) % len(ru_lower)])
        elif char in ru_upper:
            result.append(ru_upper[(ru_upper.index(char) + shift) % len(ru_upper)])
        elif char in en_lower:
            result.append(en_lower[(en_lower.index(char) + shift) % len(en_lower)])
        elif char in en_upper:
            result.append(en_upper[(en_upper.index(char) + shift) % len(en_upper)])
        else:
            result.append(char)
    return "".join(result)

def encrypt(text: str, shift: int) -> str:
    return transform_text(text, shift)

def decrypt(text: str, shift: int) -> str:
    return transform_text(text, -shift)

def main():
    print("Select an action:")
    print("1 — Encrypt text")
    print("2 — Decrypt text")
    choice = input("Your choice (1 or 2): ").strip()

    if choice not in ("1", "2"):
        print("Error: select 1 or 2.")
        return

    message = input("Enter a message: ")
    try:
        shift = int(input("Enter the shift: "))
    except ValueError:
        print("Error: the shift must be an integer.")
        return

    if choice == "1":
        result = encrypt(message, shift)
        print(f"\nEncrypted text: {result}")
    else:
        result = decrypt(message, shift)
        print(f"\nDecrypted text: {result}")

if __name__ == "__main__":
    main()
