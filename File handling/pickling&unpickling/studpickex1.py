#program to read student info from KBD and save data into the file
import pickle

with open("Studentinfo.data", "ab") as fp:
    while(True):
        lst =[] #empty list to store the data
        print("-"*50)
        sno = int(input("Enter Student Number: "))
        sname = input("Enter Student Name: ")
        smarks = float(input("Enter Student Marks: "))
        lst.append(sno)
        lst.append(sname)
        lst.append(smarks)
        #write lst data to the file
        pickle.dump(lst,fp)
        print("-"*50)
        print("Student data saved successfully to the file..!")
        print("="*50)

        #condition
        ch = input("Do you want to add another student details(Yes/No): ")
        if (ch.lower()=="no"):
            break