def load_elements(filename="elements.txt"):
    el_names = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(",")
                el_names.append(parts[2])
    return el_names


def find_longest_chain(current_word, available_elements):
    last_letter = current_word[-1].upper()
    best_chain = []

    for el in available_elements:
        if el[0].upper() == last_letter:
            remaining_elements = [item for item in available_elements if item != el]

            chain = find_longest_chain(el, remaining_elements)

            if len(chain) > len(best_chain):
                best_chain = chain

    return [current_word] + best_chain


if __name__ == "__main__":
    el_names = load_elements()
    print("=== Chemical Element Word Game ===")
    user_element = input("Please enter starting element: ").strip().capitalize()

    if user_element in el_names:
        remaining = [el for el in el_names if el != user_element]
        result = find_longest_chain(user_element, remaining)

        print(f"\nMax chain length ({len(result)} elements) starting with {user_element}:")
        for i, word in enumerate(result, 1):
            print(f"{i}. {word}")
    else:
        print(f"\nError: Element '{user_element}' is NOT valid or not in database.")