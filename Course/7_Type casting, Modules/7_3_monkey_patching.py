# Monkey patching
# A Monkey pathcing egy olyan technika, amely lehetővé teszi egy modul vagy osztály működésének módosítását futásidőben.
# Gyakori alkalmazásai:
# - Hibajavítás: Ha egy modulban vagy osztályban hibát találunk, akkor a monkey patching segítségével javíthatjuk azt.
# - Funkciók bővítése: Ha egy modulban vagy osztályban hiányzik egy funkció, akkor azt a monkey patching segítségével hozzáadhatjuk.
# - Tesztelés: A tesztelés során a monkey patching segítségével módosíthatjuk a modulok vagy osztályok működését, hogy könnyebben
#   tesztelhetőek legyenek.

import math_module as mm

try:
    print(mm.divide(10, 0))
except ZeroDivisionError as e:
    print(f"Error: {e}")

# Bug fix:


def safe_divide(x: int, y: int) -> float:
    """Safe divide that handles division by zero

    Args:
        x (int): x number
        y (int): y number

    Returns:
        float: Quotient of x and y numbers
    """
    if y == 0:
        print("Hiba: Nullával való osztás")
        return None
    return x / y


mm.divide = safe_divide
print(mm.divide(10, 0))


# Bővítés
def multiply(x: int, y: int) -> int:
    """description

    Args:
        x (int): x number
        y (int): y number

    Returns:
        int: Product of x and y numbers
    """
    return x * y


mm.multiply = multiply
print(mm.multiply(3, 4))
