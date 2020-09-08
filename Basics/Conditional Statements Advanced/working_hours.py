# Working Hours

time = int(input())
day = input()

work_time = 10 <= time <= 18
work_day = day == "Monday" or \
           day == "Tuesday" or \
           day == "Wednesday" or \
           day == "Thursday" or \
           day == "Friday" or \
           day == 'Saturday'

result = 'open' if work_day and work_time else 'closed'
print(result)
