# Ski Trip

days = int(input())
premise = input()
rating = input()

price = 0
discount = 1

if premise == 'room for one person':
    price = 18
elif premise == 'apartment':
    price = 25
    if days >= 15:
        discount -= 0.5
    elif 10 < days < 15:
        discount -= 0.35
    else:
        discount -= 0.3
elif premise == 'president apartment':
    price = 35
    if days >= 15:
        discount -= 0.2
    elif 10 < days < 15:
        discount -= 0.15
    else:
        discount -= 0.1

total = price * (days - 1) * discount
total *= 1.25 if rating == 'positive' else 0.9

result = f'{total:.2f}'

print(result)
