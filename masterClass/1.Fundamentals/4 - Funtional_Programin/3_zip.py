#3 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]


#Zip them together:
    #takes the first iterable and zips it into the second, into a tupple - (a,1) (b,2) etc etc..
print(list(zip(my_strings, sorted(my_numbers))))