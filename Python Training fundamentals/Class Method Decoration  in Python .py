# Class method :

class student:
    count = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        student.count += 1
        
    def details(self):
        print(self.name + " ia a "+ str(self.age) + " years old .")

    @classmethod
    def total(cls):
        return cls.count

a = student("karthi",18)
a.details()

print("total number odf students : ",student.total())
a1 = student("mano",16)
a1.details()
print("total number odf students : ",student.total())
