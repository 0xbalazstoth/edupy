# for ciklus listán
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# for ciklus adott start indextől
for fruit in fruits[1:]:
    print(fruit)

# for ciklus szótáron
student = {"name": "John Doe", "age": 23, "major": "Computer Science"}
for key, value in student.items():
    print(f"{key}: {value}")

# for ciklus számsorozaton
for i in range(5):
    print(i)

# enumerate (for ciklus csak index támogatással, kezdeti start indexel)
for index, fruit in enumerate(
    fruits
):  # enumerate(fruits, 2) 2-es saját indextől kezdődik az iteráció (csak az index változik meg, nem az ahanyadik elemtől való start)
    print(f"{index}: {fruit}")

# while ciklus
# Amíg nem teljesül a feltétel
count = 0
while count < 5:
    print(count)
    count += 1

# zip
# Két vagy több lista elemeit párba állítja és egyszerre iterálható
# Méretnek egyeznie kell, ami azontúl kilóg, az nem fog bekerülni az iterációba
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# List comprehension
# Tömör szintaxis listák létrehozására iterációval és esetleges feltételes logikával
squares = [x for x in range(10) if x > 3]
print(squares)

# Iterálás stringen
word = "calculator teszt"
for letter in word:
    print(
        letter, end=""
    )  # végére tesz egy % jelet, mert az a véget jelöli, megoldás iteráció utáni print() vagy iteráció utolsó karaktert kivéve
print()

for index, letter in enumerate(word):
    if index != len(word) - 1:
        print(letter, end="")
    else:
        print(letter)

# Beágyazott iteráció
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for column in row:
        print(column, end=" ")
    print()
