# Party Profit

party_size = int(input())
days = int(input())

companions = party_size
coins = 0
for day in range(1, days + 1):
    if day % 10 == 0:
        companions -= 2
    if day % 15 == 0:
        companions += 5

    coins += 50 - companions * 2

    if day % 3 == 0:
        coins -= companions * 3
    if day % 5 == 0:
        coins += companions * 20
        if day % 3 == 0:
            coins -= companions * 2

result = f'{companions} companions received ' \
         f'{int(coins / companions)} coins each.'

print(result)
