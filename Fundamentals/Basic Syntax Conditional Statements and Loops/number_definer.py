# Number Definer

number = float(input())

result = ''
if 1 > abs(number) and number != 0:
    result += 'small '
elif abs(number) > 1000000:
    result += 'large '

if number > 0:
    result += 'positive'
elif number < 0:
    result += 'negative'
else:
    result += 'zero'

print(result)
