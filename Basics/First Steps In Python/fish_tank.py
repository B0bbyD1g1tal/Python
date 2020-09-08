# Fish Tank

length = float(input())
width = float(input())
height = float(input())
percent = float(input())

volume = length * width * height * 0.001
empty_volume = volume * (1 - percent * 0.01)

print(empty_volume)
