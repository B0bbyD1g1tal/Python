# Find The Capitals

text = input()

upper_indices = []
for letter in range(len(text)):
    if text[letter].isupper():
        upper_indices.append(letter)

print(upper_indices)
