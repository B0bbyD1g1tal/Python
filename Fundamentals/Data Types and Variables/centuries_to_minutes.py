# Centuries to Minutes

YEAR = 365.2422

centuries = int(input())

years = centuries * 100
days = int(years * YEAR)
hours = days * 24
minutes = hours * 60

result = f'{centuries} centuries ' \
         f'= {years} years ' \
         f'= {days} days ' \
         f'= {hours} hours ' \
         f'= {minutes} minutes'

print(result)
