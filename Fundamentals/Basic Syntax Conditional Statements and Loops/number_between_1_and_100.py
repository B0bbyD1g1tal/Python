# Number Between 1 and 100

number = float(input())

while 1 > number or number > 100:
    number = float(input())

result = f'The number {number} is between 1 and 100'

print(result)
