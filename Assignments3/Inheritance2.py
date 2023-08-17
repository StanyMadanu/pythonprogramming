#2)Write a program for multilevel inheritance with operators 
#ACLBAMI---- 7 types of operators

class superclass():
    def values(self):
        self.a = int(input("Enter 1'st value: "))
        self.b = int(input("Enter 2'nd value: "))

class intermclass(superclass):
    def ArithOp(self):
        self.values() #function call
        print("="*50)
        print("\t1. Arithmetic Operators")
        print("="*50)
        self.add = self.a + self.b #addition
        self.sub = self.a - self.b #subtraction
        self.mul = self.a * self.b #multiplication
        self.div = self.a / self.b #divison-- quotient with decimal vals
        self.fdiv = self.a // self.b #floor divison-- int quotient
        self.mod = self.a % self.b #modulo divison-- reminder
        self.exp = self.a ** self.b #Exponent (power)

    def CompOp(self):
        self.values() #function call
        print("="*50)
        print("\t2. Comparison Operators")
        print("="*50)
        self.gr = self.a > self.b #greater than
        self.ls = self.a < self.b #less than
        self.eq = self.a == self.b #double equal to
        self.ne = self.a != self.b #not equal to
        self.geq = self.a >= self.b #greater than or equal to
        self.leq = self.a <= self.b #lessthan or equal to     

    def LogOp(self):
        self.values() #function call
        print("="*50)
        print("\t3. Logical Operators")
        print("="*50)
        self.an = (self.a > self.b) and (self.a < self.b) #and operator f
        self.r = (self.a >= self.b) or (self.a <= self.b) #or operator t
        self.nt = not(self.a == self.b) #not operator t

    def BitOp(self):
        self.values() #function call
        print("="*50)
        print("\t4. Bitwise Operators")
        print("="*50)
        self.ls = self.a << self.b #left shift operator
        self.rs = self.a >> self.b #right shif operator
        self.ad = self.a & self.b # & Operator
        self.rr = self.a | self.b # | Operator
        self.cp = ~self.a # ~ Operator(compliment) 
        self.xor = self.a ^ self.b # ^ operator
        print("="*50)

    def MemOp(self):
        print("="*50)
        print("\t5. Membership Operators")
        print("="*50)
        self.word = "python"
        self.p = "p" in self.word       # True
        self.p1 = "p" not in self.word  # False
        print("="*50)
    
    def IdOp(self):
        print("="*50)
        print("\t6. Identity Operators")
        print("="*50)
        self.num, self.num2 = 10, 10
        self.r1 = self.num is self.num2     # True
        self.r2 = self.num is not self.num2 # False
        print("="*50)


class subclass(intermclass):
    def output(self):
        self.ArithOp() #function call
        print("\tAdd of ({} + {})= {}".format(self.a,self.b,self.add))
        print("\tSub of ({} - {})= {}".format(self.a,self.b,self.sub))
        print("\tMul of ({} * {})= {}".format(self.a,self.b,self.mul))
        print("\tdiv of ({} / {})= {}".format(self.a,self.b,self.div))
        print("\tfdiv of ({} // {})= {}".format(self.a,self.b,self.fdiv))
        print("\tExp of ({} power {})={}".format(self.a,self.b,self.exp))
        print("="*50)

        self.CompOp() #function call
        print("\tGreater than ({} > {})= {}".format(self.a,self.b,self.gr))
        print("\tLess than ({} < {})= {}".format(self.a,self.b,self.ls))
        print("\tDouble equal to ({} == {})= {}".format(self.a,self.b,self.eq))
        print("\tNot equal to ({} != {})= {}".format(self.a,self.b,self.ne))
        print("\tGreater or equal to ({} >= {})= {}".format(self.a,self.b,self.geq))
        print("\tLessthan or equal to ({} <= {})= {}".format(self.a,self.b,self.leq))
        print("="*50)
    
        self.LogOp() #function call
        print("\t({}>{}) and ({}<{}) = {}".format(self.a,self.b,self.a,self.b,self.an))
        print("\t({}>={}) or ({}<={}) = {}".format(self.a,self.b,self.a,self.b,self.r))
        print("\tnot({}<{}) = {}".format(self.a,self.b,self.nt))

        self.BitOp() #function call
        print("\tLeft shift({} << {})= {}".format(self.a,self.b,self.ls))
        print("\tRight shift({} >> {})= {}".format(self.a,self.b,self.rs))
        print("\tAND({} & {})= {}".format(self.a,self.b,self.ad))
        print("\tOR({} | {})= {}".format(self.a,self.b,self.rr))
        print("\tComplement(~{})= {}".format(self.a,self.cp))
        print("\tXOR({} ^ {})= {}".format(self.a,self.b,self.xor))

        self.MemOp() #function call
        print("\t(p in {})= {}".format(self.word,self.p))
        print("\t(p not in {})= {}".format(self.word,self.p1))

        self.IdOp() #function call
        print("\t{} is {} = {}".format(self.num,self.num2, self.r1))
        print("\t{} is not {} = {}".format(self.num,self.num2, self.r2))


#main program
ansr = subclass() #object creation
ansr.output() #function call
