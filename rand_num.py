#go to google and type in python 3 module index
#this will show all modules built into python
import random

class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return (first, second) #returns a tuple


for i in range(3):
    print(random.random()) #returns floating type random numbers

for i in range(3):
    print(random.randint(10,20)) #returns random number from 10 to 20


members = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']

leader = random.choice(members)
print(leader)

#dice program

dice = Dice()

print(dice.roll())




