class A:
    def fun1(self):
        print("this is class A")

class B(A):
    def fun2(self):
        print("this is class B")

class C(B):
    def fun3(self):
        print("this is class C")

obj = C()

obj.fun3()
obj.fun2()
obj.fun1()