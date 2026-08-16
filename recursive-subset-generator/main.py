def get_all_subsets(numbers: list) -> list[list]:
    result = []

    def backtrack(start: int, current_combo: list):
        if current_combo:
            result.append(list(current_combo))

        for i in range(start, len(numbers)):
            current_combo.append(numbers[i])

            backtrack(i + 1, current_combo)

            current_combo.pop()

    backtrack(0, [])
    return result


if __name__ == "__main__":
    data = [10, 20, 30]
    subsets = get_all_subsets(data)

    print(f"Input: {data}")
    print(f"Total Subsets Generated: {len(subsets)}\n")
    for combo in subsets:
        print(combo)
