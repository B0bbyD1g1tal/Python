# Cannot Sleep Count Sheep

flock = int(input())

result = ''
for sheep in range(1, flock + 1):
    result += f'{sheep} sheep...'

print(result)
