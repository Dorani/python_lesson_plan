# #Conditions

# is_old = False
# is_licensed = True

# if is_old and is_licensed:
#     print('you are old')
# elif is_licensed:
#     print('you drive')
# else:
#     print('you are young')
    
    
    
# sam_age = 24
# ben_age = 20

# current_year = 2025
# drink_age = 21

# ##create 2 variables for sam and bens year of birth

# sam_YOB = current_year - sam_age ## 2001
# ben_YOB = current_year - ben_age ## 2005

# ## now we need to create 1 condition

# if current_year - sam_YOB >= drink_age:
#     print('you can drink! enjoy!')
# else:
#     print('you need more time before buying liquor') 
    
    
# if current_year - ben_YOB >= drink_age:
#       print('you can drink! enjoy!')
# else:
#     print('you need more time before buying liquor')   
    

## define a function that will take in yob, current_year
##determine IF that person can drink and then return the output

def check_drinking_age():
    ##ask the user for an input about when they were born, and store that into yob
    name = input('what is your name?: ')
    yob = input('what year were you born?: ')
    current_year = 2025
    drinking_age = 21

    
    user_age = current_year - int(yob)
    
    ##if the user age >= drinking_age, then print out they can drink, otherwise tell them to get lost
    if user_age >= drinking_age:
        print('DOOR OPEN!')
        print(name + ', ' + 'what would you like to drink?')
    else:
        print(name + ' ' +', get lost you are not of drinking age!!!')
        

check_drinking_age()
        
    
    
    
    


