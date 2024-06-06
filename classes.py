class Point:
    def __init__(self, x, y): #this will be called when we initialize the class
        self.x = x          #constructor 1
        self.y = y          #constructor 2
    def move(self):
        print("move")
    def draw(self):
        print("draw")


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


class mammal:
    def walk(self):
        print("walk")


class Dog(mammal): #example of inheritance
    pass #pass this line don't worry about it. Makes python happy bc empty classes are a no no


class Cat(mammal): #example of inheritance
    pass

point1 = Point(10,20)
point1.x = 10  #variables exclusive to class Point
point1.y = 20
point1.draw()

point2 = Point(20, 30) #second separate close

john = Person("John Smith")
john.talk()

bob = Person("Bob Smith")
bob.talk()



#inheritence

#dog and cat class inherit walk method from mammal class

dog1 = Dog()
dog1.walk()


