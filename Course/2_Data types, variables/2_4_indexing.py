# Indexelés (negatív indexelés is lehet, de akkor n-től 0-ig)
# 0-tól indul n-ig

txt = "Sample phrase"

# Pozitív indexek
first_char = txt[0]  # S
second_char = txt[1]  # a
# n_char = txt[22]  # out of range

# Negatív indexek
last_char = txt[-1]  # e
second_last_char = txt[-2]  # s
first_char = txt[-13]  # S

# Szeletelés (slicing)
# m:n (m-től n-ig)
# n:m (n-től m-ig)
# m::n (Minden i-edik elem kiválasztása m-től n-ig)
# m:n:i (i = lépésköz) (m-től indulva n-ig, ahol minden i-edik elemet kiválasztjuk)
first_three_chars = txt[0:3]
last_three_chars = txt[-3:]
every_second_chars = txt[::2]
from_third_to_second_last_char = txt[3:-1]
every_third_chars_from_m_to_n = txt[0:-1:2]
print()
