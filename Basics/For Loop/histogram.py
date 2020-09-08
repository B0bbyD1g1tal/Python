# Histogram

count = int(input())

numbers = []
for n in range(count):
    numbers.append(int(input()))

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for number in numbers:
    if number < 200:
        p1 += 1
    elif 200 <= number < 400:
        p2 += 1
    elif 400 <= number < 600:
        p3 += 1
    elif 600 <= number < 800:
        p4 += 1
    elif 800 <= number:
        p5 += 1

result = f'{(p1 / count * 100):.2f}%\n' \
         f'{(p2 / count * 100):.2f}%\n' \
         f'{(p3 / count * 100):.2f}%\n' \
         f'{(p4 / count * 100):.2f}%\n' \
         f'{(p5 / count * 100):.2f}%\n'

print(result)
