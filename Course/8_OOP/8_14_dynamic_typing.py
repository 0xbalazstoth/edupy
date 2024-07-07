# Duck typing (Ha úgy jár, mint egy kacsa, úgy úszik, mint egy kacsa, és úgy hápog, mint egy kacsa, akkor valószínűleg kacsa.)
# - Programozásban ez úgy értelmezhető, hogy ha egy objektum rendelkezik a szükséges metódusokkal és tulajdonságokkal, akkor használható az adott helyen,
#   akkor kezelhető úgy, mintha egy adott típusú objektum lenne, anélkül, hogy formálisan deklarálnánk annak típusát.
# Például: Ha van egy "CreditCard" osztály, akkor elvárjuk, hogy az osztály rendelkezzen olyan metódusokkal, mint a "pay" és a "get_balance" például.
# A Duck typing inkább a kényelemről szól, mintsem a biztonságról, mivel a típushibák csak futás közben derülnek ki.


class CreditCard:
    def pay(self, amount):
        print(f"Paid {amount} with credit card.")

    def get_balance(self):
        return 1000


class DebitCard:
    def pay(self, amount):
        print(f"Paid {amount} with debit card.")

    def get_balance(self):
        return 500


class Wallet:
    def pay(self, amount):
        print(f"Paid {amount} with wallet.")

    def get_balance(self):
        return 200


def pay_with_card(card, amount):
    card.pay(amount)
    print(f"Balance: {card.get_balance()}")
    print()


credit_card = CreditCard()
debit_card = DebitCard()
wallet = Wallet()

pay_with_card(credit_card, 100)
pay_with_card(debit_card, 50)
pay_with_card(wallet, 150)


# Goose typing (Nem egy hivatalos kifejezés, csak egy gúny verziója a Duck typing-nek)
# - A Goose typing egy olyan programozási stílus, amely a Duck typing és a statikus típusozás között helyezkedik el.
# - Gondolhatunk rá úgy, mint "szigorúbb" goose typing, ahol az objektumoknak ugyanúgy meg kell felelniük bizonyos elvárásoknak, de
#   szigorúbb típusellenőrzéssel.


# Példa
def pay_with_card(card, amount):
    if not hasattr(card, "pay") or not hasattr(card, "get_balance"):
        raise TypeError("The object does not have the required methods.")
    card.pay(amount)
    print(f"Balance: {card.get_balance()}")
    print()


class Bitcoin:
    def pay(self, amount):
        print(f"Paid {amount} with Bitcoin.")


credit_card = CreditCard()
debit_card = DebitCard()
wallet = Wallet()

pay_with_card(credit_card, 100)
pay_with_card(debit_card, 50)
pay_with_card(wallet, 150)

try:
    pay_with_card(Bitcoin(), 200)
except TypeError as e:
    print(e)


# Dynamic typing (Dinamikus típusozás)
# A Python egy dinamikusan típusozott nyelv, ami azt jelenti, hogy a változók típusa csak futás közben derül ki.
# A változók típusa a hozzárendelt értéktől függ.
# Hátránya, hogy a típushibák csak futás közben derülnek ki.
# Vizualizálva: https://www.pythontutorial.net/advanced-python/dynamic-typing-in-python/


# Módszerenek ennek kiküszöbölésére:
# Type hinting (Típusmegjelölés)
# - A típusmegjelölés egy olyan technika, amely segítségével a változók és a függvények típusát megjelölhetjük.
def add(x: int, y: int) -> int:
    return x + y


print(add(10, 20))


# Try, except blokkok használata
def safe_add(x, y):
    try:
        return x + y
    except TypeError:
        return None


print(safe_add(10, 22))


# isinstance() függvény használata
def safe_multiply(x, y):
    if not isinstance(x, int) or not isinstance(y, int):
        return None
    return x * y


print(safe_multiply(10, 20))


# mypy használata statikus típusellenőrzésre
# - A mypy egy olyan eszköz, amely segítségével a Python kódunkat statikusan ellenőrizhetjük.
# - Telepítés: pip install mypy


def divide(x: int, y: int) -> float:
    return x / y


print(divide(10, "2"))
