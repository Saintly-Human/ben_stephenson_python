def spell_with_elements(word, symbols):
    if not word:
        return ""

    for length in (1, 2, 3):
        if len(word) >= length:
            prefix = word[:length]
            for sym in symbols:
                if sym.upper() == prefix.upper():
                    rest = spell_with_elements(word[length:], symbols)
                    if rest != "" or len(word[length:]) == 0:
                        return sym + rest

    return ""


def load_elements(filename="elements.txt"):
    symbols = []
    names = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(",")
                symbols.append(parts[1])
                names.append(parts[2])
    return symbols, names


if __name__ == "__main__":
    symbols, names = load_elements("elements.txt")

    print("Elements that can be spelled using chemical symbols:\n")
    for name in names:
        result = spell_with_elements(name, symbols)
        if result:
            print(f"{name} can be represented as {result}")