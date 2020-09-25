# How Much Coffee Do You Need

EVENTS = ['coding', 'cat', 'dog', 'movie']

event = input()

coffee = 0
result = ''
while event != 'END':
    if event.lower() in EVENTS:
        coffee += 1 if event.islower() \
            else 2

    if coffee > 5:
        result = 'You need extra sleep'
        break

    event = input()

result = result if result \
    else coffee

print(result)
