# Iterator
# Az iterátor egy olyan objektum, amely lehetővé teszi az iteráció során
#  az elemek egyesével történő feldolgozását.
# Az iterátorokat a __iter__() és a __next__() metódusokkal lehet létrehozni.
# Az __iter__() metódus visszaad egy iterátor objektumot.
# Az __next__() metódus visszaadja a következő elemet a sorban.
# Ha nincs több elem, akkor a StopIteration kivételt dobja.
# Az iterátorokat a for ciklusban is használhatjuk.


class CustomIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:  # Ha még nem értük el a végét
            self.current += 1  # Növeli az aktuális értéket
            return self.current - 1  # Visszaadja az aktuális értéket
        else:
            raise StopIteration  # Ha nincs több elem, akkor StopIteration kivételt dobja


custom_iterator = CustomIterator(0, 5)
# for item in custom_iterator:
#     print(item)

words = ["apple", "banana", "cherry", "date", "elderberry"]

for i in custom_iterator:
    print(words[i])
