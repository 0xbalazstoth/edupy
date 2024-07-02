import os

# Fájlok kezelése
# r: Read, alapértelmezett
# a: Append, beolvassa a fájlt, létrehozza, ha nem létezik
# w: Write, beolvassa a fájlt írásra, létrehozza, ha nem létezik
# x: Create, létrehozza a fájlt, hibát dob, ha már létezik

# Abszolút elérési út: Teljes elérési út
# Relatív elérési út: Jelenlegi eléréshez képest határozza meg a fájl/könyvtár helyét

# Létező fájl beolvasása
try:
    f = open("./data/file.txt")
except FileNotFoundError as e:
    print(e)
else:
    # Teljes fájl beolvasása egy string-be
    # print(f.read())

    # Adott méretig
    # print(f.read(2))

    # Egy sor beolvasása
    # print(f.readline())

    # Beolvasás listába
    print(f.readlines())

    # Fájl beolvasásának bezárása
    f.close()  # például finally-ben!

# Fájl létrehozása, vagy meglévőhöz hozzáfűzés
f = open("./data/created_file.txt", "a")
f.write("Data")
f.close()

# Fájl létrehozása, törli a tartalmat, ha létezik ilyen fájl
f = open("./data/new_file.txt", "w")
f.write("New data")
f.close()

# Fájl létrehozása, hibát dob, ha létezik már
f = open("./data/another_new_file.txt", "x")
f.write("New data2")
f.close()

# Fájl törlése
# import os
os.remove("./data/another_new_file.txt")

# Létezik-e az adott fájl
if os.path.exists("./data/file.txt"):
    print("Exists")
else:
    print("Does not exists")

# Mappa törlése
# os.rmdir("folder_name")
