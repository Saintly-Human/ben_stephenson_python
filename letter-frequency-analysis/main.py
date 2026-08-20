import sys
from collections import Counter
def analyze_letter_frequency(file_path: str) -> None:
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            text = file.read().lower()
            letters = [char for char in text if char.isalpha()]
            if not letters:
                print("No letters were found in the file for analysis.")
                return
            counts = Counter(letters)
            total_letters = len(letters)
            print(f"Total letters found: {total_letters}\n")
            print(f"{'Letter':<8}{'Count':<12}{'Percentage':<10}")
            print("-" * 30)
            for letter, count in counts.most_common():
                percentage = (count / total_letters) * 100
                print(f"{letter:<8}{count:<12}{percentage:.2f}%")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except OSError as e:
        print(f"Error reading the file: {e}")
def main() -> None:
    if len(sys.argv) != 2:
        print("Error: Invalid number of arguments.")
        print("Usage: python frequency_analysis.py <file_name>")
        return
    analyze_letter_frequency(sys.argv[1])
if __name__ == "__main__":
    main()