# Névterek (namespaces)
# https://media.geeksforgeeks.org/wp-content/uploads/types_namespace-1.png
# A Pythonban minden változó egy névtérben van tárolva.
# A névterek a következők lehetnek:
# - Lokális (local): A függvény belsejében definiált változók
# - Enclosing: Beágyazott függvények változói
# - Globális (global): A függvényen kívül definiált változók
# - Beépített (built-in): A Python beépített változói
# A névterek hierarchiában vannak, és a változók a legbelső névterben kerülnek keresésre.
# Ha egy változó nem található a legbelső névterben, akkor a következő névterben kerül keresésre.
# A névtereket a locals() és a globals() függvényekkel lehet lekérdezni.
# A locals() függvény visszaadja a lokális névteret, a globals() függvény pedig a globális névteret.
def my_func():
    x = 10
    print(locals())
    print(globals())


my_func()


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
