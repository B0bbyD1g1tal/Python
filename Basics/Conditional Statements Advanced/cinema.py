# Cinema

projection = input()
rows = int(input())
cols = int(input())

price = 0
if projection == 'Premiere':
    price = 12
elif projection == 'Normal':
    price = 7.5
elif projection == 'Discount':
    price = 5

cost = price * rows * cols

result = f'{cost:.2f} leva'

print(result)
