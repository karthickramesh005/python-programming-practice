# function Overriding :

class emp:
    def workhrs(self):
        self.hrs = 50

    def printhrs(self):
        print("total working hrs :",self.hrs)

class train (emp):
    def workhrs(self):
        self.hrs = 78

    def resethrs (self):
        super().workhrs()


emp = emp()
emp.workhrs()
emp.printhrs()

t = train()
t.workhrs()
t.printhrs()
# reset trainhrs :

t.resethrs()
t.printhrs()
