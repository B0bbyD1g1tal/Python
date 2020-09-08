# Cake

width = int(input())
length = int(input())

cake = width * length

eaten = 0
result = ''
while True:
    command = input()
    if command == 'STOP':
        result = f'{cake - eaten} pieces are left.'
        break

    eaten += int(command)
    if eaten >= cake:
        result = f'No more cake left! You need {eaten - cake} pieces more.'
        break

print(result)
