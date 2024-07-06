# Dynamic binding (Dinamikus kötés)
# A dinamikus kötés azt jelenti, hogy a változók típusa csak futás közben derül ki.
# Kötődik a polimorfizmushoz, csak a dinamikus kötés egy adott metódus vagy attribútum
# meghatározásának folyamata futásidőben, nem pedig fordítási időben.


# Példa
class Animal:
    def sound(self):
        return "Animal sound"


class Dog(Animal):
    def sound(self):
        return "Dog sound"


class Cat(Animal):
    def sound(self):
        return "Cat sound"


animals = [Dog(), Cat()]
for animal in animals:
    print(animal.sound())


# Metódus hozzárendelése futásidőben
import types


def dog_name(self):
    return "Dog Name"


dog = Dog()
dog.dog_name = types.MethodType(dog_name, dog)
print(dog.dog_name())


# Változó hozzárendelése futásidőben
class Goat:
    pass


goat = Goat()
goat.name = "Goat Name"
print(goat.name)
