# Prime Number Checker

from math import sqrt


def is_prime(some_number):
    square_root = sqrt(some_number)
    prime_checker = 2
    is_prime_num = True

    while prime_checker <= square_root:
        if some_number % prime_checker == 0:
            is_prime_num = False
            break
        prime_checker += 1

    return is_prime_num


number = int(input())

result = is_prime(number)

print(result)
