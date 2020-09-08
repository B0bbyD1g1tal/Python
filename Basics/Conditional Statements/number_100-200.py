# Number 100-200

number = int(input())

result = ''
if number < 100:
    result = 'Less than 100'
elif 100 <= number <= 200:
    result = 'Between 100 and 200'
else:
    result = 'Greater than 200'

print(result)
