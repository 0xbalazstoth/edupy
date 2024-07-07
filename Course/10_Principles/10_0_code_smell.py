# Code smell.
# Nehezen érthető, nehezen karbantartható, nehezen bővíthető kód.


# Hosszú függvények, refaktorálható
def calculate_total_price(items, tax_rate):
    total = 0
    for item in items:
        price = item["price"]
        tax = price * tax_rate
        total += price + tax
    return total


# Javított változat
def calculate_item_price_with_tax(item, tax_rate):
    price = item["price"]
    tax = price * tax_rate
    return price + tax


def calculate_total_price(items, tax_rate):
    total = 0
    for item in items:
        total += calculate_item_price_with_tax(item, tax_rate)
    return total


# Duplikált kód
def print_user_details(user):
    print(f"Name: {user['name']}")
    print(f"Email: {user['email']}")
    print(f"Age: {user['age']}")


def print_admin_details(admin):
    print(f"Name: {admin['name']}")
    print(f"Email: {admin['email']}")
    print(f"Age: {admin['age']}")
    print(f"Role: {admin['role']}")


# Javított változat
def print_person_details(person):
    print(f"Name: {person['name']}")
    print(f"Email: {person['email']}")
    print(f"Age: {person['age']}")


def print_admin_details(admin):
    print_person_details(admin)
    print(f"Role: {admin['role']}")


# Magic numbers (varázsszámok)
def calculate_discount(price):
    return price * 0.05  # 5% discount


# Javított változat
DISCOUNT_RATE = 0.05


def calculate_discount(price):
    return price * DISCOUNT_RATE


# Nagy osztályok
class Customer:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.shopping_cart = []
        self.wishlist = []

    def add_to_cart(self, item):
        self.shopping_cart.append(item)

    def add_to_wishlist(self, item):
        self.wishlist.append(item)


# Javított változat
class Customer:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)


class Wishlist:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)


# Felesleges kommentek
# Halott/kikommentelt kódok
# Nem használt importok, változók, függvények
