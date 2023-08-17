
lst = [] #global empty list
def getVals():
    n = int(input("Enter how many numbers u have: "))
    if n<=0:
        return lst
    else:
        for i in range(1,n+1):
            val = int(input("Enter {} value: ".format(i)))
            lst.append(val)
        return lst
        

#Main program
oldval = getVals()
if (len(oldval)==0):
    print("List is empty--nothing to square")
else:
    squareval = map(lambda x: x**2,lst)
    print("Old Value\tSquare")
    print("==========================")
    for ol,sq in zip(oldval,list(squareval)):
        print("\t{}\t{}".format(ol,sq))
    print("==========================")
