# Liskov Substitution Principle (LSP) - Liskov helyettesítési elve
# - Az osztályoknak helyettesíthetőnek kell lenniük az ősosztályokkal.
# - Minden osztály legyen helyettesíthető a gyermekosztályával anélkül, hogy a program működése megváltozna.
from abc import ABC, abstractmethod


# Bad practive
class Bird:
    def fly(self):
        pass

    def tweet(self):
        pass


class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying")

    def tweet(self):
        print("Sparrow is tweeting")


class Ostrich(Bird):
    def fly(self):
        # raise NotImplementedError("Ostrich can't fly")
        # Struccok nem tudnak repülni
        # Tehát a előfordulhat olyan, hogy az örökölt metódusokat nem tudjuk megvalósítani a gyermekosztályban.
        print("Ostrich can't fly")

    def tweet(self):
        print("Ostrich is tweeting")


sparrow = Sparrow()
ostrich = Ostrich()

sparrow.fly()
sparrow.tweet()

ostrich.fly()
ostrich.tweet()


# Javított változat
class Bird(ABC):
    @abstractmethod
    def tweet(self):
        pass


class FlyingBird(Bird):
    @abstractmethod
    def fly(self):
        pass


class Sparrow(FlyingBird):
    def fly(self):
        print("Sparrow is flying")

    def tweet(self):
        print("Sparrow is tweeting")


class Ostrich(Bird):
    def tweet(self):
        print("Ostrich is tweeting")


sparrow = Sparrow()
ostrich = Ostrich()

sparrow.fly()
sparrow.tweet()

ostrich.tweet()
