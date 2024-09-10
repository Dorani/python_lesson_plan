#clean:

def is_even(num):
    if num % 2 == 0:
        return True
    elif num % 2 != 0:
        return False
    
    print(is_even(51))


#cleaner:
    
def is_even2(num):
    if num % 2 == 0:
        return True
    else:
        return False
    

# even cleaner:
def is_even3(num):
    if num % 2 == 0:
        return True
    return False


# cleanest:
def is_even3(num):
    return num % 2 == 0

    