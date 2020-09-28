# Decrypting Messages

key = int(input())
lines = int(input())

result = ''
for line in range(lines):
    character = ord(input())
    result += f'{chr(character + key)}'

print(result)
