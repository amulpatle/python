class demo:
    a = 10
    def __init__(self):## constructor
        print("hyy! , my name is Amul")

    def method1(self):
        ##print(a)--- this is wronge 
        print(self.a)

    def method2(self,x,y):
        self.c = self.a*self.a
        print(self.c)
        print(x+y)
        

obj = demo()
obj.method1()
obj.method2(10,20)
