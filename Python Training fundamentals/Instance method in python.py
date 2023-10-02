class student:
    name = "karthi"
    age = 18
    def user(self,gender):
        print("name : ",student.name)
        print("age : ",student.age)
        print("gender : ",gender)



o = student()

print(o,"user")
o.user("male")
student.user(o,"male")
