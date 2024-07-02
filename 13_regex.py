# RegEx, Reguláris Kifejezések
# Karakterek sorozata, amivel egy mintát (pattern) hozunk létre
# Teszteléshez: https://regex101.com/
import re

# Pont (.)
"""
Minta: cat
Keresés: Minden olyan szövegrészletet megtalál, amely tartalmazza a "cat" szót.
Példa szöveg: "The cat is on the roof."
"""
pattern = "c.t"
matches = re.findall(pattern, "The cat sat on the mat.")
print("Result:", matches)

# Csillag (*)
"""
Minta: ca*t
Keresés: Olyan szövegrészletet talál, ahol a "c" betűt követheti nulla vagy több "a" betű, majd egy "t" betű.
Példa szöveg: "ct, cat, caaat"
"""
pattern = "ca*t"
matches = re.findall(pattern, "ct, cat, caaat")
print("Result:", matches)

# Plusz (+)
"""
Minta: ca+t
Keresés: Olyan szövegrészletet talál, ahol a "c" betűt követi egy vagy több "a" betű, majd egy "t" betű.
Példa szöveg: "cat, caat, caaat"
"""
pattern = "ca+t"
matches = re.findall(pattern, "cat, caat, caaat")
print("Result:", matches)

# Kérdőjel (?)
"""
Minta: ca?t
Keresés: Olyan szövegrészletet talál, ahol a "c" betűt követheti nulla vagy egy "a" betű, majd egy "t" betű.
Példa szöveg: "ct, cat, caat"
"""
pattern = "ca?t"
matches = re.findall(pattern, "ct, cat, caat")
print("Result:", matches)

# Szögletes zárójelek ([])
"""
Minta: c[aeiou]t
Keresés: Olyan szövegrészletet talál, ahol a "c" betűt követi egy magánhangzó (a, e, i, o, u), majd egy "t" betű.
Példa szöveg: "cat, cet, cit, cot, cut"
"""
pattern = "c[aeiou]t"
matches = re.findall(pattern, "cat, cet, cit, cot, cut")
print("Result:", matches)

# Kivétel (^)
"""
Minta: [^aeiou]
Keresés: Olyan szövegrészletet talál, amely nem tartalmazza a magánhangzókat (a, e, i, o, u).
Példa szöveg: "apple, banana, cherry"
"""
pattern = "[^aeiou]"
matches = re.findall(pattern, "apple, banana, cherry")
print("Result:", matches)
