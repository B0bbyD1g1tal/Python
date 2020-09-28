# Special Numbers

def check_special(integer_string):
    digits_sum = sum(list(map(int, integer_string)))
    is_special = digits_sum in [5, 7, 11]
    return is_special


integer = int(input())

numbers = range(1, integer + 1)

result = ''
for number in numbers:
    result += f'{number} -> {check_special(str(number))}\n'

print(result)
