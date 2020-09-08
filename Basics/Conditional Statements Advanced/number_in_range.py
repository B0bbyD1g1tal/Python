# Number in Range

number = int(input())

is_valid = (-100 <= number <= 100) and number != 0

result = 'Yes' if is_valid else 'No'

print(result)
