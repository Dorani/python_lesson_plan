#dictionary

dictionary = {
    'a': 1,
    'b': [4,5,6,7],
    'c': True,
    'x': 'SEIF'
}


print(dictionary['b'])

print

#list of dicts
my_list = [
    {
    'a': 1,
    'b': [4,5,6,7],
    'c': True,
    'x': 'SEIF' 
    },
    {
    'l': 1212,
    'd': [4,5,6,7,3,4,45],
    'k': False,
    'q': 'Dorani'
    }
]

print(my_list[0]['b'][2])

#dictionary keys needs to be imutable, ie can not change
#primitives, but lists can not be keys
#also keys need to be unique, otherwise it gets overriden

my_keys = {
    123: [12,33,44],
    True: 'yes',
    'no': 1
}


