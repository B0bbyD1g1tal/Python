# Numbers N to 1

END = 0
STEP = -1

number = int(input())

result = ''
for number in range(number, END, STEP):
    result += f'{number}\n'

print(result)
