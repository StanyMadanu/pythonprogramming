#program for reading the data from file
try:
    with open("E:\\pyCharmProjects\\File handling\\Fleex1.py") as fp:
        filedata = fp.read()
        print("="*50)
        print(filedata)
        print("="*50)
except FileNotFoundError:
    print("File does not exist")