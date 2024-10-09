# *args **kwargs

def super_func(*args, **kwargs):
    return sum(args)


super_func(1,2,3,4)




def super_func(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total


super_func(1,2,3,4, num1 = 5, num2 = 10)