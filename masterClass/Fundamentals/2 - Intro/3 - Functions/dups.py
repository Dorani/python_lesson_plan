some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

dups = [];
for value in some_list:
    if some_list.count(value) > 1:
        if value not in dups:
            dups.append(value)

print(dups)