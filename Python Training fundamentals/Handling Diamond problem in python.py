class a :
    def dis(self):
        print("a is function display")

class b(a) :
    def dis(self):
        print("b is function display")

class c (a):
    def dis(self):
        print("c is function display")

class b (b,a):
    pass
f = b()
f.dis()
