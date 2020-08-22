# Biggest Of Three Numbers

first = int(input())
second = int(input())
third = int(input())

result = ''
if first > second and first > third:
    result = first
elif second > first and second > third:
    result = second
else:
    result = third

print(result)
