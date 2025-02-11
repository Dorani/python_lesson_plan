#Set unordered collection of unique items
arr_dups = [1,2,3,4,5,5,5,5]

#remove dups
remove_dups_from_arr = set(arr_dups)
print(remove_dups_from_arr)
##output {1,2,3,4,5}





my_set = {1,2,3,4,5,6,6,6}
#wont add dups
print(my_set)
#add to a set, order doesn't matter
my_set.add(100)

#access a set we need to grab by item in it

print(1 in my_set) # true

#counts total unique items
print(len(my_set))

#clear and copy apply as well


