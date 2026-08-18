for number in [1,2,3,4]:
    print(number)

for item in (1,2,3,4):
    print(item)

for item in {1,2,3,4}:
    print(item)

#nested
for item in (1,2,3,4):
    for x in [5,6,7,8]:
        print(item,x)



arr = [7, 6, 5, 10, 8, 4, 9, 4, 10]
arr.sort()
print(arr) #[4, 4, 5, 6, 7, 8, 9, 10, 10]
print(arr[0])
print(len(arr))
print(len(arr)-1)
arr.sort()

for i in range(len(arr)-1):
    if arr[i] == arr[i+1]:
        print(arr[i])
        break
    