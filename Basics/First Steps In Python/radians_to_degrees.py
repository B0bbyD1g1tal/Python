# Radians to Degrees

from math import pi, floor

radians = float(input())

degrees = radians * 180 / pi
result = floor(degrees)

print(result)
