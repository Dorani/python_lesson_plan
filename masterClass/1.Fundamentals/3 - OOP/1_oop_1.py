#OOP

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
       return 'run'


player_1 = PlayerCharacter('seif', 33)

print(player_1.name, player_1.age)

print(player_1.run())