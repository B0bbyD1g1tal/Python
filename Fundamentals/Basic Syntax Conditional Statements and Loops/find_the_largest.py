# Find The Largest

number = input()

largest = list(number)
largest.sort(reverse=True)

result = ''.join(largest)

print(result)
