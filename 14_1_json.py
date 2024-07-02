import json

# JSON Objektum betöltése stringből -> load(s), s a string-et jelöli
json_data = """
{
    "name": "Fake Name",
    "age": 24,
    "skills": ["skill1", "skill2"]
}
"""

data = json.loads(json_data)
print(data)
print(data["name"])

# Adat módosítás
data["name"] = "Other Name"
print(data)

# JSON fájl betöltése
with open("./data/words.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    print(data)

# JSON Objektum létrehozása dictionary-ből
dict = {"name": "Fake Nameűáé", "age": 24, "skills": ["skill1", "skill2"]}
data = json.dumps(
    dict, indent=1, ensure_ascii=False
)  # JSON adatok mentése string-be -> dump(s), s a string-et jelöli
print(data)

with open("./data/person.json", "w", encoding="utf-8") as file:
    json.dump(dict, file, indent=1, ensure_ascii=False)
