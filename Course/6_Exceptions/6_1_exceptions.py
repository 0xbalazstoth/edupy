# Kivételkezelés: Lehetséges hibákra való előkészület
# Kivételkezelési blokkok:
# try: Itt fut le a kód, ami lehet hibát fog dobni
# except: Ahol az elkapott hibát dolgozzuk fel, amiket a try blokkban kaptunk
# else: Csak akkor fut le a kód, ha nincs hiba
# finally: (opcionális) Olyan kód, amit ígyis-úgyis lefuttatnánk, annak ellenére hogy volt-e hiba vagy sem, erőforrás felszabadítás

# Exception chaining: Kivétel továbbítása
# Az egyik kivétel továbbítása egy másik kivételnek
# https://www.tutorialspoint.com/python/python_exception_chaining.htm


# Nullával való osztás
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")

# Több kivétel kezelése
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("Error: Invalid value!")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")
else:
    print(f"Result: {result}")
finally:
    print("Runs everytime!")

# Kivétel objektum kezelése: Lehetőséges biztosít a kivétel részletesebb kezelésére
try:
    score = int(input("Enter your score: "))
except Exception as e:
    print(f"Error occured: {e}")
else:
    print(f"Given score: {score}")
finally:
    print("Runs everytime!")


# Saját kivételek létrehozása
class NotEvenError(Exception):
    """Exception, when given number is not even."""

    pass


def check_even(number):
    if number % 2 != 0:
        raise NotEvenError(f"Given number is not even: {number}")  # Hiba eldobása
    else:
        print(f"Given number is even: {number}")


try:
    number = int(input("Enter a number: "))
    check_even(number)
except NotEvenError as e:
    print(f"Error occured: {e}")
except ValueError:
    print("Error: Invalid value!")
else:
    print("Number is checked successfully!")
finally:
    print("Runs everytime!")


# Exception chaining (Kivétel továbbítása)
def add(x, y):
    try:
        return x + y
    except TypeError as e:
        raise ValueError("Invalid value!") from e


try:
    result = add(10, "20")
except ValueError as e:
    print(f"Error occured: {e}")
    print(f"Original exception: {e.__cause__}")
