# Character Sequence

text = input()

result = ''
for char in range(len(text)):
    result += f'{text[char]}\n'

print(result)
