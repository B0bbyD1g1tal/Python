# Exam Preparation

unsatisfactory = int(input())

total_score = 0
problems_count = 0
failed = 0
result = ''
problem = ''
while 'Enough' not in problem:
    command = input()

    if 'Enough' in command:
        break
    else:
        problem = command
        score = int(input())

    total_score += score

    if score <= 4:
        failed += 1
        if failed >= unsatisfactory:
            result = f'You need a break, {unsatisfactory} poor grades.'
            break

    problems_count += 1

if not result:
    result = f'Average score: {(total_score / problems_count):.2f}\n' \
             f'Number of problems: {problems_count}\n' \
             f'Last problem: {problem}'

print(result)
