#Tuple

#list that CAN NOT BE MODIFIED

my_tuple = (1,2,3,4,5)

#can also use in dict

user = {
    (1,2): [1,2]
}


#copy with some values sliced
new_tuple = my_tuple[1:4]


#diversify
z,y,z, *other = (1,2,3,4,5,6,7)



#count frequency
print(my_tuple.count(5))

#index of
print(my_tuple.index(5))

#length of 
print(len(my_tuple))