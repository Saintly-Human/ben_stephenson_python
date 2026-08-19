def pure_sieve(n: int) -> list[int]:
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [num for num, prime in enumerate(is_prime) if prime]
def main():
    try:
        user_num = int(input("Enter a number: "))
        result = pure_sieve(user_num)
        print(f"All simple numbers until {user_num} are {len(result)}: {result}")
    except ValueError:
        print("Please enter a number")
if __name__ == "__main__":
    main()