class user:
    course = "python"


print(user())
print(user.course)

a = user()
print(a)
print(a.course)

# Change value different :

a.course= "java"

print(a.course)
print(user.course)
