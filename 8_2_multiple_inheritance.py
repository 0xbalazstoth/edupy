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
