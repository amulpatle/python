class A:
    def fun1(self):
        print("this is Class A")

class B(A):
    def fun2(slef):
        print("this is Class B")

obj = B()
obj.fun1()
obj.fun2()