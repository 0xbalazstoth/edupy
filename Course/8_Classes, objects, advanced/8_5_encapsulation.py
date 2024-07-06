# Encapsulation (Egységbe zárás)
# Az osztályokban az attribútumokat és a metódusokat egy egységbe zárjuk, azaz az osztályba.


class Device:
    def __init__(self, brand, model, year):
        self.__brand = brand  # Ez egy privát attribútum
        self.__model = model  # Ez egy privát attribútum
        self.__year = year  # Ez egy privát attribútum

        # Tehát nem a konkrét objektumokon keresztül érhetőek el, hanem getter és setter metódusokon keresztül.

    # Getter metódus a brand attribútumhoz
    def get_brand(self):
        return self.__brand

    # Setter metódus a brand attribútumhoz
    def set_brand(self, brand):
        self.__brand = brand

    # Getter metódus a model attribútumhoz
    def get_model(self):
        return self.__model

    # Setter metódus a model attribútumhoz
    def set_model(self, model):
        self.__model = model

    # Getter metódus a year attribútumhoz
    def get_year(self):
        return self.__year

    # Setter metódus a year attribútumhoz
    def set_year(self, year):
        if year > 1970:  # Például, az első modern számítógép 1970 után jelent meg
            self.__year = year
        else:
            print("Invalid year for a device.")


# Példa az osztály használatára
my_device = Device("Apple", "iPhone 12", 2020)

# A privát attribútumok elérése getter metódusokkal
print("Brand:", my_device.get_brand())
print("Model:", my_device.get_model())
print("Year:", my_device.get_year())

# A privát attribútumok módosítása setter metódusokkal
my_device.set_brand("Samsung")
my_device.set_model("Galaxy S21")
my_device.set_year(2021)

print("\nAfter updating:")
print("Brand:", my_device.get_brand())
print("Model:", my_device.get_model())
print("Year:", my_device.get_year())
