# Patterns

STAR = '*'

number = int(input())

result = ''
for upper in range(1, number + 1):
    result += f'{upper * STAR}\n'
for lower in range(number - 1, 0, -1):
    result += f'{lower * STAR}\n'

print(result)
