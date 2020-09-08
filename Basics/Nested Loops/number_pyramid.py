# Number Pyramid

number = int(input())

number_count = 1
current = 1

result = ''
while current <= number:
    for n in range(number_count):
        result += f'{current} '
        current += 1
        if current > number:
            break

    result += '\n'
    number_count += 1

print(result)
