# Sequence 2k plus 1

count = int(input())

result = ''
number = 1
while number <= count:
    result += f'{number}\n'
    number = number * 2 + 1

print(result)
