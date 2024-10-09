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
    
    #use method without instantiating a class
    #you can simply call the parent class and invoke a class method
    #
    @classmethod
    def adding_things(cls,num1,num2):
        return cls('SeifDelta', num1 + num2)

    #we dont care about class state.
    @staticmethod
    def subtract_things(num1, num2):
        return num1 - num2

player_1 = PlayerCharacter('seif', 33)


#observe the blueprint
#help(player_1)

print(player_1.adding_things(2,3))

#create a class method and instantiated right away
player_2 = PlayerCharacter.adding_things(2,3)