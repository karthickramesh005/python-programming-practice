# Property method Function :


class student:
    def __init__(self,total):
        self._total = total
    def avg (self):
        return self._total / 5.0

   
    def getter(self):
        return self._total

    
    def setter(self,t):
        if t < 0 or t > 500:
            print("Invalid total")
        else :
            self._total = t
    total = property(getter,setter)


o = student(450)
print("total : ",o.total)
print("average : ",o.avg())
o = student(250)
print("total : ",o.total)
print("average : ",o.avg())
