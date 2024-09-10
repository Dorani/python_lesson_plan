#dictionary
user = {
    'username': 'seif',
    'password': 'asadscssds'
}

print(user.get('username'))

#if the property doesnt exist, then add a default
print(user.get('username', 'dorani'))


#key needs not to be a string, it will detault
#not common way
user2 = dict(username = "seifd")


#loop
#true or false
print('username' in user)

#check keys in user
print('password' in user.keys())

#check values in user
print('password' in user.values())

#grab the entire item
print(user.items())

#clear and copy

user3 = user.copy()
user.clear()

print(user3)


#remove a key
print(user.pop('username')) #returns value and removes

#randomly remove a key and value
print(user.popitem())


#update a key value, if its not there it will just update the dict with a new key/value

print(user.update({'username': 'deltaforce'}))
