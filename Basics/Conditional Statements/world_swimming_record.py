# World Swimming Record

record = float(input())
distance = float(input())
time = float(input())

swim = distance * time + \
       int(distance / 15) * 12.5

result = ''
if swim < record:
    result = f'Yes, he succeeded! ' \
             f'The new world record is {swim:.2f} seconds.'
else:
    diff = abs(swim - record)
    result = f'No, he failed! ' \
             f'He was {diff:.2f} seconds slower.'

print(result)
