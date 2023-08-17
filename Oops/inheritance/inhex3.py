#Program for demonstrating Hierarchical Inheritance

class values: #super/base/parent class
    def getVals(self): #instance function
        self.a = float(input("\nEnter 1st value: "))
        self.b = float(input("Enter 2nd value: "))

class sum(values): #sub/derived/child class
    def getSum(self): #instance function
        self.getVals()
        self.s = self.a + self.b
        print("Sum {} + {}= {}".format(self.a,self.b,self.s))

class sub(values): #sub/derived/child class
    def getSub(self): #instance function
        self.getVals() 
        self.s = self.a - self.b
        print("Sub {} - {} = {}".format(self.a, self.b,self.s))

class mul(values):
    def getMul(self): #instance function
        self.getVals()
        self.m = self.a*self.b
        print("Mul {} x {} = {}".format(self.a,self.b,self.m))


class div(values):
    def getDiv(self): #instance function
        self.getVals()
        self.d = self.a % self.b
        print("Div {} / {} = {}".format(self.a,self.b,self.d))


#main program
op1 = sum() #sum object creation
op1.getSum() #function call

op2 = sub() #sub object creation
op2.getSub() #instance function call

op3=mul() #mul object creation
op3.getMul() #instance function call

op4=div() #div object creation
op4.getDiv() #instance function call