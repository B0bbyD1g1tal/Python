import os
import pathlib

fundamentals = [
    {
        "Lists Basics": {
            "Lab": [
                "Strange Zoo",
                "Courses",
                "List Statistics",
                "Search",
                "Numbers Filter"
            ],
            "Exercises": [
                "Invert Values",
                "Multiples List",
                "Football Cards",
                "Number Beggars",
                "Faro Shuffle",
                "Survival of the Biggest",
                "Easter Gifts",
                "Seize the Fire",
                "Hello France",
                "Bread Factory"
            ],
            "More Exercises": [
                "Zeros to Back",
                "Tic-Tac-Toe",
                "Josephus Permutation",
                "Battle Ships",
                "Hungry Hippos"
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
