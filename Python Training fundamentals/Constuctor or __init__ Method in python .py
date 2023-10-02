# init method in python :

class student :
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city
        print(" my name is ",self.name," my age was ",self.age, " i am commig from ",self .city)
        
    def printall(self):
        print(" my name is ",self.name," my age was ",self.age, " i am commig from ",self .city)
        print("name :  ",self.name)
        print("age :  ",self.age)
        print("city:  ",self.city)


o1 = student("karthi",18,"chennai")
o1.printall()
print("---------------------------------------")      
o2 = student("mano",16,"vandavasi")
o2.printall()
