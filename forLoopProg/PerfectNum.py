#Program to find whether the given number is perfect or not

num = int(input("Enter a number: "))

if(num<=0):
    print("{} - is a invalid input..!")
else:
    sum = 0
    for i in range(1, num//2+1):
        if(num%i==0):
            print("\t{}".format(i))
            sum = sum + i
    else:
        print("="*50)
        if(sum==num):
            print("{} is a PERFECT NUMBER".format(num))
        else:
            print("{} is not a PERFECT NUMBER".format(num))
