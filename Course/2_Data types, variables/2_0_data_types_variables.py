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
