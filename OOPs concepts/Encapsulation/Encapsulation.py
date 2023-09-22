class demo:
    def __init__(self):
        self.a = ""
    
    def getName(self):
        return self.a
    def setName(self,name):
        self.a = name

obj = demo()

obj.setName("amul")
print(obj.getName())