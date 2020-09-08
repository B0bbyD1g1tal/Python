# Yard Greening

SQUARE_METER_PRICE = 7.61
DISCOUNT = 0.18

area = float(input())

total = area * SQUARE_METER_PRICE
discount = total * DISCOUNT
final_price = total - discount

result = f'The final price is: {final_price} lv.' \
         f'The discount is: {discount} lv.'

print(result)
