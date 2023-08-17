#copy the binary files from any source folder
src = input("Enter path of the file: ")

try:
    with open(src,"rb") as fp1:
        with open("copyfile.png","wb") as fp2:
            odata = fp1.read()
            fp2.write(odata)
            print("Data copied.. successfully..!")
except FileNotFoundError:
    print("File does not exist")