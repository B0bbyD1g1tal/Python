# List Statistics

count = int(input())

positives = []
negatives = []

for i in range(count):
    number = int(input())
    if number < 0:
        negatives.append(number)
    else:
        positives.append(number)

result = f'{positives}\n' \
         f'{negatives}\n' \
         f'Count of positives: {len(positives)}. ' \
         f'Sum of negatives: {sum(negatives)}'

print(result)
