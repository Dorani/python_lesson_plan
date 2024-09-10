my_file = open('test.txt')


# #Read from file using method
# print(my_file.read())

# #See something at a specific cursor
# my_file.seek(0)

#If our text file has multiple lines
print(my_file.readline())
#Read the rest
print(my_file.readlines())
#close it
my_file.close()