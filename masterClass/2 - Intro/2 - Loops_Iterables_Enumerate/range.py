#range obj return an obj 

print(range(100))

#loop 100 times using range
for number in range(0,100):
    print(number)

for email in range(0,100):
    print('email list')

for _ in range(0,10,2):
    print(_)
    #0,2,4,6,8


#loop 2 times and create 2 lists of ranges 0-9
for _ in range(2):
    print(list(range(10)))