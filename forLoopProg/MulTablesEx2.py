#Program to accept random numbers and printing the mul tables

n = int(input("Enter how many tables u want: "))

if(n<=0):
    print("{} is invalid input".format(n))
else:
    lst = list()
    for i in range(1, n+1):
        val = int(input("Enter which table u want {}:".format(i)))
        lst.append(val)
    else:
        print("-"*50)
        print("List of tables = {}".format(lst))
        print("-"*50)
        for i in lst:
            if(i<=0):
                continue
            else:
                for j in range(1,11):
                    print("\t{} x {} = {}".format(i,j,i*j))
                else:
                    print("-"*50)
