greet = "hellooooo"
print(greet[:])
print(greet[0 :])
print(greet[0 : 9])
print(greet[0 :len(greet)])
# will iterate through entire string


#others
quote = "hello face"
print(quote.capitalize())


#See if a string exists
print(quote.find("f"))

#replace
print(quote.replace("hello", "goodbye"))
#remains in memory, however
print(quote)

#Mutate
new_quote = print(quote.replace("hello", "goodbye"))