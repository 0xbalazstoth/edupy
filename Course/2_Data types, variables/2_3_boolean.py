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
sum_nums = 5 + 5  # Összeadás
sub_nums = 5 - 5  # Kivonás
mul_nums = 5 * 5  # Szorzás
div_nums = 5 / 5  # Osztás
mod_nums = 5 % 5  # Maradékos osztás

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
number = 5
and_result = number == 5 and number != 2  # True, ha mindkettő igaz
or_result = number == 10 or number == 5  # True, ha legalább az egyik igaz
not_result = not True  # True, ha az érték hamis

# Identitás (Objektumok összehasonlítása)
# is, is not
x = 9
y = x
is_result = x is y
is_not_result = x is not y

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
preres = False and False  # False
result = True or False and False
res1 = True or False
res2 = False or True  # True
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
