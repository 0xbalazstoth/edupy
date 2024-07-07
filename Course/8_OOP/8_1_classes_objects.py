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
