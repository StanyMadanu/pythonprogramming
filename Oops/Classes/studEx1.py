#program for storing student info from instance data and also class level data: 
#id, name, marks and course

class student:
    crs = "PYTHON" #class level data member


#main program
s1 = student() #object creation

#taking instance data from kbd
s1.id = int(input("Enter 1st student id: "))
s1.name = input("Enter 1st student name: ")
s1.marks = input("Enter 1st student marks: ")

#displaying the data
print(s1.__dict__)

#2nd way of displaying the data 
for k,v in s1.__dict__.items():
    print("\t{}-->{}".format(k,v))

#3rd way of displaying the data
print("Student id :{}".format(s1.id))
print("Student name :{}".format(s1.name))
print("Student marks :{}".format(s1.marks))
print("Student COURSE :{}".format(student.crs))