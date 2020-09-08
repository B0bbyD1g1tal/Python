# Salary

banned = {'Facebook': 150,
          'Instagram': 100,
          'Reddit': 50}

tabs = int(input())
salary = int(input())

for tab in range(tabs):
    site = input()
    if site in banned.keys():
        salary -= banned[site]

    if salary <= 0:
        salary = 0
        break

result = f'{salary}' if salary \
    else 'You have lost your salary.'

print(result)
