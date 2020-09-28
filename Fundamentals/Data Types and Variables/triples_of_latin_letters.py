# Triples of Latin Letters

A = 97

letter = int(input())

letters = range(A, A + letter)

result = ''
for first in letters:
    for second in letters:
        for third in letters:
            result += f'{chr(first)}{chr(second)}{chr(third)}\n'

print(result)
