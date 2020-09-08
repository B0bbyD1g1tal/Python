# Cinema Tickets

movie = input()

standard = 0
students = 0
kids = 0

result = ''
while movie != "Finish":
    seats = int(input())
    tickets = 0
    while tickets < seats:
        ticket = input()

        if ticket == "standard":
            tickets += 1
            standard += 1
        elif ticket == "student":
            tickets += 1
            students += 1
        elif ticket == "kid":
            tickets += 1
            kids += 1
        elif ticket == "End":
            break

    result += f'{movie} - {(tickets * 100 / seats):.2f}% full.\n'
    movie = input()

all_tickets = standard + students + kids
student_percentage = students * 100 / all_tickets
standard_percentage = standard * 100 / all_tickets
kid_percentage = kids * 100 / all_tickets

result += f'Total tickets: {all_tickets}\n' \
          f'{student_percentage:.2f}% student tickets.\n' \
          f'{standard_percentage:.2f}% standard tickets.\n' \
          f'{kid_percentage:.2f}% kids tickets.'

print(result)
