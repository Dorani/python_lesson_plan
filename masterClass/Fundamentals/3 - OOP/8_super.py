#Polymorphism - Many forms: 

class User:
    def __init__(self, email):
        self.email = email
        

    def sign_in(self):
        print('logged on')


class Wizard(User):
    def __init__(self, name, power, email):
        #refer to User this way and not pass self
        super().__init__(email)
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'attacking with power of {self.power}')




wizard1 = Wizard('seif', 50, 'seif@gmail.com')


#introspective: what do we have access to?
print(dir(wizard1))
