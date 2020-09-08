# Combinations

number = int(input())

NUMBERS = range(0, number + 1)

combinations = 0
for first in NUMBERS:
    for second in NUMBERS:
        for third in NUMBERS:
            if first + second + third == number:
                combinations += 1

print(combinations)
