# Special Numbers

DIGITS = range(1, 10)

special = int(input())
result = ''
for first in DIGITS:
    for second in DIGITS:
        for third in DIGITS:
            for fourth in DIGITS:
                if special % first == 0 and \
                        special % second == 0 and \
                        special % third == 0 and \
                        special % fourth == 0:
                    result += f'{first}{second}{third}{fourth} '

print(result)
