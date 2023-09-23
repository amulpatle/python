class A:
    def showData(self):
        print("I'm in A class")

class B(A):
    def showData(self):
        super().showData()
        print("i'm in B class")

obj = B()
obj.showData()


## if we want to run A class functionn , there is function in python that name is super() , using super function we can use A class function in B class