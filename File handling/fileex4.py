#program to demonstrate file handling with r mode using "with open() as"

try:
    with open("stud.data", "r") as v:
        print("Existing file opened..! in read mode")
        print("Name of file:",v.name)
        print("Name of mode:",v.mode)
        print("is file writable:",v.writable())
        print("is file readable:",v.readable())
        print("is file closed:",v.closed)
except FileNotFoundError:
    print("File does not exist")
finally:
    print("-------------------------")
    print("Iam from finally block")
    print("is file closed:",v.closed)