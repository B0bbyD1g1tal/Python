# Sum of Chars

count = int(input())

total = 0
for i in range(count):
    char = input()
    total += ord(char)

result = f'The sum equals: {total}'

print(result)
