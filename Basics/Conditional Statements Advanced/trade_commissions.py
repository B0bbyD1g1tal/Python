# Trade Commissions

town = input()
sales = float(input())

commission = 0
has_error = False

if town == 'Sofia':
    if 0 <= sales <= 500:
        commission = 0.05
    elif 500 <= sales <= 1000:
        commission = 0.07
    elif 1000 <= sales <= 10000:
        commission = 0.08
    elif sales > 10000:
        commission = 0.12
    else:
        has_error = True
elif town == 'Varna':
    if 0 <= sales <= 500:
        commission = 0.045
    elif 500 <= sales <= 1000:
        commission = 0.075
    elif 1000 <= sales <= 10000:
        commission = 0.1
    elif sales > 10000:
        commission = 0.13
    else:
        has_error = True
elif town == 'Plovdiv':
    if 0 <= sales <= 500:
        commission = 0.055
    elif 500 <= sales <= 1000:
        commission = 0.08
    elif 1000 <= sales <= 10000:
        commission = 0.12
    elif sales > 10000:
        commission = 0.145
    else:
        has_error = True
else:
    has_error = True

result = f'{(commission * sales):.2f}' if not has_error \
    else 'error'

print(result)
