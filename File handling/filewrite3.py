a = True
b = 29.334
c = 234

with open("write.data","a") as fp:
    fp.write(str(a)+"\n")
    fp.write(str(b)+"\n")
    fp.write(str(c)+"\n")