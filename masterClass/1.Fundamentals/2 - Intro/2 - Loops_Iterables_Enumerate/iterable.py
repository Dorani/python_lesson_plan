user = {
    'name': 'golem',
    'age': 5000,
    'can_swim': False
}
#print the keys
for item in user:
    print(item)

#all
for item in user.items():
    print(item)
#values
for item in user.values():
    print(item)
#keys
for item in user.keys():
    print(item)


#keys and values
#all
for k, v in user.items():
    print(k,v)
