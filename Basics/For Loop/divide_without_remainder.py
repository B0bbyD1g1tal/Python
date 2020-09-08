# Divide Without Remainder

count = int(input())

two = 0
three = 0
four = 0

for i in range(count):
    number = int(input())

    if number % 2 == 0:
        two += 1
    if number % 3 == 0:
        three += 1
    if number % 4 == 0:
        four += 1

result = f'{(two / count * 100):.2f}%\n' \
         f'{(three / count * 100):.2f}%\n' \
         f'{(four / count * 100):.2f}%'

print(result)
