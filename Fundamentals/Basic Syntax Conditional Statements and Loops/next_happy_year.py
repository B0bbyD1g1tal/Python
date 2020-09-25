# Next Happy Year

year = input()

happy_year = year
is_happy_year = len(set(happy_year)) == len(happy_year)

while True:
    happy_year = str(int(happy_year) + 1)
    is_happy_year = len(set(happy_year)) == len(happy_year)

    if is_happy_year:
        break

print(happy_year)
