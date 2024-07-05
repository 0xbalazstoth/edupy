# Context manager
# - Bizonyos műveletsor elvégzése előtt és után is meghatározott kód fut le
# - A with utasítással használjuk, ami biztosítja, hogy a kontextuskezelő
#   mindig megfelelően lezáródik, akár hiba lép fel, akár nem.
# - A kontextuskezelők gyakran fájlkezelésnél, adatbázis-kapcsolatoknál,
#   illetve egyéb erőforrások kezelésénél hasznosak.


class LibraryBook:
    def __init__(self, title):
        self.title = title
        self.checked_out = False

    def __enter__(self):
        # Könyv kikölcsönzése
        self.checked_out = True
        print(f'Book "{self.title}" has been checked out.')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """description

        Args:
            exc_type: A kivétel típusa. Ez a paraméter a kivételosztályra mutat, például ValueError, TypeError, stb. Ha nem lép fel kivétel, akkor ennek értéke None.
            exc_val: A kivétel értéke. Ez a kivétel konkrét példánya, amelyet a kivétel dobásakor hoztak létre. Ha nem lép fel kivétel, akkor ennek értéke None.
            exc_tb: A kivétel traceback objektuma, amely tartalmazza a kivétel helyének részleteit a kódban. Ha nem lép fel kivétel, akkor ennek értéke None.
        """
        # Könyv visszavétele
        self.checked_out = False
        print(f'Book "{self.title}" has been returned.')
        # Nem nyomjuk el a kivételt, ha történt
        return False


# Használat példa
with LibraryBook("Mockingbird") as book:
    print(f'Reading "{book.title}"...')
    # Itt lehetne kivételt generálni tesztelés céljából
    # raise ValueError("An error occurred while reading the book")

print("Finished reading.")
