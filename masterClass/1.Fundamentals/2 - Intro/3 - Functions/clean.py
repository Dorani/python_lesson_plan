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

    
# Test cases
print(is_even(10))  # True
print(is_even(11))  # False
print(is_even2(10))  # True
print(is_even2(11))  # False

user_input = int(input("Enter a number: "))
if is_even3(user_input):
    print(f"{user_input} is even.")

# This will prompt the user to enter a number and check if it's even or odd.
# The function is_even3 will return True for even numbers and False for odd numbers.
# The user input is converted to an integer before passing it to the function.