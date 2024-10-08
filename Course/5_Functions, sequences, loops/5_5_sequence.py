# Lista
# Listában a duplikátumot engedélyezettek, mutable
fruits = ["apple", "banana", "cherry"]  # VAGY list(("apple", "banana", "cherry"))
print(fruits)
one, two, three = fruits  # lista kicsomagolás (unpacking)
fruits_len = len(fruits)
anything = ["one", 2, True, False]

# Hozzáférés a lista elemeihez
# Indexelés (negatív indexelés is lehet, de akkor n-től 0-ig)
# 0-tól indul n-ig
print(fruits[1])
print(fruits[1:3])
print("apple" in fruits)

# Lista elemeinek módosítása
fruits[2] = "kiwi"
print(fruits)
fruits[:2] = ["orange", "mango"]
print(fruits)
fruits[3:6] = ["strawberry"]
print(fruits)

# Beszúrás
fruits.insert(2, "lemon")
print(fruits)

# Hozzáadás
fruits.append("Papaya")
print(fruits)

other_fruits = ["pineapple", "peach"]
fruits.extend(other_fruits)
print(fruits)

# Elem törlése
fruits.remove("pineapple")
print(fruits)

# Elem törlése index alapján
fruits.pop(1)  # del fruits[0]
fruits.pop()
print(fruits)

# Lista ürítése
# fruits.clear()

# Lista törlése
# del fruits

# Lista rendezése (Alfanumerikusan rendezi, növekvő sorrendbe)
# Nagy és kisbetű érzékeny rendezés, a nagybetűket a kisbetűk elé sorolja
# ASCII tábla
fruits.sort()  # Megoldás: .sort(key = str.lower)
print(fruits)

unordered = [1, 7, 0, 2, 11]
unordered.sort()  # Csökkenő: .sort(reverse = True)
print(unordered)

# Fordított sorrend
fruits.reverse()
print(fruits)

# Lista másolása
copy_fruits = fruits.copy()  # VAGY list(fruits)

# Két lista összekapcsolása
joined_list = fruits + copy_fruits
print(joined_list)

# List comprehension: egy soros ciklus, amely lehetővé teszi a lista elemek gyors létrehozását
# szintaxis: newlist = [expression for item in iterable if condition == True]
# A kifejezés a jelenlegi elemet jelöli, az iterálható azonosítja az iterálható objektumot, a feltétel pedig opcionális
words = ["phone", "window", "door"]
filtered_words = [
    word for word in words if "w" in word
]  # itt a word a jelenlegi elemet jelöli, a feltétel pedig a kifejezés
print(filtered_words)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
letters = ["a", "b", "c"]
combined = [f"{number} {letter}" for number in numbers for letter in letters]
print(combined)

even_nums = [num for num in numbers if num % 2 == 0]
print(even_nums)

uppercased = [word.upper() for word in words]
print(uppercased)

every_second_char_uppercased = [
    "".join([char.upper() if i % 2 != 0 else char for i, char in enumerate(word)])
    for word in words
]
print(every_second_char_uppercased)

# Range
numbers = range(1, 10)  # kezdő, vég, lépés
new_numbers = [x for x in range(1, 5)]
print(new_numbers)

# Tuple: A tuple egy olyan adatszerkezet, amely lehetővé teszi az elemek csoportosítását egyetlen változóban.
# immutable
coordinates = ()
print(coordinates)
coordinates = (1,)  # Fontos a vessző, mert enélkül nem tudja tuple típusként értelmezni
print(coordinates)
coordinates = (40.7128, -74.0060)  # explicit
print(coordinates)
coordinates = 1, 2, 3  # implicit
print(coordinates)

# Hozzáférés a tuple elemeihez
num_tuples = (10, 10, 20, 30)
print(num_tuples[1])
print(num_tuples[-1])
print(num_tuples[1:3])  # n-(n-1), 0: 10, 1: 20, 2: 30, 3:??

# Összefűzés
num_tuples2 = (3, 4)
combined_tuples = num_tuples + num_tuples2
print(combined_tuples)

# Szorzás
repeated = num_tuples * 2  # megismétli az elemeket
print(repeated)

# Min, max
min_max = (min(num_tuples), max(num_tuples))
print(min_max)

# Adott elem előfordulásainak száma
occur = num_tuples.count(10)
print(occur)

# Adott elem indexe
item_index = num_tuples.index(20)
print(item_index)

# end Tuple
