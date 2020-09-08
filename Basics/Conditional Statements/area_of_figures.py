# Area of Figures

from math import pi

figure = input()

area = 0
if figure == 'square':
    side = float(input())

    area = side ** 2
elif figure == 'rectangle':
    length = float(input())
    width = float(input())

    area = length * width
elif figure == 'circle':
    radius = float(input())

    area = pi * radius ** 2
elif figure == 'triangle':
    length = float(input())
    height = float(input())

    area = length * height * 0.5

result = f'{area:.3f}'

print(area)
