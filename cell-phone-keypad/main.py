def func (text: str):
    result = ""
    dictionary = {
        '0': " ",
        '1': ".,?!:", '2': "ABC", '3': "DEF",
        '4': "GHI", '5': "JKL", '6': "MNO",
        '7': "PQRS", '8': "TUV", '9': "WXYZ"
    }
    for char in text:
        for key, value in dictionary.items():
            if char in value:
                result += key * (value.index(char) + 1)
                break
        else:
            result += char
    return result
def main():
    user_message = input("Enter your message: ")
    print(func(user_message.upper()))
if __name__ == "__main__":
    main()