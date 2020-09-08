# Moving

width = int(input())
length = int(input())
height = int(input())

free_space = width * length * height
result = ''

boxes = input()
while boxes != 'Done':
    box = int(boxes)

    free_space -= box

    if free_space <= 0:
        result = f'No more free space! ' \
                 f'You need {abs(free_space)} Cubic meters more.'
        break

    boxes = input()

if not result:
    result = f'{free_space} Cubic meters left.'

print(result)
