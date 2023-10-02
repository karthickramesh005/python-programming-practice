class student:
    name = "karthi"
    age = 18
    def user():
        print("name : ",student.name)
        print("age : ",student.age)

student.user()
print(student.__dict__)

print(getattr(student,"user"))
getattr(student,"user")()

student.__dict__['user']()
