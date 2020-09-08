# Number sequence

from sys import maxsize

MAXIMAL = -maxsize
MINIMAL = maxsize

count = int(input())

for i in range(count):
    current = int(input())

    if current > MAXIMAL:
        MAXIMAL = current

    if current < MINIMAL:
        MINIMAL = current

result = f'Max number: {MAXIMAL}\n' \
         f'Min number: {MINIMAL}'

print(result)
