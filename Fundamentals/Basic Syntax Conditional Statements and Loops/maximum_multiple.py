# Maximum Multiple

divisor = int(input())
bound = int(input())

number = 0

for number in range(bound, divisor, -1):
    if number % divisor == 0:
        break

print(number)
