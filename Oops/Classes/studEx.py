#program to store instance data members, stdid, name and marks
class Student:pass


#main program
s1=Student() #creating an object
s2=Student() #creating an object

print(id(s1), len(s1.__dict__), s1.__dict__)
print(id(s2), len(s2.__dict__), s2.__dict__)

#storing instance data
s1.stdid = 100
s1.name = "stany"
s1.marks = 33.32

#storing instance data for another object
s2.stdid = 200
s2.name = "ajay"
s2.marks = 22.33

#displaying the data
print("Address={}, length={}, data={}".format(id(s1), len(s1.__dict__), s1.__dict__))
print("Address={}, length={}, data={}".format(id(s2), len(s2.__dict__), s2.__dict__))

