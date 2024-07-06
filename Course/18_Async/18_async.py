# Aszinkron programozás
# - Az aszinkron programozás Pythonban lehetővé teszi, hogy egy program több feladatot hajtson végre egyidejűleg,
#   anélkül, hogy mindegyik feladatnak várnia kellene a többire.
# - Ez különösen hasznos olyan műveleteknél, amelyek hosszú időt vesznek igénybe, például
#   hálózati kérések vagy fájlműveletek.

# pip install asyncio

# Fogalmak:
# Coroutine: (aszinkron függvény)
# - A coroutine egy speciális függvény, amely a async def kulcsszóval kezdődik.
# - Ezek a függvények nem végzik el azonnal a feladatukat, hanem felfüggeszthetők és folytathatók később.

# Event Loop:
# -  Az event loop a szíve az aszinkron programozásnak.
# - Ez egy végtelen ciklus, amely kezeli az összes feladatot és azok állapotát.

import asyncio
import random


async def horse_race(horse_name, distance):
    """
    Szimulál egy lóversenyt. Minden ló különböző időközönként lép előre.
    """
    covered_distance = 0
    while covered_distance < distance:
        # Lépés véletlenszerű időközönként 0.1 és 1 másodperc között
        step_time = random.uniform(0.1, 1.0)
        await asyncio.sleep(step_time)
        covered_distance += 1
        print(f"{horse_name} covered {covered_distance}/{distance} distance.")
    return horse_name


async def main():
    distance = 5
    horses = ["Ló 1", "Ló 2", "Ló 3", "Ló 4", "Ló 5"]
    tasks = [horse_race(horse, distance) for horse in horses]

    # Verseny indítása és az első befejező ló meghatározása
    winner = await asyncio.gather(*tasks)
    print(f"{winner[0]} won the race!")
    # Mindig a lista első eleme lesz a nyertes


asyncio.run(main())
