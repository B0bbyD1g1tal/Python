# Charity Campaign

CAKE = 45
WAFFLE = 5.8
PANCAKE = 3.2

days = int(input())
cooks = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())

product_expenses = 1 - 1 / 8
result = cooks * days * product_expenses * \
         (cakes * CAKE +
          waffles * WAFFLE +
          pancakes * PANCAKE)

print(result)
