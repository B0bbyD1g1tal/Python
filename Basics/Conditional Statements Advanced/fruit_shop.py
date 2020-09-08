# Fruit Shop

product = input()
day = input()
quantity = float(input())

total = 0
has_error = False

if day == 'Monday' or \
        day == 'Tuesday' or \
        day == 'Wednesday' or \
        day == 'Thursday ' or \
        day == 'Friday':
    if product == 'banana':
        total = quantity * 2.5
    elif product == 'apple':
        total = quantity * 1.2
    elif product == 'orange':
        total = quantity * 0.85
    elif product == 'grapefruit':
        total = quantity * 1.45
    elif product == 'kiwi':
        total = quantity * 2.7
    elif product == 'pineapple':
        total = quantity * 5.5
    elif product == 'grapes':
        total = quantity * 3.85
    else:
        has_error = True
elif day == 'Saturday' or \
        day == 'Sunday':
    if product == 'banana':
        total = quantity * 2.7
    elif product == 'apple':
        total = quantity * 1.25
    elif product == 'orange':
        total = quantity * 0.9
    elif product == 'grapefruit':
        total = quantity * 1.6
    elif product == 'kiwi':
        total = quantity * 3.0
    elif product == 'pineapple':
        total = quantity * 5.6
    elif product == 'grapes':
        total = quantity * 4.2
    else:
        has_error = True
else:
    has_error = True

result = f'{total:.2f}' if not has_error else 'error'

print(result)
