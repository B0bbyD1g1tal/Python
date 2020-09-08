# Vowels Sum

vowels = {'a': 1,
          'e': 2,
          'i': 3,
          'o': 4,
          'u': 5}

text = input()

total = 0
for letter in text:
    if letter in vowels:
        total += vowels[letter]

print(total)
