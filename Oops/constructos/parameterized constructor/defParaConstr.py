#default parameterized constructor

class Test:
    def __init__(self,a=1,b=2): #default parameterized constructor
        self.a = a
        self.b = b


#main program
t1=Test(20,30) #object with 2 arguments
print(t1.__dict__)

t2=Test() #object with no arguments
print(t2.__dict__)

t3=Test(b=100) #object with one default argument
print(t3.__dict__)

t4=Test(a=300)
print(t4.__dict__)
