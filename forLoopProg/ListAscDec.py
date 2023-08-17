# Program to accept list of values dynamically by KBD and arrange in Ascending & Decending order
n = int(input("Enter how many values u have: "))
if(n<=0):
    print("{} is a invalid input")
else:
    lst = list()
    for i in range(1, n+1):
        val = int(input("Enter {} value: ".format(i)))
        lst.append(val)  
    else:
        print("Original list of values = {}".format(lst))
        print("-"*50)

    #sorting
    plist, nlist = [], []
    for i in lst:
        if(i<0):
            nlist.append(i)
        elif(i>0):
            plist.append(i)

    else:
        print("="*50)
        print("Negative list = {}".format(nlist))
        print("Positive list = {}".format(plist))
        lst.sort()
        print("Ascending order of list {}".format(lst))
        lst.reverse()
        print("Decending order of list {}".format(lst))
        print("="*50)