# multiple Inheritance :

class school :
   
    def school(self):
        
        print("karthi 10 std mark was : 364 ")
      
        print("karthi 12 std mark was : 512" )


class college:
    def college(self):
        
        print("karthi 1styear persantage was :85 " )
        print("karthi 2ndyear persantage was : 88")
   
        

class thirdyear(school,college) :
    def third (self):
        print("karthi 3ndyear persantage was : 90")
   




r = thirdyear()
r.school()
r.college()
r.third()


