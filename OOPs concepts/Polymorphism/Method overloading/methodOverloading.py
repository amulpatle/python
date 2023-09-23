class area:
    def find_area(self,a = None,b = None):
        if a != None and b != None :
            print("Area of rectange is :", (a*b))
        elif a != None and b == None :
            print("Area of squar is :",(a*a))
        else:
            print("Nothing is find")


obj = area()
obj.find_area(10)
obj.find_area(12,34)
obj.find_area()
        