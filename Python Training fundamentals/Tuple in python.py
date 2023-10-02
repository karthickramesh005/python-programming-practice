# Tuple:
#    tuple belong to the data type class classed as a sequence.tuple can also store a element of same or different datatype.
#  tules are immutable sequence.
#  the diffenece between tuple and list are the tuple cannot be changed. tuples are parentheses().

num = (10,20.23,100,10,75,35,10,4.4,1000)
print(num)
print(type(num))
print(100 in num)
print(100 not in num)

# Sliceoperator
print(num[2])
print(num[2:5])
print(num[:5])
print(num[:5])

# len()
l = len(num)
print(l)

#index()
x = num.index(10)
print(x)
y = num.index(10,2)
print(y)
k = num.index(10,5,9)
print(k)

c = num.count(10)
print(c)

# min() & max()
print(min(num))
print(max(num))


for i in num:
    print(i)
