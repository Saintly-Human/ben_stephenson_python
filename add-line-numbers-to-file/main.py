import sys
def add_line_numbers(input_path: str, output_path: str) -> None:
    try:
        with (
            open(input_path, mode="r", encoding="utf-8") as src,
            open(output_path, mode="w", encoding="utf-8") as dst,
        ):
            for i, line in enumerate(src, start=1):
                dst.write(f"{i}: {line}")
    except FileNotFoundError:
        print(f"Error: The source file '{input_path}' was not found.")
    except OSError as e:
        print(f"Input/Output error: {e}")
def main() -> None:
    if len(sys.argv) < 3:
        print("Usage: python script.py <source_file> <target_file>")
        return
    add_line_numbers(sys.argv[1], sys.argv[2])
if __name__ == "__main__":
    main()