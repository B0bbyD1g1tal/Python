# Weekend or Working Day

weekday = input()

result = ''
if weekday == 'Monday' or \
        weekday == 'Tuesday' or \
        weekday == 'Wednesday' or \
        weekday == "Thursday" or \
        weekday == 'Friday':
    result = 'Working day'
elif weekday == 'Saturday' or \
        weekday == "Sunday":
    result = 'Weekend'
else:
    result = 'Error'

print(result)
