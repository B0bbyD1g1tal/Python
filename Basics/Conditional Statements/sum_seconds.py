# Sum Seconds

first = int(input())
second = int(input())
third = int(input())

seconds_total = first + second + third

minutes = seconds_total // 60
seconds = seconds_total % 60

result = f'{minutes}:{seconds:02}'

print(result)
