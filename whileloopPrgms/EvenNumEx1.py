# A program to generate even number of given range

n = int(input("Enter a range to print even numbers: "))

if(n<=0):
    print("Invalid input..!")
else:
    print("="*50)
    print("Even number for a range of {}".format(n))
    print("="*50)
    i = 2
    while(i<=n):
        print("\t value of i={}".format(i))
        i += 2
    else:
        print("*"*50)
    print("Program execution completed")
