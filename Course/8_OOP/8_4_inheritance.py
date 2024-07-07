class Car:
    engine = "3.5L V6"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__serial_number = (
            "12345"  # Privát attribútum, csak az osztályon belül érhető el
        )

    def description(self):
        print(f"Name of the car: {self.name}, age: {20} years.")


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
