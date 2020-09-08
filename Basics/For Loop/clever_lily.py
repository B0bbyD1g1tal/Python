# Clever Lily

age = int(input())
washing_machine = float(input())
toy_price = int(input())

money_per_birth_day = 10
toys = 0
money = 0

for year in range(1, age + 1):
    if year % 2 == 0:
        money += money_per_birth_day - 1
        money_per_birth_day += 10
    else:
        toys += 1

total = toys * toy_price + money
difference = abs(total - washing_machine)

result = f'Yes! {difference:.2f}' \
    if total - washing_machine >= 0 \
    else f'No! {difference:.2f}'

print(result)
