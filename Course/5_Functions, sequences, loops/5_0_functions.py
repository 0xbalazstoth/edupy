# WET - Write Everything Twice (Írj mindent kétszer)
# - Redundáns kód
# - Ugyanaz a logika többször is megjelenik
print("Hello, World!")
print("Hello, World!")
print("Hello, World!")

# Függvény
# - Egy vagy több utasításokból álló kódblokk
# - Újrafelhasználható
# - Tiszta kód
# - Olvasható, karbantartható

# Szignatúra
# def function_name(param1, param2, ...):
#     pass
# A szignatúra tartalmazza a függvény nevét, a bemeneti paramétereket és a visszatérési értéket.


# DRY - Don't Repeat Yourself (Ne ismételd magad)
# - Redundancia (kódismétlés) csökkentése
# - Minden tudásnak egyetlen, egyértelmű, reprezentációval kell rendelkeznie egy rendszeren belül. - Andy Hunt, Dave Thomas (The Pragmatic Programmer)
def greet():
    print("Hello, World!")


greet()


# Függvény bemeneti paraméterekkel
def greet_person(name):
    print(f"Hello, {name}")


greet_person("Bob")


# Függvény visszatérési értékkel
def add(a: int, b: int) -> int:  # type hinting
    return a + b


result = add(5, 1)
print(result)


# Alapértelmezett paraméterek
def language(name="python"):
    print(f"Language: {name}")


language()
language("csharp")


# Több visszatérési érték és paraméter
def get_full_name(f_name, l_name):
    name = f"{f_name} {l_name}"
    return name, len(name)


name, length = get_full_name("John", "Doe")
print(name, length)


# Függvény dokumentációs string
def get_length(word):
    """This function returns the length of the given word"""
    return len(word)


length = get_length("simple")
print(length)


# Változó hosszúságú paraméterlista
def add(*args):
    return sum(args)


result = add(4, 6)
print(result)


# Kulcs-érték párok fogadása
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="Bob", age="24", city="Budapest")
