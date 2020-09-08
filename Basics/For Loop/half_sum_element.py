# Half Sum Element

from sys import maxsize

MAXIMAL = -maxsize

count = int(input())

total = 0
for number in range(count):
    current = int(input())
    if current > MAXIMAL:
        MAXIMAL = current
    total += current

sum_of_others = int(abs(total - MAXIMAL))
difference = int(abs(sum_of_others - MAXIMAL))

result = f'Yes\nSum = {MAXIMAL}' if sum_of_others == MAXIMAL \
    else f'No\nDiff = {difference}'

print(result)
