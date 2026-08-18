random_number0 = [2,4,6,7,9,11,12]
random_number1 = [4,8,6,7,9,11,12]
random_number2 = [88,4,99,7,9,11,12]
random_number3 = [77,44,88,7,9,11,12]

##create a function that loops through the random number array and print even numbers
def even_or_odd(arr):
    for number in arr:
        if number % 2 == 0:
            print('is even')
        else:
            print('is odd')
            
even_or_odd(random_number0)
even_or_odd(random_number1)
even_or_odd(random_number2)
even_or_odd(random_number3)