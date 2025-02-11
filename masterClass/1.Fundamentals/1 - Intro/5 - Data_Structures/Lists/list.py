# Data Structure:
## Form of arrays:
li = [1,2,3,4,5]

li2 = ['a', 'b', 'c']

li3 = [1,3,True, False, 'x']


print(li[0])



#List Slicing:
amazon_cart = ['apples','banana','cuccumbers','ps5']

#Slice out sunglasses using :: or skip over an element
print(amazon_cart[0::2])
##everytime you do list slicing you create a new copy

#change element, but create new list
amazon_cart[0] = 'laptop'

#new cart is copying, so that we do not modify amazon cart list
new_cart = print(amazon_cart[:])
print(amazon_cart)
print(new_cart)

#a real copy: