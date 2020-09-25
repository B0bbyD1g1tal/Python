# Wolf In Sheeps Clothing

WOLF = 'wolf'

animals = input()

herd = animals.split(', ')
herd_last = len(herd) - 1
wolf = herd.index(WOLF)

result = 'Please go away and stop eating my sheep' if wolf == herd_last \
    else f'Oi! Sheep number {herd_last - wolf}! ' \
         f'You are about to be eaten by a wolf!'

print(result)
