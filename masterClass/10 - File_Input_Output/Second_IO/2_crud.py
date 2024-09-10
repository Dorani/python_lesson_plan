#Read from file
with open('test.txt', mode='r') as my_file:
    print(my_file.readlines())


##Read and Write to a file
with open('test.txt', mode='r+') as my_file:
    text = my_file.write('BOO')
    print(text)

#Append to the end of the file by changing the mode
with open('test.txt', mode='a') as my_file:
    text = my_file.write(':)')
    print(text)

#Create file and append
with open('test2.txt', mode='w') as my_file:
    text = my_file.write(':)')
    print(text)
