# Inheritance
# Reuse code from another class - use methods - save time

class Animal():
    def __init__(self):
        print("animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")
# Create another class - passing in the other class of animal
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("DOG CREATED")

## new method of bark
    def bark(self):
        print("WOOF")

# method to over write eating
    def eat(self):
        print("Dog Eating")
# to over write an

#instantiate Animal- changed to Dog -
# inialitizes animal - creates class of dog inside

mydog = Dog()
mydog.whoAmI()
mydog.eat()
mydog.bark()
#mydog.bark()
# Special methods
