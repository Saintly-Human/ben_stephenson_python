import sys


def format_text_file(filename: str, width: int = 50) -> None:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return

    paragraphs = content.split("\n\n")
    formatted_paragraphs = []

    for paragraph in paragraphs:
        words = paragraph.split()
        if not words:
            continue

        lines = []
        current_line = []
        current_length = 0

        for word in words:
            needed_space = len(word) if not current_line else len(word) + 1

            if current_length + needed_space <= width:
                current_line.append(word)
                current_length += needed_space
            else:
                lines.append(" ".join(current_line))
                current_line = [word]
                current_length = len(word)

        if current_line:
            lines.append(" ".join(current_line))

        formatted_paragraphs.append("\n".join(lines))

    print("\n\n".join(formatted_paragraphs))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = "alice.txt"

    format_text_file(file_path, width=50)