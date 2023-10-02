# Operator overLoading :

class calc :
    def __init__(self,a):
        self.a = a
    def __add__(q1,q2):
        return q1.a + q2.a
    def __sub__(q1,q2):
        return q1.a - q2.a
    def __mul__(q1,q2):
        return q1.a * q2.a
    def __truediv__(q1,q2):
        return q1.a / q2.a


q1 = calc(10)
q2 = calc (20)

print("addition        : ",(q1+q2))
print("subtraction     : ",(q1-q2))
print("multiplication  : ",(q1*q2))
print("divition        : ",(q1/q2))
