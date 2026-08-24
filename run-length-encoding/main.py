def decrypt (data, index=0):
    if index >= len(data):
        return []
    return [data[index]] * data[index + 1] + decrypt(data, index + 2)


def encrypt (data, index=0):
    if index >= len(data):
        return []

    target = data[index]
    count = 0

    while index + count < len(data) and data[index + count] == target:
        count += 1

    return [target, count] + encrypt(data, index + count)


if __name__ == "__main__":
    en_data = [
        'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
        'B', 'B', 'B', 'B',
        'A', 'A', 'A', 'A', 'A', 'A',
        'B'
    ]

    de_data = ["A", 12, "B", 4, "A", 6, "B", 1]

    print(f'Decoded output:\n{decrypt (de_data)}')
    print(f'Encoded output:\n{encrypt (en_data)}')
