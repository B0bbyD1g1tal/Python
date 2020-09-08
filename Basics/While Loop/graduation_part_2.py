# Graduation part 2

YEARS = 12

name = input()

grades_total = 0
year = 0
is_excluded = 0
while year < YEARS:
    grade = float(input())

    if grade >= 4:
        grades_total += grade
        year += 1
    else:
        is_excluded += 1
        if is_excluded >= 2:
            break

avg = grades_total / YEARS
result = f'{name} graduated. Average grade: {avg:.2f}' \
    if is_excluded < 2 \
    else f'{name} has been excluded at {year + 1} grade'

print(result)
