# Szinkronizálás és zárak: Lóverseny számlálóval
# Ebben a példában egy globális számlálót használunk, hogy nyomon kövessük
# a lovak beérkezési sorrendjét, és zárat (lock) használunk a szinkronizációhoz.

import threading
import time

# Globális változó a lovak beérkezési sorrendjének nyomon követésére
race_position = 0

# Zár létrehozása a szinkronizációhoz
position_lock = threading.Lock()


# Függvény, amely egy ló versenyét szimulálja
def run_race(horse_name):
    global race_position  # A globális race_position változó használata
    for i in range(5):
        # Minden iterációban a ló 1 métert fut
        print(f"{horse_name} runs {i+1} meters.")
        # 1 másodperc várakozás szimulálja a futási időt
        time.sleep(1)
    # Zár használata a race_position biztonságos frissítéséhez
    with position_lock:
        race_position += 1
        # A ló befejezte a versenyt, és kiírjuk a helyezését
        print(f"{horse_name} has finished the race! Position: {race_position}")


# Több ló létrehozása és indítása
horses = []
for i in range(3):
    # Szál létrehozása a run_race függvény futtatásához, minden ló külön szálban fut
    horse_thread = threading.Thread(target=run_race, args=(f"Horse-{i+1}",))
    # A szál hozzáadása a horses listához
    horses.append(horse_thread)
    # A szál indítása
    horse_thread.start()

# Várakozás az összes ló (szál) befejezésére
for horse_thread in horses:
    # A join() metódus biztosítja, hogy a fő szál várakozzon, amíg a szál be nem fejeződik
    horse_thread.join()

# Kiírjuk, hogy a verseny véget ért
print("The race is over")
