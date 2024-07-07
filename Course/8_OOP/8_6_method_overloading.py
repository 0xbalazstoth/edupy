# Method overloading (Metódus túlterhelés)
# Az osztályokban lévő metódusokat túl lehet terhelni, azaz több változattal is rendelkezhetnek.

# Python-ban nincs metódus túlterhelés, mert az utolsó metódus felülírja az előző metódust.
# Példa
# class Calculator:
#     def add(self, a, b):
#         return a + b

#     def add(self, a, b, c):
#         return a + b + c


# # Példa
# calculator = Calculator()
# print(calculator.add(1, 2))  # Ha kitörölném, akkor működne a második metódus
# print(calculator.add(1, 2, 3))


# De lehet "szimulálni" a metódus túlterhelést.
# class Calculator:
#     def add(self, a=None, b=None, c=None):
#         if a != None and b != None and c != None:
#             return a + b + c
#         elif a != None and b != None:
#             return a + b
#         else:
#             return a


# # Példa
# calculator = Calculator()
# print(calculator.add(1, 2))
# print(calculator.add(1, 2, 3))

# Van rá package: multipledispatch
from multipledispatch import dispatch


class Calculator:
    @dispatch(int, int)
    def add(self, a, b):
        return a + b

    @dispatch(int, int, int)
    def add(self, a, b, c):
        return a + b + c


# Példa
calculator = Calculator()
print(calculator.add(1, 2))
print(calculator.add(1, 2, 3))
