# Travelling

result = ''
while True:
    destination = input()
    if destination == 'End':
        break
    budget = float(input())
    money = 0

    while money < budget:
        money += float(input())
    result += f'Going to {destination}!\n'

print(result)
