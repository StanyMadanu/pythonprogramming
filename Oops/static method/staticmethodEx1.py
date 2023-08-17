class Student:
    def readstddata(self):
        self.sno = int(input("Enter Student number: "))
        self.sname = input("Enter Student Name: ")
        self.marks = float(input("Enter Student Marks: "))

class Employee:
    def readempdata(self):
        self.eno = int(input("Enter Emp number: "))
        self.ename = input("Enter Emp Name: ")


class Teacher:
    def readtchrdata(self):
        self.tno = int(input("Enter Teacher Number: "))
        self.tname = input("Enter Teacher Name: ")
        self.subj = input("Enter Teacher subject: ")
        self.subexp = float(input("Enter Teacher sub Experience: "))


class Hyd:
    @staticmethod
    def disobjdata(obj, objref):
        print("{} information".format(objref))
        print("="*50)
        for k,v in obj.__dict__.items():
            print("\t{}\t{}".format(k,v))
        print("="*50)




#main program
s = Student() #student object creation
e = Employee() #employee object creation
t = Teacher() #teacher object creation

#read student data
s.readstddata() #function call
#read employee data
e.readempdata()
#read teacher data
t.readtchrdata()

h = Hyd() #object creation
h.disobjdata(s,"Student") #calling static method w.r.t object name
Hyd.disobjdata(e, "Employee") #calling static method w.r.t class name
h.disobjdata(t, "Teacher")