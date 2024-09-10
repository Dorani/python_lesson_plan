#OOP

class PlayerCharacter:
    #class object attribute
    #static attribute
    membership = True

    def __init__(self, name, age):
        if self.membership:
            #attributes
            self.name = name
            self.age = age

    def shout(self):
       return(f'my name is {self.name}')


player_1 = PlayerCharacter('seif', 33)


#observe the blueprint
#help(player_1)

print(player_1.shout())