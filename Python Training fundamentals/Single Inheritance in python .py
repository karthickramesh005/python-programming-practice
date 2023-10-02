# Single inheritance :

class redmi:
    company = "RedMi India"
    Website = "WWW.RedMi-india.com"
    
    def address(self):
        print("address : velachery main road,chennai,India")

class redmi9pow (redmi):
    def __init__(self):
        self.name = "RedMi 9Power"
        self.year = 2023

    def details(self):
        print("name : ", self.name)
        print("year : ", self.year)
        print("company : ", self.company)
        print(" Website: ", self. Website)


mobile = redmi9pow()
mobile.details()
mobile.address()
