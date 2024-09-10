#Reading from another folder, using paths etc:

try:
    with open('../First_IO/test.txt', mode='r') as my_file:
        print(my_file.read())

except FileNotFoundError as err:
    print('No such file exists')
    raise err

except IOError as err:
    print('io error')
    raise err