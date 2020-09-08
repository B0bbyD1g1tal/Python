# Operations Between Numbers

first = int(input())
second = int(input())
operator = input()

result = ''
calculated = 0

if operator == '+' or \
        operator == '-' or \
        operator == '*':
    if operator == '+':
        calculated = first + second
    elif operator == '-':
        calculated = first - second
    elif operator == '*':
        calculated = first * second

    result += f'{first} {operator} {second} = ' \
              f'{calculated} - {"even" if calculated % 2 == 0 else "odd"}'
elif (operator == '/' or operator == '%') \
        and second != 0:
    if operator == '/':
        calculated = f'{(first / second):.2f}'
    elif operator == '%':
        calculated = first % second

    result = f'{first} {operator} {second} = {calculated}'
else:
    result = f'Cannot divide {first} by zero'

print(result)
