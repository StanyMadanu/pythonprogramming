class Test:
    def __init__(self,x,y):
        self.a=x
        self.b=y

class Test1:
    def __init__(self,x,y,z):
        self.a=x
        self.b=y
        self.c=z

#main program
t1 = Test(200,500) #creating object with formal parameters
t2 = Test(20,50) #creating object with formal parameters
t3 = Test1(11,12,13)
print(t1.__dict__)
print(t2.__dict__)
print(t3.__dict__)
