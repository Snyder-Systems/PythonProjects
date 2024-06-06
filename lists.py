names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']

print(names)

print(names[-1]) #prints last item

print(names[-2]) #prints 2nd to last item

print(names[:]) #prints all elements in list

names[0] = 'Jon' # changes element 0 to Jon
print('\n')
#finding the largest number in a list

numbers = [3, 6, 2, 8, 23, 4, 10]

max = numbers[0]

for x in numbers:
    if x > max:
        max = x

print(max)
print('\n')

#2D lists

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[0][1]) #prints the first row, second column element
print('\n')
for row in matrix:
    for item in row:
        print(item)

print('\n')
#list methods

numbers.append(20) #this will add 20 to the end of the list
print(numbers)


numbers.insert(0,10) #this will replace the first element with 10
print(numbers)

print(numbers.pop()) #will pop out the last item in the list, can specify index of removed number

print(numbers.index(6)) #will return the index of the first occurence in the number

print(numbers.count(6)) #will return how many elements 6 are in the list

print(numbers.sort()) #will sort numbers in ascending order

print(numbers.reverse()) #this will reverse the order of elements. When used after sort will produce descending order list

numbers2 = numbers.copy() #will copy the list numbers to numbers2

print(numbers.clear()) #will clear the list

print('\n')
#removes duplicates in a list
list = [1, 3, 8, 5, 3, 3, 2, 9, 2, 1]
print(f'Program that removes duplicates in a list:\n\nList before:{list} \n\n')

for x in list:
    while list.count(x) > 1:
        list.pop(list.index(x))

print(f'List after removing duplicates:{list}')

#tuples

list_tuple = (1, 3, 4) #tuples are immutable, lists that cannot be changed

x, y, z = list_tuple #this will set x = 1, y = 3, z = 4. this is an example of unpacking

