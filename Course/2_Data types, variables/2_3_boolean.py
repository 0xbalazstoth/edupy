#  A | B | A AND B
# ---|---|--------
#  0 | 0 |    0
#  0 | 1 |    0
#  1 | 0 |    0
#  1 | 1 |    1

#  A | B | A OR B
# ---|---|-------
#  0 | 0 |   0
#  0 | 1 |   1
#  1 | 0 |   1
#  1 | 1 |   1

# Aritmetikus
# +, -, *, /, %
sum_nums = 5 + 5
sub_nums = 5 - 5
mul_nums = 5 * 5
div_nums = 5 / 5
mod_nums = 5 % 5

# Értékadó
# =, +=, -=
sum_nums += 5  # sum_nums = sum_nums + 5
sub_nums -= 5  # sub_nums = sub_nums - 5

# Összehasonlító (Érték alapján)
# ==, !=, >, <, >=, <=
equal = 5 == 5
not_equal = 5 != 5
greater_than = 5 > 5
less_than = 5 < 5
greater_than_or_equal = 5 >= 5
less_than_or_equal = 5 <= 5

# Logikai
# and, or, not
and_result = True and False  # True, ha mindkettő igaz
or_result = True or False  # True, ha legalább az egyik igaz
not_result = not True  # True, ha az érték hamis

# Identitás (Objektumok összehasonlítása)
# is, is not
is_result = 5 is 5
is_not_result = 5 is not 5

# Tartalmazó (Membership)
# in, not in
in_result = "Doe" in "John Doe"
not_in_result = "Doe" not in "John Doe"

print((5 + 1) - (5 + 1))

# Operátor precedencia:
# Operátor precedencia (műveleti sorrend) a különböző
# műveletek végrehajtási sorrendjét határozza meg egy kifejezésben.

# Matematikai műveletek precedenciája
# Kifejezés: 2 + 3 * 4
# A * (szorzás) operátor előbb hajtódik végre, mint a + (összeadás)
result = 2 + 3 * 4
print(result)  # Output: 14

# Zárójelek használata a precedencia megváltoztatására
# Kifejezés: (2 + 3) * 4
# A zárójelek miatt az összeadás előbb hajtódik végre
result = (2 + 3) * 4
print(result)  # Output: 20

# Logikai műveletek precedenciája
# Kifejezés: True or False and False
# Az and (ÉS) operátor előbb hajtódik végre, mint az or (VAGY)
result = True or False and False
print(result)  # Output: True

# Összehasonlító és aritmetikai műveletek precedenciája
# Kifejezés: 5 > 2 + 3
# Az összeadás előbb hajtódik végre, mint az összehasonlítás
result = 5 > 2 + 3
print(result)  # Output: False

# Különböző operátorok precedenciája
# Kifejezés: not True or False
# A not (tagadás) operátor előbb hajtódik végre, mint az or (VAGY)
result = not True or False
print(result)  # Output: False

# Vegyes példák
# Kifejezés: 3 + 4 * 2 / (1 - 5) ** 2
# A ** (hatványozás) operátor előbb hajtódik végre, majd a zárójelek,
# ezt követően a * és / (szorzás és osztás), végül az összeadás
result = 3 + 4 * 2 / (1 - 5) ** 2
print(result)  # Output: 3.5

# Példák:
name = "John Doe"
age = 23

is_valid = True
has_access = False
is_doe_in_name = "Doe" in name
is_blabla_in_name = "blabla" not in name
print(1 == 1)
print(2 != 1)
print(age > 18)
print(age >= 18)
print(age < 35)
print(age <= 35)
print(age == 18 or age == 23)
