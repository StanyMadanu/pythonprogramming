#Program for reading and displaying employee values such as:
#eno, ename, sal and cname

class Emp:
    
    @classmethod
    def getcompname(cls):
        cls.cname = "TCS" #here cname is a class level data member
    
    @classmethod
    def getaddr(cls):
        cls.addr = "HYD" #here addr is a class leve data member


    def readempinfo(self):
        self.eno = int(input("Enter employee number: "))
        self.ename = input("Enter employee name: ")
        self.sal = float(input("Enter employee salary: "))
        self.dispempinfo()
        
    
    def dispempinfo(self):
        print("\tEmployee Number: ",self.eno)
        print("\tEmployee Name: ", self.ename)
        print("\tEmployee Salary: ", self.sal)
        print("\tCompany name: ", Emp.cname)
        print("\tCompany Addr: ",Emp.addr)



#main program
Emp.getcompname() #calling Class Level Methods w.r.t class name
Emp.getaddr() #calling Class Level Methods w.r.t class name
e1 = Emp() #creating an object

#calling instance class function
e1.readempinfo()
