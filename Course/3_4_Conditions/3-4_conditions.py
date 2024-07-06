result = None

# Elágazások
# if, elif, else

x = 7

if x > 10:
    print("x greater than 5")
elif x > 5:
    print("x greater than 5 but not greater than 10")
else:
    print("x is 5 or less")

# Beágyazott elágazások
position = 9

if position >= 1 and position <= 3:
    print("podium finish")
else:
    print("non-podium placement")

# Short Hand if, Ternary operator, rövidített if-else elágazás egysorban
# value_if_true if condition else value_if_false
podium_result = "podium" if position >= 1 and position <= 3 else "non-podium placement"
print(podium_result)

# pass
# Ha az elágazás nem lehet üres (todo jellegű)
if x != 7:
    pass

# Switch case (match)
# Egyezik-e vagy sem
match position:
    case 1:
        print("first")
    case 2:
        print("second")
    case 3:
        print("third")
    case _ if position > 3 and position < 10:
        print("non-podium placement")
    case _:
        print("unkown position")
