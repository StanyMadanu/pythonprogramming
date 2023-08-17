class Student:
    def appendstddata(self):
        print("memory address of current instance object={}".format(id(self)))
        self.id = int(input("Enter student id: "))
        self.name = input("Enter student name: ")
        self.marks = input("Enter student marks: ")


#main program
s1=Student() #object creation
s2=Student() #object creation

print("s1 memory: {}".format(id(s1)))
print("s2 memory: {}".format(id(s2)))

print("="*50)
s1.appendstddata() #function call
s2.appendstddata() #function call
print("="*50)

#displaying the data
print(s1.__dict__)
print(s2.__dict__)