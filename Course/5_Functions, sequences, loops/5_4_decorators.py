# Dekorátor
# - Olyan függvények, amelyek módosítják egy másik függvény működését, anélkül, hogy azt megváltoztatnák.


# Egyszerű dekorátor
def fc_barcelona(func):
    def wrapper():
        print("Visca el", end=" ")
        func()

    return wrapper


@fc_barcelona
def club():
    print("Barca")


club()


# Dekorátor paraméterrel
def get_result(func):
    def wrapper(a, b):
        print(f"Arguments: {a}, {b}")
        result = func(a, b)
        print(f"Result: {result}")
        return result

    return wrapper


@get_result
def add(a, b):
    return a + b


add(2, 3)


# Osztály dekorátor
# - Egy osztályban található metódusokat tudunk például hozzáadni.
def add_animal(cls):
    def new_animal(self, animal):
        return f"New animal added: {animal}"

    cls.new_animal = new_animal
    return cls


@add_animal
class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


animal = Animal("Dog")
print(animal.get_name())
print(animal.new_animal("Horse"))


# Dekorátorok egymásba ágyazása
def uppercase(func):
    def wrapper(text):
        result = func(text)
        return result.upper()

    return wrapper


def lowercase(func):
    def wrapper(text):
        result = func(text)
        return result.lower()

    return wrapper


def remove_space(func):
    def wrapper(text):
        result = func(text)
        return result.replace(" ", "")

    return wrapper


# @uppercase
@lowercase
@remove_space
def text(text):
    return text


result = text("Hello World")
print(result)
