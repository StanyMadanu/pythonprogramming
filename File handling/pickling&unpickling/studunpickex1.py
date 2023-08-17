#program to read the student records from the file
import pickle

try:
    with open("Studentinfo.data","rb") as fp:
        print("="*50)
        while(True):
            try:
                obj = pickle.load(fp)
                for val in obj:
                    print("{}".format(val),end="\t")
                print()
            except EOFError:
                print("="*50)
                break
            
except FileNotFoundError:
    print("File does not exist..!")