# Personal Titles

age = float(input())
gender = input()

is_adult = age >= 16

result = ''
if gender == 'f':
    result = 'Ms.' if is_adult else 'Miss'
elif gender == 'm':
    result = 'Mr.' if is_adult else 'Master'

print(result)
