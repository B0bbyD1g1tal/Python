# Min Number

from sys import maxsize

minimal = maxsize

while True:
    current = input()
    if current == 'Stop':
        break

    number = int(current)

    if number < minimal:
        minimal = number

print(minimal)
