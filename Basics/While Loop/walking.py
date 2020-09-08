# Walking

GOAL = 10000

steps = 0
result = ''
while True:
    action = input()

    if action == 'Going home':
        steps += int(input())
        difference = abs(GOAL - steps)

        if steps < GOAL:
            result = f'{difference} more steps to reach goal.'
            break
    else:
        steps += int(action)
        difference = abs(GOAL - steps)

    if steps >= GOAL:
        result = f'Goal reached! Good job!\n' \
                 f'{difference} steps over the goal!'
        break

print(result)
