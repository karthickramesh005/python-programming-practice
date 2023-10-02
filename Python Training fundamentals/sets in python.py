# Set :
#   sets are datatype we can store the different value which are not-repeated.ignore duplicate value.
#  not index based.not maintaining any order.Value mention in {} curly brackets.

num = {10,20,10,"java","python",35,100,75,"java"}
print(num)
print(type(num))

#len() : lenght of the sets
i = len(num)
print(i)

# add() : Add the value
num.add(200)
print(num)

#Update : update the value
num.update({1,2,3})
print(num)

#remove : remove the value
num.remove(10)
print(num)

#discard() :
num.discard(10)
print(num)

# pop(): remove the first value
p = num.pop()
print(p)
print(num)

#copy()
c = num.copy()
print(num)

#clear() : clear the all data
# num.clear()
print(num)

# union() : join the two sets but not repeated
num1 = {10,20,10,"sql","pycharm",35,100,75,"javascript"}
print(num.union (num1))

# intersection() : num and num1 same values are printed
print(num.intersection(num1))
print(num1 & num)

print(num)
print(num1)
#difference() : num & num1 defference value are printed
print(num1.difference(num))
print(num - num1)

print(num.difference(num1))
print(num1 - num)

# symmetric()
print(num.symmetric_difference(num1))




