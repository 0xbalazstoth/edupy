# Metaclasses (Metaosztályok)
# A metaclasses egy olyan osztály, amely egy másik osztályt reprezentál.
# A metaclasses használatakor az osztályokat egy másik osztály példányaként hozzuk létre.
# A metaclasses használatakor a metaclass attribútumot kell megadni az osztály definíciójában.
# A metaclasses használatakor a metaclass __new__ metódusát kell felülírni.
# A metaclasses használatakor a metaclass __new__ metódusának vissza kell térnie egy osztály példánnyal.
# A metaclasses használatakor a metaclass __init__ metódusát is felül lehet írni.
# A metaclasses használatakor a metaclass __init__ metódusa az osztály példányát kapja, amelyet inicializál.
# A metaclasses használatakor a metaclass __init__ metódusa nem tér vissza semmivel.


class RemoveSpaces(type):
    def __new__(cls, name, bases, dct):
        new_dct = {}
        for attr, value in dct.items():
            if isinstance(value, str):  # Ha a value string típusú
                new_value = value.replace(" ", "")
                new_dct[attr] = new_value
            else:
                print(f"Attribute is not a string. {attr}: {value}")
                new_dct[attr] = value
        return super().__new__(cls, name, bases, new_dct)


class Text(metaclass=RemoveSpaces):
    title = "Python Programming Language"
    author = "Guido van Rossum"
    description = "Python is a high-level programming language."
    release_date = 1991


text = Text()
print(text.title)
print(text.author)
print(text.description)
print(text.release_date)
