# Property getter and setter method :

class student:
    def __init__(self,total):
        self._total = total
    def avg (self):
        return self._total / 5.0

    @property # --> Getter Method :
    def total(self):
        return self._total

    @total.setter
    def total(self,t):
        if t < 0 or t > 500:
            print("Invalid total")
        else :
            self._total = t


o = student(450)
print("total : ",o.total)
print("average : ",o.avg())
o = student(350)
print("total : ",o.total)
print("average : ",o.avg())
