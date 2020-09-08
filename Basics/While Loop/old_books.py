# Old Books

book = input()

result = ''
counter = 0
while True:
    current_book = input()

    if current_book == book:
        result = f'You checked {counter} books and found it.'
        break
    elif current_book == 'No More Books':
        break

    counter += 1

if not result:
    result = f'The book you search is not here!\n' \
             f'You checked {counter} books.'

print(result)
