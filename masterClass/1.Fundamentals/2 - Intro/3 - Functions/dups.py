some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

dups = set;
for value in some_list:
    if some_list.count(value) > 1:
        dups.append(value)

print(dups)