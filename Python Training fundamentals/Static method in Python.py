# Static method in python :

class student :
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno

    def print(self):
        print("student name : " + self.name)
        print("student RollNo : " +str (self.rollno))

    @staticmethod
    def welcome():
        print("welcome to our School ❤❤")

a = student("kamesh",19)

a.welcome()
a.print()
print("----------------------")
a1 = student("bivan",20)

a1.welcome()
a1.print()
