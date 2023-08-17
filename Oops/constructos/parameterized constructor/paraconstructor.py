class Test:
    def __init__(self,a,b): #parameterized constructor
        self.a=a
        self.b=b


#main program
t1 = Test(100,200) #creating an object
print(t1.__dict__)
