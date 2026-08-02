import re

def is_letter_palindrome (text: str) -> bool:
    text = text.lower()
    pattern = r"\w+(?:'\w+)*"
    words = re.findall(pattern, text)
    if not words:
        return False
    return words == words[::-1]

def main():
    user_text = input("Enter your text: ")

    if is_letter_palindrome(user_text):
        print("Your text is palindrome ( •̀ ω •́ )✧")
    else:
        print("Your text is NOT palindrome .·´¯`(>▂<)´¯`·.")

if __name__ == "__main__":
    main()