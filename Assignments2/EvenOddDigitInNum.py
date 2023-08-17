# Program to find an integer (n >= 0) with the given number of even and odd digits.
print("-"*50)
num = int(input("\tEnter any number: "))
print("-"*50)

if(num<=0):
    print("\tInvalid input..!")
else:
    for i in str(num):
        if(int(i)%2 == 0):
            print("\t{} ---> is Even".format(i))
        else:
            print("\t{} --> is Odd".format(i))

print("-"*50)
