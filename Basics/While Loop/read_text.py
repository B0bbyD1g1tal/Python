# Read Text

text = input()

result = ''
while text != 'Stop':
    result += f'{text}\n'
    text = input()

print(result)
