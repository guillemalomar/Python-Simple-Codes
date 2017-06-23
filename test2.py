
for i in range(1,101):
    if i%3==0 or i%5==0:
        to_return = ''
        if i%3==0:
            to_return += 'Fizz'
        if i%5==0:
            to_return += 'Buzz'
    else:
        to_return = str(i)
    print to_return
