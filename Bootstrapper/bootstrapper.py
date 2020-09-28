import os
import pathlib

fundamentals = [
    {
        "Data Types and Variables": {
            "Lab": [
                "Concat Names",
                "Centuries to Minutes",
                "Special Numbers",
                "Convert Meters to Kilometers",
                "Pounds to Dollars"
            ],
            "Exercises": [
                "Integer Operations",
                "Chars to String",
                "Elevator",
                "Sum of Chars",
                "Print Part of the ASCII Table",
                "Triples of Latin Letters",
                "Water Overflow",
                "Party Profit",
                "Snowballs",
                "Gladiator Expenses"
            ],
            "More Exercises": [
                "Biggest of 3 Numbers",
                "Exchange Integers",
                "Prime Number Checker",
                "Decrypting Messages",
                "Balanced Brackets"
            ]
        }
    }
]
course_path = "/home/b0bby/Code/Python/Fundamentals/"
for lecture in fundamentals:
    for lecture_name, lecture_content in lecture.items():
        lecture_dir = pathlib.Path(course_path, lecture_name)
        os.makedirs(lecture_dir)
        with open(f'{lecture_dir}/README.md', 'w+') as readme:
            readme.write(f'# {lecture_name}\n')
            for tasks in lecture_content:
                readme.write(f'\n## {tasks}\n')
                readme.write(f'### [{tasks} tasks](./)\n\n')
                problems = lecture_content[tasks]
                for problem in enumerate(problems, start=1):
                    file_name = f'{problem[1].replace(" ", "_").lower()}.py'
                    with open(f'{lecture_dir}/{file_name}', 'w+') as solution:
                        solution.write(f'# {problem[1]}\n')
                        solution.close()
                    readme.write(
                        f'{problem[0]}. [{problem[1]}](./{file_name})\n')
        readme.close()
