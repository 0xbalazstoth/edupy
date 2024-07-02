# pip install matplotlib
import matplotlib.pyplot as plt

# Adatok
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Diagram létrehozása
plt.plot(x, y)

# Diagram címek hozzáadása
plt.title("Egyszerű vonaldiagram")
plt.xlabel("X tengely")
plt.ylabel("Y tengely")

# Diagram megjelenítése
plt.show()
