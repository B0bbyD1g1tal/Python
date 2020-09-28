# Balanced Brackets

OPENING = '('
CLOSING = ')'

lines = int(input())

checker_stack = []

result = ''
for line in range(lines):
    current = input()
    if current == OPENING and not checker_stack:
        checker_stack.append(current)
    elif current == CLOSING and checker_stack:
        checker_stack.pop()
    elif current != OPENING and current != CLOSING:
        continue
    else:
        result = 'UNBALANCED'
        break

if len(checker_stack) == 0:
    result = 'BALANCED'

print(result)
