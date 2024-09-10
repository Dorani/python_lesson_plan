#Map
#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capitalize(string):
    return string.upper()

#map through the entire list, and capitlize the pet names
print(list(map(capitalize, my_pets)))