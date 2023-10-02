# Multilevel Inheritance :

class grandpa:
    def house(self):
        print("grandfather house")

class father(grandpa):
    def bike (self):
        print("fathee have a own bike")

class son (father):
    def car(self):
        print("son have super car")

s = son()
s.house()
s.bike()
s.car()
