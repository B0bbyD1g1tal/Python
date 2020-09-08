# Projects Creation

PROJECT_TIME = 3

name = input()
projects_count = int(input())

hours = projects_count * PROJECT_TIME

result = f'The architect {name} ' \
         f'will need {hours} hours ' \
         f'to complete {projects_count} project/s.'

print(result)
