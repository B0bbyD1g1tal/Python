# Water Overflow

CAPACITY = 255

quantities = int(input())

water = 0
result = ''
for quantity in range(quantities):
    liters = int(input())

    if liters + water > CAPACITY:
        result += 'Insufficient capacity!\n'
    else:
        water += liters

result += f'{water}'

print(result)
