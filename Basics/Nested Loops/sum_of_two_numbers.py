# Sum of Two Numbers

start = int(input())
end = int(input())
magic_number = int(input())

NUMBERS = range(start, end + 1)

combinations = 0
result = ''
for first in NUMBERS:
    for second in NUMBERS:
        combinations += 1
        if first + second == magic_number:
            result = f'Combination N:{combinations} ' \
                     f'({first} + {second} = {magic_number})'
            break
    if result:
        break

if not result:
    result = f'{combinations} combinations - ' \
             f'neither equals {magic_number}'

print(result)
