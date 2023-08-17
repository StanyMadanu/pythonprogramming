#program for demonstrating file handing with w mode

v = open("stud.txt","w")
print("File created and opened in w mode")
v.close() #manually closing
print("is file closed:",v.closed)
