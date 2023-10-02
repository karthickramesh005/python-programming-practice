# Dictionary

# dictionary is akey value pairs
# hey does not allow duplicate
# value allow duplicate (key: value)

num = {1:"java",2:"sql",3:"sql",4:"selanium",5:"oracle"}
print (num)
print (type(num))

#len()
i = len(num)
print(i)

#get()
x = num.get(5)
print(x)

x1 = num.get(56,"key not found")
print(x1)

# to get the key from dict keys()

k = num.keys()
print(k)
for i in k :
    print(i)

# to get the value from dict values()

v = num.values()
print(v)
for j in v:
    print(j)

# to get the keys and values items()
z = num.items()
print(z)
for o in z:
    print(o)

#update()
num.update({1:"java",2:"javascript"})
print(num)

# pop()
p = num.pop(2)
print(p)
print(num)

#pop the last element in dict popitem()
p1 = num.popitem()
print(p1)
print(num)

#copy
c = num.copy()
print(c)

#clear()

#num.clear()
print(num)

print(2 in num)
print(2 not in num)

print("sql" in num.values())
print("sql" not in  num.values())
