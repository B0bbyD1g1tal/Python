# Password Generator

FIRST_LETTER = 97

number = int(input())
letter = int(input())

numbers_range = range(1, number + 1)
letters_range = range(FIRST_LETTER, FIRST_LETTER + letter)

result = ''
for first in numbers_range:
    for second in numbers_range:
        for third in letters_range:
            for fourth in letters_range:
                for fifth in range(min(first, second), number + 1):
                    if fifth > first and fifth > second:
                        result += f'{first}{second}{chr(third)}{chr(fourth)}{fifth} '

print(result)
