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

    def check_arrows(self):
        print(f'attack with arrows: arrows left {self.num_arrows}')

class HybridBord(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self,name, arrows)
        Wizard.__init__(self,name, power)


hb1 = HybridBord('borgie', 50, 100)
hb1.check_arrows()
hb1.attack()
hb1.sign_in()