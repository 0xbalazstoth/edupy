# Dynamic typing (Dinamikus típusozás)
# A Python egy dinamikusan típusozott nyelv, ami azt jelenti, hogy a változók típusa csak futás közben derül ki.
# A változók típusa a hozzárendelt értéktől függ.
# Hátránya, hogy a típushibák csak futás közben derülnek ki.

# Csharp kód példa rá, csak hogy hogyan néz ki egy erősen típusos nyelvben:
# int number = 5;
# string text = "Hello";
# number = "World";  // Fordítási hiba
# text = 10;  // Fordítási hiba

# Python kód példa:
text = "Hello"

# Bizonyítás, hogy a változók típusa futás közben derül ki
print(type(text))  # <class 'str'>
print("id of text:", id(text))
# https://www.tutorialspoint.com/python/python_dynamic_typing.htm
