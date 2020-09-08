# Building

floors = int(input())
premises = int(input())

result = ''
for floor in range(floors, 0, -1):
    if floor == floors:
        notation = 'L'
    else:
        notation = 'O' if floor % 2 == 0 else 'A'
    for premise in range(premises):
        result += f'{notation}{floor}{premise} '
    result += '\n'

print(result)
