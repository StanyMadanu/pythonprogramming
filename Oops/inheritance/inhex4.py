#Program to demonstrate multiple inheritance
class sum: #super/base/parent class
    def getSum(self):
        self.s = self.a + self.b
        print("sum {} + {} = {}".format(self.a,self.b,self.s))

class sub: #super/base/parent class
    def getSub(self):
        self.sb = self.a - self.b
        print("Sub {} - {} = {}".format(self.a,self.b,self.sb))       

class mul: #super/base/parent class
    def getMul(self):
        self.m = self.a  *self.b
        print("Mul {} x {} = {}".format(self.a,self.b,self.m))

class pow: #super/base/parent class
    def getPow(self):
        self.p = self.a ** self.b
        print("{} power {} = {}".format(self.a,self.b, self.p))

class main(sum,sub,mul,pow): #sub/derived/child class
    def getAns(self):
        self.a = float(input("Enter 1st Value: "))
        self.b = float(input("Enter 2nd Value: "))
        self.getSum()
        self.getSub()
        self.getMul()
        self.getPow()

#main program
ans = main() #main object creation
ans.getAns() #instance function call