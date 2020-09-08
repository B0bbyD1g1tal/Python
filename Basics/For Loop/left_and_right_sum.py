# Left and Right Sum

count = int(input())

half = range(count)

left_sum = 0
for left in half:
    left_sum += int(input())

right_sum = 0
for right in half:
    right_sum += int(input())

difference = abs(left_sum - right_sum)

result = f'Yes, sum = {right_sum}' \
    if not difference \
    else f'No, diff = {difference}'

print(result)
