# Account Balance

result = ''
balance = 0
while True:
    payment = input()
    if payment == 'NoMoreMoney':
        break

    income = float(payment)

    if income < 0:
        result += f'Invalid operation!\n'
        break
    else:
        balance += income
        result += f'Increase: {income:.2f}\n'

result += f'Total: {balance:.2f}'

print(result)
