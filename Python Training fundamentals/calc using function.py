def add(a,b):
    sum = a+b
    return sum
def sub(a,b):
    sum = a-b
    return sum
def mul(a,b):
    sum = a*b
    return sum
def div(a,b):
    sum = a/b
    return sum
def mod(a,b):
    sum = a%b
    return sum

a = int(input("enter first value : "))
b = int(input("enter second value : "))
op = str(input("enter operation : "))


if op == '+':
    print("addition of ",a," and" ,b," is :",add(a,b))
elif op == '-':
    print("subtraction of ",a," and" ,b," is :",sub(a,b))
elif op == '*':
    print("multiplication of ",a," and" ,b," is :",mul(a,b))
elif op == '/':
    print("divition of ",a," and" ,b," is :",div(a,b))
elif op == '%':
    print("modulo of ",a," and" ,b," is :",mod(a,b))



