# Duck typing (Ha úgy jár, mint egy kacsa, úgy úszik, mint egy kacsa, és úgy hápog, mint egy kacsa, akkor valószínűleg kacsa.)
# - Programozásban ez úgy értelmezhető, hogy ha egy objektum rendelkezik a szükséges metódusokkal és tulajdonságokkal, akkor használható az adott helyen,
#   akkor kezelhető úgy, mintha egy adott típusú objektum lenne, anélkül, hogy formálisan deklarálnánk annak típusát.
# Például: Ha van egy "Book" osztály, akkor elvárjuk, hogy az osztály rendelkezzen egy "title" és egy "author" tulajdonsággal például,
#          adja vissza a könyv címét és szerzőjét, esetleg oldalak számát.
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

# Csharp kód példa rá, csak hogy hogyan néz ki egy erősen típusos nyelvben:
# int number = 5;
# string text = "Hello";
# number = "World";  // Fordítási hiba
# text = 10;  // Fordítási hiba

# Python kód példa:
text = "Hello"

# Bizonyítás, hogy a változók típusa futás közben derül ki
print(type(text))  # <class 'str'>
print("id of text:", id(text))
# https://www.tutorialspoint.com/python/python_dynamic_typing.htm
