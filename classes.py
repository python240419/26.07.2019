class Car:
    # automatically called
    def __init__(self):
        print("Creating a car...")
    def drive(self):
        print("I am driving...")
    def __private(self):
        print("I am driving...")
toyota = Car()
mitsubishi = Car()
print(type(toyota))

class Dog:
    def __init__(self):
        print("new dog is born...")

    def bark(self):
        print("dog is barking")

rex = Dog()
rex.bark()
bonny = Dog()
bonny.bark()



