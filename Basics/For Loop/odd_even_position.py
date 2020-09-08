# Odd Even Position

from sys import maxsize

MAXIMAL = -maxsize
MINIMAL = maxsize

count = int(input())

odd_sum = 0.0
odd_minimal = MINIMAL
odd_maximal = MAXIMAL

even_sum = 0.0
even_minimal = MINIMAL
even_maximal = MAXIMAL

for number in range(count):
    current = float(input())
    if number % 2 != 0:
        even_sum += current
        if current <= even_minimal:
            even_minimal = current
        if current >= even_maximal:
            even_maximal = current
    else:
        odd_sum += current
        if current <= odd_minimal:
            odd_minimal = current
        if current >= odd_maximal:
            odd_maximal = current

result = ''
if count == 0:
    result = f'OddSum={odd_sum:.2f},\n' \
             f'OddMin=No,\n' \
             f'OddMax=No,\n' \
             f'EvenSum={even_sum:.2f},\n' \
             f'EvenMin=No,\n' \
             f'EvenMax=No'
elif count == 1:
    result = f'OddSum={odd_sum:.2f},\n' \
             f'OddMin={odd_minimal:.2f},\n' \
             f'OddMax={odd_maximal:.2f},\n' \
             f'EvenSum={even_sum:.2f},\n' \
             f'EvenMin=No,\n' \
             f'EvenMax=No'
else:
    result = f'OddSum={odd_sum:.2f},\n' \
             f'OddMin={odd_minimal:.2f},\n' \
             f'OddMax={odd_maximal:.2f},\n' \
             f'EvenSum={even_sum:.2f},\n' \
             f'EvenMin={even_minimal:.2f},\n' \
             f'EvenMax={even_maximal:.2f}'

print(result)
