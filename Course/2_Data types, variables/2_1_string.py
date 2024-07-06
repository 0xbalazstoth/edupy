greeting = "Hello"
print(type(greeting))

name = "John Doe!"
greeting_user = greeting + ", " + name
first_name, last_name = "John", "Doe"
multiline_text = """Multi
line
text.
"""

# string hossza
length = len(greeting)

x = y = z = "Same value"
print(x, y, z)

char = "a"  # Karakter

upper = greeting.upper()
lower = greeting.lower()
remove_whitespace = name.strip()
replace = name.replace("H", "J")
split = greeting_user.split(", ")
escaping = 'Hello "There"!'  # \', \\, \n, \r, \t, \b

# input
name = input("Enter your name: ")
print(name)

test: str = "asd"
print(type(test))

# Fordítási időben (nem értékelődik ki) str marad
test = 5  # Futásidőben (értékelődik ki) int-re változik
print(type(test))
