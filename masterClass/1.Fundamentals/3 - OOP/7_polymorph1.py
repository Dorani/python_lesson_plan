#Polymorphism - Many forms: 

class User:
    def sign_in(self):
        print('logged on')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attack with arrows: arrows left {self.num_arrows}')



wizard1 = Wizard('seif', 50)
archer1 = Archer('robin', 100)

def player_attack(character):
    character.attack()

#Polymorphism in Action: redefine methods in many forms, while modifying classes for our specific needs, and not repeat ourselves.
player_attack(wizard1)
player_attack(archer1)

