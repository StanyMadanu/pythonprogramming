# Program to find the factorial of a given number
num = int(input("Enter a Number: "))

if(num<0):
    print("{} is a invalid input".format(num))
else:
    f = 1
    for i in range(1, num+1):
        f = f * i
    else:
        print("Factorial({}) = {}".format(num,f))