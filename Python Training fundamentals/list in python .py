# List :
#  the list datatype used to store values of same and different datatypes. this was mutable datatype.
# Its allow duplicate values. It was indide of box[].

num = [10,1.2,1+2j,"java","python",10,100,35,"java",75]
print(num)
print(type(num))

# sliceoperator()
print(num[2])
print(num[2:5])
print(num[2:])
print(num[:5])

# len()
i = len(num)
print(i)

#insert()
num.insert(3,200)
print(num)

#remove
num.remove(200)
print(num)

# pop()
p = num.pop()
print(p)
print(num)
p1 = num.pop(1)
print(p1)
print(num)

# del()
del num[1:3]
print(num)

#clear()
j = [10,1.2,1+2j,"java","python",10]
j.clear()
print(j)

num1 = [10,1.2,1+2j,"java","python",10,100,35,"java",75]

#index()
# index (value)
# index (value,start)
# index (value,start,end)
# to find index position particular value

i = num1.index("java")
print(i)
j = num1.index(10,2)
print(j)
k = num1.index(10,5,9)
print(k)

# count()
c  = num1.count(10)
print(c)

num2 = [1,2,3,5,67,45,45,2]
# max()
print(max(num2))

#min ()
print(min(num2))

# append()
num1.append(300)
print(num1)

# extend()
num1.extend([1,2,3])
print(num1)

# sort()
num2.sort()
print(num)

# sorted()
l = sorted(num2)
print(l)

# reverse()
l.reverse()
print(l)

c = num2.copy()
print(c)

print (10 in num2)
print(10 not in num2)

for i in num:
    print(i)




