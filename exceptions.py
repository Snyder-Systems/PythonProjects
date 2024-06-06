try: #try these lines of code
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError: #if we encounter this error, instead of crashing the program, display this
    print('Invalid value')

#you can find these error values in the terminal when your program crashes

