# Numbers 1 to N with Step 3

START = 1
STEP = 3

number = int(input())
result = ''
for number in range(START, number + 1, STEP):
    result += f'{number}\n'

print(result)
