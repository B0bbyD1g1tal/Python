# Mutate Strings

first = input()
second = input()

length = len(first)
mutant = first
results = []
for index in range(length):
    mutant = f'{mutant[:index]}{second[index]}{mutant[index + 1:]}'
    if mutant != first and mutant not in results:
        results.append(mutant)

result = '\n'.join(results)

print(result)
