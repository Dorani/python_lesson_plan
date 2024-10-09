import random

#random val
print(random)

#random number
print(random.random())

#random integer
print(random.randint(1,10))

#random choice to make, from a list or wtvr
print(random.choice([1,2,3,4,5]))

#random shuffling
my_list = [1,2,3]
random.shuffle(my_list)
print(my_list)