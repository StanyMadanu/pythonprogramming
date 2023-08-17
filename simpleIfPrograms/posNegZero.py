# a program to find whether the given number is postive or negative or zero by using simple if statement

num = int(input("Enter any number: "))

if (num==0):
    print("The given number is Zero")
if (num>0):
    print("{} is a positive number".format(num))
if (num<0):
    print("{} is a negative number".format(num))

print("Execution completed")