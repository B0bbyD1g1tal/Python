# Password

user = input()
password = input()
secret = input()

while secret != password:
    secret = input()

print(f'Welcome {user}!')
