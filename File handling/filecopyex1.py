#copy the text files from any source folder

fileSrc = input("Enter file source: ")
try:
    with open(fileSrc,"rt") as fp1:
        with open("addcopy.data","wt") as fp2:
            filedata = fp1.read()
            fp2.write(filedata)
            print("Data copied..!")
except FileNotFoundError:
    print("file does'nt exist")