class Test:
    def __init__(self): #default constructor
        self.a = 10
        self.b = 20
        self.c = self.a + self.b
        

#main program
t1 = Test()
print(t1.__dict__)