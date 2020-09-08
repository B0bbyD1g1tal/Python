# Scholarship

income = float(input())
grade = float(input())
wage = float(input())

gets_social = income < wage and grade >= 4.5
gets_excellence = grade >= 5.5

social = int(wage * 0.35)
excellence = int(grade * 25)

result = ''
if not gets_excellence and not gets_social:
    result = 'You cannot get a scholarship!'
elif gets_social and not gets_excellence:
    result = f'You get a Social scholarship {social} BGN'
elif gets_excellence and not gets_social:
    result = f'You get a scholarship for excellent results {excellence} BGN'
else:
    bigger = social if social >= excellence else excellence
    result = f'You get a scholarship for excellent results {bigger} BGN'

print(result)
