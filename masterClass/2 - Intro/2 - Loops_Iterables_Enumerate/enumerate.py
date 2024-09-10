for i, char in enumerate('Hellooooo'):
    print(i, char)

#prints the index of each char so we can use and access the location
    
for i, num in enumerate((1,2,3)):
    print(i, num)

#create a str that enumerates a list of numbers
    
for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f'index of 50 is: {i}')