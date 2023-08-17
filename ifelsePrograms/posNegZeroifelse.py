# a program to find whether the given number is +ve or -ve or zero - by using if else statements

num = int(input("Enter any number: "))

if(num>0):
    print("{} --> is a positive number".format(num))
else:
    if(num<0):
        print("{} --> is a negative number".format(num))
    else:
        print("The given number is Zero")
