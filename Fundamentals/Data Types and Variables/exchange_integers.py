# Exchange Integers

a = int(input())
b = int(input())

result = f'Before:\n' \
         f'a = {a}\n' \
         f'b = {b}\n'

a, b = b, a

result += f'After:\n' \
          f'a = {a}\n' \
          f'b = {b}'

print(result)
