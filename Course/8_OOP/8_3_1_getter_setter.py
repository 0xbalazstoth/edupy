# Getter és setter
# - Getter: Az attribútum értékének lekérdezése
# - Setter: Az attribútum értékének beállítása
# - Property: Az attribútumot úgy állíthatjuk be, hogy a getter és setter metódusokat hívja meg


# Példa
class Car:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def description(self):
        return f"Name of the car: {self.name}, age: {self.age} years."

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color


car = Car("Nissan 350z", 20)
car.color = "red"
print(car.description)
print(car.color)
