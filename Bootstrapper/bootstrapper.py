import os
import pathlib

fundamentals = [
    {
        "Basic Syntax Conditional Statements and Loops": {
            "Lab": [
                "Biggest Of Three Numbers",
                "Number Definer",
                "Word Reverse",
                "Number Between 1 and 100",
                "Patterns"
            ],
            "Exercises": [
                "Jennys Secret Message",
                "Drink Something",
                "Leonardo DiCaprio Oscars",
                "Double Char",
                "Cannot Sleep Count Sheep",
                "Next Happy Year",
                "Maximum Multiple",
                "Mutate Strings",
                "Easter Cozonacs",
                "Christmas Spirit"
            ],
            "More Exercises": [
                "Find The Largest",
                "Find The Capitals",
                "Wolf In Sheeps Clothing",
                "Sum Of A Beach",
                "How Much Coffee Do You Need"
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
