# Journey

budget = float(input())
season = input()

result = 'Somewhere in '
if budget <= 100:
    result += 'Bulgaria\n'
    result += f'Camp - {(budget * 0.3):.2f}' \
        if season == 'summer' \
        else f'Hotel - {(budget * 0.7):.2f}'
elif 100 < budget <= 1000:
    result += 'Balkans\n'
    result += f'Camp - {(budget * 0.4):.2f}' \
        if season == 'summer' \
        else f'Hotel - {(budget * 0.8):.2f}'
else:
    result += f'Europe\nHotel - {(budget * 0.9):.2f}'

print(result)
