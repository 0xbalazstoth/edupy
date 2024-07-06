import threading
import time


def run_race(horse_name):
    for i in range(5):
        print(f"{horse_name} runs {i+1} meters.")
        time.sleep(1)


# Több ló létrehozása és indítása
horses = []
for i in range(3):
    horse_thread = threading.Thread(target=run_race, args=(f"Horse-{i+1}",))
    horses.append(horse_thread)
    horse_thread.start()

# Várakozás az összes ló befejezésére
for horse_thread in horses:
    horse_thread.join()

print("The race is over")
