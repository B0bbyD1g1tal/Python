# Summer Outfit

grads = int(input())
day_time = input()

outfit = ''
shoes = ''
if 10 <= grads <= 18:
    if day_time == 'Morning':
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif day_time == 'Afternoon' or \
            day_time == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
elif 18 < grads <= 24:
    if day_time == 'Morning' or \
            day_time == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif day_time == 'Afternoon':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
elif grads >= 25:
    if day_time == 'Morning':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif day_time == 'Afternoon':
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
    elif day_time == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'

result = f'It\'s {grads} degrees, ' \
         f'get your {outfit} and {shoes}.'

print(result)
