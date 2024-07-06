# Enum
# Az enum egy olyan osztály, amelynek az elemei konstansok.
# Az enumokat a Python 3.4-től támogatja a Python.
# Immutable, azaz nem változtatható.

from enum import Enum, auto


# Enum osztály létrehozása
class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

    def __init__(self, value):
        if not isinstance(value, int):
            raise ValueError(f"Value for {self.name} must be an integer")

    def __str__(self):
        return f"{self.name} ({self.value})"


# Enum értékek kiírása
print(Color.RED)

# Enum érték nevének kiírása
print(Color.RED.name)

# Enum érték értékének kiírása
print(Color.RED.value)

# Enum értékek kiírása
for color in Color:
    print(color)

# Használati példa
selected_color = Color.RED

if selected_color == Color.RED:
    print("Red color selected")
