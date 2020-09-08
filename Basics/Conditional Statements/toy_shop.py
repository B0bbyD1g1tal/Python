# Toy Shop

PUZZLE = 2.6
DOLL = 3
BEAR = 4.1
MINION = 8.2
TRUCK = 2

excursion_price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

total = puzzles * PUZZLE + \
        dolls * DOLL + \
        bears * BEAR + \
        minions * MINION + \
        trucks * TRUCK
toys_count = puzzles + dolls + bears + minions + trucks
if toys_count >= 50:
    total *= 0.75
total *= 0.9

difference = abs(total - excursion_price)
result = f'Yes! {difference:.2f} lv left.' if total >= excursion_price \
    else f'Not enough money! {difference:.2f} lv needed.'

print(result)
