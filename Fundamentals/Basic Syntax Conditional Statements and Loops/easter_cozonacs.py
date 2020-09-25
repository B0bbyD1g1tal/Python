# Easter Cozonacs

budget = float(input())
flour_price = float(input())

eggs_price = flour_price * 0.75
milk_price = flour_price * 1.25
cozonac_price = flour_price + \
                eggs_price + \
                0.25 * milk_price

money = budget
cozonacs = 0
colored_eggs = 0
while True:
    if money >= cozonac_price:
        money -= cozonac_price
        cozonacs += 1
        colored_eggs += 3

        if cozonacs % 3 == 0:
            colored_eggs -= cozonacs - 2
    else:
        break

result = f'You made {cozonacs} cozonacs! ' \
         f'Now you have {colored_eggs} eggs ' \
         f'and {money:.2f}BGN left.'

print(result)
