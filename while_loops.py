
size = int(input('Enter a size for the pyramid: '))
i = 1
while i <= size:
    print('*' * i)
    i += 1
print('done')


#car game using while loop

command = ""
started = False
while command != "quit":
    command = input("> ").lower() #we use lower here to make sure input is always lower case
    if command == "start":
        if started:
            print("Car is already started")
            continue
        started = True
        print("Car Started...")
    elif command == "stop":
        if not started:
            print('Car is not started')
            continue
        started = False
        print("Car stopped.")
    elif command == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit
        """)
    elif command == "quit":
        break

    else:
        print("I don't understand that")
