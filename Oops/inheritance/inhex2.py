#Program for demonstraing multi-level inheritance
class c1: #super/base class
    def getA(self): 
        self.a = 10        

class c2(c1): #derived/sub class & super class-----intermediate base class
    def getB(self):
        self.b = 20

class c3(c2): #sub/child/derived class
    def getC(self):
        self.getA() #function call inside child class
        self.getB() #function call inside child class
        self.c = self.a + self.b

        #printing the values
        print("value of a: ",self.a)
        print("value of b: ",self.b)
        print("value of c: ",self.c)


#main program
obj3 = c3() #object creation

obj3.getC() #instance function call

