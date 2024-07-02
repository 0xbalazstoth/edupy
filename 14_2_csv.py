import csv

# CSV fájl beolvasása
with open("./data/words.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# CSV fájl beolvasása fejléccel
with open("./data/words.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

# Adatok írása
data = [
    ["name", "age", "skills"],
    ["John Doe", 30, "skill1, skill2"],
    ["Jane Doe", 25, "skill"],
]

with open("./data/person.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Adatok írása fejléccel
data = [
    {"Name": "John Doe", "Age": 30, "Skills": "programming, reading"},
    {"Name": "Jane Doe", "Age": 25, "Skills": "painting, yoga"},
]

with open("./data/new_data.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["Name", "Age", "Skills"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(data)
