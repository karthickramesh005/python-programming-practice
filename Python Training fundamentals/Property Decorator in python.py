# property Decorator s

class user:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @property   
    def msg(self):
        return self.name +" was "+str(self.age)+" years old. "

a = user("karthi",18)
print(a.name)
print(a.age)
print(a.msg)
a.age = 24
a.name = "dinesh"
print(a.msg)
