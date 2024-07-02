# Függvény
def greet():
    print("Hello, World!")


greet()


# Függvény bemeneti paraméterekkel
def greet(name):
    print(f"Hello, {name}")


greet("Bob")


# Függvény visszatérési értékkel
def add(a: int, b: int) -> int:
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


# Beágyazott függvények
def outer_function(text):
    def inner_function():
        print(text)

    inner_function()


outer_function("Hello from the inner function!")
