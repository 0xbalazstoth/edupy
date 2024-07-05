# Polimorfizmus
# A polimorfizmus lehetővé teszi, hogy azonos metódusokat hívjunk meg különböző osztályok példányain
class Position:
    def show_position(self):
        pass


class Goalkeeper(Position):
    def show_position(self):
        return "Goalkeeper"


class Defender(Position):
    def show_position(self):
        return "Defender"


class Midfielder(Position):
    def show_position(self):
        return "Midfielder"


class Forward(Position):
    def show_position(self):
        return "Forward"


def show_player_position(player):
    print(player.position())


# Creating instances of each class
goalkeeper = Goalkeeper()
defender = Defender()
midfielder = Midfielder()
forward = Forward()

# Demonstrating polymorphism
show_player_position(goalkeeper)
show_player_position(defender)
show_player_position(midfielder)
show_player_position(forward)
