#program demonstrating file handling with r mode

try:
    v = open("stud.txt","r")
    print("Existed file opened")
    print("is file closed:",v.closed)

except FileNotFoundError:
    print("File does not exist")
finally:
    print("Iam from finally block")
    v.close() #manually closing
    print("is file closed:",v.closed)


