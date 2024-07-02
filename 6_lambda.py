# Lambda egy anonymus függvény
# Bármennyi argumentuma lehet, de egy kifejezése lehet csak
# Szintaxis: lambda argumentumok : kifejezés

result = lambda n: n * 2
print(result(5))

# Lambda függvény, amely visszaadja a nagyobb számot
max_number = lambda x, y: x if x > y else y
result = max_number(10, 15)
print(result)

# Rendezés az első elem szerint
points = [(2, 3), (4, 1), (3, 7), (1, 5)]
points_sorted = sorted(points, key=lambda point: point[0])
print(points_sorted)

# Páros számok szűrése
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Minden szám négyzetének kiszámítása
squares = list(map(lambda x: x**2, numbers))
print(squares)
