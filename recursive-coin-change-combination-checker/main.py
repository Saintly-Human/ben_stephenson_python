COINS = (25, 10, 5, 1)
def can_make_amount(amount, coin_count, coin_index=0):
    if amount == 0 and coin_count == 0:
        return True
    if amount < 0 or coin_count <= 0 or coin_index >= len(COINS):
        return False

    take_coin = can_make_amount(amount - COINS[coin_index], coin_count - 1, coin_index)

    skip_coin = can_make_amount(amount, coin_count, coin_index + 1)

    return take_coin or skip_coin


if __name__ == '__main__':
    target_amount = int(input("Enter target amount in cents (e.g., 100 for $1.00): "))
    target_coins = int(input("Enter target number of coins: "))

    if can_make_amount(target_amount, target_coins):
        print(f"Yes, it is possible to make {target_amount} cents with exactly {target_coins} coins.")
    else:
        print(f"No, it is NOT possible to make {target_amount} cents with exactly {target_coins} coins.")
