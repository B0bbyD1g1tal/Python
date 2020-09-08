# Even Powers of 2

TWO = 2
START = 0
STEP = 2

power = int(input())

result = ''
for p in range(START, power + 1, STEP):
    result += f'{TWO ** p}\n'

print(result)
