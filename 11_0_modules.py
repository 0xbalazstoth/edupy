# Module: Amolyan könyvtár, adott kód részletet tudunk becsomagolni egy modulba,
# amit máshol is fel akarunk a későbbiekben használni

import math_module as mm  # Modul átnevezése "as" kulcsszóval
from math_module import (
    subtract,  # Modulból csak adott funkciót importál be "from" kulcsszóval
)

res_sum = mm.add(3, 4)
print(sum)

res_sub = mm.subtract(4, 3)
print(res_sub)


def aaa():
    print("asd")
