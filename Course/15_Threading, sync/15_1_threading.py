# Szálkezelés

# Szál (Thread):
# - Egy szál egy különálló végrehajtási útvonal egy programban.
# - Több szál használatával egy program különböző részei párhuzamosan futtathatók.

# GIL (Global Interpreter Lock):
# - GIL egy olyan mechanizmus, ami megakadályozza, hogy több natív szál egyidejűleg hajtsa végre a kódot.
# - Ez szükséges, mert a Python interpreter nem szálbiztos.

# Alap szálkezelés: Egyetlen ló futása
import threading
import time


def run_race(horse_name):
    for i in range(5):
        print(f"{horse_name} runs {i+1} meters.")
        time.sleep(1)


# Ló létrehozása
horse_thread = threading.Thread(target=run_race, args=("Horse-1",))

# Ló indítása
horse_thread.start()

# Fő szál várakozása a ló befejezésére
horse_thread.join()

print("The race is over")
