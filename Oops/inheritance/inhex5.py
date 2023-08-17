#Program to demonstrate Hybrid Inheritance

class grandFather: #super/base/parent class
    def gfather(self):
        print("Grand Father Property")

class father(grandFather): #sub/derived & super/parent/base - intermediate class
    def father(self):
        print("Father Property")
        self.gfather()

class mother(): #sub/derived & super/parent/base - intermediate class
    def mother(self):
        print("Mother Property")

class child(father,mother): #child/derived/sub class
    def chil(self):
        self.father()
        self.mother()


#main program
prop = child() #child object creation
prop.chil() #instance function call