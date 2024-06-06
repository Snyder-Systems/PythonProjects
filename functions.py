def greet_user():
    print("Hi there!")
    print("Welcome aboard")


def greet_user2(first_name, last_name):
    print(f"Hi there {first_name} {last_name}!")
    print("Welcome aboard")


def square(number):
    return number*number


print("Start") #when you define a function, insert two line breaks afterwards
greet_user()
greet_user2("John", "Smith")
greet_user2(last_name="Smith", first_name="Mary") #function with keyword arguments
print("Finish")


print(square(3))





