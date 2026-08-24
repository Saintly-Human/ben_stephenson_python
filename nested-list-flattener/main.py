# 1. Classical Recursive Slicing (Educational)
def flatten_recursive(data):
    if not data:
        return []
    if isinstance(data[0], list):
        return flatten_recursive(data[0]) + flatten_recursive(data[1:])
    return [data[0]] + flatten_recursive(data[1:])


# 2. Generator with yield from (Pythonic & Optimized)
def flatten_generator(data):
    for item in data:
        if isinstance(item, list):
            yield from flatten_generator(item)
        else:
            yield item


# 3. Iterative Stack Approach (Production-Ready)
def flatten_iterative(data):
    result = []
    stack = [data]
    while stack:
        curr = stack.pop()
        if isinstance(curr, list):
            stack.extend(reversed(curr))
        else:
            result.append(curr)
    return result


if __name__ == "__main__":
    test_data = [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]

    print("Input data:", test_data)
    print("-" * 50)

    # Testing Approach 1
    res_rec = flatten_recursive(test_data)
    print("1. Recursive Slicing: ", res_rec)

    # Testing Approach 2 (converting generator to list)
    res_gen = list(flatten_generator(test_data))
    print("2. Generator (yield):", res_gen)

    # Testing Approach 3
    res_iter = flatten_iterative(test_data)
    print("3. Iterative (Stack):", res_iter)
