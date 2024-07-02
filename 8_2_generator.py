# Generator
# A generátorok olyan függvények, amelyek lehetővé teszik a sorozatok elemenkénti létrehozását és visszatérését,
# - anélkül, hogy előre kiszámítanák és tárolnák az összes elemet a memóriában.
# Ezt a yield kulcsszóval érjük el.


def number_generator(n: int):
    for i in range(n):
        yield i


# Használat
gen = number_generator(5)

for number in gen:
    print(number)
