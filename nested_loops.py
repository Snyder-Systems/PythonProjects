for x in range(4):
    for y in range(3):
        print(f'({x},{y})')


print('\n\n')

#draw F challenge

numbers = [5, 2, 5, 2, 2]

for x in numbers:
    string = ""
    for y in range(x):
        string = string + "x"
    print(string)
