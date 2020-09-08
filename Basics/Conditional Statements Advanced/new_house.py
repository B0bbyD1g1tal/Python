# New House

ROSE = 5
DAHLIA = 3.8
TULIP = 2.8
NARCISSUS = 3
GLADIOLUS = 2.5

flower = input()
count = int(input())
budget = int(input())

cost = 0
if flower == 'Roses':
    cost = ROSE * count
    if count > 80:
        cost *= 0.9
elif flower == 'Dahlias':
    cost = DAHLIA * count
    if count > 90:
        cost *= 0.85
elif flower == 'Tulips':
    cost = TULIP * count
    if count > 80:
        cost *= 0.85
elif flower == 'Narcissus':
    cost = NARCISSUS * count
    if count < 120:
        cost *= 1.15
elif flower == 'Gladiolus':
    cost = GLADIOLUS * count
    if count < 80:
        cost *= 1.2

difference = abs(budget - cost)

result = f'Hey, you have a great garden with {count} {flower} ' \
         f'and {difference:.2f} leva left.' if budget >= cost \
    else f'Not enough money, ' \
         f'you need {difference:.2f} leva more.'

print(result)
