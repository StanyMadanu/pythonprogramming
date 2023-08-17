# A program to print n to 1 numbers, where n is +ve

n = int(input("Enter any number you want to print: "))

if(n<=0):
    print("Invalid input..!")
else:
    print("="*50)
    print("Numbers with in {}".format(n))
    print("="*50)

    i = n #initialization part
    while(i>0): #condition part
        print("\tvalue of i={}".format(i))
        i = i - 1   #updation part
    else:
        print("*"*50)
    print("Program execution completed")