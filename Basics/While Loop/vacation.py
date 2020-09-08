# Vacation

trip_price = float(input())
total = float(input())

spending = 0
day = 1

result = ''
while True:
    action = input()
    amount = float(input())
    if action == 'spend':
        total -= amount
        if total < 0:
            total = 0

        spending += 1
        if spending >= 5:
            result = f'You can\'t save the money.\n{day}'
            break

    elif action == 'save':
        total += amount
        spending = 0

        if total >= trip_price:
            result = f'You saved the money for {day} days.'
            break

    day += 1

print(result)
