# Square
my_list = [5, 4, 3]
#using them for functions that we only use once
#occasionally, we only need to use a function once, its also annonymous
print(list(map(lambda item: item*item, my_list)))

# List Sorting
a = [(0, 2), (4, 3), (9, 9), (10, -2)]

a.sort(key=lambda x: x[1])
print(a)

