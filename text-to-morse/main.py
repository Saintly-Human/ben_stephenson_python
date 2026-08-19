def text_to_morse (text: str) -> str:
    result = []
    dictionary = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
    }
    for char in text:
        if char in dictionary:
            result.append(dictionary[char])
        elif char == " ":
            result.append(" ")
    return ' '.join(result)
def main():
    user_message = input("Enter your message: ")
    print(text_to_morse(user_message.upper()))
if __name__ == "__main__":
    main()