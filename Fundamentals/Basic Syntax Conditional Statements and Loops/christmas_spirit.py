# Christmas Spirit

ORNAMENT_SET_PRICE = 2
TREE_SKIRT_PRICE = 5
TREE_GARLANDS_PRICE = 3
TREE_LIGHTS_PRICE = 15

quantity = int(input())
days = int(input())

days_to_christmas = range(1, days + 1)
spirit = 0
total = 0
for day in days_to_christmas:
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        total += quantity * ORNAMENT_SET_PRICE
        spirit += 5
    if day % 3 == 0:
        total += quantity * (TREE_SKIRT_PRICE +
                             TREE_GARLANDS_PRICE)
        spirit += 13
    if day % 5 == 0:
        total += quantity * TREE_LIGHTS_PRICE
        spirit += 17
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        total += TREE_SKIRT_PRICE + \
                 TREE_GARLANDS_PRICE + \
                 TREE_LIGHTS_PRICE
        spirit -= 20

if days % 10 == 0:
    spirit -= 30

result = f'Total cost: {total}\n' \
         f'Total spirit: {spirit}'

print(result)
