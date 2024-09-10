#Inheritance - Extend out and inherent build in functionality and properties from other classes.


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

wizard1.attack()
archer1.attack()

#Check to see if an object instantianted is an instance of a class, same with sub classes etc...
print(isinstance(wizard1, Wizard))