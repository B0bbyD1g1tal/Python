# Numbers Ending in 7

START = 1
END = 1000 + 1

result = ''
for number in range(START, END):
    if number % 10 == 7:
        result += f'{number}\n'

print(result)
