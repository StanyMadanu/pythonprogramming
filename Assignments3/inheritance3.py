#3)Write a program for Multiple inheritance using some functions
class parent1():
    def addop(self):
        self.add = 10 + 20

class parent2():
    def subop(self):
        self.s = 10 - 20

class parent3():
    def divop(self):
        self.div = 10 / 20

class child(parent1,parent2,parent3):
    def ch(self):
        self.addop() # function call
        self.subop() # function call
        self.divop() # function call

        print("\tAddition of (10 + 20) =",self.add)
        print("\tSubtraction of (10 - 20) =",self.s)
        print("\tDivision of (10 / 20) =",self.div)

#main program
chld = child() #object creation
chld.ch() #function call