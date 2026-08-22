import sys

LETTERS = {
    'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta',
    'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel',
    'I': 'India', 'J': 'Juliet', 'K': 'Kilo', 'L': 'Lima',
    'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa',
    'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
    'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray',
    'Y': 'Yankee', 'Z': 'Zulu'
}


def func (word):
    if len(word) <= 1:
        return LETTERS.get(word, word)
    return f"{LETTERS.get(word[0], word[0])} {func(word[1:])}"


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python main.py word")
    else:
        print(func(sys.argv[1].upper()))
