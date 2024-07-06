# Type casting (Típus konverzió)
# - Az egyik típusú változót átkonvertáljuk egy másik típusú változóvá

# int átalakítása stringgé
number = 10
number_str = str(number)
print(number_str)
print(type(number_str))

# string átalakítása int-té
number_str = "12"
number = int(number_str)
print(number)
print(type(number))

# string átalakítása float-tá
number_str = "12.5"
number = float(number_str)
print(number)
print(type(number))

# float átalakítása stringgé
number = 6.7
number_str = str(number)
print(number_str)
print(type(number_str))

# float átalakítása int-té
number = 20.2
number_int = int(number)
print(number_int)
print(type(number_int))

# int átalakítása float-tá
number = 18
number_float = float(number)
print(number_float)
print(type(number_float))

# list átalakítása set-té
fruits = ["apple", "banana", "cherry"]
fruits_set = set(fruits)
print(fruits_set)
print(type(fruits_set))

# set átalakítása list-té
fruits_set = {"apple", "banana", "cherry"}
fruits = list(fruits_set)
print(fruits)
print(type(fruits))

# string átalakítása list-té (minden karakter külön listaelem lesz)
string = "apple"
char_list = list(string)
print(char_list)
print(type(char_list))

# list átalakítása stringgé
char_list = ["a", "p", "p", "l", "e"]
string = "".join(char_list)
print(string)
print(type(string))

# tuple átalakítása list-té
fruits = ("apple", "banana", "cherry")
fruits_list = list(fruits)
print(fruits_list)
print(type(fruits_list))

# list átalakítása tuple-é
fruits_list = ["apple", "banana", "cherry"]
fruits = tuple(fruits_list)
print(fruits)
print(type(fruits))

# tuple átalakítása set-té
fruits = ("apple", "banana", "cherry")
fruits_set = set(fruits)
print(fruits_set)
print(type(fruits_set))

# set átalakítása tuple-é
fruits_set = {"apple", "banana", "cherry"}
fruits = tuple(fruits_set)
print(fruits)
print(type(fruits))
