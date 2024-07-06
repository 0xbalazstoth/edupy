# Beágyazott függvények
# Closure függvény (Zárófüggvény)
# A closure függvény egy olyan függvény, amely egy másik függvényből származik,
# és hozzáfér a külső függvény változóihoz.
def outer_function(text):  # Külső függvény
    def inner_function():  # Closure függvény
        print(text)

    inner_function()  # Closure függvény meghívása


outer_function("Hello from the inner function!")
