# Time add 15 Minutes

hours = int(input())
minutes = int(input())

minutes += 15
hours += minutes // 60
hours %= 24
minutes %= 60

result = f'{hours}:{minutes:02}'

print(result)
