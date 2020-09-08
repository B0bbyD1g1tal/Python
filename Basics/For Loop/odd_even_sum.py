# Odd Even Sum

count = int(input())

odd_sum = 0
even_sum = 0
for number in range(count):
    if number % 2 == 0:
        even_sum += int(input())
    else:
        odd_sum += int(input())

difference = int(abs(odd_sum - even_sum))

result = f'Yes\n' \
         f'Sum = {even_sum}' \
    if not difference \
    else f'No\n' \
         f'Diff = {difference}'

print(result)
