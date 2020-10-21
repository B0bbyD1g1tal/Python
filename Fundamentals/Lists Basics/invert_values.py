# Invert Values

def invert(some_number):
    return some_number[1:] if some_number[0] == '-' \
        else f'-{some_number}'


numbers = input()

inverted = [int(invert(number)) for number in numbers.split(' ')]

print(inverted)
