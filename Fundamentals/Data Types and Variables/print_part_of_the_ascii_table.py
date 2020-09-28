# Print Part of the ASCII Table

start = int(input())
end = int(input())

ascii_part = range(start, end + 1)

result = ''
for symbol in ascii_part:
    result += f'{chr(symbol)} '

print(result)
