# Method chaining (Metódus láncolás)
# - A metódus láncolás egy olyan programozási technika, amelynek során egy objektum metódusait egymás után hívjuk meg.
# - A metódus láncolás hasznos lehet, ha egy objektum több metódust is végrehajt egymás után.


class PizzaOrder:
    def __init__(self):
        self.size = ""
        self.toppings = []
        self.extra_cheese = False

    def set_size(self, size):
        self.size = size
        return self

    def add_topping(self, topping):
        self.toppings.append(topping)
        return self

    def add_extra_cheese(self):
        self.extra_cheese = True
        return self

    def build(self):
        order = {
            "size": self.size,
            "toppings": self.toppings,
            "extra_cheese": self.extra_cheese,
        }
        return order

    def __str__(self):
        cheese = "with extra cheese" if self.extra_cheese else "without extra cheese"
        return (
            f"Size: {self.size} size\n"
            f"Toppings: {', '.join(self.toppings)}, {cheese}"
        )


order = PizzaOrder()
order.set_size("large").add_topping("mushrooms").add_topping("corn").add_extra_cheese()
print(order)
