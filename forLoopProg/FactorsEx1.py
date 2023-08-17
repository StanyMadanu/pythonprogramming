# A program to find the factors of a given number

num = int(input("Enter a Number to find factors: "))

if(num<=0):
    print("{} is a invalid input..!".format(num))
else:
    print("Factors of {}".format(num))
    for i in range(1, num//2+1):
        if(num%i==0):
            print("\t{}".format(i))

