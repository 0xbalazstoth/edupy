# Indexelés (negatív indexelés is lehet, de akkor n-től 0-ig)
# 0-tól indul n-ig

txt = "Sample phrase"

# Pozitív indexek (előrefele haladunk, vagyis az irány)
first_char = txt[0]  # S
second_char = txt[1]  # a
# n_char = txt[22]  # out of range

# Negatív indexek (hátrafele haladunk, vagyis az irány)
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

# 0 1 2 3 4 5 6 7 8 9 10 11 12
# S a m p l e   p h r a  s  e
# Kiinduló pont a 0 (i-edik elem), az lesz a legelső elem, majd a harmadik indextől kezdve, minden harmadik elem lesz kiválasztva
every_third_chars_from_m_to_n = txt[0:-1:2]  # Sp r

revversed_chars = txt[::-1]  # Elejétől a végéig, de visszafele haladva

print(txt[3::-1])  # Karakterek visszafele, de a harmadik elemtől az utolsóig: pmaS

empty = txt[5:3]  # Üres, mert a kezdő index nagyobb, mint a vég index

txt_copy = txt[:]
