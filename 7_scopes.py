# Scope (hatókör)
# Meghatározza, hogy egy változó mikor és hol érhető el a kódban.
# Lokális (local scope): Egy függvény belsejében definiált változók csak azon függvény belsejében érhetők el
def my_func():
    x = 10
    print(x)


my_func()
# print(x) # Hibát okoz, mert x nincs definiálva globális scope-ban

# Globális (global scope): Globális változókat a függvényen kívül hozunk létre, és azok az egész kódban elérhetőek
z = 20


def other_func():
    print(z)


other_func()
print(z)


# Beágyazott (enclosing scope): Egy beágyazott függvény hozzáférhet a külső függvény változóihoz
def outer_func():
    y = 30  # Beágyazott scope

    def inner_func():
        print(y)

    inner_func()


outer_func()
# print(y) Hibát okoz, mert y nincs definiálva globális scope-ban

# Beépített (built-in scope): Beépített scope olyan funkciókat és változókat tartalmaz, amiket a Python biztosít.
print(len("Word"))
