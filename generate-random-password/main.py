import sys
import random
def generate_password(file_path: str) -> None:
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            words = [line.strip() for line in file if line.strip()]
        if not words:
            print("Error: The file is empty or contains only whitespace.")
            return
        password_length = random.randint(8, 11)
        n1_length = random.randint(3, password_length - 3)
        n2_length = password_length - n1_length
        first_candidates = [w for w in words if len(w) == n1_length]
        second_candidates = [w for w in words if len(w) == n2_length]
        if not first_candidates or not second_candidates:
            print("Error: Failed to find words of the required length in the file.")
            return
        first_part = random.choice(first_candidates).capitalize()
        second_part = random.choice(second_candidates).capitalize()
        print(f"Your Generated Password: {first_part}{second_part}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except OSError as e:
        print(f"Input/Output Error: {e}")
def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python main.py <file_name>")
        return
    generate_password(sys.argv[1])
if __name__ == "__main__":
    main()