my_set = {1,2,3,4,5,6}
your_set = {4,5,6,7,8,9}

print(my_set.difference(your_set))# {1,2,3}
print(my_set.discard(5)) #discards the number 5

#unlike difference, it will also remove them
print(my_set.difference_update(your_set))
print(my_set)


#common items intersection # 4,5,6
print(my_set.intersection(your_set))

#are those 2 sets overlapping? ie do they have anything in common?
print(my_set.isdisjoint(your_set))


#unions, subsets and issupersets

#create a new set that unifies both while removing dups
print(my_set.union(your_set))
print(my_set | your_set)


#check to see if one set is a subset of another
new_set = {4,5}
your_new = {4,5,6,7}

print(new_set.issubset(your_new)) #true

#does my set emcompass yours?
print(your_new.issuperset(new_set))

