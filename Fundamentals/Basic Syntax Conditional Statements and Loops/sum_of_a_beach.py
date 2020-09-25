# Sum Of A Beach

STRINGS = ["sand", "water", "fish", "sun"]

text = input()

l_text = text.lower()
occurrences = 0

for word in STRINGS:
    start = 0
    while True:
        start = l_text.find(word, start)
        if start == -1:
            break
        else:
            occurrences += 1
            start += len(word)

print(occurrences)
