# A program to print 1 to n numbers, where n is +ve

n = int(input("Enter how many numbers u want to print: "))

if(n<=0):
    print("Invalid input..!")
else:
    print("="*50)
    print("Numbers within {}".format(n))
    print("=" * 50)
    i = 1   #initialization part
    while(i<=n): #condition part
        print("\tvalue of i = {}".format(i))
        i += 1  # updation part
    else:
        print("*"*50)
    print("Program execution completed")