# Program generation marks report - sno, sname, cm, cppm and pym
while(True):
    sno = int(input("Enter Student Number (100 - 200) : "))
    if(sno>=100) and (sno<=200):
        break
    print("{} Invalid Student Number, Try again..!".format(sno))

#-----------Student Name----------------
sname = input("Enter Student Name: ")

#-----------Marks in subjects------------
while(True):
    cm = int(input("Enter C Marks: "))
    if(cm>=0) and (cm<=100):
        break
    print("{} is invalid C Marks, try again".format(cm))
while(True):
    cppm = int(input("Enter C++ Marks: "))
    if(cppm>=0) and (cppm<=100):
        break
    print("{} is invalid C++ Marks, try again".format(cppm))
while(True):
    pym = int(input("Enter Python Marks: "))
    if(pym>=0) and (pym<=100):
        break
    print("{} is invalid Python Marks, try again".format(pym))

#Calculate total marks and percentage
totmarks = cm + cppm + pym
percent = (totmarks/300)*100

#------------------------Grade--------------------------------
if(cm<40) or (cppm<40) or (pym<40):
    grade = "FALI"
else:
    if(totmarks<=300) and (totmarks>=250):
        grade = "DISTINCTION"
    elif(totmarks<=249) and (totmarks>=200):
        grade = "FIRST"
    elif(totmarks<=199) and (totmarks>=150):
        grade = "SECOND"
    elif(totmarks<=149) and(totmarks>=120):
        grade = "THIRD"

#Display the marks report
print("="*50)
print("\tStudent Marks Report")
print("="*50)
print("\tStudent Number: {}".format(sno))
print("\tStudent Name: {}".format(sname))
print("\tStudent Marks in C: {}".format(cm))
print("\tStudent Marks in C++: {}".format(cppm))
print("\tStudent Marks in Python: {}".format(pym))
print("\n\tStudent Total Marks: {}".format(totmarks))
print("\tStudent Percentage: %0.2f".format(round(percent, 2)))
print("-"*50)
print("\tStudent Grade: {}".format(grade))
print("="*50)

