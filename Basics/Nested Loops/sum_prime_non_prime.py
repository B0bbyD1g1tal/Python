# Sum Prime Non Prime

from math import sqrt

entry = input()

prime_sum = 0
non_prime_sum = 0

result = ''
while entry != 'stop':
    is_prime = True
    number = int(entry)

    if number < 0:
        result += 'Number is negative.\n'
        number = 0
    elif number < 2:
        is_prime = False
    else:
        square_root = int(sqrt(number))
        for n in range(2, square_root + 1):
            if number % n == 0:
                is_prime = False
                break
    if is_prime:
        prime_sum += number
    else:
        non_prime_sum += number

    entry = input()

result += f'Sum of all prime numbers is: {prime_sum}\n' \
          f'Sum of all non prime numbers is: {non_prime_sum}'

print(result)
