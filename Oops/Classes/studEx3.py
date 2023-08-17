
class Student:
    def appendstdinfo(self):
        self.stdid= int(input("Enter student id: "))
        self.name=input("Enter student name: ")
        self.marks= input("Enter student marks: ")
        self.dispstdinfo()

    def dispstdinfo(self):
        print("\tStudent ID: ", self.stdid)
        print("\tStudent Name: ", self.name)
        print("\tStudent Marks: ", self.marks)


#main program
s1 = Student() #creating object

s1.appendstdinfo() #function call