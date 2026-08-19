def simple_numbers(num):
    all_nums = list(range(num + 1))
    all_nums[0] = 0
    all_nums[1] = 0
    p = 2
    while p < num and p != 0:
        for i in range(len(all_nums)):
            if all_nums[i] != 0 and all_nums[i] % p == 0 and all_nums[i] != p:
                all_nums[i] = 0
        p += 1
        while p <= num and all_nums[p] == 0:
            p += 1
        if p > num:
            p = 0
    return [i for i in all_nums if i != 0]
def main():
    try:
        user_num = int(input("Enter a number: "))
        result = simple_numbers(user_num)
        print(f"All simple numbers until {user_num} are {len(result)}: {result}")
    except ValueError:
        print("Please enter a number")
if __name__ == "__main__":
    main()