import secrets
import string
def generate_password() -> str:
    chars = string.ascii_letters + string.digits + string.punctuation
    length = secrets.choice(range(7, 11))
    return "".join(secrets.choice(chars) for _ in range(length))
def main():
    print(f"Your password: {generate_password()}")
if __name__ == "__main__":
    main()