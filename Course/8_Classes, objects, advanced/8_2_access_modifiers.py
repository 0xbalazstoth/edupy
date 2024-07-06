# Access modifiers (Láthatósági módosítók)
# - Public: Minden osztályból elérhető
# - Protected: Csak az osztályból és a leszármazott osztályokból elérhető (Python-ban ez csak konvenció)
# - Private: Csak az osztályból elérhető


# Példa
class Car:
    def __init__(self, name, color):
        self.name = name
        self._color = color
        self.__year = 2021

    def description(self):
        print(
            f"Name of the car: {self.name}, color: {self._color}, year: {self.__year}"
        )


# Példa
car = Car("Nissan 350z", "red")
car.description()

# Példa
print(car.name)
print(car._color)

# Name mangling (Név átírás)
# - A Python a privát változókat nehezíti meg az elérésüket a külvilág számára
# - A privát változók neve elé egy _ és az osztály neve kerül
# - Például: _Car__color
# - A változók elérése a következőképpen történik: objektum._Osztály__változó
# - Például: car._Car__color = "red"
# - A name mangling nem biztonsági funkció, csak egy konvenció

# print(car.__year)  # Nem elérhető
print(car._Car__year)  # Name mangling
# car._Car__year = 2022
# print(car._Car__year)

# Példa
car._color = "blue"
car.description()

# Példa
car._Car__year = 2022
car.description()
# car.__year = 2022  # Nem elérhető
# car.description()
