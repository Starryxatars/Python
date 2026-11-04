class Animal:
    def sound(self):
        print("Some generic animal sound")


class Dog(Animal):
    def sound(self):
        print("Dog says: Woof! Woof!")


class Cat(Animal):
    def sound(self):
        print("Cat says: Meow!")


class Cow(Animal):
    def sound(self):
        print("Cow says: Moo!")


class Lion(Animal):
    def sound(self):
        print("Lion says: Roar!")


for animal in (Dog(), Cat(), Cow(), Lion()):
    animal.sound()
