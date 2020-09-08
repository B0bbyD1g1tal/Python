# Clock

HOURS = 24
MINUTES = 60

result = ''
for hour in range(HOURS):
    for minute in range(MINUTES):
        result += f'{hour}:{minute}\n'

print(result)
