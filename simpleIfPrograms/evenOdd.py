# a program to find the even or odd numbers - by using simple if statement

num = int(input("Enter any number: "))

if(num%2 == 0):
    print("{} --> is even number".format(num))
if(num%2!=0):
    print("{} --> is odd number".format(num))
print("Execution completed")