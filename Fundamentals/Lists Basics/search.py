# Search

count = int(input())
word = input()

strings = []
strings_with_word = []

for i in range(count):
    string = input()
    strings.append(string)
    if word in string:
        strings_with_word.append(string)

result = f'{strings}\n{strings_with_word}'

print(result)
