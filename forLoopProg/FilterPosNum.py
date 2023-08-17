# Program for accepting list of values dynamically from KBD and find list of positive values

n = int(input("Enter how many values u want: "))

if(n<=0):
    print("{} is invalid input".format(n))
else:
    lst = list() #empty list
    for i in range(1, n+1):
        val = int(input("Enter {} value:".format(i)))
        lst.append(val)
    else:
        print("List of values {}".format(lst))
    print("-"*50)

    #condition to print postive values
    print("List of positive values")
    for i in lst:
        if(i<0):
            continue
        else:
            print("\t{}".format(i))
    print("-"*50)



