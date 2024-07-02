# Python egy objektum orientált programozási nyelv (OOP)
# Tehát vannak objektumok, függvények


# Osztály
# Amolyan sablon, ami meghatározza, milyen tulajdonságokkal és viselkedéssel rendelkezik az adott típusú objektum
class Car:
    # Osztályszintű attribútum: Attribútumok olyan változók, amik az osztályhoz vagy objektumhoz tartoznak
    engine = "3.5L V6"

    # Konstruktor: Az osztály példányosításakor fut le, inicializációs blokk
    # Dunder (Double underscore) __init__(), __add__, stb
    def __init__(
        self, name, age
    ):  # self paraméter egy hivatkozás az osztály aktuális példányára, és az osztályhoz tartozó változók elérésére szolgál, lehet más a neve is
        self.name = name
        self.age = age

    def description(self):
        print(f"Name of the car: {self.name}, age: {20} years.")


# Objektum példányosítás
# Objektumokat hozunk létre az osztályból
car = Car("Nissan 350z", 20)
car.description()


# Öröklődés (Inheritance)
# Öröklődés segítségével új osztályokat hozhatunk létre meglévő osztályokból, örökölve azok tulajdonságait és metódusait
# Szülő -> gyermek kapcsolat, örököl tulajdonságokat a gyermek a szülőtől
class Sport(Car):
    def get_engine(self):
        print(f"Engine: {self.engine}")


sport_car = Sport("Nissan 350z", 20)
sport_car.description()
sport_car.get_engine()


# Többszörös öröklődés
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass

    def __str__(self):
        return f"{self.name}, sound: {self.sound()}"


class Dog(Animal):
    # def __init__(self): A gyermek __init__() függvénye felülírja a szülő __init__() függvényét
    #     print(self.name)

    def sound(self):
        return "Dog sound"


class Cat(Animal):
    def sound(self):
        return "Cat sound"


dog = Dog("DogName")
print(dog.sound())

cat = Cat("CatName")
print(cat.sound())


# super()
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)  # Szülő teljes tulajdonságainak öröklődése
        self.department = department

    def get_details(self):
        return super().get_details() + f", Department: {self.department}"


# Objektum létrehozása és metódusok hívása
employee = Employee("Alice", 50000)
manager = Manager("Bob", 80000, "HR")
print(employee.get_details())
print(manager.get_details())

# Polimorfizmus
# A polimorfizmus lehetővé teszi, hogy azonos metódusokat hívjunk meg különböző osztályok példányain
animals = [Dog("DogName"), Cat("CatName")]
for animal in animals:
    # print(f"{animal.name}, sound: {animal.sound()}")
    print(animal)
