# Multiplication Table

NUMBERS = range(1, 11)

result = ''
for multiplicand in NUMBERS:
    for multiplier in NUMBERS:
        product = multiplicand * multiplier
        result += f'{multiplicand} * {multiplier} = {product}\n'

print(result)
