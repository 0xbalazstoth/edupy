# Típusok:
# Primitív: Előre meghatározott adattípus
# Nem-primitív: Előre meghatározott adattípusokból származik, de plusz funkciókkal.

# Szöveg (Text): str (string)
# Szám (Number): int, float, complex
# Szekvencia (Sequence): list, tuple, range
# Leképezés (Mapping): dict
# Halmaz (Set): set, frozenset
# Logikai (Boolean): bool
# Bináris (Binary): bytes, bytearray, memoryview
# Értékhiány (None): NoneType

# Elnevezési konvenciók
# - Legyen olvasható, könnyen értelmezhető, egyértelmű
# - Konzisztens elnevezési "stílus"
# - Osztályoknál CamelCase
# - Konstansok legyenek NAGYBETŰSEK

age = 23
pi = 3.14159

# Típus konverzió
# int -> float
age_float = float(age)

# float -> int
pi_int = int(pi)

# int -> str
age_str = str(age)

# str -> int
age = int(age_str)

# [!] Nem lehet komplex számokat más szám típusúvá átalakítani
# end Típus konverzió

# Casting
score = int(5)
# end Casting
