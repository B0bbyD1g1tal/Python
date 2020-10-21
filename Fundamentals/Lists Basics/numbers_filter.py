# Numbers Filter

count = int(input())

numbers = []
evens = []
odds = []
positives = []
negatives = []

for i in range(count):
    number = int(input())
    numbers.append(number)

    if number % 2 == 0:
        evens.append(number)
    else:
        odds.append(number)

    if number < 0:
        negatives.append(number)
    else:
        positives.append(number)

command = input()

result = ''
if command == 'even':
    result = f'{evens}'
elif command == 'odd':
    result = f'{odds}'
elif command == 'positive':
    result = f'{positives}'
elif command == 'negative':
    result = f'{negatives}'

print(result)
