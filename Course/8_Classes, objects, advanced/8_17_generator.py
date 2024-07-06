import psutil


# Lista nélkül, eltárolva a memóriában
def number_list(n: int):
    numbers = []
    for i in range(n):
        numbers.append(i)
    return numbers


numbers = number_list(5000000)

for number in numbers:
    print(number)

# from memory_profiler import profile

process = psutil.Process()
# python -m memory_profiler 8_6_generator.py

# Generator
# A generátorok olyan függvények, amelyek lehetővé teszik a sorozatok elemenkénti létrehozását és visszatérését,
# - anélkül, hogy előre kiszámítanák és tárolnák az összes elemet a memóriában.
# Ezt a yield kulcsszóval érjük el.

# Ha például egy listán akarsz iterálni, a Python a teljes listára memóriát foglal.
# Egy generátor nem fogja az egész sorozatot a memóriában tartani, és csak igény szerint "generálja" a sorozat következő elemét.


# Generátorral, nem tárolja az összes elemet a memóriában
# @profile
# def number_generator(n: int):
#     for i in range(n):
#         yield i


# # Használat
# gen = number_generator(5000000)

# if __name__ == "__main__":
#     for number in gen:
#         print(number)

print("Memory usage:", process.memory_info().rss / 1024**2, "MB")
print("CPU usage:", process.cpu_percent())

# TODO: Rajzoljuk a generátorhoz és listával való megoldással (működés bemutatása, összehasonlítása)
