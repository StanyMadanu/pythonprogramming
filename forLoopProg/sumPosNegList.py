# Program to accept the list of values dynamically from KBD and sum of -ve & +ve numbers
n = int(input("Enter how many numbers u want : "))

if(n<=0):
    print("{} is a invalid input")
else:
    lst = list()
    for i in range(1, n+1):
        val = int(input("Enter {} value: ".format(i)))
        lst.append(val)
    else:
        print("Original list of values: {}".format(lst))

    #Separating values
    plist, nlist = list(), list()
    nsum, psum, avg = 0, 0, 0

    for i in lst:
        if(i<0):
            nlist.append(i)
            nsum = nsum + i
        elif(i>0):
            plist.append(i)
            psum = psum + i
            avg = psum/len(plist)
    else:
        print("-"*50)
        print("List of positive values: {} and sum={} and Avg= {}".format(plist,psum, avg))
        print("List of negative values: {} and Negative sum={}".format(nlist,nsum))
        print("-"*50)
