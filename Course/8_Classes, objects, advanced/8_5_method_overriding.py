# Method overriding (Metódus felülírás)
# Az osztályokban lévő metódusokat felül lehet írni az osztályok közötti hierarchiában.
# Azért lehet rá szükség, mert a szülőosztályban lévő metódus és a gyermekosztályban lévő metódus nem feltétlenül ugyanazt a műveletet végzi.
# A metódus felülírás során a gyermekosztályban lévő metódus felülírja a szülőosztályban lévő metódust.


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


# Példa
dog = Dog()
print(dog.sound())

cat = Cat()
print(cat.sound())


# Beépített metódusok felülírása
# Felülírás akkor ajánlott, ha sajátos viselkedést szeretnénk megvalósítani az adott osztályban
# __str__() metódus: Az objektum sztring reprezentációját adja vissza
# __len__() metódus: Az objektum hosszát adja vissza
# __del__() metódus: Az objektum törlésekor fut le
# __add__() metódus: Az objektumok összeadásakor fut le
# __sub__() metódus: Az objektumok kivonásakor fut le
# __mul__() metódus: Az objektumok szorzásakor fut le


# Példa
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

    def __len__(self):
        return self.age

    def __del__(self):
        print("Object deleted")

    def __add__(self, other):
        return self.age + other.age

    def __sub__(self, other):
        return self.age - other.age

    def __mul__(self, other):
        return self.age * other.age


# Példa
person = Person("John", 30)
print(person)

print(len(person))

# del person

person1 = Person("John", 30)
person2 = Person("Doe", 40)

print(person1 + person2)
print(person1 - person2)
print(person1 * person2)
