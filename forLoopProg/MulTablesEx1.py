# Program to accept 1 - n numbers and display multiplication tables

n = int(input("Enter how many tables u want: "))

if(n<=0):
    print("{} is invalid input".format(n))
else:
    for i in range(1, n+1):
        for j in range(1,11):
            print("\t{} x {} = {}".format(i, j, i*j))
        else:
            print("-"*50)
