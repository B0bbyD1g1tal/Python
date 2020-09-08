# Godzilla vs Kong

budget = float(input())
supernumerary = int(input())
clothes = float(input())

decoration = 0.1 * budget
clothing = 0.9 * clothes * supernumerary \
    if supernumerary > 150 \
    else clothes * supernumerary
total = decoration + clothing
diff = abs(budget - total)

result = f'Action!\n' \
         f'Wingard starts filming with {diff:.2f} leva left.' \
    if budget >= total \
    else f'Not enough money!\n' \
         f'Wingard needs {diff:.2f} leva more.'

print(result)
