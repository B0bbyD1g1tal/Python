# Coins

COINS = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]

change = float(input())

coins_count = 0
coin = 0
while coin < len(COINS):
    current_coin = COINS[coin]

    if change >= current_coin:
        count = change // current_coin
        coins_count += count
        change = round(change - count * current_coin, 2)

    coin += 1

result = int(coins_count)

print(result)
