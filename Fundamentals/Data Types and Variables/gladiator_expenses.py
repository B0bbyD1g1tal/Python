# Gladiator Expenses

lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmets = 0
swords = 0
shields = 0
armors = 0
for fight in range(1, lost_fights + 1):
    if fight % 2 == 0:
        helmets += 1
    if fight % 3 == 0:
        swords += 1
        if fight % 2 == 0:
            shields += 1
            if shields % 2 == 0:
                armors += 1

expenses = helmets * helmet_price \
           + swords * sword_price \
           + shields * shield_price \
           + armors * armor_price

result = f'Gladiator expenses: {expenses:.2f} aureus'

print(result)