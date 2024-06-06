#String Indexes
start = 'Python for Beginners'


print(start[0:3])

print(start[:])

print(start[1:-1])

#formatting strings
first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder' #formatted string

print(msg)

#string methods
course = 'Python for beginners'
print(len(course)) #prints the length of the string

print(course.upper()) #converts string to uppercase
print(course.lower()) #converts string to lowercase

print(course.find('P')) #this will return the index of the first occurence of this character

print(course.replace('beginners', 'Abosolute Beginners')) #this will replace the first with the second in the string

print('Python' in course) # will return True if the string is found in the variable course



