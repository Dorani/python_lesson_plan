#length of a list

basket = [1,2,3,4,5,6,7]

print(len(basket))
#add to the end of the list
basket.append(100);
print(basket)


#adding to a specific index
basket.insert(1,100)

#takes an iterable, ie a data structure you can loop over
new_list = basket.extend([100,101,102])
print(new_list)
#removing, removes what is at the end of the list
new_list.pop()

#remove at an index
new_list.pop(3)

#give it a value in the list
new_list.remove(4)


#clear out the list
new_list.clear()


#what index is a certain element
new_list.index(3) #output 2

#optional paramater, start looking, and end looking
is_it_in_basket = print(3 in new_list)

#count how many times an item occurs
new_list.count(5)


#sorting list
new_list.sort()


new_basket = new_list[:] #or use copy, basket.copy()
new_basket.sort()
print(new_basket)


#reverse the list
new_list.reverse()



#create a list ranged from 0-99
print(list(range(100)))


#joins

sentence = ' '

new_sen = sentence.join(['hi','my','name','is','seif'])
print(new_sen)

#list unpacking, in js destructring
a,b,c = [1,2,3]


a,b,c, *other = [1,2,3,4,5,6,7,78,8,9]