# Vscode: python inlay hints (function, variable types)

# Típusok:
# Primitív (alaptípusok): Előre meghatározott adattípus:
# Szöveg (Text): str (string)
# Szám (Number): int, float, complex
# Logikai (Boolean): bool
# Értékhiány (None): NoneType

# Nem-primitív (összetett típusok): Előre meghatározott adattípusokból származik, de plusz funkciókkal:
# Szekvencia (Sequence): list, tuple, range
# Szótárak (Mapping): dict
# Halmaz (Set): set, frozenset
# Bináris (Binary): bytes, bytearray, memoryview


# Elnevezési konvenciók
# - Legyen olvasható, könnyen értelmezhető, egyértelmű
# - Konzisztens elnevezési "stílus"
# - Osztályoknál CamelCase
# - Konstansok legyenek NAGYBETŰSEK
# - Változók, függvények, metódusok, modulok, csomagok legyenek kisbetűsek snake_case-el

# Python-ban a változók dinamikus típusúak
# és a változók valójában referencia típusok (tehát hivatkozásokat).

value = "Hello, World!"
print(hex(id(value)))
print(type(value))

print("\n")

value = 10
print(hex(id(value)))
print(type(value))

other_value = value
print(hex(id(other_value)))
print(type(other_value))

value = 11
print(hex(id(value)))
print(type(value))

print("\n")
del value  # Névtérből törlődik csak
# print(value)

# Memóriában még mindig létezik, de innentől kezdve a garbage collectorra van bízva
print(hex(id(other_value)))
print(type(other_value))

# Csharp-ban a változók két fő kategóriába sorolhatók:
# - érték típusok (value types) és referencia típusok (reference types).
#   Az érték típusok közvetlenül a stack memóriában vannak tárolva
# - referencia típusok a heap memóriában vannak, és a hivatkozásuk a stack memóriában van.


message: str = "message"
message = 5  # Fordítási időben még mindig string, de futásidőben már int
