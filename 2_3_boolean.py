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
