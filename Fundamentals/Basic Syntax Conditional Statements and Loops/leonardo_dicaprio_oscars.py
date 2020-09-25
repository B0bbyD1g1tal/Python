# Leonardo DiCaprio Oscars

oscar = int(input())

result = ''
if oscar == 88:
    result = 'Leo finally won the Oscar! Leo is happy'
elif oscar == 86:
    result = 'Not even for Wolf of Wall Street?!'
elif oscar != 86 and oscar < 88:
    result = 'When will you give Leo an Oscar?'
else:
    result = 'Leo got one already!'

print(result)
