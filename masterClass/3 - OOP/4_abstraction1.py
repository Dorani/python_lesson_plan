#Abstraction - Hiding Info

#Encapsulation - Biding of data and functions that manipulate that data, and encapsulate in 1 big object

class PlayerCharacter:
    #class object attribute
    #static attribute
    membership = True

    def __init__(self, name, age):
            #attributes that should not be modified
            self._name = name
            self._age = age

    def run(self):
          print('run')

    def speak(self):
          print(f'my name is {self.name} and I am {self.age} year old')


player1 = PlayerCharacter('seif', 100)
player1.speak
