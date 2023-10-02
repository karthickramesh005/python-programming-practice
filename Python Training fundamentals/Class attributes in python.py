class student():
    name ="karthi"
    age  = 18

# get Attributes :

print(getattr(student,'name'))
print(getattr(student,'age'))
print(getattr(student,'clg','cls not found'))

# dot method :

print(student.name)
print(student.age)

# set attributes :

setattr(student,'gender','male')
print(student.gender)
print(setattr(student,'name','mano'))
print(student.name)

# dot method :

student.city = 'chennai'
print(student.city)

# remove attributes :
delattr(student,'city')
print(student.__dict__)

# Dot method to delete :
del student.gender
print(student.__dict__)
