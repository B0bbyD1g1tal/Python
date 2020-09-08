# Max Number

from sys import maxsize

maximal = -maxsize

while True:
    current = input()
    if current == 'Stop':
        break

    number = int(current)

    if number > maximal:
        maximal = number

print(maximal)
