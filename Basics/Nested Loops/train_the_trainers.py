# Train The Trainers

jury_members = int(input())
presentation = input()

grades_total = 0
presentations = 0
result = ''
while presentation != 'Finish':
    presentations += 1
    presentation_grade = 0
    for jury in range(jury_members):
        grade = float(input())
        presentation_grade += grade

    presentation_average = presentation_grade / jury_members
    result += f'{presentation} - {presentation_average:.2f}.\n'

    grades_total += presentation_average

    presentation = input()

total_grades = grades_total / presentations
result += f"Student's final assessment is{total_grades: .2f}."

print(result)
