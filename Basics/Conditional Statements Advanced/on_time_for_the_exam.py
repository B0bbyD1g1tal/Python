# On Time for the Exam

exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

arrival = arrival_hour * 60 + arrival_minute
exam = exam_hour * 60 + exam_minute

result = ''
if arrival > exam:
    result = 'Late\n'
elif exam >= arrival >= exam - 30:
    result = 'On time\n'
else:
    result = 'Early\n'

difference = abs(arrival - exam)
time_diff = f'{difference // 60}:{(difference % 60):02} hours' \
    if difference >= 60 \
    else f'{difference % 60} minutes'

if arrival < exam:
    result += f'{time_diff} before the start'
elif arrival > exam:
    result += f'{time_diff} after the start'

print(result)
