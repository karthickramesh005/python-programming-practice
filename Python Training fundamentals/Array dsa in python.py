# Array data structure :

import array as arr

# Array Implementation :

arr = arr.array('i',[1,2,3,4,5])

print(arr)
print(type (arr))

print(*arr)

# append & insert element :

arr.append(66)
arr.append(7)
arr.append(66)
arr.append(66)

for i in arr:
    print(i,end =" ")
print()

# Calling Element on Array :

print("Access element is : ",arr[5])

# Removing Element on the Array :

 #print(arr.remove(9))

for i in arr:
    print(i,end =" ")
print()

# complexity for removing Particular element :

sliced_array = arr[3:8]
print(sliced_array)
sliced_array = arr[5:]
print(sliced_array)

# Searching element on array :
print(arr.index(3))

# Updating Elements On array :

arr[5]=77

for i in arr:
    print(i,end =" ")
print()

#Counting Elements On Array :

count = arr.count(66)
print(count)

# Reversing Elements On Array :

 #   arr.reverse()
print(*arr)

# Addind a multiple Elements on Array Extend :

arr.extend([44,55,66,77,11])
for i in arr:
    print(i,end =" ")
print()
