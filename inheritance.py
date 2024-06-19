class Animal:
    hasScales = True
    def sound(self):
        print("animal is swimming")
# child class
class Duck(Animal):
    hasWings = True
    def move(self):
        print("duck is swimming")

class Mouse:
    def move(self):
        print("mouse is walking")

a = Animal()

d = Duck()

m = Mouse()








