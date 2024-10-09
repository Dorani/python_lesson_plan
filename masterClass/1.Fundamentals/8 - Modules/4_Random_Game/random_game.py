from random import randint
import sys
#generate random number
answer = randint(sys.argv[1], [2])

#get input from user:
guess = input('guess a number 1-10')

#check that input is a number:
while True:
    try:
        guess = int(input('guess a number between 1 and 10'))
        if 0 < guess > 11:
            #check if it the right guess
            if guess == answer:
                print('you nailed it!')
                break
        else:
            print('please make sure its 1 to 10 range')
    except ValueError:
        print('please enter valid number')
        continue