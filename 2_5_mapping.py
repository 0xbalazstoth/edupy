# Dictionary
# key, value pár
student = {
    "name": "John Doe",
    "age": 23,
    "skills": ["cooking", "singing"],
    "major": {  # Beágyazott szótár a szótárban
        "name": "Computer Science",
    },
}  # VAGY dict(name="John Doe", ...)

# Kulcsok
print(student.keys())
print(student.values())

# Hozzáférés: kulcssal
skills_of_student = student["skills"]
print(skills_of_student)

# Elem hozzáadása, módosítása
student["hair_color"] = "blonde"
student["age"] = 24
print(student)

# Elem eltávolítása
# del student["hair_color"]
age = student.pop("age")
print(age, student)
