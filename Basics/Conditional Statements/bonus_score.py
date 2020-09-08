# Bonus Score

score = int(input())

bonus = 0
if score > 1000:
    bonus = score * 0.1
elif score > 100:
    bonus = score * 0.2
elif score <= 100:
    bonus += 5

if score % 2 == 0:
    bonus += 1
if score % 10 == 5:
    bonus += 2

result = f'{bonus}\n{score + bonus}'

print(result)
