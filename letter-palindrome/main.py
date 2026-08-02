import re

def is_letter_palindrome (text: str) -> bool:
    text = text.lower()
    cleaned_text = "".join(re.findall(r"\w", text))
    if not cleaned_text:
        return False
    return cleaned_text == cleaned_text[::-1]

def main():
    text = input("Enter your text: ")

    if is_letter_palindrome(text):
        print("Your text is palindrome (^///^)")
    else:
        print("Your text is NOT palindrome (´。＿。｀)")

if __name__ == "__main__":
    main()