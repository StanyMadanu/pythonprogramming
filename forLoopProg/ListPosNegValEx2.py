#Program to accept list of +ve & -ve values and display +ve & -ve values separetly in a list form

n = int(input("Enter how many value u want:"))

if(n<=0):
    print("{} is a invalid input..!")
else:
    lst = []
    for i in range(1, n+1):
        val = int(input("Enter {} value:".format(i)))
        lst.append(val)
    else:
        print("-" * 50)
        print("Contains list of values {}".format(lst))
        print("-" * 50)

    #to print +ve & -ve list of values
    plist, nlist = list(), list()
    for i in lst:
        if(i<0):
            nlist.append(i)
        elif(i>0):
            plist.append(i)
    else:
        print("-"*50)
        print("List of Positive values: {}".format(plist))
        print("List of Negative values: {}".format(nlist))
        print("-"*50)

