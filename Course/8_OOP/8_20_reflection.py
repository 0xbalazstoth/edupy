# Reflection (Reflexió)
# A reflexió egy olyan programozási technika, amely lehetővé teszi az objektumok introspekción alapuló vizsgálatát és manipulációját.
# A Python egyik legnagyobb ereje a reflexióban rejlik, mivel a nyelv nagyon dinamikus és lehetővé teszi az objektumok módosítását futásidőben.
# A reflexió segítségével az objektumok attribútumait, metódusait és tulajdonságait is megvizsgálhatjuk és módosíthatjuk.


# A Python reflexiós moduljai:
# - type(): Az objektum típusának lekérdezésére használjuk.
class Person:
    pass


person = Person()
print(type(person))

# - isinstance(): Az objektum típusának ellenőrzésére használjuk.
print(isinstance(person, Person))
print(isinstance(person, object))
print(isinstance(person, int))


# - issubclass(): Az osztály leszármazottságának ellenőrzésére használjuk.
class Student(Person):
    pass


print(issubclass(Student, Person))
print(issubclass(Person, Student))


# - callable(): Az objektum hívhatóságának ellenőrzésére használjuk.
def message():
    return "This is a message."


class Greeter:
    def __call__(self):
        return "Greeter class is callable!"


greeter = Greeter()
print(callable(message))
print(callable(greeter))

# Változó hívható-e
number = 10
print(callable(number))


# - getattr(): Az objektum attribútumainak lekérdezésére használjuk.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


car = Car("Nissan", "350z")
print(getattr(car, "brand"))
print(getattr(car, "model"))
print(
    getattr(car, "year", "Unknown")
)  # Ha nincs ilyen attribútum, akkor az alapértelmezett érték jelenik meg.


# - setattr(): Az objektum attribútumainak beállítására használjuk.
setattr(car, "name", "370z")  # Meglévő attribútum értékének módosítása.
print(getattr(car, "name"))

# Új attribútum hozzáadása
setattr(car, "year", 2005)  # Futásidőben hozzáadunk egy attribútumot az objektumhoz.
print(getattr(car, "year"))


# - hasattr(): Az objektum attribútumainak létezésének ellenőrzésére használjuk.
print(hasattr(car, "brand"))
print(hasattr(car, "model"))
print(hasattr(car, "year"))
print(hasattr(car, "name"))
print(hasattr(car, "price"))

# - dir(): Az objektum attribútumainak listázására használjuk.
print(dir(car))
