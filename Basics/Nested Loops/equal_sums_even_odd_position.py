# Equal Sums Even Odd Position

DIGITS_COUNT = 6

first = int(input())
second = int(input())

result = ''
for number in range(first, second + 1):
    even_sum = 0
    odd_sum = 0
    current_number = number
    for position in range(DIGITS_COUNT):
        digit = current_number % 10
        current_number //= 10

        if position % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    if even_sum == odd_sum:
        result += f'{number} '

print(result)
