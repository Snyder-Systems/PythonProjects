#type conversion
birth_year = input('Birth year: ')
print(type(birth_year)) #prints the variable type
age = 2024 - int(birth_year) #type conversion


print(type(age))
print(birth_year + ' is the patients birth year, which means they are ', age, ' years old')




name = input('Enter the patients name\n')  #string
age = input('Enter the patients age\n')  #integer
new = False #boolean

if new:
    print(name, ' is a new patient age ', age)
else:
    print(name + ' is not a new patient age ', age)


