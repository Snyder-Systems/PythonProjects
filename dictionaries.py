customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer["name"]) #will print what is saved in name in the dictionary customer

customer.get("birthdate", "Jan 1 1980") #will look for "birthdate" in the dictionary and if it doesn't find it, will return defuault value "Jan 1 1980

customer["name"] = "Jack Smith"


customer["birthdate"] = "Jan 1 1980" #will add and define birthdate with Jan 1 1980 to customer dictionary



#Program that takes phone numbers as an input and returns the words for the number

numbers = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero"
    }

string = input('Enter Phone number here: ')
num_string = ""
for element in string:
    num_string = num_string + " " + numbers[element]

print(num_string)


#program that displays emojis
message = input(">")

words = message.split(' ') #split will seperate elements in list by input in parenthesis, in this case a space

emojis = {
    ":)": "🙂",
    ":(": "☹️"
}

output = ""

for word in words:
    output += emojis.get(word, word) + " "

print(output)


