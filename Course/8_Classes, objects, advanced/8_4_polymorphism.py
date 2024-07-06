# Polimorfizmus
# A polimorfizmus lehetővé teszi, hogy azonos metódusokat hívjunk meg különböző osztályok példányain
class Position:
    def show_position(self):
        pass


class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def show_name(self):
        return self.name

    def show_position(self):
        return self.position.show_position()


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


def show_player_info(player):
    print(f"Player: {player.show_name()}, Position: {player.show_position()}")


# Creating instances of each position class
goalkeeper_position = Goalkeeper()
defender_position = Defender()
midfielder_position = Midfielder()
forward_position = Forward()

# Creating instances of Player class with different positions
goalkeeper = Player("Buffon", goalkeeper_position)
defender = Player("Piqué", defender_position)
midfielder = Player("Iniesta", midfielder_position)
forward = Player("Ronaldinho", forward_position)

# Demonstrating polymorphism
show_player_info(goalkeeper)
show_player_info(defender)
show_player_info(midfielder)
show_player_info(forward)
