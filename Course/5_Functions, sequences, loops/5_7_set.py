# Set (halmaz)
# Egyedi elemek csak, mutable, elemek sorrendje nem garantált, set elemei hash-elhetők kell legyenek
unique_numbers = {1, 2, 3, 4, 5}

# Elem hozzáadása
unique_numbers.add(6)

# Elem eltávolítása
unique_numbers.remove(3)

# Elem eltávolítása, nem érdekel hogy benne van-e vagy sem
unique_numbers.discard(3)

# Összes elem eltávolítása
unique_numbers.clear()

# Halmazműveletek
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Unió
union = set1 | set2  # VAGY unique_numbers.union(set1)
print(union)

# Metszet
intersection = set1 & set2  # VAGY unique_numbers.intersection(set1)
print(intersection)

# Különbség
difference = set1 - set2  # unique_numbers.difference(set1)
print(difference)

# Szimmetrikus különbség
symmetric_difference = set1 ^ set2  # unique_numbers.symmetric_difference(set1)
print(symmetric_difference)

# Frozen set
# Halmaz, immutable
frozen_set = frozenset([6, 7, 8, 9, 10])
